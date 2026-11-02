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
python manage.py createsuperuser   # usuario administrador de la demo
```

## Arranque

```bash
python manage.py runserver
```

Abrir <http://127.0.0.1:8000/admin/> e iniciar sesión con el usuario creado.

## Comprobación

```bash
ruff check .
python manage.py check
pytest
```

Son las mismas comprobaciones que hace la integración continua en cada push (`.github/workflows/ci.yml`).

Los datos de demostración se cargarán con un comando cuando esté hecha US-003 (TK-006).

## Tiempo medido (evidencia de NFR-008)

| Fecha | Equipo | Rama | Resultado |
|---|---|---|---|
| 01/11/2026 | Windows 11, Python 3.14.4 | `feature/GC02-171-entorno-base` | **1 min** desde el `git clone` hasta tener `/admin/` respondiendo (HTTP 200) y las comprobaciones en verde. |

Desglose: clonar, 2 s; crear el entorno virtual, 11 s; instalar dependencias, 38 s; `migrate` y `createsuperuser`, 2 s; arranque, 2 s; comprobaciones, 4 s. La mayor parte es la descarga de dependencias, así que depende de la conexión. Los comandos se ejecutaron seguidos, sin contar el tiempo de escribirlos.
