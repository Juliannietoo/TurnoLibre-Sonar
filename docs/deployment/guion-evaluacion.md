# US-023 · Guion mínimo final de instalación y evaluación (Parte 1)

Trazabilidad: GC02-108 · US-023 (GC02-106) · US-023-AC-01 a US-023-AC-03 · G04, M04 · NFR-003, NFR-008 · D-18, D-24, D-27 y D-28.

Este documento constituye la **Parte 1** del guion paso a paso para que una persona ajena al desarrollo instale TurnoLibre desde un entorno limpio en menos de 10 minutos (`NFR-008`), cargue o restablezca los datos ficticios (`NFR-003`) y verifique sin ayuda del equipo (`M04`) los flujos de acceso por rol (`US-002`), consulta de calendario y turnos compatibles (`US-005` y `US-006`) y propuesta de un intercambio (`US-009`).

La **Parte 2** se completa en IT-6 (`D-24`, `D-27`, `D-28`) e incorpora los pasos de aceptar o rechazar una propuesta (`US-010`), resolver la solicitud como responsable (`US-018`) y el acta de validación con el evaluador externo.

---

## 1. Requisitos previos del equipo evaluador

- **Sistema operativo:** Windows 10/11, Linux o macOS.
- **Software necesario:**
  - `Git` instalado y accesible desde la terminal.
  - `Python 3.12` (o superior compatible con Django 5.2, con el módulo estándar `venv`).
  - Un navegador web moderno (Chrome, Edge, Firefox o Safari).
- **Conexión a internet:** solo necesaria durante el `git clone` y la descarga inicial de paquetes con `pip install`.
- **Tiempo estimado de instalación desde cero:** entre **1 y 2 minutos** (límite máximo de `NFR-008`: **10 minutos**).

---

## 2. Instalación desde un entorno limpio (`US-023-AC-01`, `NFR-008`)

Abrir una terminal en una carpeta vacía donde se quiera descargar el proyecto y ejecutar los siguientes comandos en orden. Anotar la hora de inicio antes del `git clone` y la de finalización al terminar `cargar_demo`.

### En Windows (PowerShell)

```powershell
git clone https://github.com/UniExtremadura/TurnoLibre_GC02.git
cd TurnoLibre_GC02
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo
```

*(Si `python` no se reconoce en Windows, usar `py -3.12 -m venv .venv` y después `.\.venv\Scripts\python.exe`)*

### En Linux o macOS

```bash
git clone https://github.com/UniExtremadura/TurnoLibre_GC02.git
cd TurnoLibre_GC02
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo
```

### Resultado esperado al terminar la instalación

La orden `python manage.py cargar_demo` debe terminar con el mensaje:

```text
Cuadrante de demostración cargado: 16 empleados, 1 responsable y 240 turnos.
```

Para comprobar opcionalmente que toda la batería automática y las reglas del proyecto están en verde en el entorno instalado:

```bash
ruff check .
python manage.py check
pytest
```

---

## 3. Arranque del servidor y restablecimiento de datos (`US-023-AC-02`)

### Arrancar la aplicación web

En la misma terminal con el entorno virtual activo:

```bash
python manage.py runserver
```

Abrir en el navegador: **<http://127.0.0.1:8000/>**

### Cómo restablecer los datos ficticios en cualquier momento (`US-003`)

Si durante la evaluación se han creado propuestas, reservas o cambios de estado y se desea volver exactamente al cuadrante inicial limpio:

```bash
python manage.py cargar_demo
```

El comando se ejecuta dentro de una única transacción atómica y **elimina primero todas las solicitudes de intercambio y reservas activas o terminadas**, además de los turnos, empleados, categorías, servicios y cuentas de demostración previos, volviendo a cargar el cuadrante ficticio original de noviembre de 2026 sin errores de clave protegida ni duplicados.

---

## 4. Cuentas ficticias por rol y categoría (`US-023-AC-02`, `NFR-003`)

Todos los datos son 100 % ficticios (`NFR-003`) y pertenecen al servicio de **Urgencias** sobre el cuadrante de **noviembre de 2026** (cobertura diaria 3 mañanas, 3 tardes y 2 noches).

- **Contraseña común de todas las cuentas:** `demo-turnolibre`

| Usuario | Nombre ficticio | Rol | Categoría | Uso principal en el guion |
|---|---|---|---|---|
| `empleado01` | Ana Vega | Empleado | Enfermería | Proponente principal (turnos de mañana en noviembre) |
| `empleado02` | Berta Prado | Empleado | Enfermería | Compañera compatible con `empleado01` (`RN-03`) |
| `empleado04` | David Soto | Empleado | Enfermería | Tercer empleado del mismo servicio ajeno a una solicitud entre Ana y Berta |
| `empleado15` | Olga Montes | Empleado | Enfermería | Empleada con turnos de noche (`22:00–08:00` del día siguiente) |
| `empleado03` | Carla Lago | Empleado | Auxiliar de enfermería | Empleada de **otra categoría** para verificar rechazo por `RN-03` |
| `responsable01` | Rosa Núñez | Responsable | *(Sin categoría ni turnos)* | Responsable del servicio de Urgencias |

---

## 5. Pasos de evaluación guiada · Parte 1 (`US-023-AC-02`)

### Paso 1 · Inicio de sesión, autorización por rol y cierre de sesión (`US-002`)

1. Abrir <http://127.0.0.1:8000/>. El sistema redirige automáticamente al formulario de inicio de sesión (`/entrar/`).
2. Probar una contraseña incorrecta con `empleado01`: debe mostrarse un mensaje de error claro sin revelar si falla el usuario o la contraseña.
3. Iniciar sesión con **`empleado01`** y contraseña **`demo-turnolibre`**.
   - **Resultado esperado:** entra al calendario propio; en la cabecera aparece el nombre (`Ana Vega`), su rol/servicio y el botón «Cerrar sesión», sin opciones exclusivas del responsable.
4. Intentar abrir en la barra de direcciones <http://127.0.0.1:8000/responsable/>.
   - **Resultado esperado:** el servidor bloquea el acceso con **HTTP 403**.
5. Pulsar «Cerrar sesión» e iniciar sesión con **`responsable01`** / **`demo-turnolibre`**.
   - **Resultado esperado:** accede al panel del responsable del servicio de Urgencias; si abre «Turnos compatibles», el sistema indica que los responsables no tienen turnos propios para intercambiar.
6. Cerrar sesión para continuar con el siguiente paso.

### Paso 2 · Consultar mi calendario de turnos y accesibilidad con teclado (`US-005`, `NFR-004`)

1. Iniciar sesión con **`empleado01`** / **`demo-turnolibre`**.
2. En la navegación superior, abrir **«Mi calendario»** y situarse en **noviembre de 2026** (`?mes=2026-11`, o usando los enlaces «Mes anterior» / «Mes siguiente»).
   - **Resultado esperado:** se listan únicamente los turnos propios de Ana Vega en noviembre de 2026 con fecha, franja (`Mañana (M)`, `08:00–15:00`) y servicio (`Urgencias`).
3. Usar los controles «Mes anterior» y «Mes siguiente» (también con las teclas `Tab` y `Enter`).
   - **Resultado esperado:** el cambio de mes funciona sin ratón; en un mes sin turnos asignados (por ejemplo, diciembre de 2026) se indica claramente que no hay turnos registrados.
4. *(Opcional)* Iniciar sesión con **`empleado15`** / **`demo-turnolibre`** y abrir noviembre de 2026 en «Mi calendario».
   - **Resultado esperado:** cada turno de noche (`N`) aparece en la fecha en que comienza (`22:00–08:00 del día siguiente`).

### Paso 3 · Consultar turnos compatibles (`US-006`, `RN-03`)

1. Con la sesión iniciada como **`empleado01`** (Enfermería · Urgencias), abrir **«Turnos compatibles»** en noviembre de 2026 (<http://127.0.0.1:8000/compatibles/?mes=2026-11>).
   - **Resultado esperado:**
     - Solo aparecen turnos **futuros** respecto de la hora actual del servidor pertenecientes a compañeros de **Enfermería** de **Urgencias** (como `Berta Prado`, `David Soto`, etc.).
     - **No** aparecen los turnos propios de Ana Vega ni los turnos de Auxiliares de enfermería (como `Carla Lago`, `empleado03`).
     - Cada turno compatible muestra el enlace **«Proponer intercambio»**.
2. Cambiar a diciembre de 2026 (`?mes=2026-12`).
   - **Resultado esperado:** se muestra un mensaje explicando que no hay turnos compatibles en ese periodo.
3. Cerrar sesión, entrar con **`empleado03`** (`Carla Lago`, Auxiliar de enfermería) y abrir «Turnos compatibles» en noviembre de 2026.
   - **Resultado esperado:** solo se listan turnos futuros de compañeros de la categoría **Auxiliar de enfermería**, cumpliendo `RN-03`.

### Paso 4 · Proponer un intercambio y consultar su detalle (`US-009`)

> **Nota sobre fechas:** el cuadrante de demostración está definido en **noviembre de 2026**. Elegir siempre un turno de compañero y un turno propio cuya fecha y hora de inicio sean **posteriores** a la hora actual del servidor.

1. Iniciar sesión con **`empleado01`** (`Ana Vega`) y abrir **«Turnos compatibles»** en noviembre de 2026 (`/compatibles/?mes=2026-11`).
2. En un turno futuro de **`Berta Prado`** (`empleado02`), pulsar **«Proponer intercambio»** (se puede recorrer con `Tab`, flechas para los botones de opción y `Enter`).
   - **Resultado esperado:** se abre la pantalla de propuesta mostrando el turno solicitado de Berta Prado y la lista de turnos propios futuros y libres de Ana Vega como botones de radio con su `<label>` asociado.
3. Seleccionar uno de los turnos propios futuros de Ana Vega y pulsar **«Confirmar propuesta»**.
   - **Resultado esperado (`US-009-AC-01` y `AC-02`):**
     - Redirige al **detalle de la solicitud** (`/intercambios/<id>/`) con un aviso de confirmación.
     - El estado es **`Propuesta`**, la última acción es «Propuesta del intercambio» con autora `Ana Vega` y fecha/hora actual, y la siguiente acción indica: *«Pendiente de que Berta Prado la acepte o la rechace.»*
     - La tabla muestra ambos turnos (*Ofrecido* de Ana Vega y *Solicitado* de Berta Prado).
4. Abrir **«Mi calendario»** en noviembre de 2026 (`/calendario/?mes=2026-11`) con `empleado01`.
   - **Resultado esperado (`US-009-AC-09`):** el turno ofrecido por Ana Vega aparece marcado con **«Solicitud pendiente»** y enlaza al detalle de la solicitud.
5. Comprobar la **exclusividad de reservas (`US-009-AC-03`)**:
   - Volver a abrir la URL de propuesta del mismo turno de Berta Prado (`/intercambios/proponer/<id_turno_berta>/`): el sistema informa de que ese turno ya forma parte de otra solicitud activa y no muestra el botón de confirmar.
   - Si Ana abre la propuesta sobre otro turno libre de otro compañero, el turno propio que ya ofreció a Berta **no** aparece entre sus turnos disponibles para ofrecer.
6. Comprobar los **permisos del detalle y la marca en el compañero (`US-009-AC-02` y `AC-09`)**:
   - Cerrar sesión y entrar con **`empleado02`** (`Berta Prado`): en «Mi calendario» de noviembre de 2026 su turno solicitado también muestra **«Solicitud pendiente»**; al seguir el enlace se abre el mismo detalle e indica: *«Te toca responder: aceptar o rechazar la propuesta.»*
   - Cerrar sesión y entrar con **`responsable01`**: puede abrir la URL `/intercambios/<id>/` (HTTP 200) para consultar el detalle de su servicio.
   - Cerrar sesión y entrar con **`empleado04`** (`David Soto`, no participante): al abrir `/intercambios/<id>/` el servidor responde **HTTP 403**.
7. Comprobar los **rechazos de reglas en el servidor (`US-009-AC-04` y `AC-05`)**:
   - Con `empleado01`, si se intenta abrir la URL de propuesta sobre un turno propio (`/intercambios/proponer/<id_turno_propio>/`), el sistema muestra: *«No puedes proponer un intercambio sobre un turno propio.»*
   - Si se intenta abrir la URL de propuesta sobre un turno de `empleado03` (Auxiliar de enfermería), el sistema rechaza la operación indicando la regla **`RN-03`** y el motivo (*categorías distintas*), sin crear solicitud ni reservar turnos.

---

## 6. Parte 2 (pendiente de completar en IT-6 · `GC02-109` / `US-023`)

En IT-6, una vez integradas `US-010` y `US-018`, se completarán en este mismo guion:

1. **Paso 5 · Responder a la propuesta (`US-010`):** aceptación y rechazo con `empleado02` desde el detalle de la solicitud, liberación de turnos al rechazar y paso a estado *Aceptada* (pendiente de aprobación) al aceptar.
2. **Paso 6 · Resolver la solicitud como responsable (`US-018`):** acceso con `responsable01` a la bandeja del servicio, revalidación en servidor de `RN-01`, `RN-03` y `RN-06`, aprobación con permuta atómica en ambos calendarios y rechazo manual con motivo obligatorio.
3. **Registro de validación externa (`US-023-AC-01`, `AC-03`, `M04`, `NFR-008`):** ficha de ejecución por la persona ajena al equipo (fecha, sistema operativo, tiempo total de instalación `< 10 min`, pasos superados sin ayuda e incidencias observadas).
