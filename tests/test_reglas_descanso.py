"""Pruebas de RN-01 (descanso de 12 h) y RN-06 (sin solapes) sobre un intercambio (US-012)."""

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

import pytest

from cuadrante.models import Categoria, Empleado, Servicio, Turno
from reglas.validadores import validar_descanso_y_solapes

MADRID = ZoneInfo("Europe/Madrid")
HORARIO = {"M": (time(8), time(15)), "T": (time(15), time(22)), "N": (time(22), time(8))}

pytestmark = pytest.mark.django_db


def instante(dia, hora):
    return datetime.combine(dia, hora, MADRID)


def turno(empleado, dia, franja):
    dia = date.fromisoformat(dia)
    inicio, fin = HORARIO[franja]
    dia_fin = dia + timedelta(days=1) if franja == "N" else dia
    return Turno.objects.create(
        empleado=empleado,
        fecha=dia,
        franja=franja,
        inicio=instante(dia, inicio),
        fin=instante(dia_fin, fin),
    )


@pytest.fixture
def plantilla():
    servicio = Servicio.objects.create(codigo="urgencias", nombre="Urgencias")
    categoria = Categoria.objects.create(codigo="enfermeria", nombre="Enfermería")

    def empleado(codigo, nombre):
        return Empleado.objects.create(
            codigo=codigo, nombre=nombre, servicio=servicio, categoria=categoria
        )

    return empleado("ana", "Ana"), empleado("luis", "Luis")


def reglas(fallos):
    return sorted({fallo.regla for fallo in fallos})


# Casos de ejemplo de business-rules.md: Ana trabaja la noche del lunes 02/11
# (termina el martes 03/11 a las 08:00) y cede su mañana del jueves 05/11.


def test_rn01_noche_seguida_de_manana_cero_horas(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "N")
    cedido = turno(ana, "2026-11-05", "M")
    recibido = turno(luis, "2026-11-03", "M")
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-01"]
    assert "0 h de descanso" in fallos[0].mensaje
    assert fallos[0].empleado == "ana"


def test_rn01_noche_seguida_de_tarde_siete_horas(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "N")
    cedido = turno(ana, "2026-11-05", "M")
    recibido = turno(luis, "2026-11-03", "T")
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-01"]
    assert "7 h de descanso" in fallos[0].mensaje
    assert "el mínimo es 12 h" in fallos[0].mensaje


def test_rn01_noche_seguida_de_noche_catorce_horas_es_valido(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "N")
    cedido = turno(ana, "2026-11-05", "M")
    recibido = turno(luis, "2026-11-03", "N")
    assert validar_descanso_y_solapes(cedido, recibido) == []


def test_rn01_exactamente_doce_horas_es_valido(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "N")  # termina el 03/11 a las 08:00
    cedido = turno(ana, "2026-11-05", "M")
    recibido = Turno.objects.create(
        empleado=luis,
        fecha=date(2026, 11, 3),
        franja="T",
        inicio=instante(date(2026, 11, 3), time(20)),
        fin=instante(date(2026, 11, 3), time(23)),
    )
    assert validar_descanso_y_solapes(cedido, recibido) == []


def test_rn01_noche_del_domingo_se_mide_desde_su_fin_real_del_lunes(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-08", "N")  # domingo; termina el lunes 09/11 a las 08:00
    cedido = turno(ana, "2026-11-12", "M")
    recibido = turno(luis, "2026-11-09", "M")
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-01"]
    assert "0 h de descanso" in fallos[0].mensaje


def test_rn01_comprueba_tambien_el_turno_posterior(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-04", "M")  # empieza el 04/11 a las 08:00
    cedido = turno(ana, "2026-11-10", "M")
    recibido = turno(luis, "2026-11-03", "N")  # terminaría el 04/11 a las 08:00
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-01"]
    assert "0 h de descanso" in fallos[0].mensaje


def test_se_comprueban_los_dos_empleados(plantilla):
    ana, luis = plantilla
    cedido = turno(ana, "2026-11-05", "M")
    turno(luis, "2026-11-04", "N")  # termina el 05/11 a las 08:00
    recibido = turno(luis, "2026-11-10", "M")
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-01"]
    assert fallos[0].empleado == "luis"


def test_rn06_dos_turnos_con_la_misma_fecha(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-03", "M")
    cedido = turno(ana, "2026-11-05", "M")
    recibido = turno(luis, "2026-11-03", "N")
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert "RN-06" in reglas(fallos)
    assert "dos turnos el 03/11" in next(f for f in fallos if f.regla == "RN-06").mensaje


def test_rn06_turnos_solapados(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "N")  # 02/11 22:00 – 03/11 08:00
    cedido = turno(ana, "2026-11-05", "M")
    recibido = Turno.objects.create(
        empleado=luis,
        fecha=date(2026, 11, 3),
        franja="M",
        inicio=instante(date(2026, 11, 3), time(6)),
        fin=instante(date(2026, 11, 3), time(13)),
    )
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["RN-06"]
    assert "solapados" in fallos[0].mensaje


def test_el_turno_cedido_ya_no_cuenta(plantilla):
    ana, luis = plantilla
    cedido = turno(ana, "2026-11-03", "M")
    recibido = turno(luis, "2026-11-03", "T")
    assert validar_descanso_y_solapes(cedido, recibido) == []


def test_faltan_datos_bloquea_la_validacion(plantilla):
    ana, luis = plantilla
    cedido = turno(ana, "2026-11-05", "M")
    recibido = Turno(empleado=luis, fecha=date(2026, 11, 3), franja="M", inicio=None, fin=None)
    fallos = validar_descanso_y_solapes(cedido, recibido)
    assert reglas(fallos) == ["Datos incompletos"]
    assert "falta inicio" in fallos[0].mensaje


def test_intercambio_valido_no_devuelve_incumplimientos(plantilla):
    ana, luis = plantilla
    turno(ana, "2026-11-02", "M")
    cedido = turno(ana, "2026-11-05", "M")
    turno(luis, "2026-11-02", "T")
    recibido = turno(luis, "2026-11-07", "T")
    assert validar_descanso_y_solapes(cedido, recibido) == []
