"""Pruebas del calendario propio en lista y de su accesibilidad (US-005)."""

import re

import pytest
from django.test import override_settings
from django.urls import reverse

from cuadrante.demo import cargar, leer_fuente

CLAVE = "clave-de-prueba"
NOVIEMBRE = {"mes": "2026-11"}

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def datos():
    with override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]):
        cargar(leer_fuente(), CLAVE)
        yield


@pytest.fixture
def empleado01(client):
    client.login(username="empleado01", password=CLAVE)
    return client


def filas(respuesta):
    return re.findall(r"<tr>\s*<td>", respuesta.content.decode())


def test_ac01_lista_del_mes_con_fecha_franja_y_servicio(empleado01):
    respuesta = empleado01.get(reverse("calendario"), NOVIEMBRE)
    contenido = respuesta.content.decode()
    # empleado01 trabaja de mañana los días impares, del 1 al 29 de noviembre: 15 turnos.
    assert len(filas(respuesta)) == 15
    assert "martes 3 de noviembre" in contenido
    assert "Mañana (M)" in contenido
    assert "Urgencias" in contenido


def test_ac01_solo_aparecen_los_turnos_propios(empleado01):
    contenido = empleado01.get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert "Tarde (T)" not in contenido
    assert "Noche (N)" not in contenido


def test_ac02_avanzar_y_retroceder_de_mes(empleado01):
    contenido = empleado01.get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert "?mes=2026-10" in contenido
    assert "?mes=2026-12" in contenido
    octubre = empleado01.get(reverse("calendario"), {"mes": "2026-10"})
    assert "No tienes turnos en octubre de 2026" in octubre.content.decode()
    diciembre = empleado01.get(reverse("calendario"), {"mes": "2026-12"})
    assert "?mes=2027-01" in diciembre.content.decode()


def test_la_noche_aparece_en_la_fecha_en_que_empieza(client):
    client.login(username="empleado15", password=CLAVE)
    contenido = client.get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert "lunes 2 de noviembre" in contenido
    assert "22:00–08:00 del día siguiente" in contenido


def test_el_responsable_ve_su_calendario_sin_turnos(client):
    client.login(username="responsable01", password=CLAVE)
    respuesta = client.get(reverse("calendario"), NOVIEMBRE)
    assert respuesta.status_code == 200
    assert "no tienes turnos asignados" in respuesta.content.decode()


def test_sin_sesion_redirige_al_inicio_de_sesion(client):
    respuesta = client.get(reverse("calendario"))
    assert respuesta.status_code == 302
    assert respuesta.url.startswith(reverse("entrar"))


def test_mes_no_valido_muestra_el_mes_actual(empleado01):
    assert empleado01.get(reverse("calendario"), {"mes": "nada"}).status_code == 200


def test_accesibilidad_tabla_con_titulo_y_cabeceras(empleado01):
    contenido = empleado01.get(reverse("calendario"), NOVIEMBRE).content.decode()
    assert "<caption>Turnos de noviembre de 2026</caption>" in contenido
    assert contenido.count('<th scope="col">') == 4
    assert 'aria-label="Cambiar de mes"' in contenido


def test_accesibilidad_teclado_y_sin_depender_del_color(empleado01):
    contenido = empleado01.get(reverse("calendario"), NOVIEMBRE).content.decode()
    # Navegación con enlaces y botones nativos (accesibles con Tab y Enter) y salto al contenido.
    assert 'href="#contenido"' in contenido
    assert 'tabindex="-1"' not in contenido
    # La franja se indica con texto, no solo con color.
    assert "Mañana (M)" in contenido
    assert "style=" not in contenido


def test_enlace_al_calendario_en_la_navegacion(empleado01):
    contenido = empleado01.get(reverse("inicio")).content.decode()
    assert reverse("calendario") in contenido
