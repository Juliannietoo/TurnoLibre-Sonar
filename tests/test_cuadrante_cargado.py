"""TK-007: las reglas RN-01, RN-02, RN-04 y RN-06 se cumplen con los datos cargados en Django."""

import importlib.util
from datetime import date
from pathlib import Path

import pytest
from django.core.management import call_command

from cuadrante.demo import leer_fuente
from cuadrante.models import Empleado, Turno

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validar_cuadrante", ROOT / "tools/validar_cuadrante.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

pytestmark = pytest.mark.django_db


def cuadrante_persistido():
    """Reconstruye desde la base de datos el mismo formato que data/demo/cuadrante.json."""
    datos = leer_fuente()
    datos["empleados"] = [
        {
            "id": e.codigo,
            "nombre": e.nombre,
            "servicio_id": e.servicio.codigo,
            "categoria_id": e.categoria.codigo,
        }
        for e in Empleado.objects.filter(es_responsable=False).select_related(
            "servicio", "categoria"
        )
    ]
    datos["asignaciones"] = [
        {"empleado_id": t.empleado.codigo, "fecha": t.fecha.isoformat(), "turno": t.franja}
        for t in Turno.objects.select_related("empleado")
    ]
    return datos


def test_los_datos_cargados_cumplen_las_reglas():
    call_command("cargar_demo")
    resultado = validator.validate(cuadrante_persistido())
    assert resultado["ok"], resultado["errors"]
    assert resultado["assignments"] == 240


def test_los_datos_restablecidos_cumplen_las_reglas():
    call_command("cargar_demo")
    Turno.objects.filter(fecha=date(2026, 11, 10)).delete()
    assert not validator.validate(cuadrante_persistido())["ok"]
    call_command("cargar_demo")
    resultado = validator.validate(cuadrante_persistido())
    assert resultado["ok"], resultado["errors"]
