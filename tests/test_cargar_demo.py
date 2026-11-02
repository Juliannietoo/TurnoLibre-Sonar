"""Carga y restablecimiento del cuadrante ficticio (US-003, TK-006)."""

from collections import Counter
from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

from cuadrante.models import Empleado, Turno

pytestmark = pytest.mark.django_db
MADRID = ZoneInfo("Europe/Madrid")


def test_carga_el_cuadrante_completo():
    call_command("cargar_demo")
    assert Empleado.objects.filter(es_responsable=False).count() == 16
    assert Empleado.objects.filter(es_responsable=True).count() == 1
    assert Turno.objects.count() == 240


def test_cobertura_3_3_2_cada_dia():
    call_command("cargar_demo")
    por_dia = Counter(Turno.objects.values_list("fecha", "franja"))
    for fecha in Turno.objects.values_list("fecha", flat=True).distinct():
        assert (por_dia[(fecha, "M")], por_dia[(fecha, "T")], por_dia[(fecha, "N")]) == (3, 3, 2)


def test_la_noche_termina_a_las_8_del_dia_siguiente_en_hora_de_madrid():
    call_command("cargar_demo")
    noche = Turno.objects.get(empleado__codigo="empleado15", fecha=date(2026, 11, 2))
    assert noche.franja == "N"
    assert noche.inicio == datetime(2026, 11, 2, 22, 0, tzinfo=MADRID)
    assert noche.fin == datetime(2026, 11, 3, 8, 0, tzinfo=MADRID)


def test_cuentas_con_rol_y_contrasena_argon2():
    call_command("cargar_demo", password="clave-demo")
    usuarios = get_user_model().objects
    empleado = usuarios.get(username="empleado01")
    responsable = usuarios.get(username="responsable01")
    assert empleado.groups.filter(name="Empleado").exists()
    assert responsable.groups.filter(name="Responsable").exists()
    assert empleado.password.startswith("argon2")
    assert empleado.check_password("clave-demo")


def test_restablecer_deja_los_datos_como_la_fuente_sin_duplicados():
    call_command("cargar_demo")
    Turno.objects.filter(fecha=date(2026, 11, 2)).delete()
    Empleado.objects.filter(codigo="empleado16").update(nombre="Cambiado")
    call_command("cargar_demo")
    assert Turno.objects.count() == 240
    assert Empleado.objects.get(codigo="empleado16").nombre == "Pablo Brisa"
    assert get_user_model().objects.filter(username__startswith="empleado").count() == 16
