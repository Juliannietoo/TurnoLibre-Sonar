"""Mutaciones que impiden aceptar datos de demostración incoherentes."""

import importlib.util
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validar_cuadrante", ROOT / "tools/validar_cuadrante.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


@pytest.fixture
def data():
    return json.loads((ROOT / "data/demo/cuadrante.json").read_text(encoding="utf-8"))


def assert_rejected(data, rule):
    result = validator.validate(data)
    assert not result["ok"]
    assert any(error.startswith(rule) for error in result["errors"]), result["errors"]


def test_cuadrante_real_cumple_reglas(data):
    result = validator.validate(data)
    assert result["ok"], result["errors"]
    assert result["employees"] == 16
    assert result["assignments"] == 240
    assert result["days"] == 30
    assert result["min_rest_hours"] == 38
    assert (
        max(
            hours
            for weeks in result["weekly_hours"].values()
            for hours in weeks.values()
        )
        == 38
    )


def test_falta_cobertura(data):
    del data["asignaciones"][0]
    assert_rejected(data, "RN-04")


def test_duplicar_asignacion_no_simula_cobertura(data):
    removed = data["asignaciones"].pop(0)
    existing = next(
        item
        for item in data["asignaciones"]
        if item["fecha"] == removed["fecha"] and item["turno"] == removed["turno"]
    )
    data["asignaciones"].append(existing.copy())
    assert_rejected(data, "RN-04")
    assert_rejected(data, "RN-06")


def test_descanso_insuficiente(data):
    # M el lunes y T el domingo anterior: entre las 22:00 y las 08:00 solo hay 10 h.
    employee = next(
        item["empleado_id"]
        for item in data["asignaciones"]
        if item["fecha"] == "2026-11-02" and item["turno"] == "M"
    )
    data["asignaciones"].append(
        {"empleado_id": employee, "fecha": "2026-11-01", "turno": "T"}
    )
    assert_rejected(data, "RN-01")


def test_noche_domingo_se_reparte_en_dos_semanas():
    zone = ZoneInfo("Europe/Madrid")
    totals = validator.weekly_seconds(
        [
            (
                datetime(2026, 11, 1, 22, tzinfo=zone),
                datetime(2026, 11, 2, 8, tzinfo=zone),
            )
        ]
    )
    assert totals == {date(2026, 10, 26): 2 * 3600, date(2026, 11, 2): 8 * 3600}


def test_horas_semana_incluyen_noche_de_guarda(data):
    employee = "empleado01"
    data["asignaciones"] = [
        item for item in data["asignaciones"] if item["empleado_id"] != employee
    ]
    # Cinco mañanas suman 35 h; la noche del domingo anterior añade otras 8: 43 h.
    data["asignaciones"].append(
        {"empleado_id": employee, "fecha": "2026-11-01", "turno": "N"}
    )
    for day in range(2, 7):
        data["asignaciones"].append(
            {"empleado_id": employee, "fecha": f"2026-11-{day:02}", "turno": "M"}
        )
    assert_rejected(data, "RN-02")


def test_dos_turnos_misma_fecha_y_descanso_noche_manana(data):
    employee = next(
        item["empleado_id"]
        for item in data["asignaciones"]
        if item["fecha"] == "2026-11-02" and item["turno"] == "M"
    )
    data["asignaciones"].append(
        {"empleado_id": employee, "fecha": "2026-11-02", "turno": "N"}
    )
    data["asignaciones"].append(
        {"empleado_id": employee, "fecha": "2026-11-03", "turno": "M"}
    )
    assert_rejected(data, "RN-06")


@pytest.mark.parametrize(
    "field,value", [("categoria_id", "inexistente"), ("servicio_id", "otro")]
)
def test_referencias_invalidas(data, field, value):
    data["empleados"][0][field] = value
    assert_rejected(data, "FORMATO")


def test_guardas_no_pueden_faltar(data):
    data["asignaciones"] = [
        item for item in data["asignaciones"] if item["fecha"] != "2026-11-01"
    ]
    assert_rejected(data, "RN-04")


def test_rechaza_periodo_con_cambio_de_hora(data):
    # Desplazar dos semanas conserva lunes/domingo pero incluye el cambio del 25/10.
    for field in ("inicio", "fin"):
        data["periodo"][field] = str(
            date.fromisoformat(data["periodo"][field]) - timedelta(days=14)
        )
    for assignment in data["asignaciones"]:
        assignment["fecha"] = str(
            date.fromisoformat(assignment["fecha"]) - timedelta(days=14)
        )
    assert_rejected(data, "A-05")


@pytest.mark.parametrize("value", [None, [], {}, {"schema_version": 2}])
def test_entrada_invalida_nunca_es_cuadrante_correcto(value):
    assert_rejected(value, "FORMATO")
