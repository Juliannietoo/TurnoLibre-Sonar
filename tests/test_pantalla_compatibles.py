"""Pruebas de la pantalla de turnos compatibles (US-006)."""

import re
from datetime import datetime
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.test import override_settings
from django.urls import reverse

from cuadrante.compatibles import ConsultaNoDisponible
from cuadrante.demo import cargar, leer_fuente

CLAVE = "clave-de-prueba"
NOVIEMBRE = {"mes": "2026-11"}
AHORA = datetime(2026, 11, 1, 9, tzinfo=ZoneInfo("Europe/Madrid"))

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def datos():
    with override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]):
        cargar(leer_fuente(), CLAVE)
        with mock.patch("cuadrante.views.timezone.now", return_value=AHORA):
            yield


def entrar(client, usuario):
    client.login(username=usuario, password=CLAVE)
    return client


def filas(contenido):
    return re.findall(r"<tr>\s*<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>",
                      contenido, re.S)


def test_ac01_lista_de_companeros_compatibles(client):
    contenido = entrar(client, "empleado01").get(reverse("compatibles"), NOVIEMBRE).content.decode()
    nombres = {nombre for *_, nombre in filas(contenido)}
    assert nombres
    assert "Ana Vega" not in nombres  # la propia empleada
    assert "Carla Lago" not in nombres  # auxiliar: otra categoría


def test_ac02_solo_nombre_y_turno(client):
    contenido = entrar(client, "empleado01").get(reverse("compatibles"), NOVIEMBRE).content.decode()
    assert contenido.count('<th scope="col">') == 4
    assert "empleado02" not in contenido  # ni el usuario ni otros datos del compañero


def test_no_muestra_turnos_que_ya_han_empezado(client):
    with mock.patch(
        "cuadrante.views.timezone.now",
        return_value=datetime(2026, 11, 29, 23, tzinfo=ZoneInfo("Europe/Madrid")),
    ):
        respuesta = entrar(client, "empleado01").get(reverse("compatibles"), NOVIEMBRE)
    assert "noviembre" in respuesta.content.decode()
    assert all("29 de noviembre" not in fecha for fecha, *_ in filas(respuesta.content.decode()))


def test_ac03_mes_sin_turnos_muestra_lista_vacia(client):
    contenido = entrar(client, "empleado01").get(
        reverse("compatibles"), {"mes": "2026-12"}
    ).content.decode()
    assert "No hay turnos pendientes de compañeros" in contenido


def test_ac03_un_fallo_muestra_su_motivo(client):
    with mock.patch(
        "cuadrante.views.turnos_compatibles",
        side_effect=ConsultaNoDisponible("No se han podido consultar los turnos."),
    ):
        contenido = entrar(client, "empleado01").get(
            reverse("compatibles"), NOVIEMBRE
        ).content.decode()
    assert 'role="alert"' in contenido
    assert "No se han podido consultar los turnos." in contenido
    assert "No hay turnos pendientes" not in contenido


def test_el_responsable_no_consulta_compatibles(client):
    contenido = entrar(client, "responsable01").get(reverse("compatibles")).content.decode()
    assert "Solo los empleados con categoría" in contenido


def test_sin_sesion_redirige_al_inicio_de_sesion(client):
    respuesta = client.get(reverse("compatibles"))
    assert respuesta.status_code == 302
    assert respuesta.url.startswith(reverse("entrar"))


def test_enlace_en_la_navegacion(client):
    contenido = entrar(client, "empleado01").get(reverse("inicio")).content.decode()
    assert reverse("compatibles") in contenido
