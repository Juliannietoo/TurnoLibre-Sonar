"""Pruebas de acceso y autorización (US-002)."""

import pytest
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import reverse

from cuadrante.demo import cargar, leer_fuente

CLAVE = "clave-de-prueba"

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def datos():
    # Las pruebas usan un hash rápido; Argon2 se comprueba en test_smoke y test_cargar_demo.
    with override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]):
        cargar(leer_fuente(), CLAVE)
        yield


def entrar(client, usuario, clave=CLAVE):
    return client.post(reverse("entrar"), {"username": usuario, "password": clave}, follow=True)


def test_ac01_empleado_entra_y_no_ve_opciones_del_responsable(client):
    respuesta = entrar(client, "empleado01")
    contenido = respuesta.content.decode()
    assert respuesta.wsgi_request.user.username == "empleado01"
    assert "Ana Vega" in contenido
    assert "empleado" in contenido
    assert reverse("panel_responsable") not in contenido


def test_ac02_responsable_entra_con_su_rol_y_servicio(client):
    contenido = entrar(client, "responsable01").content.decode()
    assert "responsable" in contenido
    assert "Urgencias" in contenido
    assert reverse("panel_responsable") in contenido
    assert client.get(reverse("panel_responsable")).status_code == 200


@pytest.mark.parametrize("usuario, clave", [("empleado01", "mala"), ("noexiste", CLAVE)])
def test_ac03_credenciales_incorrectas_mensaje_generico(client, usuario, clave):
    respuesta = entrar(client, usuario, clave)
    assert "Usuario o contraseña incorrectos." in respuesta.content.decode()
    assert not respuesta.wsgi_request.user.is_authenticated


def test_ac04_sin_sesion_redirige_al_inicio_de_sesion(client):
    for url in (reverse("inicio"), reverse("panel_responsable")):
        respuesta = client.get(url)
        assert respuesta.status_code == 302
        assert respuesta.url.startswith(reverse("entrar"))


def test_ac05_empleado_no_puede_usar_operaciones_del_responsable(client):
    entrar(client, "empleado01")
    assert client.get(reverse("panel_responsable")).status_code == 403


def test_ac09_cerrar_sesion_invalida_el_acceso(client):
    entrar(client, "empleado01")
    client.post(reverse("salir"))
    assert client.get(reverse("inicio")).status_code == 302


def test_usuario_con_mayusculas_y_espacios_se_normaliza(client):
    respuesta = entrar(client, "  EMPLEADO01 ")
    assert respuesta.wsgi_request.user.username == "empleado01"


def test_la_contrasena_no_se_normaliza(client):
    assert not entrar(client, "empleado01", CLAVE.upper()).wsgi_request.user.is_authenticated


def test_formulario_accesible_con_etiquetas(client):
    contenido = client.get(reverse("entrar")).content.decode()
    assert '<label for="id_username">' in contenido
    assert '<label for="id_password">' in contenido
    assert 'lang="es"' in contenido


def test_las_contrasenas_no_se_guardan_en_claro():
    assert CLAVE not in get_user_model().objects.get(username="empleado01").password
