"""Pruebas de caducidad automática y orden caducar_solicitudes (US-009-AC-08, GC02-55)."""

import threading
from datetime import date, datetime, time, timedelta
from io import StringIO
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.core.management import call_command
from django.db import connections
from django.urls import reverse

from cuadrante.models import Categoria, Empleado, Servicio, Turno
from intercambios.caducidad import MOTIVO_CADUCIDAD, caducar_vencidas
from intercambios.models import ReservaTurno, SolicitudIntercambio
from intercambios.propuestas import proponer_intercambio

MADRID = ZoneInfo("Europe/Madrid")
INICIO_BASE = datetime(2026, 11, 1, 9, 0, tzinfo=MADRID)

pytestmark = pytest.mark.django_db


def crear_turno(empleado, fecha_iso, franja="M"):
    dia = date.fromisoformat(fecha_iso)
    horarios = {"M": (time(8), time(15)), "T": (time(15), time(22)), "N": (time(22), time(8))}
    h_ini, h_fin = horarios[franja]
    dia_fin = dia + timedelta(days=1) if franja == "N" else dia
    return Turno.objects.create(
        empleado=empleado,
        fecha=dia,
        franja=franja,
        inicio=datetime.combine(dia, h_ini, MADRID),
        fin=datetime.combine(dia_fin, h_fin, MADRID),
    )


def preparar_equipo():
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
    return ana, berta, clara


def test_ac08_justo_antes_del_primer_inicio_no_caduca():
    ana, berta, _ = preparar_equipo()
    t_ana = crear_turno(ana, "2026-11-05", "M")  # 05/11 08:00
    t_berta = crear_turno(berta, "2026-11-08", "T")  # 08/11 15:00

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    un_segundo_antes = t_ana.inicio - timedelta(seconds=1)
    assert caducar_vencidas(ahora=un_segundo_antes) == 0

    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.filter(solicitud=solicitud).count() == 2


@pytest.mark.parametrize(
    "estado_inicial",
    [SolicitudIntercambio.Estado.PROPUESTA, SolicitudIntercambio.Estado.ACEPTADA],
)
@pytest.mark.parametrize("primero", ["ofrecido", "solicitado"])
def test_ac08_exactamente_al_primer_inicio_caduca_y_libera_reservas(
    estado_inicial, primero
):
    ana, berta, _ = preparar_equipo()
    if primero == "ofrecido":
        t_ana = crear_turno(ana, "2026-11-05", "M")
        t_berta = crear_turno(berta, "2026-11-09", "T")
        primer_inicio = t_ana.inicio
    else:
        t_ana = crear_turno(ana, "2026-11-09", "M")
        t_berta = crear_turno(berta, "2026-11-05", "T")
        primer_inicio = t_berta.inicio

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    if estado_inicial == SolicitudIntercambio.Estado.ACEPTADA:
        solicitud.estado = SolicitudIntercambio.Estado.ACEPTADA
        solicitud.ultima_accion = "ACEPTADA"
        solicitud.autor_ultima_accion = berta
        solicitud.save(update_fields=["estado", "ultima_accion", "autor_ultima_accion"])

    assert caducar_vencidas(ahora=primer_inicio) == 1

    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.CADUCADA
    assert solicitud.ultima_accion == "CADUCADA"
    assert solicitud.fecha_ultima_accion == primer_inicio
    assert solicitud.motivo_ultima_accion == MOTIVO_CADUCIDAD
    assert not ReservaTurno.objects.filter(solicitud=solicitud).exists()


def test_caducar_vencidas_usa_hora_del_servidor_por_defecto():
    ana, berta, _ = preparar_equipo()
    t_ana = crear_turno(ana, "2026-11-05", "M")
    t_berta = crear_turno(berta, "2026-11-07", "T")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    with mock.patch("django.utils.timezone.now", return_value=t_ana.inicio):
        assert caducar_vencidas() == 1

    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.CADUCADA
    assert not ReservaTurno.objects.exists()


def test_caducar_vencidas_es_idempotente_y_preserva_terminales():
    ana, berta, clara = preparar_equipo()
    t_ana_1 = crear_turno(ana, "2026-11-05", "M")
    t_berta_1 = crear_turno(berta, "2026-11-07", "T")
    t_clara_1 = crear_turno(clara, "2026-11-06", "M")
    t_ana_2 = crear_turno(ana, "2026-11-08", "M")
    t_berta_2 = crear_turno(berta, "2026-11-09", "T")
    t_clara_2 = crear_turno(clara, "2026-11-10", "M")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        activa = proponer_intercambio(ana, t_ana_1, t_berta_1)

    aprobada = SolicitudIntercambio.objects.create(
        turno_ofrecido=t_clara_1,
        turno_solicitado=t_ana_2,
        empleado_proponente=clara,
        empleado_solicitado=ana,
        estado=SolicitudIntercambio.Estado.APROBADA,
        ultima_accion="APROBADA",
        autor_ultima_accion=ana,
        motivo_ultima_accion="",
    )
    rechazada = SolicitudIntercambio.objects.create(
        turno_ofrecido=t_berta_2,
        turno_solicitado=t_clara_2,
        empleado_proponente=berta,
        empleado_solicitado=clara,
        estado=SolicitudIntercambio.Estado.RECHAZADA,
        ultima_accion="RECHAZADA",
        autor_ultima_accion=clara,
        motivo_ultima_accion="Motivo manual",
    )

    instante_1 = t_ana_1.inicio + timedelta(hours=1)
    assert caducar_vencidas(ahora=instante_1) == 1
    assert caducar_vencidas(ahora=instante_1 + timedelta(hours=2)) == 0

    activa.refresh_from_db()
    aprobada.refresh_from_db()
    rechazada.refresh_from_db()
    assert activa.fecha_ultima_accion == instante_1
    assert aprobada.estado == SolicitudIntercambio.Estado.APROBADA
    assert aprobada.ultima_accion == "APROBADA"
    assert rechazada.estado == SolicitudIntercambio.Estado.RECHAZADA
    assert rechazada.motivo_ultima_accion == "Motivo manual"


def test_orden_caducar_solicitudes_funciona_sin_visitar_pantalla():
    ana, berta, _ = preparar_equipo()
    t_ana = crear_turno(ana, "2026-11-05", "M")
    t_berta = crear_turno(berta, "2026-11-08", "T")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    salida_1 = StringIO()
    with mock.patch("django.utils.timezone.now", return_value=t_ana.inicio):
        call_command("caducar_solicitudes", stdout=salida_1)

    assert "Solicitudes caducadas: 1." in salida_1.getvalue()
    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.CADUCADA
    assert not ReservaTurno.objects.exists()

    salida_2 = StringIO()
    with mock.patch("django.utils.timezone.now", return_value=t_ana.inicio):
        call_command("caducar_solicitudes", stdout=salida_2)

    assert "No hay solicitudes vencidas pendientes de caducar." in salida_2.getvalue()


def test_proponer_intercambio_caduca_solicitud_vencida_y_libera_contraparte_futura():
    ana, berta, clara = preparar_equipo()
    t_ana = crear_turno(ana, "2026-11-05", "M")
    t_berta = crear_turno(berta, "2026-11-10", "T")
    t_clara = crear_turno(clara, "2026-11-12", "M")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        vencida = proponer_intercambio(ana, t_ana, t_berta)

    despues_del_primer_turno = datetime(2026, 11, 5, 10, 0, tzinfo=MADRID)
    with mock.patch("django.utils.timezone.now", return_value=despues_del_primer_turno):
        nueva = proponer_intercambio(clara, t_clara, t_berta)

    vencida.refresh_from_db()
    assert vencida.estado == SolicitudIntercambio.Estado.CADUCADA
    assert nueva.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert ReservaTurno.objects.filter(solicitud=vencida).count() == 0
    assert ReservaTurno.objects.get(turno=t_berta).solicitud == nueva


def test_ac08_detalle_muestra_caducada_sin_accion_disponible(client, django_user_model):
    ana, berta, _ = preparar_equipo()
    user_ana = django_user_model.objects.create_user(username="ana", password="clave")
    ana.usuario = user_ana
    ana.save(update_fields=["usuario"])

    t_ana = crear_turno(ana, "2026-11-05", "M")
    t_berta = crear_turno(berta, "2026-11-08", "T")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    caducar_vencidas(ahora=t_ana.inicio)
    client.force_login(user_ana)
    respuesta = client.get(reverse("detalle_solicitud", args=[solicitud.pk]))
    contenido = respuesta.content.decode()

    assert respuesta.status_code == 200
    assert "Caducada" in contenido
    assert "Caducidad" in contenido
    assert "Ninguna: la solicitud ha terminado." in contenido
    assert MOTIVO_CADUCIDAD in contenido


@pytest.mark.django_db(transaction=True)
def test_ac08_concurrencia_dos_hilos_caducando_a_la_vez():
    """Dos hilos simultáneos caducando la misma solicitud producen un único efecto."""
    ana, berta, _ = preparar_equipo()
    t_ana = crear_turno(ana, "2026-11-05", "M")
    t_berta = crear_turno(berta, "2026-11-08", "T")

    with mock.patch("django.utils.timezone.now", return_value=INICIO_BASE):
        solicitud = proponer_intercambio(ana, t_ana, t_berta)

    barrera = threading.Barrier(2)
    resultados = []
    errores = []
    cerrojo = threading.Lock()

    def ejecutar():
        try:
            barrera.wait(timeout=5)
            n = caducar_vencidas(ahora=t_ana.inicio)
            with cerrojo:
                resultados.append(n)
        except Exception as exc:
            with cerrojo:
                errores.append(exc)
        finally:
            connections.close_all()

    hilos = [threading.Thread(target=ejecutar), threading.Thread(target=ejecutar)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join(timeout=10)

    assert errores == []
    assert sum(resultados) == 1
    solicitud.refresh_from_db()
    assert solicitud.estado == SolicitudIntercambio.Estado.CADUCADA
    assert not ReservaTurno.objects.exists()
