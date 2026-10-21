# Jira · ficha de Paula (PaulaJCruz)

Práctica 2 · proyecto **GC02-GPS26** (clave `GC02`) · <https://gc02-gps26.atlassian.net/jira/software/projects/GC02/boards/1>

Generada desde el catálogo V1, las fichas de épica y el plan (Excel v5). Cada elemento lo crea la persona responsable del requisito, como pide el enunciado.

**Antes de empezar**
- Las épicas, los sprints IT-1 a IT-6, las versiones R1, R2 y R3 · MVP y las 30 tareas MGT las crea Paula. Espera a su aviso.
- En el campo *Estimación original* escribe las horas como `2h` o `1h 30m` (0,5 h = `30m`, 0,25 h = `15m`).
- La descripción va en el bloque gris de cada elemento: cópiala tal cual.
- Los **enlaces** («está bloqueada por») se añaden al final, cuando todos hayan creado sus historias: abre tu historia → *Vincular actividad* → «está bloqueada por» → busca el código (por ejemplo `US-006`).

**Te tocan:** EP-006 (4 historias), sus subtareas y tus subtareas de gestión.


## 1. Épicas (crear primero)

*Crear* → tipo **Épica**. En «Fecha de inicio» y «Fecha de vencimiento» pon las del plan; así salen en el Cronograma.

| Resumen | Descripción (copiar) | Inicio | Vencimiento |
|---|---|---|---|
| `EP-001. Base del producto: acceso y datos de demostración` | Cualquier persona puede instalar el producto, entrar con una cuenta ficticia de empleado o de responsable y encontrar un cuadrante de demostración coherente con las reglas. Objetivos: G04. Historias: US-001, US-002, US-003, US-004. | 21/10/2026 | 03/11/2026 |
| `EP-002. Calendario de turnos` | El empleado sabe en todo momento qué turnos tiene y cuáles podría intercambiar. Objetivos: G01. Historias: US-005, US-006. | 28/10/2026 | 10/11/2026 |
| `EP-003. Intercambio de turnos` | Dos empleados pueden acordar un intercambio sin ayuda y dejarlo pendiente de aprobación (métrica M01). Objetivos: G01. Historias: US-007, US-008, US-009, US-010, US-011. | 11/11/2026 | 24/11/2026 |
| `EP-004. Validación de reglas` | Ningún intercambio que incumpla una regla puede aprobarse, y el empleado entiende por qué (métrica M02, principio 4 de la constitución). Objetivos: G02. Historias: US-012, US-013, US-014, US-015, US-016. | 04/11/2026 | 10/11/2026 |
| `EP-005. Aprobación del responsable` | El responsable resuelve cada solicitud con las reglas vigentes del MVP comprobadas y el cuadrante se actualiza sin inconsistencias. M03 conserva la meta de menos de 1 minuto por decisión; si no se realiza US-024, queda pendiente de validación (D-23). Objetivos: G03. Historias: US-017, US-018. | 18/11/2026 | 01/12/2026 |
| `EP-006. Vistas ampliadas de estado e historial` | El empleado puede consultar juntas sus solicitudes y el responsable recorrer una cronología ampliada. Estas mejoras facilitan la consulta de información que ya conserva el flujo básico. Objetivos: G01, G03. Historias: US-019, US-020, US-021, US-022. | — | — |
| `EP-007. Calidad y entrega` | Un tercero instala y evalúa la versión final siguiendo el guion mínimo sin ayuda. Si se realiza la prueba Should US-024, se obtienen las evidencias de M01 y M03; si no, ambas métricas quedan pendientes de validación (D-18/D-23). Objetivos: G04. Historias: US-023, US-024. | 18/11/2026 | 01/12/2026 |

---

## 2. Tareas de gestión MGT (30)

*Crear* → tipo **Tarea**, sin épica, etiqueta `mgt`, asignada a Paula (facilita la ceremonia). Repite el bloque para IT-1 a IT-6, cambiando el número y el sprint. Cuando estén creadas, avisa al grupo para que cada uno añada sus subtareas.

| Resumen | Sprint | Estimación original | Descripción (copiar) |
|---|---|---|---|
| `MGT IT-X. Sprint planning` | IT-X | 2 h (suma de las 4 subtareas) | Planning del sprint: objetivo y selección del backlog (30 min por persona). |
| `MGT IT-X. Dailies (2 × 15 min)` | IT-X | 2 h (suma de las 4 subtareas) | Dos dailies por Discord, viernes y lunes (15 min cada una). |
| `MGT IT-X. Coordinación de roles` | IT-X | 3 h (suma de las 4 subtareas) | Coordinación propia de cada rol: PO 0,5 h · SM 1 h · TL 1 h · DevOps/QA 0,5 h. |
| `MGT IT-X. Sprint review` | IT-X | 1 h (suma de las 4 subtareas) | Revisión del incremento con el profesor en la sesión del miércoles (15 min por persona). |
| `MGT IT-X. Sprint retrospective` | IT-X | 1 h (suma de las 4 subtareas) | Retrospectiva del sprint (15 min por persona). |

Ejemplo: `MGT IT-1. Sprint planning`, sprint «IT-1. Goal: Base técnica y datos», versión R1. Para IT-3 e IT-4 la versión es R2; para IT-5 e IT-6, R3 · MVP.

---

## EP-006. Vistas ampliadas de estado e historial

### US-019. Consultar una vista unificada de mis solicitudes

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-019. Consultar una vista unificada de mis solicitudes` |
| Épica (principal) | EP-006. Vistas ampliadas de estado e historial |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero ver todas mis solicitudes juntas y agrupadas por estado, para revisarlas sin abrir cada turno del calendario.

Prioridad MoSCoW: Should. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-009 (funcional), US-010 (funcional), US-018 (funcional)

Criterios de aceptación:
- US-019-AC-01: El empleado dispone de una pantalla unificada de sus solicitudes, agrupadas en activas (Propuesta y Aceptada) y terminadas (Aprobada, Rechazada, Caducada y, si existe US-011, Cancelada), ordenadas por última actividad.
- US-019-AC-02: Cada elemento muestra los turnos y el estado, y enlaza al detalle básico existente, incluido el motivo de rechazo manual o por regla cuando exista.

Ficha completa: specs/EP-006…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-009, US-010, US-018

### US-020. Consultar una cronología ampliada de intercambios

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-020. Consultar una cronología ampliada de intercambios` |
| Épica (principal) | EP-006. Vistas ampliadas de estado e historial |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero ver en una cronología los eventos de cada solicitud de mi servicio, para seguir visualmente su evolución.

Prioridad MoSCoW: Should. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-018 (funcional)

Criterios de aceptación:
- US-020-AC-01: El responsable ve los eventos registrados de una solicitud en orden temporal, con acción, autor y fecha; una propuesta aún no aceptada no muestra una aceptación inventada.
- US-020-AC-02: La cronología coincide con el detalle básico y solo es accesible al responsable del servicio. La cancelación aparece únicamente si se incorpora US-011.

Ficha completa: specs/EP-006…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-018

### US-021. Recibir avisos dentro de la aplicación

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-021. Recibir avisos dentro de la aplicación` |
| Épica (principal) | EP-006. Vistas ampliadas de estado e historial |
| Prioridad | Low (Baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `could` · `incertidumbre-media` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero recibir un aviso dentro de la aplicación cuando cambie el estado de una solicitud, para no tener que revisarla constantemente.

Prioridad MoSCoW: Could. Incertidumbre: Media. Estimación tras D-18: 3 h-p.
Predecesoras: US-019 (funcional)

Criterios de aceptación:
- US-021-AC-01: Al entrar, el empleado ve un indicador con los cambios de estado desde su última visita.

Ficha completa: specs/EP-006…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-019

### US-022. Filtrar el historial

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-022. Filtrar el historial` |
| Épica (principal) | EP-006. Vistas ampliadas de estado e historial |
| Prioridad | Lowest (Más baja) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 2 h |
| Etiquetas | `wont` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero filtrar el historial por empleado y fechas, para encontrar un cambio concreto.

Prioridad MoSCoW: Won't. Incertidumbre: Baja. Estimación tras D-18: 2 h-p.
Predecesoras: US-020 (funcional)

Criterios de aceptación:
- US-022-AC-01: El responsable puede limitar las decisiones de su servicio por empleado y por un intervalo de fechas inclusivo.
- US-022-AC-02: Un intervalo cuyo inicio sea posterior al fin se rechaza con un mensaje; cero coincidencias muestra una lista vacía, sin ocultar un error de permisos.

Ficha completa: specs/EP-006…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-020

---

## Tus subtareas de gestión (MGT)

Paula crea las 30 tareas MGT (5 por sprint). Cuando estén, entra en cada una y pulsa *Añadir subtarea* con tu parte. Son 30 subtareas: 5 por sprint.

| Dentro de la tarea | Resumen de tu subtarea | Asignado | Estimación |
|---|---|---|---|
| `MGT IT-1. Sprint planning` | `MGT IT-1. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-1. Dailies (2 × 15 min)` | `MGT IT-1. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-1. Coordinación de roles` | `MGT IT-1. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-1. Sprint review` | `MGT IT-1. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-1. Sprint retrospective` | `MGT IT-1. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-2. Sprint planning` | `MGT IT-2. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-2. Dailies (2 × 15 min)` | `MGT IT-2. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-2. Coordinación de roles` | `MGT IT-2. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-2. Sprint review` | `MGT IT-2. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-2. Sprint retrospective` | `MGT IT-2. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-3. Sprint planning` | `MGT IT-3. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-3. Dailies (2 × 15 min)` | `MGT IT-3. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-3. Coordinación de roles` | `MGT IT-3. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-3. Sprint review` | `MGT IT-3. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-3. Sprint retrospective` | `MGT IT-3. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-4. Sprint planning` | `MGT IT-4. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-4. Dailies (2 × 15 min)` | `MGT IT-4. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-4. Coordinación de roles` | `MGT IT-4. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-4. Sprint review` | `MGT IT-4. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-4. Sprint retrospective` | `MGT IT-4. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-5. Sprint planning` | `MGT IT-5. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-5. Dailies (2 × 15 min)` | `MGT IT-5. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-5. Coordinación de roles` | `MGT IT-5. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-5. Sprint review` | `MGT IT-5. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-5. Sprint retrospective` | `MGT IT-5. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-6. Sprint planning` | `MGT IT-6. Sprint planning · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-6. Dailies (2 × 15 min)` | `MGT IT-6. Dailies (2 × 15 min) · Paula` | Paula (PaulaJCruz) | 0,5 h |
| `MGT IT-6. Coordinación de roles` | `MGT IT-6. Coordinación de roles · Paula` | Paula (PaulaJCruz) | 1 h |
| `MGT IT-6. Sprint review` | `MGT IT-6. Sprint review · Paula` | Paula (PaulaJCruz) | 0,25 h |
| `MGT IT-6. Sprint retrospective` | `MGT IT-6. Sprint retrospective · Paula` | Paula (PaulaJCruz) | 0,25 h |

Total de tus horas de gestión: **15 h**.
