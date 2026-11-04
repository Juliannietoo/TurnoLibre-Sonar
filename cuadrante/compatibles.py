"""Consulta de turnos de compañeros compatibles (US-006, RN-03)."""

from django.db import DatabaseError

from .models import Turno


class ConsultaNoDisponible(Exception):
    """La consulta ha fallado; no debe presentarse como una lista vacía (US-006-AC-03)."""


def turnos_compatibles(empleado, desde, hasta):
    """Turnos de otros empleados de la misma categoría y servicio que empiezan en [desde, hasta).

    Solo se cargan los datos que se muestran: fecha, franja, horario y nombre (US-006-AC-02).
    """
    try:
        return list(
            Turno.objects.filter(
                empleado__servicio_id=empleado.servicio_id,
                empleado__categoria_id=empleado.categoria_id,
                empleado__es_responsable=False,
                inicio__gte=desde,
                inicio__lt=hasta,
            )
            .exclude(empleado=empleado)
            .select_related("empleado")
            .only("fecha", "franja", "inicio", "fin", "empleado__nombre")
            .order_by("inicio", "empleado__nombre")
        )
    except DatabaseError as error:
        raise ConsultaNoDisponible(
            "No se han podido consultar los turnos de tus compañeros. "
            "Inténtalo de nuevo dentro de unos minutos."
        ) from error
