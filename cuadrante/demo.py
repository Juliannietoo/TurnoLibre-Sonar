"""Carga y restablecimiento del cuadrante ficticio de US-003 (contrato en data/demo/README.md)."""

import json
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction

from intercambios.models import SolicitudIntercambio

from .models import Categoria, Empleado, Servicio, Turno

FUENTE = Path(settings.BASE_DIR) / "data" / "demo" / "cuadrante.json"
GRUPO_EMPLEADO = "Empleado"
GRUPO_RESPONSABLE = "Responsable"


def leer_fuente(ruta=FUENTE):
    with open(ruta, encoding="utf-8") as fichero:
        datos = json.load(fichero)
    if datos.get("schema_version") != 1:
        raise ValueError("Versión de esquema no soportada")
    return datos


def instantes(fecha, franja, turnos, zona):
    """Inicio y fin conscientes de zona horaria; la noche termina al día siguiente."""
    horario = turnos[franja]
    inicio = datetime.combine(fecha, time.fromisoformat(horario["inicio"]), zona)
    dia_fin = fecha if horario["fin"] > horario["inicio"] else fecha + timedelta(days=1)
    fin = datetime.combine(dia_fin, time.fromisoformat(horario["fin"]), zona)
    return inicio, fin


@transaction.atomic
def cargar(datos, password):
    """Sustituye en una sola transacción los datos ficticios por los de la fuente."""
    zona = ZoneInfo(datos["timezone"])
    responsable = datos["responsable"]
    personas = [responsable, *datos["empleados"]]
    usuarios = get_user_model()

    SolicitudIntercambio.objects.all().delete()
    Turno.objects.all().delete()
    Empleado.objects.all().delete()
    Categoria.objects.all().delete()
    Servicio.objects.all().delete()
    usuarios.objects.filter(username__in=[p["id"] for p in personas]).delete()

    grupo_empleado, _ = Group.objects.get_or_create(name=GRUPO_EMPLEADO)
    grupo_responsable, _ = Group.objects.get_or_create(name=GRUPO_RESPONSABLE)
    servicio = Servicio.objects.create(
        codigo=datos["servicio"]["id"], nombre=datos["servicio"]["nombre"]
    )
    categorias = {
        c["id"]: Categoria.objects.create(codigo=c["id"], nombre=c["nombre"])
        for c in datos["categorias"]
    }

    empleados = {}
    for persona in personas:
        es_responsable = persona is responsable
        usuario = usuarios.objects.create_user(
            username=persona["id"], password=password, first_name=persona["nombre"]
        )
        usuario.groups.add(grupo_responsable if es_responsable else grupo_empleado)
        empleados[persona["id"]] = Empleado.objects.create(
            codigo=persona["id"],
            nombre=persona["nombre"],
            servicio=servicio,
            categoria=None if es_responsable else categorias[persona["categoria_id"]],
            es_responsable=es_responsable,
            usuario=usuario,
        )

    turnos = []
    for asignacion in datos["asignaciones"]:
        fecha = date.fromisoformat(asignacion["fecha"])
        inicio, fin = instantes(fecha, asignacion["turno"], datos["turnos"], zona)
        turnos.append(
            Turno(
                empleado=empleados[asignacion["empleado_id"]],
                fecha=fecha,
                franja=asignacion["turno"],
                inicio=inicio,
                fin=fin,
            )
        )
    Turno.objects.bulk_create(turnos)
    return {"empleados": len(datos["empleados"]), "turnos": len(turnos)}
