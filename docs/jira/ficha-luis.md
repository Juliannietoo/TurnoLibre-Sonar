# Jira · ficha de Luis (Lucansado)

Práctica 2 · proyecto **GC02-GPS26** (clave `GC02`) · <https://gc02-gps26.atlassian.net/jira/software/projects/GC02/boards/1>

Generada desde el catálogo V1, las fichas de épica y el plan (Excel v5). Cada elemento lo crea la persona responsable del requisito, como pide el enunciado.

**Antes de empezar**
- Las épicas, los sprints IT-1 a IT-6, las versiones R1, R2 y R3 · MVP y las 30 tareas MGT las crea Paula. Espera a su aviso.
- En el campo *Estimación original* escribe las horas como `2h` o `1h 30m` (0,5 h = `30m`, 0,25 h = `15m`).
- La descripción va en el bloque gris de cada elemento: cópiala tal cual.
- Los **enlaces** («está bloqueada por») se añaden al final, cuando todos hayan creado sus historias: abre tu historia → *Vincular actividad* → «está bloqueada por» → busca el código (por ejemplo `US-006`).

**Te tocan:** EP-002, EP-003 (7 historias), sus subtareas y tus subtareas de gestión.


## EP-002. Calendario de turnos

### US-005. Consultar mi calendario de turnos

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-005. Consultar mi calendario de turnos` |
| Épica (principal) | EP-002. Calendario de turnos |
| Prioridad | Highest (Más alta) |
| Sprint | IT-2. Goal: Acceso y calendario |
| Versión de corrección (Fix version) | R1 |
| Responsable (asignado) | Luis (Lucansado) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-baja` · `R1` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero consultar mis turnos en una lista, para saber qué días trabajo y qué turno puedo ofrecer.

Prioridad MoSCoW: Must. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-002 (funcional), US-003 (técnica)
Cambio D-18 (06/10/2026): calendario en formato lista de próximos turnos, en lugar de cuadrícula mensual.

Criterios de aceptación:
- US-005-AC-01: El empleado ve sus turnos del mes actual en formato lista, con fecha, franja (M/T/N) y servicio (D-18).
- US-005-AC-02: Puede avanzar y retroceder de mes.

Ficha completa: specs/EP-002…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-005 · Calendario en lista: revisión y aceptación del PO` | Luis (Lucansado) | 1,5 h |
| `US-005 · Pantalla del calendario` | Paula (PaulaJCruz) | 1 h |
| `US-005 · Pruebas y accesibilidad con teclado` | Julián (Juliannietoo) | 0,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-002, US-003

### US-006. Consultar los turnos de compañeros compatibles

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-006. Consultar los turnos de compañeros compatibles` |
| Épica (principal) | EP-002. Calendario de turnos |
| Prioridad | Highest (Más alta) |
| Sprint | IT-3. Goal: Compatibles y reglas |
| Versión de corrección (Fix version) | R2 |
| Responsable (asignado) | Luis (Lucansado) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-baja` · `R2` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero ver los turnos de compañeros de mi categoría y servicio, para elegir el turno sobre el que proponer directamente un intercambio.

Prioridad MoSCoW: Must. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-005 (funcional)
Cambio D-18 (06/10/2026): pasa a Must: es el punto de partida de la propuesta directa sobre un turno de un compañero compatible (sustituye a US-007 y US-008).

Criterios de aceptación:
- US-006-AC-01: Solo se muestran compañeros de la misma categoría y servicio (RN-03).
- US-006-AC-02: No se muestran datos personales más allá del nombre ficticio y el turno.
- US-006-AC-03: Si la consulta termina correctamente y no hay turnos compatibles, se muestra un mensaje de lista vacía que lo explica. Un fallo de consulta muestra su motivo y no se presenta como una lista vacía (R-07, D-23).

Ficha completa: specs/EP-002…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-006 · Consulta de turnos compatibles y lista vacía` | Luis (Lucansado) | 2 h |
| `US-006 · Pantalla de turnos compatibles` | Paula (PaulaJCruz) | 1 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-005

---

## EP-003. Intercambio de turnos

### US-007. Publicar un turno para cambiar

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-007. Publicar un turno para cambiar` |
| Épica (principal) | EP-003. Intercambio de turnos |
| Prioridad | Lowest (Más baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `wont` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero publicar un turno que quiero cambiar, para que mis compañeros compatibles lo vean.

Prioridad MoSCoW: Won't. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-005 (funcional)
Cambio D-18 (06/10/2026): fuera de esta versión; la propuesta se hace directamente sobre un turno compatible (US-006 + US-009). Se conserva el identificador.

Criterios de aceptación:
- US-007-AC-01: El empleado puede publicar uno de sus turnos futuros desde el calendario.
- US-007-AC-02: No puede publicar un turno pasado ni uno ya publicado.
- US-007-AC-03: El turno publicado aparece marcado en su calendario.

Ficha completa: specs/EP-003…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-005

### US-008. Ver los turnos publicados compatibles

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-008. Ver los turnos publicados compatibles` |
| Épica (principal) | EP-003. Intercambio de turnos |
| Prioridad | Lowest (Más baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `wont` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero ver los turnos publicados por compañeros compatibles, para encontrar un cambio posible.

Prioridad MoSCoW: Won't. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-007 (funcional)
Cambio D-18 (06/10/2026): fuera de esta versión; la propuesta se hace directamente sobre un turno compatible (US-006 + US-009). Se conserva el identificador.

Criterios de aceptación:
- US-008-AC-01: Solo se listan turnos de empleados de la misma categoría y servicio (RN-03).
- US-008-AC-02: No aparecen turnos pasados, los propios ni aquellos que ya estén implicados en una solicitud activa.
- US-008-AC-03: Si no hay turnos compatibles, se muestra un mensaje que lo explica.

Ficha completa: specs/EP-003…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-007

### US-009. Proponer un intercambio

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-009. Proponer un intercambio` |
| Épica (principal) | EP-003. Intercambio de turnos |
| Prioridad | Highest (Más alta) |
| Sprint | IT-4. Goal: Propuesta de intercambio |
| Versión de corrección (Fix version) | R2 |
| Responsable (asignado) | Marcelino (MarvelinoGG) |
| Estimación original | 8 h |
| Etiquetas | `must` · `incertidumbre-media` · `R2` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero proponer un intercambio ofreciendo uno de mis turnos a cambio de un turno de un compañero compatible, para cambiar un turno que no puedo hacer.

Prioridad MoSCoW: Must. Incertidumbre: Media. Estimación tras D-18: 8 h-p.
Predecesoras: US-006 (funcional), US-005 (funcional), US-003 (técnica)
Cambio D-18 (06/10/2026): propuesta directa sobre un turno de un compañero compatible, sin publicación previa; se mantiene una única propuesta activa por turno.

Criterios de aceptación:
- US-009-AC-01: Dado un turno futuro de un compañero compatible seleccionado desde US-006, el empleado elige uno de sus turnos futuros y confirma, sin publicación previa; la solicitud queda en estado *Propuesta*.
- US-009-AC-02: Ambos empleados pueden abrir el detalle de su solicitud desde su calendario, con los dos turnos, el estado actual y la siguiente acción disponible. Solo sus participantes y el responsable del servicio pueden acceder a ella; el servidor rechaza el acceso de otros usuarios.
- US-009-AC-03: Ninguno de los dos turnos puede formar parte de otra solicitud activa. Una solicitud está activa mientras está en estado Propuesta o Aceptada, pendiente de aprobación. Si alguno está ocupado, el sistema rechaza la nueva propuesta y explica el motivo.
- US-009-AC-04: No se puede proponer sobre un turno propio.
- US-009-AC-05: Al registrar la propuesta se comprueba RN-03: misma categoría y servicio. Si falla, no se crea la solicitud ni se reservan los turnos; se indica la regla y el motivo. El mínimo de 48 h de RN-05 solo se comprueba si el equipo incorpora US-015 (Should, D-18).
- US-009-AC-06: Si llegan dos propuestas simultáneas sobre el mismo turno, solo una se registra. La otra no ocupa turnos ni crea una solicitud y recibe un mensaje indicando que el turno ya no está disponible.
- US-009-AC-07: El detalle básico sigue siendo accesible cuando la solicitud termina; muestra el estado final, quién realizó la última acción y cuándo, y el motivo del rechazo manual o por regla cuando proceda. Esta consulta forma parte del flujo esencial y funciona sin US-019.
- US-009-AC-08: Con la hora del servidor, una solicitud cuyo primer turno ya ha empezado se muestra como Caducada, libera los dos turnos y no permite aceptarla ni aprobarla. El detalle básico se actualiza sin depender de que alguien abra la pantalla; el efecto es consistente ante peticiones simultáneas o repetidas (R-04, D-22).
- US-009-AC-09: Los turnos implicados en una solicitud pendiente aparecen marcados en el calendario de ambos empleados (US-005). Trasladado desde US-005-AC-03 (IPR-v01-010, D-24).

Ficha completa: specs/EP-003…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-009 · Reserva de turnos y transacción de la propuesta` | Marcelino (MarvelinoGG) | 2 h |
| `US-009 · Pruebas de concurrencia y caducidad` | Julián (Juliannietoo) | 2 h |
| `US-009 · Flujo de propuesta: revisión y aceptación del PO` | Luis (Lucansado) | 2 h |
| `US-009 · Pantalla de propuesta` | Paula (PaulaJCruz) | 2 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-006, US-005, US-003

### US-010. Responder a una propuesta

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-010. Responder a una propuesta` |
| Épica (principal) | EP-003. Intercambio de turnos |
| Prioridad | Highest (Más alta) |
| Sprint | IT-5. Goal: Respuesta y preparación |
| Versión de corrección (Fix version) | R3 · MVP |
| Responsable (asignado) | Luis (Lucansado) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-baja` · `R3` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero aceptar o rechazar una propuesta recibida, para cerrar el acuerdo con mi compañero.

Prioridad MoSCoW: Must. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-009 (funcional)

Criterios de aceptación:
- US-010-AC-01: Al aceptar, la solicitud pasa a *Aceptada* y queda pendiente de aprobación.
- US-010-AC-02: Al rechazar, la solicitud pasa a *Rechazada* y se liberan ambos turnos.
- US-010-AC-03: Una propuesta solo puede aceptarse antes del inicio más temprano de sus turnos; al llegar ese inicio queda Caducada. Si se incorpora US-015, las 48 h de RN-05 se comprueban al registrar la propuesta, no de nuevo al aceptarla.
- US-010-AC-04: Solo el destinatario de una propuesta puede responderla. Su respuesta se refleja en el detalle básico de ambos empleados con fecha y autor; repetir la misma acción no cambia dos veces el estado.
- US-010-AC-05: Con la hora del servidor, una solicitud cuyo primer turno ya ha empezado se muestra como Caducada, libera los dos turnos y no permite aceptarla ni aprobarla. La caducidad forma parte del flujo Must aunque no se incorpore US-015 (R-04, D-22).

Ficha completa: specs/EP-003…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-010 · Aceptar o rechazar: revisión y aceptación del PO` | Luis (Lucansado) | 1 h |
| `US-010 · Pantalla de respuesta` | Paula (PaulaJCruz) | 1 h |
| `US-010 · Lógica de servidor: aceptar o rechazar, liberar turnos y caducidad` | Marcelino (MarvelinoGG) | 0,5 h |
| `US-010 · Pruebas de respuesta y caducidad` | Julián (Juliannietoo) | 0,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-009

### US-011. Cancelar una solicitud de intercambio

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-011. Cancelar una solicitud de intercambio` |
| Épica (principal) | EP-003. Intercambio de turnos |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero cancelar una solicitud de intercambio en la que participo mientras no esté aprobada, para retirar un cambio que ya no necesito.

Prioridad MoSCoW: Should. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-009 (funcional)

Criterios de aceptación:
- US-011-AC-01: Cualquiera de los dos participantes puede cancelar una solicitud Propuesta o Aceptada antes de aprobarse. Cancelar registra autor y fecha y actualiza el detalle básico de ambos.
- US-011-AC-02: No se puede cancelar una solicitud Aprobada, Rechazada o Caducada, ni actuar sobre solicitudes ajenas.
- US-011-AC-03: Cancelar una solicitud libera ambos turnos.

Ficha completa: specs/EP-003…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-009

---

## Tus subtareas de gestión (MGT)

Paula crea las 30 tareas MGT (5 por sprint). Cuando estén, entra en cada una y pulsa *Añadir subtarea* con tu parte. Son 30 subtareas: 5 por sprint.

| Dentro de la tarea | Resumen de tu subtarea | Asignado | Estimación |
|---|---|---|---|
| `MGT IT-1. Sprint planning` | `MGT IT-1. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-1. Dailies (2 × 15 min)` | `MGT IT-1. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-1. Coordinación de roles` | `MGT IT-1. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-1. Sprint review` | `MGT IT-1. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-1. Sprint retrospective` | `MGT IT-1. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-2. Sprint planning` | `MGT IT-2. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-2. Dailies (2 × 15 min)` | `MGT IT-2. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-2. Coordinación de roles` | `MGT IT-2. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-2. Sprint review` | `MGT IT-2. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-2. Sprint retrospective` | `MGT IT-2. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-3. Sprint planning` | `MGT IT-3. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-3. Dailies (2 × 15 min)` | `MGT IT-3. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-3. Coordinación de roles` | `MGT IT-3. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-3. Sprint review` | `MGT IT-3. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-3. Sprint retrospective` | `MGT IT-3. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-4. Sprint planning` | `MGT IT-4. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-4. Dailies (2 × 15 min)` | `MGT IT-4. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-4. Coordinación de roles` | `MGT IT-4. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-4. Sprint review` | `MGT IT-4. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-4. Sprint retrospective` | `MGT IT-4. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-5. Sprint planning` | `MGT IT-5. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-5. Dailies (2 × 15 min)` | `MGT IT-5. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-5. Coordinación de roles` | `MGT IT-5. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-5. Sprint review` | `MGT IT-5. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-5. Sprint retrospective` | `MGT IT-5. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-6. Sprint planning` | `MGT IT-6. Sprint planning · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-6. Dailies (2 × 15 min)` | `MGT IT-6. Dailies (2 × 15 min) · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-6. Coordinación de roles` | `MGT IT-6. Coordinación de roles · Luis` | Luis (Lucansado) | 0,5 h |
| `MGT IT-6. Sprint review` | `MGT IT-6. Sprint review · Luis` | Luis (Lucansado) | 0,25 h |
| `MGT IT-6. Sprint retrospective` | `MGT IT-6. Sprint retrospective · Luis` | Luis (Lucansado) | 0,25 h |

Total de tus horas de gestión: **12 h**.
