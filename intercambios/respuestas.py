"""Respuesta a propuestas de intercambio (US-010)."""

import time

from django.db import OperationalError, transaction
from django.utils import timezone

from cuadrante.models import Empleado

from .caducidad import caducar_vencidas
from .models import ReservaTurno, SolicitudIntercambio
from .propuestas import PropuestaIntercambioError


class NoEsDestinatarioError(PropuestaIntercambioError):
    """El empleado no es el destinatario de la propuesta."""


class SolicitudNoPendienteError(PropuestaIntercambioError):
    """La solicitud ya no está pendiente de respuesta."""


def _estado_respuesta(acepta):
    return (
        SolicitudIntercambio.Estado.ACEPTADA
        if acepta
        else SolicitudIntercambio.Estado.RECHAZADA
    )


def _responder_una_vez(empleado, solicitud, acepta, motivo):
    nuevo_estado = _estado_respuesta(acepta)
    accion = "ACEPTADA" if acepta else "RECHAZADA"
    ahora = timezone.now()

    with transaction.atomic():
        actualizadas = SolicitudIntercambio.objects.filter(
            pk=solicitud.pk,
            estado=SolicitudIntercambio.Estado.PROPUESTA,
        ).update(
            estado=nuevo_estado,
            ultima_accion=accion,
            autor_ultima_accion=empleado,
            fecha_ultima_accion=ahora,
            motivo_ultima_accion=motivo,
        )

        if actualizadas:
            if not acepta:
                ReservaTurno.objects.filter(
                    solicitud_id=solicitud.pk,
                ).delete()

            solicitud.refresh_from_db()
            return solicitud

        actual = SolicitudIntercambio.objects.get(pk=solicitud.pk)

        # Repetir exactamente la misma respuesta es idempotente:
        # no cambia de nuevo el estado, la fecha, el autor ni las reservas.
        if (
            actual.estado == nuevo_estado
            and actual.autor_ultima_accion_id == empleado.id
        ):
            return actual

        raise SolicitudNoPendienteError(
            "La solicitud ya no está pendiente de respuesta."
        )


def responder_propuesta(
    empleado: Empleado,
    solicitud: SolicitudIntercambio,
    acepta: bool,
    motivo: str = "",
) -> SolicitudIntercambio:
    """Acepta o rechaza una propuesta pendiente.

    Antes de responder se aplican las caducidades vencidas.

    Solo el empleado destinatario puede responder. La transición se realiza
    únicamente desde PROPUESTA y de forma condicional, para que dos respuestas
    simultáneas no puedan modificar dos veces la misma solicitud.

    Al aceptar, la solicitud pasa a ACEPTADA y conserva sus reservas.
    Al rechazar, pasa a RECHAZADA y libera ambos turnos.

    Repetir la misma respuesta es idempotente.

    Excepciones:
        NoEsDestinatarioError:
            Si el empleado no es el destinatario de la propuesta.
        SolicitudNoPendienteError:
            Si la solicitud ya no admite una nueva respuesta.
    """
    caducar_vencidas()

    if solicitud.empleado_solicitado_id != empleado.id:
        raise NoEsDestinatarioError(
            "Solo el destinatario de la propuesta puede responderla."
        )

    motivo = motivo.strip()

    for intento in range(5):
        try:
            return _responder_una_vez(
                empleado,
                solicitud,
                acepta,
                motivo,
            )
        except OperationalError as error:
            if "locked" not in str(error).lower() or intento == 4:
                raise
            time.sleep(0.02)

    raise SolicitudNoPendienteError(
        "No se ha podido responder a la solicitud."
    )