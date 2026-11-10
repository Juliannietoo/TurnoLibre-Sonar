"""Validación en el servidor de las reglas de un intercambio (EP-004).

Un intercambio es una permuta uno a uno: el empleado A cede su turno ``turno_a`` y
recibe ``turno_b``; el empleado B cede ``turno_b`` y recibe ``turno_a``. Cada validador
devuelve la lista de incumplimientos; una lista vacía significa que la regla se cumple.
"""

from datetime import timedelta

from django.utils import timezone

from .incumplimiento import Incumplimiento

DESCANSO_MINIMO = timedelta(hours=12)
NOMBRE_FRANJA = {"M": "mañana", "T": "tarde", "N": "noche"}


def describir(turno):
    fecha = timezone.localtime(turno.inicio).strftime("%d/%m")
    return f"{NOMBRE_FRANJA.get(turno.franja, turno.franja)} del {fecha}"


def horas(intervalo):
    total = intervalo.total_seconds() / 3600
    return f"{total:g}"


def cuadrante_resultante(empleado, cede, recibe):
    """Turnos del empleado tras la permuta, ordenados por inicio."""
    turnos = [t for t in empleado.turnos.all() if t.pk != cede.pk]
    turnos.append(recibe)
    return sorted(turnos, key=lambda t: t.inicio)


def datos_incompletos(empleado, turnos):
    """RN-01 y RN-06 no se pueden comprobar sin inicio, fin y fecha (US-012, casos límite)."""
    return [
        Incumplimiento(
            "Datos incompletos",
            empleado.codigo,
            f"falta {campo} en el turno {turno.pk}; no se puede validar el intercambio.",
        )
        for turno in turnos
        for campo in ("inicio", "fin", "fecha")
        if getattr(turno, campo) is None
    ]


def validar_rn06(empleado, turnos):
    """Sin turnos solapados ni dos turnos con la misma fecha de inicio."""
    fallos = []
    for anterior, siguiente in zip(turnos, turnos[1:]):
        if anterior.fecha == siguiente.fecha:
            fallos.append(Incumplimiento(
                "RN-06",
                empleado.codigo,
                f"{empleado.nombre} tendría dos turnos el {siguiente.fecha:%d/%m} "
                f"({describir(anterior)} y {describir(siguiente)}).",
            ))
        elif siguiente.inicio < anterior.fin:
            fallos.append(Incumplimiento(
                "RN-06",
                empleado.codigo,
                f"{empleado.nombre} tendría solapados el turno de {describir(anterior)} "
                f"y el de {describir(siguiente)}.",
            ))
    return fallos


def validar_rn01(empleado, turnos, recibe):
    """Descanso mínimo de 12 h antes y después del turno recibido."""
    fallos = []
    for anterior, siguiente in zip(turnos, turnos[1:]):
        if recibe not in (anterior, siguiente) or siguiente.inicio < anterior.fin:
            continue  # los solapes los indica RN-06
        descanso = siguiente.inicio - anterior.fin
        if descanso < DESCANSO_MINIMO:
            fallos.append(Incumplimiento(
                "RN-01",
                empleado.codigo,
                f"Entre el turno de {describir(anterior)} y el de {describir(siguiente)}, "
                f"{empleado.nombre} solo tendría {horas(descanso)} h de descanso; "
                "el mínimo es 12 h.",
            ))
    return fallos


def validar_empleado(empleado, cede, recibe):
    turnos = cuadrante_resultante(empleado, cede, recibe)
    incompletos = datos_incompletos(empleado, turnos)
    if incompletos:
        return incompletos
    return validar_rn06(empleado, turnos) + validar_rn01(empleado, turnos, recibe)


def validar_descanso_y_solapes(turno_a, turno_b):
    """RN-01 y RN-06 sobre el cuadrante resultante de los dos empleados (US-012)."""
    return validar_empleado(turno_a.empleado, turno_a, turno_b) + validar_empleado(
        turno_b.empleado, turno_b, turno_a
    )
