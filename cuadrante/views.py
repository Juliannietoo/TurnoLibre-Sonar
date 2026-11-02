from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from .models import Turno


def mes_pedido(valor):
    """Interpreta ?mes=AAAA-MM; si falta o no es válido, usa el mes actual."""
    try:
        anio, mes = (int(parte) for parte in valor.split("-"))
        return date(anio, mes, 1)
    except (AttributeError, ValueError):
        return timezone.localdate().replace(day=1)


def desplazar(primero, meses):
    indice = primero.year * 12 + primero.month - 1 + meses
    return date(indice // 12, indice % 12 + 1, 1)


@login_required
def calendario(request):
    """Turnos propios del mes en formato lista (US-005, D-18)."""
    primero = mes_pedido(request.GET.get("mes"))
    siguiente = desplazar(primero, 1)
    empleado = getattr(request.user, "empleado", None)
    turnos = Turno.objects.none()
    if empleado is not None:
        turnos = (
            Turno.objects.filter(empleado=empleado, fecha__gte=primero, fecha__lt=siguiente)
            .select_related("empleado__servicio")
            .order_by("fecha")
        )
    return render(
        request,
        "cuadrante/calendario.html",
        {
            "empleado": empleado,
            "mes": primero,
            "anterior": desplazar(primero, -1),
            "siguiente": siguiente,
            "turnos": turnos,
        },
    )
