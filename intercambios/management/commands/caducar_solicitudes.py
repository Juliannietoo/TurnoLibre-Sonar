from django.core.management.base import BaseCommand

from intercambios.caducidad import caducar_vencidas


class Command(BaseCommand):
    help = (
        "Marca como caducadas las solicitudes activas cuyo primer turno ya ha comenzado "
        "y libera sus reservas (US-009-AC-08)."
    )

    def handle(self, *args, **options):
        caducadas = caducar_vencidas()
        if caducadas == 0:
            mensaje = "No hay solicitudes vencidas pendientes de caducar."
        else:
            mensaje = f"Solicitudes caducadas: {caducadas}."
        self.stdout.write(self.style.SUCCESS(mensaje))
