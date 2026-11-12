"""Pruebas del servicio de propuestas, reservas y concurrencia (US-009, GC02-55).

Cubre la validación de reglas y propiedad (AC-01, AC-04, AC-05), la exclusividad
de reservas (AC-03), la atomicidad ante fallos (NFR-007, RT-02) y la exclusión en
propuestas simultáneas (AC-06) tanto con dos hilos y barrera (concurrencia real)
como simulando la colisión sobre la restricción única y el bloqueo de SQLite.
"""

import threading
from datetime import date, datetime, time, timedelta
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.db import IntegrityError, OperationalError, connections, transaction

from cuadrante.models import Categoria, Empleado, Servicio, Turno
from intercambios.models import ReservaTurno, SolicitudIntercambio
from intercambios.propuestas import (
    ConflictoConcurrenciaError,
    IncompatibilidadRN03Error,
    TurnoNoDisponibleError,
    TurnoNoValidoError,
    proponer_intercambio,
)

MADRID = ZoneInfo("Europe/Madrid")
AHORA = datetime(2026, 11, 1, 9, 0, tzinfo=MADRID)

pytestmark = pytest.mark.django_db


def crear_turno(empleado, fecha_iso, franja="M", inicio=None, fin=None):
    dia = date.fromisoformat(fecha_iso)
    horarios = {"M": (time(8), time(15)), "T": (time(15), time(22)), "N": (time(22), time(8))}
    h_ini, h_fin = horarios[franja]
    dia_fin = dia + timedelta(days=1) if franja == "N" else dia
    return Turno.objects.create(
        empleado=empleado,
        fecha=dia,
        franja=franja,
        inicio=inicio or datetime.combine(dia, h_ini, MADRID),
        fin=fin or datetime.combine(dia_fin, h_fin, MADRID),
    )


def escenario_base():
    urgencias = Servicio.objects.create(codigo="urgencias", nombre="Urgencias")
    planta = Servicio.objects.create(codigo="planta", nombre="Planta")
    enfermeria = Categoria.objects.create(codigo="enfermeria", nombre="Enfermería")
    auxiliar = Categoria.objects.create(codigo="auxiliar", nombre="Auxiliar")

    ana = Empleado.objects.create(
        codigo="ana", nombre="Ana", servicio=urgencias, categoria=enfermeria
    )
    berta = Empleado.objects.create(
        codigo="berta", nombre="Berta", servicio=urgencias, categoria=enfermeria
    )
    clara = Empleado.objects.create(
        codigo="clara", nombre="Clara", servicio=urgencias, categoria=enfermeria
    )
    diego = Empleado.objects.create(
        codigo="diego", nombre="Diego", servicio=urgencias, categoria=auxiliar
    )
    elena = Empleado.objects.create(
        codigo="elena", nombre="Elena", servicio=planta, categoria=enfermeria
    )
    jefe = Empleado.objects.create(
        codigo="jefe", nombre="Jefe", servicio=urgencias, es_responsable=True
    )
    return {
        "ana": ana,
        "berta": berta,
        "clara": clara,
        "diego": diego,
        "elena": elena,
        "jefe": jefe,
    }


@pytest.fixture
def contexto():
    datos = escenario_base()
    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        yield datos


def test_propuesta_valida_crea_solicitud_y_dos_reservas(contexto):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")

    solicitud = proponer_intercambio(contexto["ana"], t_ana, t_berta)

    assert solicitud.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert solicitud.ultima_accion == "PROPUESTA"
    assert solicitud.autor_ultima_accion == contexto["ana"]
    assert solicitud.empleado_proponente == contexto["ana"]
    assert solicitud.empleado_solicitado == contexto["berta"]
    assert set(solicitud.reservas.values_list("turno_id", flat=True)) == {t_ana.id, t_berta.id}


def test_mvp_permite_proponer_con_menos_de_48h_sin_rn05(contexto):
    t_ana = crear_turno(
        contexto["ana"],
        "2026-11-01",
        "M",
        inicio=AHORA + timedelta(hours=1),
        fin=AHORA + timedelta(hours=8),
    )
    t_berta = crear_turno(
        contexto["berta"],
        "2026-11-01",
        "T",
        inicio=AHORA + timedelta(hours=2),
        fin=AHORA + timedelta(hours=9),
    )

    solicitud = proponer_intercambio(contexto["ana"], t_ana, t_berta)

    assert solicitud.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.count() == 2


def test_ac04_no_se_propone_sobre_turno_propio(contexto):
    t1 = crear_turno(contexto["ana"], "2026-11-05", "M")
    t2 = crear_turno(contexto["ana"], "2026-11-06", "T")

    with pytest.raises(TurnoNoValidoError, match="otro empleado"):
        proponer_intercambio(contexto["ana"], t1, t2)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


def test_ac01_no_se_ofrece_turno_de_otro_empleado(contexto):
    t_clara = crear_turno(contexto["clara"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")

    with pytest.raises(TurnoNoValidoError, match="no pertenece"):
        proponer_intercambio(contexto["ana"], t_clara, t_berta)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


@pytest.mark.parametrize(
    ("cual", "desfase"),
    [
        ("ofrecido", timedelta(0)),
        ("ofrecido", timedelta(minutes=-1)),
        ("solicitado", timedelta(0)),
        ("solicitado", timedelta(minutes=-30)),
    ],
)
def test_no_se_propone_si_algun_turno_ya_ha_empezado(contexto, cual, desfase):
    inicio_invalido = AHORA + desfase
    if cual == "ofrecido":
        t_ana = crear_turno(
            contexto["ana"],
            "2026-11-01",
            "M",
            inicio=inicio_invalido,
            fin=inicio_invalido + timedelta(hours=7),
        )
        t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")
    else:
        t_ana = crear_turno(contexto["ana"], "2026-11-06", "M")
        t_berta = crear_turno(
            contexto["berta"],
            "2026-11-01",
            "T",
            inicio=inicio_invalido,
            fin=inicio_invalido + timedelta(hours=7),
        )

    with pytest.raises(TurnoNoValidoError, match="futuros"):
        proponer_intercambio(contexto["ana"], t_ana, t_berta)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


@pytest.mark.parametrize("destino", ["diego", "elena", "jefe"])
def test_ac05_rechaza_rn03_por_categoria_servicio_o_datos_ausentes(contexto, destino):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_otro = crear_turno(contexto[destino], "2026-11-06", "T")

    with pytest.raises(IncompatibilidadRN03Error, match="RN-03"):
        proponer_intercambio(contexto["ana"], t_ana, t_otro)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


@pytest.mark.parametrize(
    "estado_activo",
    [SolicitudIntercambio.Estado.PROPUESTA, SolicitudIntercambio.Estado.ACEPTADA],
)
@pytest.mark.parametrize("rol_reservado", ["ofrecido", "solicitado"])
def test_ac03_rechaza_turno_ofrecido_o_solicitado_ya_reservado(
    contexto, estado_activo, rol_reservado
):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")
    t_clara = crear_turno(contexto["clara"], "2026-11-07", "M")

    solicitud_activa = proponer_intercambio(contexto["ana"], t_ana, t_berta)
    if estado_activo == SolicitudIntercambio.Estado.ACEPTADA:
        solicitud_activa.estado = SolicitudIntercambio.Estado.ACEPTADA
        solicitud_activa.save(update_fields=["estado"])

    with pytest.raises(TurnoNoDisponibleError, match="ya no está disponible"):
        if rol_reservado == "ofrecido":
            proponer_intercambio(contexto["ana"], t_ana, t_clara)
        else:
            proponer_intercambio(contexto["clara"], t_clara, t_berta)

    assert SolicitudIntercambio.objects.count() == 1
    assert ReservaTurno.objects.count() == 2


def test_turno_liberado_tras_rechazo_puede_proponerse_de_nuevo(contexto):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")
    t_clara = crear_turno(contexto["clara"], "2026-11-07", "M")

    primera = proponer_intercambio(contexto["ana"], t_ana, t_berta)
    primera.estado = SolicitudIntercambio.Estado.RECHAZADA
    primera.save(update_fields=["estado"])
    primera.reservas.all().delete()

    segunda = proponer_intercambio(contexto["clara"], t_clara, t_berta)

    assert segunda.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.filter(solicitud=segunda).count() == 2


def test_atomicidad_revierte_solicitud_y_reserva_si_falla_segunda_reserva(contexto):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")

    crear_original = ReservaTurno.objects.create
    llamadas = 0

    def crear_con_fallo(**kwargs):
        nonlocal llamadas
        llamadas += 1
        if llamadas == 2:
            raise RuntimeError("Fallo simulado al crear la segunda reserva")
        return crear_original(**kwargs)

    with mock.patch.object(ReservaTurno.objects, "create", side_effect=crear_con_fallo):
        with pytest.raises(RuntimeError, match="Fallo simulado"):
            proponer_intercambio(contexto["ana"], t_ana, t_berta)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


def test_restriccion_unica_secuencial_impide_dos_reservas_en_un_turno(contexto):
    """Prueba secuencial de la restricción única OneToOne sobre ReservaTurno.turno."""
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")
    t_clara = crear_turno(contexto["clara"], "2026-11-07", "M")

    solicitud = proponer_intercambio(contexto["ana"], t_ana, t_berta)
    otra = SolicitudIntercambio.objects.create(
        turno_ofrecido=t_clara,
        turno_solicitado=t_berta,
        empleado_proponente=contexto["clara"],
        empleado_solicitado=contexto["berta"],
        autor_ultima_accion=contexto["clara"],
    )

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            ReservaTurno.objects.create(solicitud=otra, turno=t_berta)

    assert ReservaTurno.objects.filter(turno=t_berta).count() == 1
    assert ReservaTurno.objects.get(turno=t_berta).solicitud == solicitud


def test_ac06_carrera_simulada_dispara_integrity_error_y_revierte_perdedora(contexto):
    """Simula la carrera cuando dos transacciones leen sin reserva antes de insertar."""
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")
    t_clara = crear_turno(contexto["clara"], "2026-11-07", "M")

    ganadora = proponer_intercambio(contexto["ana"], t_ana, t_berta)

    with mock.patch("intercambios.propuestas._alguno_reservado", return_value=False):
        with pytest.raises(TurnoNoDisponibleError, match="ya no está disponible"):
            proponer_intercambio(contexto["clara"], t_clara, t_berta)

    assert SolicitudIntercambio.objects.count() == 1
    assert SolicitudIntercambio.objects.get() == ganadora
    assert ReservaTurno.objects.count() == 2
    assert not ReservaTurno.objects.filter(turno=t_clara).exists()


def test_ac06_reintento_ante_bloqueo_sqlite_sin_reservas_parciales(contexto):
    t_ana = crear_turno(contexto["ana"], "2026-11-05", "M")
    t_berta = crear_turno(contexto["berta"], "2026-11-06", "T")

    with mock.patch(
        "intercambios.propuestas._crear_propuesta",
        side_effect=OperationalError("database is locked"),
    ):
        with pytest.raises(ConflictoConcurrenciaError, match="conflicto concurrente"):
            proponer_intercambio(contexto["ana"], t_ana, t_berta)

    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


@pytest.mark.django_db(transaction=True)
def test_ac06_concurrencia_real_dos_hilos_compiten_por_el_mismo_turno():
    """Concurrencia real con dos hilos y Barrier(2) en prueba transaccional (AC-06)."""
    datos = escenario_base()
    t_ana = crear_turno(datos["ana"], "2026-11-05", "M")
    t_berta = crear_turno(datos["berta"], "2026-11-06", "T")
    t_clara = crear_turno(datos["clara"], "2026-11-07", "M")

    barrera = threading.Barrier(2)
    resultados = []
    errores = []
    cerrojo = threading.Lock()

    def competir(empleado, turno_propio):
        try:
            barrera.wait(timeout=5)
            solicitud = proponer_intercambio(empleado, turno_propio, t_berta)
            with cerrojo:
                resultados.append((empleado.codigo, solicitud.pk))
        except Exception as exc:
            with cerrojo:
                errores.append((empleado.codigo, exc))
        finally:
            connections.close_all()

    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        hilos = [
            threading.Thread(target=competir, args=(datos["ana"], t_ana)),
            threading.Thread(target=competir, args=(datos["clara"], t_clara)),
        ]
        for hilo in hilos:
            hilo.start()
        for hilo in hilos:
            hilo.join(timeout=10)

    assert len(resultados) == 1
    assert len(errores) == 1
    assert isinstance(errores[0][1], TurnoNoDisponibleError)
    assert "ya no está disponible" in str(errores[0][1])

    assert SolicitudIntercambio.objects.count() == 1
    assert ReservaTurno.objects.count() == 2
    ganadora = SolicitudIntercambio.objects.get()
    assert ganadora.pk == resultados[0][1]
    turno_perdedor = t_clara if ganadora.empleado_proponente == datos["ana"] else t_ana
    assert not ReservaTurno.objects.filter(turno=turno_perdedor).exists()
