import os

from django.core.management.base import BaseCommand

from cuadrante.demo import FUENTE, cargar, leer_fuente


class Command(BaseCommand):
    help = (
        "Carga o restablece el cuadrante ficticio de demostración (US-003). Sustituye en una "
        "sola transacción el servicio, las categorías, los empleados, sus cuentas y los turnos."
    )

    def add_arguments(self, parser):
        parser.add_argument("--fuente", default=str(FUENTE), help="Ruta del JSON del cuadrante.")
        parser.add_argument(
            "--password",
            default=os.environ.get("TURNOLIBRE_DEMO_PASSWORD", "demo-turnolibre"),
            help="Contraseña de todas las cuentas ficticias (solo para la demostración).",
        )

    def handle(self, *args, **opciones):
        resumen = cargar(leer_fuente(opciones["fuente"]), opciones["password"])
        self.stdout.write(
            self.style.SUCCESS(
                f"Cuadrante de demostración cargado: {resumen['empleados']} empleados, "
                f"1 responsable y {resumen['turnos']} turnos."
            )
        )
