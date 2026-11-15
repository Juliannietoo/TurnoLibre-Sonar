from django.db import models

from cuadrante.models import Empleado, Turno


class SolicitudIntercambio(models.Model):
    """Solicitud de intercambio de dos turnos entre empleados."""

    class Estado(models.TextChoices):
        PROPUESTA = "PROPUESTA", "Propuesta"
        ACEPTADA = "ACEPTADA", "Aceptada"
        APROBADA = "APROBADA", "Aprobada"
        RECHAZADA = "RECHAZADA", "Rechazada"
        CADUCADA = "CADUCADA", "Caducada"

    turno_ofrecido = models.ForeignKey(
        Turno,
        on_delete=models.PROTECT,
        related_name="solicitudes_como_ofrecido",
    )
    turno_solicitado = models.ForeignKey(
        Turno,
        on_delete=models.PROTECT,
        related_name="solicitudes_como_solicitado",
    )
    empleado_proponente = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name="solicitudes_propuestas",
    )
    empleado_solicitado = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name="solicitudes_recibidas",
    )

    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.PROPUESTA,
    )

    ultima_accion = models.CharField(max_length=32, default="PROPUESTA")
    autor_ultima_accion = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name="acciones_intercambio",
    )
    fecha_ultima_accion = models.DateTimeField(auto_now_add=True)
    motivo_ultima_accion = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha_ultima_accion"]

    def __str__(self):
        return (
            f"{self.empleado_proponente.codigo}: "
            f"{self.turno_ofrecido_id} -> {self.turno_solicitado_id}"
        )


class ReservaTurno(models.Model):
    """Reserva exclusiva de un turno mientras una solicitud está activa."""

    solicitud = models.ForeignKey(
        SolicitudIntercambio,
        on_delete=models.CASCADE,
        related_name="reservas",
    )
    turno = models.OneToOneField(
        Turno,
        on_delete=models.CASCADE,
        related_name="reserva_intercambio",
    )
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva turno {self.turno_id} · solicitud {self.solicitud_id}"