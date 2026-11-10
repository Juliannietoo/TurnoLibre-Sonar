"""RN-03: solo intercambian empleados de la misma categoría y el mismo servicio (US-014).

RN-04 (cobertura 3/3/2) no se valida por intercambio: la garantiza el cuadrante de partida
(US-003) y una permuta uno a uno dentro de la misma categoría y servicio no la cambia (D-18).
"""

from .incumplimiento import Incumplimiento


def validar_rn03(empleado_a, empleado_b):
    """Devuelve los incumplimientos de RN-03 entre los dos empleados del intercambio."""
    faltan = [
        Incumplimiento(
            "Datos incompletos",
            empleado.codigo,
            f"{empleado.nombre} no tiene {campo}; no se puede validar RN-03.",
        )
        for empleado in (empleado_a, empleado_b)
        for campo, valor in (
            ("categoría", empleado.categoria_id),
            ("servicio", empleado.servicio_id),
        )
        if valor is None
    ]
    if faltan:
        return faltan

    fallos = []
    if empleado_a.categoria_id != empleado_b.categoria_id:
        fallos.append(Incumplimiento(
            "RN-03",
            empleado_a.codigo,
            f"{empleado_a.nombre} ({empleado_a.categoria}) y {empleado_b.nombre} "
            f"({empleado_b.categoria}) son de categorías distintas.",
        ))
    if empleado_a.servicio_id != empleado_b.servicio_id:
        fallos.append(Incumplimiento(
            "RN-03",
            empleado_a.codigo,
            f"{empleado_a.nombre} ({empleado_a.servicio}) y {empleado_b.nombre} "
            f"({empleado_b.servicio}) son de servicios distintos.",
        ))
    return fallos


def validar_compatibilidad(turno_a, turno_b):
    """RN-03 aplicada a los dos turnos de un intercambio."""
    return validar_rn03(turno_a.empleado, turno_b.empleado)
