# Jira · ficha de Marcelino (MarvelinoGG)

Práctica 2 · proyecto **GC02-GPS26** (clave `GC02`) · <https://gc02-gps26.atlassian.net/jira/software/projects/GC02/boards/1>

Generada desde el catálogo V1, las fichas de épica y el plan (Excel v5). Cada elemento lo crea la persona responsable del requisito, como pide el enunciado.

**Antes de empezar**
- Las épicas, los sprints IT-1 a IT-6, las versiones R1, R2 y R3 · MVP y las 30 tareas MGT las crea Paula. Espera a su aviso.
- En el campo *Estimación original* escribe las horas como `2h` o `1h 30m` (0,5 h = `30m`, 0,25 h = `15m`).
- La descripción va en el bloque gris de cada elemento: cópiala tal cual.
- Los **enlaces** («está bloqueada por») se añaden al final, cuando todos hayan creado sus historias: abre tu historia → *Vincular actividad* → «está bloqueada por» → busca el código (por ejemplo `US-006`).

**Te tocan:** EP-001, EP-005 (6 historias), sus subtareas y tus subtareas de gestión.


## EP-001. Base del producto: acceso y datos de demostración

### US-001. Preparar el entorno base

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-001. Preparar el entorno base` |
| Épica (principal) | EP-001. Base del producto: acceso y datos de demostración |
| Prioridad | Highest (Más alta) |
| Sprint | IT-1. Goal: Base técnica y datos |
| Versión de corrección (Fix version) | R1 |
| Responsable (asignado) | Marcelino (MarvelinoGG) |
| Estimación original | 5 h |
| Etiquetas | `must` · `incertidumbre-media` · `R1` |

**Descripción** (copiar y pegar):

```text
Como equipo de desarrollo, quiero un repositorio con integración continua y un entorno de demostración, para integrar y desplegar cada incremento de forma estable.

Prioridad MoSCoW: Must. Incertidumbre: Media. Estimación tras D-18: 5 h-p.
Predecesoras: —; externa: confirmación de tecnologías autorizadas

Criterios de aceptación:
- US-001-AC-01: Un push a una rama ejecuta automáticamente la compilación y las pruebas.
- US-001-AC-02: La integración de cambios en `main` requiere que la compilación y las pruebas terminen correctamente.
- US-001-AC-03: La versión de `main` puede desplegarse en el entorno de demostración siguiendo un procedimiento documentado.

Ficha completa: specs/EP-001…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `TK-001. Crear la estructura técnica y arquitectónica básica del proyecto con la tecnología autorizada (condicionada a su confirmación)` | Marcelino (MarvelinoGG) | 1,5 h |
| `TK-002. Integración continua: compilar y pasar las pruebas en cada push; bloquear la integración si falla` | Julián (Juliannietoo) | 1,5 h |
| `TK-003. Entorno de demostración y documentación del despliegue` | Julián (Juliannietoo) | 1 h |
| `TK-004. Prueba de humo y revisión de la base técnica` | Marcelino (MarvelinoGG) | 1 h |

### US-002. Iniciar sesión con rol

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-002. Iniciar sesión con rol` |
| Épica (principal) | EP-001. Base del producto: acceso y datos de demostración |
| Prioridad | Highest (Más alta) |
| Sprint | IT-2. Goal: Acceso y calendario |
| Versión de corrección (Fix version) | R1 |
| Responsable (asignado) | Marcelino (MarvelinoGG) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-media` · `R1` |

**Descripción** (copiar y pegar):

```text
Como usuario de TurnoLibre, quiero iniciar sesión con mi cuenta ficticia, para acceder solo a las funciones de mi rol (empleado o responsable).

Prioridad MoSCoW: Must. Incertidumbre: Media. Estimación tras D-18: 3 h-p.
Predecesoras: US-001 (técnica), US-003 (técnica)
Cambio D-18 (06/10/2026): sin bloqueo por intentos fallidos; queda como mejora futura.

Criterios de aceptación:
- US-002-AC-01: Con usuario y contraseña correctos de un empleado, se inicia una sesión identificada con su rol y se muestra su página de inicio, sin opciones exclusivas del responsable.
- US-002-AC-02: Con credenciales del responsable, se inicia una sesión con su rol y servicio. El acceso no depende de que el calendario o la bandeja estén implementados; cada función se incorpora a la navegación al estar disponible.
- US-002-AC-03: Con credenciales incorrectas, se muestra "Usuario o contraseña incorrectos" sin indicar cuál de los dos falla.
- US-002-AC-04: Un usuario sin sesión que abre una página interna es redirigido al inicio de sesión.
- US-002-AC-05: Una petición al servidor a una operación del responsable hecha con sesión de empleado es rechazada.
- US-002-AC-09: Cerrar sesión invalida el acceso a operaciones protegidas en el servidor; una sesión caducada se trata como una sesión no iniciada.

Ficha completa: specs/EP-001…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-002 · Autenticación y roles en el servidor` | Marcelino (MarvelinoGG) | 2 h |
| `US-002 · Pruebas de acceso y autorización` | Julián (Juliannietoo) | 1 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-001, US-003

### US-003. Cargar los datos de demostración

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-003. Cargar los datos de demostración` |
| Épica (principal) | EP-001. Base del producto: acceso y datos de demostración |
| Prioridad | Highest (Más alta) |
| Sprint | IT-1. Goal: Base técnica y datos |
| Versión de corrección (Fix version) | R1 |
| Responsable (asignado) | Luis (Lucansado) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-media` · `R1` |

**Descripción** (copiar y pegar):

```text
Como evaluador, quiero que la aplicación arranque con empleados, turnos y un cuadrante ficticios, para poder probarla sin preparar datos.

Prioridad MoSCoW: Must. Incertidumbre: Media. Estimación tras D-18: 3 h-p.
Predecesoras: US-001 (técnica)
Cambio D-18 (06/10/2026): un solo servicio con 2 categorías y sin semanas con cambio de hora; RN-04 (cobertura 3/3/2) se comprueba aquí, al preparar el cuadrante.

Criterios de aceptación:
- US-003-AC-01: Tras la instalación existe 1 servicio con 2 categorías profesionales, 1 responsable y los empleados necesarios para cubrir el mínimo 3/3/2 (D-18).
- US-003-AC-02: El cuadrante inicial cumple RN-01, RN-02, RN-04 y RN-06. Hay empleados compatibles para probar RN-03 y fechas que permiten solicitudes con RN-05; los escenarios inválidos se preparan de forma controlada para las pruebas.
- US-003-AC-03: Los datos pueden restablecerse a su estado inicial con un único paso documentado.

Ficha completa: specs/EP-001…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `TK-005. Diseñar el cuadrante ficticio: 1 servicio, categorías, cobertura 3/3/2, sin cambio de hora` | Luis (Lucansado) | 1 h |
| `TK-006. Script de carga y restablecimiento de los datos en un paso` | Paula (PaulaJCruz) | 1,5 h |
| `TK-007. Comprobar que el cuadrante cumple RN-01, RN-02, RN-04 y RN-06 (US-003-AC-02)` | Luis (Lucansado) | 0,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-001

### US-004. Mantener los turnos del cuadrante

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-004. Mantener los turnos del cuadrante` |
| Épica (principal) | EP-001. Base del producto: acceso y datos de demostración |
| Prioridad | Low (Baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 5 h |
| Etiquetas | `could` · `incertidumbre-media` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero dar de alta y modificar turnos asignados, para mantener el cuadrante de demostración.

Prioridad MoSCoW: Could. Incertidumbre: Media. Estimación tras D-18: 5 h-p.
Predecesoras: US-002 (funcional), US-003 (técnica), US-012 (técnica), US-013 (técnica), US-014 (técnica)

Criterios de aceptación:
- US-004-AC-01: El responsable puede asignar un turno libre a un empleado de su servicio.
- US-004-AC-02: El sistema impide modificar un turno que forma parte de una solicitud pendiente.
- US-004-AC-03: Solo el responsable del servicio puede modificar sus turnos; la asignación resultante respeta descansos, horas, solapes y cobertura mínima.

Ficha completa: specs/EP-001…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-002, US-003, US-012, US-013, US-014

---

## EP-005. Aprobación del responsable

### US-017. Consultar solicitudes y decisiones del servicio

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-017. Consultar solicitudes y decisiones del servicio` |
| Épica (principal) | EP-005. Aprobación del responsable |
| Prioridad | Lowest (Más baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | sin estimación (fusionada en US-018) |
| Etiquetas | `fusionada` · `incertidumbre-media` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero consultar las solicitudes pendientes y las decisiones anteriores de mi servicio, para resolver cambios y comprobar su resultado.

Prioridad MoSCoW: Fusionada. Incertidumbre: Media. Estimación tras D-18: — h-p.
Predecesoras: — (fusionada en US-018)
Cambio D-18 (06/10/2026): fusionada en US-018 (una sola pantalla para consultar las pendientes y resolverlas). Se conserva el identificador.

Criterios de aceptación:
- US-017-AC-01: El responsable dispone de una lista de solicitudes Aceptadas de su servicio, ordenadas por el inicio más próximo, y de una lista básica de las que ya aprobó o rechazó. No accede a solicitudes de otros servicios.
- US-017-AC-02: Cada solicitud muestra empleados, turnos y el resultado de cada regla vigente del MVP (cumple / incumple); las Should solo se muestran como comprobadas si se incorporan. RN-04 se garantiza en el cuadrante inicial de US-003.
- US-017-AC-03: Si no hay solicitudes pendientes, se muestra un mensaje que lo indica.
- US-017-AC-04: El detalle de una decisión conserva los turnos originales, solicitante y destinatario, fechas de propuesta y aceptación, responsable, fecha y resultado de la decisión y motivo del rechazo cuando proceda. Este historial básico está disponible sin US-020.

Ficha completa: specs/EP-005…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-018

### US-018. Resolver una solicitud

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-018. Resolver una solicitud` |
| Épica (principal) | EP-005. Aprobación del responsable |
| Prioridad | Highest (Más alta) |
| Sprint | IT-6. Goal: Resolución y guion |
| Versión de corrección (Fix version) | R3 · MVP |
| Responsable (asignado) | Marcelino (MarvelinoGG) |
| Estimación original | 6,5 h |
| Etiquetas | `must` · `incertidumbre-alta` · `R3` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero aprobar o rechazar con motivo una solicitud, para mantener el cuadrante correcto y que los empleados conozcan el resultado.

Prioridad MoSCoW: Must. Incertidumbre: Alta. Estimación tras D-18: 8 h-p.
Predecesoras: US-010 (funcional), US-012 (funcional), US-014 (funcional)
Cambio D-18 (06/10/2026): una sola pantalla para consultar las pendientes y resolverlas (absorbe US-017); se mantiene el registro básico de la decisión y el resultado visible para ambos empleados.

Criterios de aceptación:
- US-018-AC-01: Al aprobar una solicitud válida, los turnos se intercambian en el calendario de ambos empleados y la solicitud pasa a *Aprobada*.
- US-018-AC-02: Cuando el responsable rechaza manualmente, es obligatorio escribir un motivo, que ven ambos empleados. La solicitud pasa a *Rechazada* y se liberan ambos turnos.
- US-018-AC-03: Antes de aprobar se comprueba la caducidad (AC-07); si la solicitud sigue Aceptada y no ha caducado, se repite en el servidor la validación de las reglas vigentes del MVP. Si detecta una regla incumplida, la solicitud pasa a Rechazada por regla: se conserva el estado Rechazada y se registra la RN y su motivo, se liberan ambos turnos y el cuadrante no se intercambia. Estado, motivo, detalle básico y reservas se actualizan de forma consistente e indivisible; una petición repetida no duplica la decisión (R-09, D-23).
- US-018-AC-04: El botón *Aprobar* está desactivado si la solicitud incumple una regla vigente o ya está terminada. El servidor mantiene esos límites aunque una petición omita la interfaz.
- US-018-AC-05: Cada decisión queda registrada con fecha, hora y responsable.
- US-018-AC-06: La decisión actualiza el detalle básico de los empleados (US-009) y el historial del responsable integrado desde US-017. Repetir una aprobación o enviarla desde dos pestañas produce un único intercambio y una única decisión; una solicitud ya terminada no puede volver a resolverse.
- US-018-AC-07: Con la hora del servidor, una solicitud cuyo primer turno ya ha empezado se muestra como Caducada, libera los dos turnos y no permite aceptarla ni aprobarla. La aprobación comprueba ese límite incluso si el responsable abrió el detalle antes del inicio (R-04, D-22).

Ficha completa: specs/EP-005…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-018 · Parte 2: implementación de la transacción y la revalidación` | Marcelino (MarvelinoGG) | 1,5 h |
| `US-018 · Pruebas de revalidación, caducidad y concurrencia` | Julián (Juliannietoo) | 2 h |
| `US-018 · Pantalla de pendientes y decisión con motivo` | Paula (PaulaJCruz) | 1,5 h |
| `US-018 · Flujo de decisión: revisión y aceptación del PO` | Luis (Lucansado) | 1,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-010, US-012, US-014

### US-018 · parte 1 (tarea en IT-5)

La historia se cierra en IT-6, pero una parte se hace antes, en IT-5 (excepción explícita de D-24). En Jira una historia solo puede estar en un sprint, así que esta parte va como **tarea** aparte.

| Campo | Valor |
|---|---|
| Tipo | Tarea |
| Resumen | `US-018 · parte 1: diseño de la transacción y la revalidación` |
| Épica (principal) | EP-005. Aprobación del responsable |
| Prioridad | Highest (Más alta) |
| Sprint | IT-5. Goal: Respuesta y preparación |
| Versión de corrección | R3 · MVP |
| Asignado | Marcelino (MarvelinoGG) |
| Estimación original | 1,5 h |
| Etiquetas | `must` · `R3` · `parte-1` |

**Descripción** (copiar y pegar):

```text
Parte 1: diseño de la transacción y la revalidación (mitigación del riesgo, decisión del TL).
Preparación de US-018 en IT-5; la historia se cierra en IT-6 (D-24, D-27, D-28).
```

**Enlace:** esta tarea *bloquea* → US-018

---

## Tus subtareas de gestión (MGT)

Paula crea las 30 tareas MGT (5 por sprint). Cuando estén, entra en cada una y pulsa *Añadir subtarea* con tu parte. Son 30 subtareas: 5 por sprint.

| Dentro de la tarea | Resumen de tu subtarea | Asignado | Estimación |
|---|---|---|---|
| `MGT IT-1. Sprint planning` | `MGT IT-1. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-1. Dailies (2 × 15 min)` | `MGT IT-1. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-1. Coordinación de roles` | `MGT IT-1. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-1. Sprint review` | `MGT IT-1. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-1. Sprint retrospective` | `MGT IT-1. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-2. Sprint planning` | `MGT IT-2. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-2. Dailies (2 × 15 min)` | `MGT IT-2. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-2. Coordinación de roles` | `MGT IT-2. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-2. Sprint review` | `MGT IT-2. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-2. Sprint retrospective` | `MGT IT-2. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-3. Sprint planning` | `MGT IT-3. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-3. Dailies (2 × 15 min)` | `MGT IT-3. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-3. Coordinación de roles` | `MGT IT-3. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-3. Sprint review` | `MGT IT-3. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-3. Sprint retrospective` | `MGT IT-3. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-4. Sprint planning` | `MGT IT-4. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-4. Dailies (2 × 15 min)` | `MGT IT-4. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-4. Coordinación de roles` | `MGT IT-4. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-4. Sprint review` | `MGT IT-4. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-4. Sprint retrospective` | `MGT IT-4. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-5. Sprint planning` | `MGT IT-5. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-5. Dailies (2 × 15 min)` | `MGT IT-5. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-5. Coordinación de roles` | `MGT IT-5. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-5. Sprint review` | `MGT IT-5. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-5. Sprint retrospective` | `MGT IT-5. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-6. Sprint planning` | `MGT IT-6. Sprint planning · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-6. Dailies (2 × 15 min)` | `MGT IT-6. Dailies (2 × 15 min) · Marcelino` | Marcelino (MarvelinoGG) | 0,5 h |
| `MGT IT-6. Coordinación de roles` | `MGT IT-6. Coordinación de roles · Marcelino` | Marcelino (MarvelinoGG) | 1 h |
| `MGT IT-6. Sprint review` | `MGT IT-6. Sprint review · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |
| `MGT IT-6. Sprint retrospective` | `MGT IT-6. Sprint retrospective · Marcelino` | Marcelino (MarvelinoGG) | 0,25 h |

Total de tus horas de gestión: **15 h**.
