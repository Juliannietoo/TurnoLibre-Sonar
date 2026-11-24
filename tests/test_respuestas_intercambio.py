"""Pruebas del servicio de respuesta a propuestas, caducidad y concurrencia (US-010, GC02-61).

Cubre la aceptación conservando reservas (AC-01), el rechazo liberando reservas (AC-02),
la comprobación de caducidad antes de responder y ausencia de RN-05 en el MVP (AC-03, AC-05),
la autorización exclusiva del destinatario e idempotencia al repetir respuesta (AC-04),
la atomicidad ante fallos y la concurrencia de dos respuestas simultáneas (NFR-007) tanto
con dos hilos y barrera como con carrera simulada.
"""

import threading
from datetime import date, datetime, time, timedelta
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.db import OperationalError, connections

from cuadrante.models import Categoria, Empleado, Servicio, Turno
from intercambios.caducidad import MOTIVO_CADUCIDAD
from intercambios.models import ReservaTurno, SolicitudIntercambio
from intercambios.propuestas import proponer_intercambio
from intercambios.respuestas import (
    NoEsDestinatarioError,
    SolicitudNoPendienteError,
    responder_propuesta,
)

MADRID = ZoneInfo("Europe/Madrid")
AHORA = datetime(2026, 11, 1, 9, 0, tzinfo=MADRID)
MOMENTO_RESPUESTA = datetime(2026, 11, 1, 11, 30, tzinfo=MADRID)

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
    enfermeria = Categoria.objects.create(codigo="enfermeria", nombre="Enfermería")
    ana = Empleado.objects.create(
        codigo="ana", nombre="Ana", servicio=urgencias, categoria=enfermeria
    )
    berta = Empleado.objects.create(
        codigo="berta", nombre="Berta", servicio=urgencias, categoria=enfermeria
    )
    clara = Empleado.objects.create(
        codigo="clara", nombre="Clara", servicio=urgencias, categoria=enfermeria
    )
    jefe = Empleado.objects.create(
        codigo="jefe", nombre="Jefe", servicio=urgencias, es_responsable=True
    )
    return {"ana": ana, "berta": berta, "clara": clara, "jefe": jefe}


@pytest.fixture
def contexto():
    datos = escenario_base()
    t_ana = crear_turno(datos["ana"], "2026-11-05", "M")
    t_berta = crear_turno(datos["berta"], "2026-11-06", "T")
    t_clara = crear_turno(datos["clara"], "2026-11-07", "M")
    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        solicitud = proponer_intercambio(datos["ana"], t_ana, t_berta)
    datos.update(
        {"t_ana": t_ana, "t_berta": t_berta, "t_clara": t_clara, "solicitud": solicitud}
    )
    return datos


def test_ac01_aceptar_pasa_a_aceptada_y_conserva_las_dos_reservas(contexto):
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        actualizada = responder_propuesta(
            contexto["berta"],
            contexto["solicitud"],
            acepta=True,
            motivo="  De acuerdo con el cambio.  ",
        )

    assert actualizada.estado == SolicitudIntercambio.Estado.ACEPTADA
    assert actualizada.ultima_accion == "ACEPTADA"
    assert actualizada.autor_ultima_accion == contexto["berta"]
    assert actualizada.fecha_ultima_accion == MOMENTO_RESPUESTA
    assert actualizada.motivo_ultima_accion == "De acuerdo con el cambio."
    assert set(actualizada.reservas.values_list("turno_id", flat=True)) == {
        contexto["t_ana"].id,
        contexto["t_berta"].id,
    }


def test_ac02_rechazar_pasa_a_rechazada_y_libera_ambos_turnos(contexto):
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        actualizada = responder_propuesta(
            contexto["berta"],
            contexto["solicitud"],
            acepta=False,
            motivo="  No puedo ese día.  ",
        )

    assert actualizada.estado == SolicitudIntercambio.Estado.RECHAZADA
    assert actualizada.ultima_accion == "RECHAZADA"
    assert actualizada.autor_ultima_accion == contexto["berta"]
    assert actualizada.fecha_ultima_accion == MOMENTO_RESPUESTA
    assert actualizada.motivo_ultima_accion == "No puedo ese día."
    assert not ReservaTurno.objects.exists()

    # Los turnos liberados pueden volver a proponerse si siguen siendo futuros.
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        nueva = proponer_intercambio(
            contexto["clara"], contexto["t_clara"], contexto["t_berta"]
        )
    assert nueva.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.filter(solicitud=nueva).count() == 2


@pytest.mark.parametrize("quien", ["ana", "clara", "jefe"])
def test_ac04_solo_el_destinatario_puede_responder(contexto, quien):
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        with pytest.raises(NoEsDestinatarioError, match="Solo el destinatario"):
            responder_propuesta(contexto[quien], contexto["solicitud"], acepta=True)

    contexto["solicitud"].refresh_from_db()
    assert contexto["solicitud"].estado == SolicitudIntercambio.Estado.PROPUESTA
    assert contexto["solicitud"].autor_ultima_accion == contexto["ana"]
    assert ReservaTurno.objects.filter(solicitud=contexto["solicitud"]).count() == 2


@pytest.mark.parametrize("acepta", [True, False])
def test_ac03_justo_antes_del_primer_inicio_permite_responder_sin_exigir_48h(
    contexto, acepta
):
    un_segundo_antes = contexto["t_ana"].inicio - timedelta(seconds=1)
    with mock.patch("django.utils.timezone.now", return_value=un_segundo_antes):
        resultado = responder_propuesta(
            contexto["berta"], contexto["solicitud"], acepta=acepta
        )

    esperado = (
        SolicitudIntercambio.Estado.ACEPTADA
        if acepta
        else SolicitudIntercambio.Estado.RECHAZADA
    )
    assert resultado.estado == esperado
    assert resultado.fecha_ultima_accion == un_segundo_antes


@pytest.mark.parametrize("primero", ["ofrecido", "solicitado"])
@pytest.mark.parametrize("acepta", [True, False])
def test_ac03_ac05_al_llegar_al_primer_inicio_caduca_libera_y_rechaza_respuesta(
    primero, acepta
):
    datos = escenario_base()
    if primero == "ofrecido":
        t_ana = crear_turno(datos["ana"], "2026-11-05", "M")
        t_berta = crear_turno(datos["berta"], "2026-11-09", "T")
        primer_inicio = t_ana.inicio
    else:
        t_ana = crear_turno(datos["ana"], "2026-11-09", "M")
        t_berta = crear_turno(datos["berta"], "2026-11-05", "T")
        primer_inicio = t_berta.inicio

    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        solicitud = proponer_intercambio(datos["ana"], t_ana, t_berta)

    with mock.patch("django.utils.timezone.now", return_value=primer_inicio):
        with pytest.raises(SolicitudNoPendienteError, match="no está pendiente"):
            responder_propuesta(datos["berta"], solicitud, acepta=acepta)

    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.CADUCADA
    assert solicitud.ultima_accion == "CADUCADA"
    assert solicitud.motivo_ultima_accion == MOTIVO_CADUCIDAD
    assert not ReservaTurno.objects.exists()


@pytest.mark.parametrize("acepta", [True, False])
def test_ac04_repetir_la_misma_respuesta_es_idempotente(contexto, acepta):
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        primera = responder_propuesta(
            contexto["berta"],
            contexto["solicitud"],
            acepta=acepta,
            motivo="Motivo inicial",
        )

    instante_posterior = MOMENTO_RESPUESTA + timedelta(minutes=15)
    with mock.patch("django.utils.timezone.now", return_value=instante_posterior):
        segunda = responder_propuesta(
            contexto["berta"],
            contexto["solicitud"],
            acepta=acepta,
            motivo="Motivo distinto en reintento",
        )

    assert segunda.estado == primera.estado
    assert segunda.fecha_ultima_accion == MOMENTO_RESPUESTA
    assert segunda.motivo_ultima_accion == "Motivo inicial"
    assert ReservaTurno.objects.count() == (2 if acepta else 0)


@pytest.mark.parametrize(
    ("primera_decision", "segunda_decision"),
    [(True, False), (False, True)],
)
def test_ac04_respuesta_opuesta_posterior_falla_sin_alterar_estado(
    contexto, primera_decision, segunda_decision
):
    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        responder_propuesta(
            contexto["berta"],
            contexto["solicitud"],
            acepta=primera_decision,
            motivo="Primera decisión",
        )

    instante_posterior = MOMENTO_RESPUESTA + timedelta(minutes=10)
    with mock.patch("django.utils.timezone.now", return_value=instante_posterior):
        with pytest.raises(SolicitudNoPendienteError, match="no está pendiente"):
            responder_propuesta(
                contexto["berta"],
                contexto["solicitud"],
                acepta=segunda_decision,
                motivo="Intento opuesto",
            )

    contexto["solicitud"].refresh_from_db()
    esperado = (
        SolicitudIntercambio.Estado.ACEPTADA
        if primera_decision
        else SolicitudIntercambio.Estado.RECHAZADA
    )
    assert contexto["solicitud"].estado == esperado
    assert contexto["solicitud"].fecha_ultima_accion == MOMENTO_RESPUESTA
    assert contexto["solicitud"].motivo_ultima_accion == "Primera decisión"
    assert ReservaTurno.objects.count() == (2 if primera_decision else 0)


@pytest.mark.parametrize(
    "estado_terminal",
    [
        SolicitudIntercambio.Estado.APROBADA,
        SolicitudIntercambio.Estado.CADUCADA,
        SolicitudIntercambio.Estado.RECHAZADA,
    ],
)
def test_no_se_puede_responder_una_solicitud_ya_terminada(contexto, estado_terminal):
    SolicitudIntercambio.objects.filter(pk=contexto["solicitud"].pk).update(
        estado=estado_terminal,
        ultima_accion=estado_terminal,
        autor_ultima_accion=contexto["ana"],
    )

    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        with pytest.raises(SolicitudNoPendienteError, match="no está pendiente"):
            responder_propuesta(
                contexto["berta"], contexto["solicitud"], acepta=True
            )

    contexto["solicitud"].refresh_from_db()
    assert contexto["solicitud"].estado == estado_terminal


def test_atomicidad_si_falla_liberar_reservas_al_rechazar_revierte_el_estado(contexto):
    with mock.patch.object(
        ReservaTurno.objects,
        "filter",
        side_effect=RuntimeError("Fallo simulado al borrar reservas"),
    ):
        with pytest.raises(RuntimeError, match="Fallo simulado"):
            responder_propuesta(
                contexto["berta"], contexto["solicitud"], acepta=False
            )

    contexto["solicitud"].refresh_from_db()
    assert contexto["solicitud"].estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.filter(solicitud=contexto["solicitud"]).count() == 2


def test_reintento_ante_bloqueo_transitorio_de_sqlite(contexto):
    from intercambios import respuestas as mod_respuestas

    original = mod_respuestas._responder_una_vez
    llamadas = 0

    def con_bloqueo_inicial(*args, **kwargs):
        nonlocal llamadas
        llamadas += 1
        if llamadas == 1:
            raise OperationalError("database table is locked")
        return original(*args, **kwargs)

    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        with mock.patch(
            "intercambios.respuestas._responder_una_vez",
            side_effect=con_bloqueo_inicial,
        ):
            resultado = responder_propuesta(
                contexto["berta"], contexto["solicitud"], acepta=True
            )

    assert llamadas == 2
    assert resultado.estado == SolicitudIntercambio.Estado.ACEPTADA


@pytest.mark.django_db(transaction=True)
def test_concurrencia_real_dos_hilos_con_respuestas_opuestas():
    """Dos hilos simultáneos (aceptar vs rechazar): solo uno gana y el estado es consistente."""
    datos = escenario_base()
    t_ana = crear_turno(datos["ana"], "2026-11-05", "M")
    t_berta = crear_turno(datos["berta"], "2026-11-06", "T")
    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        solicitud = proponer_intercambio(datos["ana"], t_ana, t_berta)

    barrera = threading.Barrier(2)
    exitos = []
    errores = []
    cerrojo = threading.Lock()

    def intentar(acepta, motivo):
        try:
            barrera.wait(timeout=5)
            res = responder_propuesta(
                datos["berta"], solicitud, acepta=acepta, motivo=motivo
            )
            with cerrojo:
                exitos.append((acepta, res.estado))
        except Exception as exc:
            with cerrojo:
                errores.append((acepta, exc))
        finally:
            connections.close_all()

    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        hilos = [
            threading.Thread(target=intentar, args=(True, "Acepto")),
            threading.Thread(target=intentar, args=(False, "Rechazo")),
        ]
        for hilo in hilos:
            hilo.start()
        for hilo in hilos:
            hilo.join(timeout=10)

    assert len(exitos) == 1
    assert len(errores) == 1
    assert isinstance(errores[0][1], SolicitudNoPendienteError)

    solicitud.refresh_from_db()
    ganadora_acepto = exitos[0][0]
    if ganadora_acepto:
        assert solicitud.estado == SolicitudIntercambio.Estado.ACEPTADA
        assert solicitud.motivo_ultima_accion == "Acepto"
        assert ReservaTurno.objects.filter(solicitud=solicitud).count() == 2
    else:
        assert solicitud.estado == SolicitudIntercambio.Estado.RECHAZADA
        assert solicitud.motivo_ultima_accion == "Rechazo"
        assert ReservaTurno.objects.filter(solicitud=solicitud).count() == 0


@pytest.mark.django_db(transaction=True)
def test_concurrencia_real_dos_hilos_con_la_misma_respuesta_son_idempotentes():
    """Dos hilos simultáneos enviando la misma respuesta terminan ambos sin error."""
    datos = escenario_base()
    t_ana = crear_turno(datos["ana"], "2026-11-05", "M")
    t_berta = crear_turno(datos["berta"], "2026-11-06", "T")
    with mock.patch("django.utils.timezone.now", return_value=AHORA):
        solicitud = proponer_intercambio(datos["ana"], t_ana, t_berta)

    barrera = threading.Barrier(2)
    resultados = []
    errores = []
    cerrojo = threading.Lock()

    def intentar():
        try:
            barrera.wait(timeout=5)
            res = responder_propuesta(
                datos["berta"], solicitud, acepta=True, motivo="Confirmado"
            )
            with cerrojo:
                resultados.append(res.estado)
        except Exception as exc:
            with cerrojo:
                errores.append(exc)
        finally:
            connections.close_all()

    with mock.patch("django.utils.timezone.now", return_value=MOMENTO_RESPUESTA):
        hilos = [threading.Thread(target=intentar), threading.Thread(target=intentar)]
        for hilo in hilos:
            hilo.start()
        for hilo in hilos:
            hilo.join(timeout=10)

    assert errores == []
    assert resultados == [
        SolicitudIntercambio.Estado.ACEPTADA,
        SolicitudIntercambio.Estado.ACEPTADA,
    ]
    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.ACEPTADA
    assert ReservaTurno.objects.filter(solicitud=solicitud).count() == 2
