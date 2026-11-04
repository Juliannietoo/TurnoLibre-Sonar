"""Resultado común de los validadores de reglas (EP-004)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Incumplimiento:
    """Regla incumplida, empleado afectado y explicación para el usuario (NFR-005)."""

    regla: str
    empleado: str
    mensaje: str

    def __str__(self):
        return f"{self.regla}: {self.mensaje}"
