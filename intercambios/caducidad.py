"""Caducidad automática de solicitudes de intercambio (US-009-AC-08)."""

import time

from django.db import OperationalError, transaction
from django.db.models import Q
from django.utils import timezone

from .models import ReservaTurno, SolicitudIntercambio

ESTADOS_ACTIVOS = (
    SolicitudIntercambio.Estado.PROPUESTA,
    SolicitudIntercambio.Estado.ACEPTADA,
)
MOTIVO_CADUCIDAD = "El primer turno ha comenzado antes de resolverse la solicitud."


def _aplicar_caducidad(pks, ahora):
    with transaction.atomic():
        actualizadas = SolicitudIntercambio.objects.filter(
            pk__in=pks,
            estado__in=ESTADOS_ACTIVOS,
        ).update(
            estado=SolicitudIntercambio.Estado.CADUCADA,
            ultima_accion="CADUCADA",
            fecha_ultima_accion=ahora,
            motivo_ultima_accion=MOTIVO_CADUCIDAD,
        )
        ReservaTurno.objects.filter(
            solicitud_id__in=pks,
            solicitud__estado=SolicitudIntercambio.Estado.CADUCADA,
        ).delete()
        return actualizadas


def caducar_vencidas(ahora=None) -> int:
    """Marca como caducadas las solicitudes cuyo primer turno ya ha comenzado.

    Libera las reservas asociadas y no modifica solicitudes ya terminadas.
    Es idempotente: llamadas repetidas o concurrentes solo transicionan cada
    solicitud activa una vez.
    """
    instante = timezone.now() if ahora is None else ahora
    for intento in range(3):
        try:
            pks = list(
                SolicitudIntercambio.objects.filter(estado__in=ESTADOS_ACTIVOS)
                .filter(
                    Q(turno_ofrecido__inicio__lte=instante)
                    | Q(turno_solicitado__inicio__lte=instante)
                )
                .values_list("pk", flat=True)
            )
            if not pks:
                return 0
            return _aplicar_caducidad(pks, instante)
        except OperationalError as error:
            if "locked" not in str(error).lower() or intento == 2:
                raise
            time.sleep(0.01)
    return 0
