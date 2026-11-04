"""Pruebas de RN-03 y de la conservación de la cobertura en la permuta (US-014)."""

from collections import Counter

import pytest
from django.test import override_settings

from cuadrante.demo import cargar, leer_fuente
from cuadrante.models import Categoria, Empleado, Servicio, Turno
from reglas.compatibilidad import validar_compatibilidad, validar_rn03

pytestmark = pytest.mark.django_db


@pytest.fixture
def perfiles():
    urgencias = Servicio.objects.create(codigo="urgencias", nombre="Urgencias")
    planta = Servicio.objects.create(codigo="planta", nombre="Planta")
    enfermeria = Categoria.objects.create(codigo="enfermeria", nombre="Enfermería")
    celador = Categoria.objects.create(codigo="celador", nombre="Celador")

    def empleado(codigo, servicio, categoria):
        return Empleado.objects.create(
            codigo=codigo, nombre=codigo.capitalize(), servicio=servicio, categoria=categoria
        )

    return {
        "ana": empleado("ana", urgencias, enfermeria),
        "berta": empleado("berta", urgencias, enfermeria),
        "carlos": empleado("carlos", urgencias, celador),
        "dora": empleado("dora", planta, enfermeria),
    }


def test_misma_categoria_y_servicio_cumple_rn03(perfiles):
    assert validar_rn03(perfiles["ana"], perfiles["berta"]) == []


def test_enfermera_y_celador_incumplen_rn03(perfiles):
    fallos = validar_rn03(perfiles["ana"], perfiles["carlos"])
    assert [f.regla for f in fallos] == ["RN-03"]
    assert "categorías distintas" in fallos[0].mensaje


def test_distinto_servicio_incumple_rn03(perfiles):
    fallos = validar_rn03(perfiles["ana"], perfiles["dora"])
    assert [f.regla for f in fallos] == ["RN-03"]
    assert "servicios distintos" in fallos[0].mensaje


def test_sin_categoria_no_se_puede_validar(perfiles):
    sin_categoria = Empleado.objects.create(
        codigo="rosa", nombre="Rosa", servicio=perfiles["ana"].servicio, es_responsable=True
    )
    fallos = validar_rn03(perfiles["ana"], sin_categoria)
    assert [f.regla for f in fallos] == ["Datos incompletos"]
    assert "no tiene categoría" in fallos[0].mensaje


@override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])
def test_la_permuta_compatible_conserva_la_cobertura_3_3_2():
    cargar(leer_fuente(), "clave-de-prueba")
    turnos = list(Turno.objects.select_related("empleado"))

    def cobertura(asignacion):
        """Personas por servicio, fecha y franja (RN-04)."""
        return Counter((e.servicio_id, t.fecha, t.franja) for t, e in asignacion)

    antes = [(t, t.empleado) for t in turnos]
    a = next(t for t in turnos if t.empleado.categoria.codigo == "enfermeria" and t.franja == "M")
    b = next(
        t for t in turnos
        if t.empleado.categoria == a.empleado.categoria and t.empleado != a.empleado
        and t.franja == "N"
    )
    assert validar_compatibilidad(a, b) == []

    # Permuta uno a uno: cada empleado se queda con el turno del otro.
    despues = [
        (t, b.empleado if t == a else a.empleado if t == b else e) for t, e in antes
    ]
    assert cobertura(despues) == cobertura(antes)
    franjas = Counter(franja for (_, _, franja) in cobertura(despues).elements())
    assert set(franjas) == {"M", "T", "N"}
