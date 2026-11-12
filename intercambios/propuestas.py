"""Creación de propuestas de intercambio (US-009)."""

from django.db import IntegrityError, OperationalError, transaction
from django.utils import timezone

from cuadrante.models import Empleado, Turno
from reglas.compatibilidad import validar_rn03

from .models import ReservaTurno, SolicitudIntercambio


class PropuestaIntercambioError(Exception):
    """Error de negocio al intentar crear una propuesta de intercambio."""


class TurnoNoValidoError(PropuestaIntercambioError):
    """Alguno de los turnos no puede participar en la propuesta."""


class IncompatibilidadRN03Error(PropuestaIntercambioError):
    """Los empleados incumplen RN-03: categoría o servicio incompatibles."""


class TurnoNoDisponibleError(PropuestaIntercambioError):
    """Alguno de los turnos ya está reservado por otra solicitud activa."""


class ConflictoConcurrenciaError(PropuestaIntercambioError):
    """No se pudo completar la propuesta por un conflicto concurrente."""


def _validar_propuesta(empleado, turno_propio, turno_companero):
    if turno_propio.empleado_id != empleado.id:
        raise TurnoNoValidoError(
            "El turno ofrecido no pertenece al empleado que realiza la propuesta."
        )

    if turno_companero.empleado_id == empleado.id:
        raise TurnoNoValidoError(
            "El turno solicitado debe pertenecer a otro empleado."
        )

    ahora = timezone.now()
    if turno_propio.inicio <= ahora or turno_companero.inicio <= ahora:
        raise TurnoNoValidoError(
            "Los dos turnos deben ser futuros."
        )

    incumplimientos = validar_rn03(
        turno_propio.empleado,
        turno_companero.empleado,
    )
    if incumplimientos:
        raise IncompatibilidadRN03Error(
            "Los empleados no cumplen RN-03: deben pertenecer "
            "a la misma categoría y al mismo servicio."
        )


def _alguno_reservado(turno_propio, turno_companero):
    return ReservaTurno.objects.filter(
        turno_id__in=[turno_propio.id, turno_companero.id]
    ).exists()


@transaction.atomic
def _crear_propuesta(empleado, turno_propio, turno_companero):
    if _alguno_reservado(turno_propio, turno_companero):
        raise TurnoNoDisponibleError(
            "El turno ya no está disponible."
        )

    solicitud = SolicitudIntercambio.objects.create(
        turno_ofrecido=turno_propio,
        turno_solicitado=turno_companero,
        empleado_proponente=empleado,
        empleado_solicitado=turno_companero.empleado,
        estado=SolicitudIntercambio.Estado.PROPUESTA,
        ultima_accion="PROPUESTA",
        autor_ultima_accion=empleado,
    )

    ReservaTurno.objects.create(
        solicitud=solicitud,
        turno=turno_propio,
    )
    ReservaTurno.objects.create(
        solicitud=solicitud,
        turno=turno_companero,
    )

    return solicitud


def proponer_intercambio(
    empleado: Empleado,
    turno_propio: Turno,
    turno_companero: Turno,
) -> SolicitudIntercambio:
    """Crea una propuesta y reserva sus dos turnos de forma atómica.

    Excepciones:
        TurnoNoValidoError:
            Si los turnos no cumplen las condiciones básicas.
        IncompatibilidadRN03Error:
            Si los empleados no cumplen RN-03.
        TurnoNoDisponibleError:
            Si alguno de los turnos está reservado.
        ConflictoConcurrenciaError:
            Si persiste un conflicto de base de datos.
    """
    _validar_propuesta(empleado, turno_propio, turno_companero)

    for intento in range(2):
        try:
            return _crear_propuesta(
                empleado,
                turno_propio,
                turno_companero,
            )
        except IntegrityError as error:
            raise TurnoNoDisponibleError(
                "El turno ya no está disponible."
            ) from error
        except OperationalError as error:
            if "locked" not in str(error).lower():
                raise ConflictoConcurrenciaError(
                    "No se ha podido completar la propuesta."
                ) from error

            try:
                if _alguno_reservado(turno_propio, turno_companero):
                    raise TurnoNoDisponibleError(
                        "El turno ya no está disponible."
                    ) from error
            except OperationalError:
                pass

            if intento == 1:
                raise ConflictoConcurrenciaError(
                    "No se ha podido completar la propuesta "
                    "por un conflicto concurrente."
                ) from error

    raise ConflictoConcurrenciaError(
        "No se ha podido completar la propuesta."
    )