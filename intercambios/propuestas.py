"""Creación de propuestas de intercambio (US-009)."""

from cuadrante.models import Empleado, Turno

from .models import SolicitudIntercambio


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


def proponer_intercambio(
    empleado: Empleado,
    turno_propio: Turno,
    turno_companero: Turno,
) -> SolicitudIntercambio:
    """Crea una propuesta de intercambio y reserva sus dos turnos.

    Contrato:
    - ``turno_propio`` debe pertenecer a ``empleado``.
    - ``turno_companero`` debe pertenecer a otro empleado.
    - Ambos turnos deben ser futuros.
    - Los dos empleados deben cumplir RN-03.
    - Ninguno de los turnos puede estar reservado por otra solicitud activa.
    - La solicitud y sus dos reservas se crean en una única transacción.

    Devuelve:
        La ``SolicitudIntercambio`` creada en estado ``PROPUESTA``.

    Excepciones:
        TurnoNoValidoError:
            Si los turnos no cumplen las condiciones básicas.
        IncompatibilidadRN03Error:
            Si los empleados no cumplen RN-03.
        TurnoNoDisponibleError:
            Si alguno de los turnos ya no está disponible.
        ConflictoConcurrenciaError:
            Si persiste un conflicto de base de datos durante la operación.
    """
    raise NotImplementedError("Lógica de proponer_intercambio pendiente de completar.")