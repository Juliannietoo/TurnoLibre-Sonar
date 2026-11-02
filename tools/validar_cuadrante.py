"""Comprueba el diseño ficticio de US-003; no valida la carga de Django (TK-006)."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import UTC, date, datetime, time, timedelta
from itertools import pairwise
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]
SHIFT_TIMES = {
    "M": ("08:00", "15:00", 7),
    "T": ("15:00", "22:00", 7),
    "N": ("22:00", "08:00", 10),
}
MINIMUM_COVERAGE = {"M": 3, "T": 3, "N": 2}


def weekly_seconds(intervals: list[tuple[datetime, datetime]]) -> dict[date, float]:
    """Reparte tiempo real en semanas locales, incluso una noche domingo-lunes."""
    totals: dict[date, float] = defaultdict(float)
    for start, end in intervals:
        cursor = start
        while cursor < end:
            monday = cursor.date() - timedelta(days=cursor.weekday())
            boundary = datetime.combine(
                monday + timedelta(days=7), time(), cursor.tzinfo
            )
            stop = min(end, boundary)
            totals[monday] += (
                stop.astimezone(UTC) - cursor.astimezone(UTC)
            ).total_seconds()
            cursor = stop
    return dict(totals)


def validate(data: dict) -> dict:
    """Devuelve errores y métricas; los errores de entrada nunca equivalen a éxito."""
    errors: list[str] = []
    result = {
        "ok": False,
        "errors": errors,
        "employees": 0,
        "assignments": 0,
        "days": 0,
        "weeks": [],
        "weekly_hours": {},
        "min_rest_hours": None,
    }
    if not isinstance(data, dict):
        errors.append("FORMATO: la raíz debe ser un objeto JSON")
        return result
    try:
        if data["schema_version"] != 1 or data["timezone"] != "Europe/Madrid":
            raise ValueError("se requiere schema_version=1 y timezone=Europe/Madrid")
        zone = ZoneInfo(data["timezone"])
        first = date.fromisoformat(data["periodo"]["inicio"])
        last = date.fromisoformat(data["periodo"]["fin"])
        if first.weekday() != 0 or last.weekday() != 6 or first > last:
            raise ValueError(
                "el período central debe contener semanas completas de lunes a domingo"
            )
        service = data["servicio"]["id"]
        if not isinstance(service, str) or not service:
            raise ValueError("el servicio debe tener un identificador")
        categories = {item["id"] for item in data["categorias"]}
        if len(data["categorias"]) != 2 or len(categories) != 2:
            raise ValueError("deben existir exactamente dos categorías distintas")
        manager = data["responsable"]
        if (
            manager["servicio_id"] != service
            or not manager["id"]
            or not manager["nombre"]
        ):
            raise ValueError("se requiere un responsable del servicio")
        employees = {item["id"]: item for item in data["empleados"]}
        if not employees or len(employees) != len(data["empleados"]):
            raise ValueError("empleados vacíos o identificadores repetidos")
        if manager["id"] in employees:
            raise ValueError(
                "el responsable no debe contarse como empleado del cuadrante"
            )
        for employee in employees.values():
            if (
                not employee["id"]
                or not employee["nombre"]
                or employee["servicio_id"] != service
                or employee["categoria_id"] not in categories
            ):
                raise ValueError("empleado sin nombre, categoría o servicio válidos")
        if {item["categoria_id"] for item in employees.values()} != categories:
            raise ValueError("ambas categorías deben tener empleados")
        if set(data["turnos"]) != set(SHIFT_TIMES):
            raise ValueError("deben definirse las franjas M, T y N")
        for code, expected in SHIFT_TIMES.items():
            shift = data["turnos"][code]
            if (shift["inicio"], shift["fin"], shift["horas"]) != expected:
                raise ValueError(f"horario o duración incorrectos de {code}")
        assignments = data["asignaciones"]
        if not isinstance(assignments, list):
            raise TypeError("asignaciones debe ser una lista")
    except (KeyError, TypeError, ValueError, ZoneInfoNotFoundError) as exc:
        errors.append(f"FORMATO: {exc}")
        return result

    guard_first, guard_last = first - timedelta(days=1), last + timedelta(days=1)
    expected_days = [
        guard_first + timedelta(days=i)
        for i in range((guard_last - guard_first).days + 1)
    ]
    for day in expected_days:
        start = datetime.combine(day, time(), zone)
        end = datetime.combine(day + timedelta(days=1), time(), zone)
        if start.utcoffset() != end.utcoffset():
            errors.append(
                f"A-05: cambio de hora el {day}; no se admite en los datos de demostración"
            )

    coverage: dict[tuple[date, str], set[str]] = defaultdict(set)
    by_employee: dict[str, list[tuple[datetime, datetime]]] = defaultdict(list)
    starts: Counter = Counter()
    seen: set[tuple[str, date, str]] = set()
    for index, assignment in enumerate(assignments, 1):
        try:
            employee_id = assignment["empleado_id"]
            day = date.fromisoformat(assignment["fecha"])
            code = assignment["turno"]
            if employee_id not in employees or code not in SHIFT_TIMES:
                raise ValueError("referencia a empleado o franja inexistentes")
            if not guard_first <= day <= guard_last:
                raise ValueError("fecha fuera del período y sus dos días de guarda")
            key = (employee_id, day, code)
            if key in seen:
                errors.append(f"RN-06: asignación duplicada {employee_id} {day} {code}")
            seen.add(key)
            starts[employee_id, day] += 1
            start_text, end_text, _ = SHIFT_TIMES[code]
            start = datetime.combine(day, time.fromisoformat(start_text), zone)
            end_day = day + timedelta(days=code == "N")
            end = datetime.combine(end_day, time.fromisoformat(end_text), zone)
            coverage[day, code].add(employee_id)
            by_employee[employee_id].append((start, end))
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(f"FORMATO: asignación {index}: {exc}")

    for day in expected_days:
        for code, minimum in MINIMUM_COVERAGE.items():
            count = len(coverage[day, code])
            if count < minimum:
                errors.append(
                    f"RN-04: {day} {code}: cobertura {count}, mínimo {minimum}"
                )
    for (employee_id, day), count in starts.items():
        if count > 1:
            errors.append(
                f"RN-06: {employee_id} tiene {count} turnos con inicio el {day}"
            )

    rest_hours: list[float] = []
    core_weeks = [
        first + timedelta(days=i) for i in range(0, (last - first).days + 1, 7)
    ]
    weekly = {}
    for employee_id in employees:
        intervals = sorted(by_employee[employee_id])
        for previous, current in pairwise(intervals):
            elapsed = (
                current[0].astimezone(UTC) - previous[1].astimezone(UTC)
            ).total_seconds()
            rest_hours.append(elapsed / 3600)
            if elapsed < 0:
                errors.append(f"RN-06: solape de {employee_id} el {current[0].date()}")
            if elapsed < 12 * 3600:
                errors.append(
                    f"RN-01: {employee_id} solo descansa {elapsed / 3600:g} h "
                    f"antes de {current[0].isoformat()}"
                )
        totals = weekly_seconds(intervals)
        weekly[employee_id] = {
            str(week): totals.get(week, 0) / 3600 for week in core_weeks
        }
        for week in core_weeks:
            hours = totals.get(week, 0) / 3600
            if hours > 40:
                errors.append(
                    f"RN-02: {employee_id}, semana {week}: {hours:g} h > 40 h"
                )

    result.update(
        ok=not errors,
        employees=len(employees),
        assignments=len(assignments),
        days=len(expected_days),
        weeks=[str(week) for week in core_weeks],
        weekly_hours=weekly,
        min_rest_hours=min(rest_hours) if rest_hours else None,
    )
    return result


def markdown_report(result: dict) -> str:
    """Evidencia del diseño; la carga y restablecimiento se comprueban después de TK-006."""
    lines = [
        "# TK-007 · Comprobación del diseño de cuadrante",
        "",
        "Trazabilidad: GC02-186 · US-003-AC-02 · RN-01, RN-02, RN-04 y RN-06.",
        "",
        f"Resultado del diseño: **{'CORRECTO' if result['ok'] else 'CON ERRORES'}**.",
        "",
        (
            f"{result['employees']} empleados; {result['assignments']} asignaciones; "
            f"{result['days']} fechas, incluidos los dos días de guarda."
        ),
        "",
        (
            "Se comprueban las semanas centrales completas. Los días de guarda "
            "permiten comprobar descansos en los extremos y repartir la noche del domingo anterior."
        ),
        "",
        "| Empleado | " + " | ".join(result["weeks"]) + " |",
        "|---|" + "---:|" * len(result["weeks"]),
    ]
    for employee_id, weeks in sorted(result["weekly_hours"].items()):
        lines.append(
            f"| {employee_id} | "
            + " | ".join(f"{hours:g} h" for hours in weeks.values())
            + " |"
        )
    lines.extend(
        [
            "",
            f"Descanso mínimo observado: {result['min_rest_hours']} h.",
            "",
            (
                "La cobertura usa empleados distintos por fecha y franja. Las horas se calculan "
                "con tiempo UTC realmente transcurrido y semanas locales Europe/Madrid."
            ),
            "",
        ]
    )
    if result["errors"]:
        lines.extend(
            ["## Errores", "", *[f"- {error}" for error in result["errors"]], ""]
        )
    lines.extend(
        [
            "## Pendiente de integración",
            "",
            (
                "Esta evidencia valida el JSON de diseño. TK-007 continúa pendiente de comprobar "
                "que el comando de Django de TK-006 carga y restablece esos mismos datos "
                "sin pérdidas ni duplicados. No acredita US-003-AC-03 ni completa la "
                "historia US-003."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "archivo", nargs="?", type=Path, default=ROOT / "data/demo/cuadrante.json"
    )
    parser.add_argument(
        "--report", type=Path, help="Guardar evidencia Markdown del diseño"
    )
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.archivo.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FORMATO: {exc}")
        return 1
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(markdown_report(result), encoding="utf-8")
    print(
        f"{'CORRECTO' if result['ok'] else 'ERROR'}: {result['employees']} empleados, "
        f"{result['assignments']} asignaciones, {result['days']} fechas"
    )
    for error in result["errors"]:
        print(error)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
