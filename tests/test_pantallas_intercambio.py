"""Pruebas de las pantallas de propuesta, detalle y marca en el calendario (US-009, GC02-57)."""

from datetime import datetime
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.test import override_settings
from django.urls import reverse

from cuadrante.demo import cargar, leer_fuente
from cuadrante.models import Turno
from intercambios.models import ReservaTurno, SolicitudIntercambio
from intercambios.propuestas import TurnoNoDisponibleError

CLAVE = "clave-de-prueba"
NOVIEMBRE = {"mes": "2026-11"}
AHORA = datetime(2026, 11, 1, 9, tzinfo=ZoneInfo("Europe/Madrid"))

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def datos():
    with override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]):
        cargar(leer_fuente(), CLAVE)
        with mock.patch("django.utils.timezone.now", return_value=AHORA):
            yield


def entrar(client, usuario):
    client.login(username=usuario, password=CLAVE)
    return client


def primer_turno(codigo):
    turnos = Turno.objects.filter(empleado__codigo=codigo, inicio__gt=AHORA)
    return turnos.order_by("inicio").first()


def proponer(client, turno_propio, turno_companero):
    return client.post(
        reverse("proponer_intercambio", args=[turno_companero.pk]),
        {"turno_propio": turno_propio.pk},
    )


@pytest.fixture
def solicitud(client):
    """Ana Vega (empleado01) ofrece su primer turno por el primero de Berta Prado (empleado02)."""
    proponer(entrar(client, "empleado01"), primer_turno("empleado01"), primer_turno("empleado02"))
    client.logout()
    return SolicitudIntercambio.objects.get()


# --- Propuesta (AC-01, AC-03 a AC-06) ---


def test_ac01_enlace_para_proponer_desde_turnos_compatibles(client):
    contenido = entrar(client, "empleado01").get(reverse("compatibles"), NOVIEMBRE).content.decode()
    destino = reverse("proponer_intercambio", args=[primer_turno("empleado02").pk])
    assert f'href="{destino}"' in contenido


def test_ac01_formulario_con_mis_turnos_futuros(client):
    respuesta = entrar(client, "empleado01").get(
        reverse("proponer_intercambio", args=[primer_turno("empleado02").pk])
    )
    contenido = respuesta.content.decode()
    assert respuesta.status_code == 200
    assert "Berta Prado" in contenido
    assert "<legend>Elige el turno que ofreces a cambio</legend>" in contenido
    propios = Turno.objects.filter(empleado__codigo="empleado01", inicio__gt=AHORA).count()
    assert contenido.count('type="radio"') == propios
    assert "Confirmar propuesta" in contenido


def test_ac01_confirmar_crea_la_solicitud_y_abre_su_detalle(client):
    propio, ajeno = primer_turno("empleado01"), primer_turno("empleado02")
    respuesta = proponer(entrar(client, "empleado01"), propio, ajeno)
    solicitud = SolicitudIntercambio.objects.get()
    assert respuesta.status_code == 302
    assert respuesta.url == reverse("detalle_solicitud", args=[solicitud.pk])
    assert solicitud.estado == SolicitudIntercambio.Estado.PROPUESTA
    assert set(solicitud.reservas.values_list("turno_id", flat=True)) == {propio.pk, ajeno.pk}
    contenido = client.get(respuesta.url).content.decode()
    assert 'role="status"' in contenido
    assert "Propuesta enviada a Berta Prado" in contenido


def test_ac03_turno_ocupado_explica_el_motivo_y_no_crea_nada(client, solicitud):
    entrar(client, "empleado04")
    url = reverse("proponer_intercambio", args=[solicitud.turno_solicitado.pk])
    contenido = client.get(url).content.decode()
    assert 'role="alert"' in contenido
    assert "ya forma parte de otra solicitud activa" in contenido
    assert "Confirmar propuesta" not in contenido
    client.post(url, {"turno_propio": primer_turno("empleado04").pk})
    assert SolicitudIntercambio.objects.count() == 1
    assert ReservaTurno.objects.count() == 2


def test_ac03_no_se_ofrecen_turnos_propios_ya_reservados(client, solicitud):
    contenido = entrar(client, "empleado01").get(
        reverse("proponer_intercambio", args=[primer_turno("empleado04").pk])
    ).content.decode()
    assert f'value="{solicitud.turno_ofrecido.pk}"' not in contenido


def test_ac04_no_se_propone_sobre_un_turno_propio(client):
    propio = primer_turno("empleado01")
    contenido = entrar(client, "empleado01").get(
        reverse("proponer_intercambio", args=[propio.pk])
    ).content.decode()
    assert "No puedes proponer un intercambio sobre un turno propio." in contenido
    assert "Confirmar propuesta" not in contenido


def test_ac05_rn03_indica_la_regla_y_el_motivo_sin_crear_nada(client):
    auxiliar = primer_turno("empleado03")  # Carla Lago, auxiliar de enfermería
    entrar(client, "empleado01")
    contenido = client.get(reverse("proponer_intercambio", args=[auxiliar.pk])).content.decode()
    assert 'role="alert"' in contenido
    assert "RN-03:" in contenido
    assert "categorías distintas" in contenido
    proponer(client, primer_turno("empleado01"), auxiliar)
    assert not SolicitudIntercambio.objects.exists()
    assert not ReservaTurno.objects.exists()


def test_ac06_propuesta_simultanea_recibe_turno_no_disponible(client):
    entrar(client, "empleado01")
    with mock.patch(
        "intercambios.views.proponer_intercambio",
        side_effect=TurnoNoDisponibleError("El turno ya no está disponible."),
    ):
        respuesta = proponer(client, primer_turno("empleado01"), primer_turno("empleado02"))
    contenido = respuesta.content.decode()
    assert respuesta.status_code == 200
    assert 'role="alert"' in contenido
    assert "El turno ya no está disponible." in contenido
    assert not SolicitudIntercambio.objects.exists()


def test_sin_elegir_turno_propio_pide_elegirlo(client):
    respuesta = entrar(client, "empleado01").post(
        reverse("proponer_intercambio", args=[primer_turno("empleado02").pk])
    )
    assert "Elige uno de tus turnos" in respuesta.content.decode()
    assert not SolicitudIntercambio.objects.exists()


def test_no_se_ofrece_un_turno_de_otro_empleado(client):
    respuesta = entrar(client, "empleado01").post(
        reverse("proponer_intercambio", args=[primer_turno("empleado02").pk]),
        {"turno_propio": primer_turno("empleado04").pk},
    )
    assert "Elige uno de tus turnos" in respuesta.content.decode()
    assert not SolicitudIntercambio.objects.exists()


def test_turno_que_ya_ha_empezado(client):
    pasado = Turno.objects.filter(empleado__codigo="empleado02", inicio__lte=AHORA).first()
    if pasado is None:  # los datos empiezan después de AHORA: se mueve uno al pasado
        pasado = primer_turno("empleado02")
        Turno.objects.filter(pk=pasado.pk).update(
            inicio=datetime(2026, 10, 31, 8, tzinfo=ZoneInfo("Europe/Madrid")),
            fin=datetime(2026, 10, 31, 15, tzinfo=ZoneInfo("Europe/Madrid")),
        )
    contenido = entrar(client, "empleado01").get(
        reverse("proponer_intercambio", args=[pasado.pk])
    ).content.decode()
    assert "ya ha empezado" in contenido
    assert "Confirmar propuesta" not in contenido


def test_el_responsable_no_propone(client):
    respuesta = entrar(client, "responsable01").get(
        reverse("proponer_intercambio", args=[primer_turno("empleado02").pk])
    )
    assert respuesta.status_code == 403


def test_proponer_sin_sesion_redirige(client):
    respuesta = client.get(reverse("proponer_intercambio", args=[primer_turno("empleado02").pk]))
    assert respuesta.status_code == 302
    assert respuesta.url.startswith(reverse("entrar"))


# --- Detalle (AC-02, AC-07) ---


def test_ac02_detalle_con_turnos_estado_y_siguiente_accion(client, solicitud):
    contenido = entrar(client, "empleado01").get(
        reverse("detalle_solicitud", args=[solicitud.pk])
    ).content.decode()
    assert "Propuesta" in contenido
    assert "Pendiente de que Berta Prado la acepte o la rechace." in contenido
    assert "Ana Vega" in contenido and "Berta Prado" in contenido
    assert '<th scope="row">Ofrecido</th>' in contenido
    assert '<th scope="row">Solicitado</th>' in contenido


def test_ac02_la_companera_ve_que_le_toca_responder(client, solicitud):
    contenido = entrar(client, "empleado02").get(
        reverse("detalle_solicitud", args=[solicitud.pk])
    ).content.decode()
    assert "Te toca responder" in contenido


@pytest.mark.parametrize(
    ("usuario", "estado"),
    [("empleado01", 200), ("empleado02", 200), ("responsable01", 200), ("empleado04", 403)],
)
def test_ac02_solo_participantes_y_responsable(client, solicitud, usuario, estado):
    respuesta = entrar(client, usuario).get(reverse("detalle_solicitud", args=[solicitud.pk]))
    assert respuesta.status_code == estado


def test_ac02_detalle_sin_sesion_redirige(client, solicitud):
    respuesta = client.get(reverse("detalle_solicitud", args=[solicitud.pk]))
    assert respuesta.status_code == 302
    assert respuesta.url.startswith(reverse("entrar"))


def test_ac07_detalle_de_una_solicitud_terminada(client, solicitud):
    SolicitudIntercambio.objects.filter(pk=solicitud.pk).update(
        estado=SolicitudIntercambio.Estado.RECHAZADA,
        ultima_accion="RECHAZADA",
        autor_ultima_accion=solicitud.empleado_solicitado,
        motivo_ultima_accion="No puedo cubrir esa mañana.",
    )
    contenido = entrar(client, "empleado01").get(
        reverse("detalle_solicitud", args=[solicitud.pk])
    ).content.decode()
    assert "Rechazada" in contenido
    assert "Ninguna: la solicitud ha terminado." in contenido
    assert "No puedo cubrir esa mañana." in contenido
    assert "Berta Prado" in contenido  # quién hizo la última acción


def test_ac07_ultima_accion_quien_y_cuando(client, solicitud):
    contenido = entrar(client, "empleado01").get(
        reverse("detalle_solicitud", args=[solicitud.pk])
    ).content.decode()
    assert "Propuesta del intercambio" in contenido
    assert "1 de noviembre de 2026, 09:00" in contenido


# --- Marca en el calendario (AC-09) ---


@pytest.mark.parametrize("usuario", ["empleado01", "empleado02"])
def test_ac09_marca_en_el_calendario_de_los_dos(client, solicitud, usuario):
    contenido = entrar(client, usuario).get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert contenido.count("Solicitud pendiente") == 1
    assert reverse("detalle_solicitud", args=[solicitud.pk]) in contenido


def test_ac09_sin_marca_cuando_la_solicitud_termina(client, solicitud):
    SolicitudIntercambio.objects.filter(pk=solicitud.pk).update(
        estado=SolicitudIntercambio.Estado.RECHAZADA
    )
    contenido = entrar(client, "empleado01").get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert "Solicitud pendiente" not in contenido


# --- Teclado (NFR-004) ---


def test_formulario_usable_con_teclado(client):
    contenido = entrar(client, "empleado01").get(
        reverse("proponer_intercambio", args=[primer_turno("empleado02").pk])
    ).content.decode()
    assert 'tabindex="-1"' not in contenido
    assert contenido.count("<label for=\"turno-") == contenido.count('type="radio"')
    assert '<button type="submit">Confirmar propuesta</button>' in contenido
