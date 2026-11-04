"""Pruebas de la consulta de turnos compatibles (US-006)."""

from datetime import datetime
from unittest import mock
from zoneinfo import ZoneInfo

import pytest
from django.db import DatabaseError
from django.test import override_settings

from cuadrante.compatibles import ConsultaNoDisponible, turnos_compatibles
from cuadrante.demo import cargar, leer_fuente
from cuadrante.models import Empleado

MADRID = ZoneInfo("Europe/Madrid")
NOVIEMBRE = (datetime(2026, 11, 1, tzinfo=MADRID), datetime(2026, 12, 1, tzinfo=MADRID))

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def datos():
    with override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]):
        cargar(leer_fuente(), "clave-de-prueba")


def empleado(codigo):
    return Empleado.objects.get(codigo=codigo)


def test_ac01_solo_companeros_de_la_misma_categoria_y_servicio():
    ana = empleado("empleado01")
    turnos = turnos_compatibles(ana, *NOVIEMBRE)
    assert turnos
    assert {t.empleado.categoria_id for t in turnos} == {ana.categoria_id}
    assert {t.empleado.servicio_id for t in turnos} == {ana.servicio_id}


def test_no_aparecen_los_turnos_propios():
    ana = empleado("empleado01")
    assert all(t.empleado_id != ana.pk for t in turnos_compatibles(ana, *NOVIEMBRE))


def test_otra_categoria_ve_otros_companeros():
    auxiliar = empleado("empleado03")
    turnos = turnos_compatibles(auxiliar, *NOVIEMBRE)
    assert {t.empleado.categoria.codigo for t in turnos} == {"auxiliar"}


def test_solo_turnos_que_empiezan_dentro_del_intervalo():
    ana = empleado("empleado01")
    desde = datetime(2026, 11, 20, tzinfo=MADRID)
    turnos = turnos_compatibles(ana, desde, NOVIEMBRE[1])
    assert turnos
    assert all(desde <= t.inicio < NOVIEMBRE[1] for t in turnos)


def test_ac03_sin_turnos_devuelve_lista_vacia():
    diciembre = (datetime(2026, 12, 1, tzinfo=MADRID), datetime(2027, 1, 1, tzinfo=MADRID))
    assert turnos_compatibles(empleado("empleado01"), *diciembre) == []


def test_ac03_un_fallo_no_se_confunde_con_una_lista_vacia():
    with mock.patch("cuadrante.compatibles.Turno.objects.filter", side_effect=DatabaseError):
        with pytest.raises(ConsultaNoDisponible, match="No se han podido consultar"):
            turnos_compatibles(empleado("empleado01"), *NOVIEMBRE)
