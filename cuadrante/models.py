from django.conf import settings
from django.db import models


class Servicio(models.Model):
    codigo = models.SlugField(unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    codigo = models.SlugField(unique=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    """Persona del hospital; el responsable del servicio no tiene categoría ni turnos."""

    codigo = models.SlugField(unique=True)
    nombre = models.CharField(max_length=100)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name="empleados")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, null=True, blank=True, related_name="empleados"
    )
    es_responsable = models.BooleanField(default=False)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="empleado",
    )

    class Meta:
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Turno(models.Model):
    class Franja(models.TextChoices):
        MANANA = "M", "Mañana"
        TARDE = "T", "Tarde"
        NOCHE = "N", "Noche"

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="turnos")
    fecha = models.DateField(help_text="Fecha de inicio del turno, en hora local de Madrid.")
    franja = models.CharField(max_length=1, choices=Franja.choices)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    class Meta:
        ordering = ["fecha", "inicio", "empleado__codigo"]
        constraints = [
            models.UniqueConstraint(
                fields=["empleado", "fecha"], name="un_turno_por_empleado_y_dia"
            ),
            models.CheckConstraint(
                condition=models.Q(fin__gt=models.F("inicio")), name="fin_posterior_al_inicio"
            ),
        ]

    def __str__(self):
        return f"{self.empleado.codigo} {self.fecha} {self.franja}"
