# TurnoLibre — Tecnologías del proyecto

Decisión D-29 (28/10/2026), aceptada por todo el equipo con la conformidad del TL (MarvelinoGG). Cierra el riesgo RT-04.

| Pieza | Tecnología | Motivo |
|---|---|---|
| Lenguaje | Python 3.12 | Ya se ha usado en el proyecto para generar la planificación y es legible para los cuatro miembros. |
| Framework web | Django 5.2 (LTS) | Incluye usuarios, sesiones, grupos y permisos (US-002, NFR-001), hash de contraseñas configurable a Argon2id (NFR-002), transacciones atómicas (NFR-007, RT-02), ORM, migraciones y panel de administración. |
| Interfaz | Plantillas HTML de Django y CSS; JavaScript solo si hace falta | HTML semántico sin frameworks de cliente: facilita la accesibilidad básica (NFR-004) y la compatibilidad con navegadores (NFR-009). |
| Base de datos | SQLite | Un fichero sin servidor: instalación en menos de 10 min (NFR-008) y transacciones ACID. |
| Datos de demostración | Comando de gestión de Django | Carga y restablecimiento en un paso (US-003, TK-006). |
| Pruebas | pytest con pytest-django | Pruebas de aceptación y de reglas (M02). |
| Estilo de código | Ruff | Revisión automática del estilo en la integración continua. |
| Integración continua | GitHub Actions | En cada push y pull request: instalar, revisar el estilo, comprobar migraciones y pasar las pruebas (US-001-AC-01, TK-002). |
| Control de versiones | Git con GitFlow y smart commits de Jira | Ver [docs/git/README.md](../git/README.md). |

## Estructura prevista del repositorio

```text
manage.py
requirements.txt          dependencias fijadas
pyproject.toml            configuración de pytest y Ruff
turnolibre/               configuración del proyecto Django (settings, urls)
<apps>/                   una aplicación Django por área: cuentas, cuadrante, intercambios…
templates/                plantillas HTML comunes
static/                   CSS
tests/                    pruebas
.github/workflows/ci.yml  integración continua
```

El TL decide las aplicaciones y su organización interna en TK-001. Cualquier cambio de tecnología se registra como una nueva decisión.

## Puesta en marcha en local

```bash
python -m venv .venv
.venv\Scripts\activate         # en Windows; en Linux o macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pruebas y estilo, igual que en la integración continua:

```bash
ruff check .
pytest
```
