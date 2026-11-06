# Entorno de demostración

Cómo instalar y arrancar TurnoLibre desde cero para la demostración (TK-003, US-001-AC-03). NFR-008 pide que cueste menos de 10 minutos.

Requisitos: Python 3.12 y Git.

## Instalación (una vez)

```bash
git clone https://github.com/UniExtremadura/TurnoLibre_GC02.git
cd TurnoLibre_GC02
git checkout main
python -m venv .venv               # en Windows, si «python» no se reconoce: py -3.12 -m venv .venv
.venv\Scripts\activate             # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo       # cuadrante ficticio de noviembre de 2026 y cuentas de demostración
```

Para entrar también en la administración de Django: `python manage.py createsuperuser` (opcional).

## Arranque

```bash
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/> e iniciar sesión con una de las cuentas de demostración.

## Cuentas de demostración

Contraseña de todas: `demo-turnolibre` (se puede cambiar con `python manage.py cargar_demo --password <otra>`).

| Usuario | Rol | Qué tiene |
|---|---|---|
| `empleado01` | Empleado · Enfermería | Mañanas de noviembre |
| `empleado03` | Empleado · Auxiliar de enfermería | Turnos de otra categoría (para comprobar RN-03) |
| `empleado15` | Empleado · Enfermería | Noches de noviembre |
| `responsable01` | Responsable del servicio | Sin turnos; acceso al panel del responsable |

## Qué se puede probar (IT-1 a IT-3)

| Pantalla | Historia | Cómo |
|---|---|---|
| Inicio y cierre de sesión con rol | US-002 | Entrar con cualquier cuenta; «Cerrar sesión» en la cabecera. Un empleado no puede abrir `/responsable/` (403). |
| Mi calendario | US-005 | Menú «Mi calendario»: turnos propios del mes en lista, con «Mes anterior» y «Mes siguiente». Ir a noviembre de 2026. |
| Turnos compatibles | US-006 | Menú «Turnos compatibles»: turnos futuros de compañeros de la misma categoría y servicio (RN-03). Con `empleado01` solo salen enfermeras; con `empleado03`, solo auxiliares. En un mes sin turnos se indica que la lista está vacía. |

Las reglas RN-01, RN-03 y RN-06 (US-012 y US-014) se validan en el servidor y se comprueban con las pruebas automáticas; se usarán en pantalla al proponer un intercambio (US-009, IT-4).

Para volver a los datos de partida en cualquier momento: `python manage.py cargar_demo`.

## Comprobación

```bash
ruff check .
python manage.py check
pytest
```

Son las mismas comprobaciones que hace la integración continua en cada push (`.github/workflows/ci.yml`).

## Tiempo medido (evidencia de NFR-008)

| Fecha | Equipo | Rama | Resultado |
|---|---|---|---|
| 01/11/2026 | Windows 11, Python 3.14.4 | `feature/GC02-171-entorno-base` | **1 min** desde el `git clone` hasta tener `/admin/` respondiendo (HTTP 200) y las comprobaciones en verde. |
| 06/11/2026 | Windows 11, Python 3.14.4 | `develop` | **1 min 25 s** desde el `git clone` hasta entrar con `empleado01` y ver *Turnos compatibles*, con las comprobaciones en verde (75 pruebas). |

Desglose del 01/11: clonar, 2 s; crear el entorno virtual, 11 s; instalar dependencias, 38 s; `migrate` y `createsuperuser`, 2 s; arranque, 2 s; comprobaciones, 4 s. La mayor parte es la descarga de dependencias, así que depende de la conexión. Los comandos se ejecutaron seguidos, sin contar el tiempo de escribirlos.
