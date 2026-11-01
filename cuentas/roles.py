"""Roles de TurnoLibre y control de acceso en el servidor (US-002, NFR-001)."""

from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

EMPLEADO = "Empleado"
RESPONSABLE = "Responsable"


def tiene_rol(usuario, rol):
    return usuario.is_authenticated and usuario.groups.filter(name=rol).exists()


def es_responsable(usuario):
    return tiene_rol(usuario, RESPONSABLE)


def es_empleado(usuario):
    return tiene_rol(usuario, EMPLEADO)


def requiere_rol(rol):
    """Exige sesión iniciada y el rol indicado; si falta el rol, responde 403."""

    def decorador(vista):
        @login_required
        @wraps(vista)
        def envoltura(request, *args, **kwargs):
            if not tiene_rol(request.user, rol):
                raise PermissionDenied
            return vista(request, *args, **kwargs)

        return envoltura

    return decorador


solo_empleado = requiere_rol(EMPLEADO)
solo_responsable = requiere_rol(RESPONSABLE)
