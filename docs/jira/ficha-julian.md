# Jira · ficha de Julián (Juliannietoo)

Práctica 2 · proyecto **GC02-GPS26** (clave `GC02`) · <https://gc02-gps26.atlassian.net/jira/software/projects/GC02/boards/1>

Generada desde el catálogo V1, las fichas de épica y el plan (Excel v5). Cada elemento lo crea la persona responsable del requisito, como pide el enunciado.

**Antes de empezar**
- Las épicas, los sprints IT-1 a IT-6, las versiones R1, R2 y R3 · MVP y las 30 tareas MGT las crea Paula. Espera a su aviso.
- En el campo *Estimación original* escribe las horas como `2h` o `1h 30m` (0,5 h = `30m`, 0,25 h = `15m`).
- La descripción va en el bloque gris de cada elemento: cópiala tal cual.
- Los **enlaces** («está bloqueada por») se añaden al final, cuando todos hayan creado sus historias: abre tu historia → *Vincular actividad* → «está bloqueada por» → busca el código (por ejemplo `US-006`).

**Te tocan:** EP-004, EP-007 (7 historias), sus subtareas y tus subtareas de gestión.


## EP-004. Validación de reglas

### US-012. Validar descanso mínimo y solapes

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-012. Validar descanso mínimo y solapes` |
| Épica (principal) | EP-004. Validación de reglas |
| Prioridad | Highest (Más alta) |
| Sprint | IT-3. Goal: Compatibles y reglas |
| Versión de corrección (Fix version) | R2 |
| Responsable (asignado) | Marcelino (MarvelinoGG) |
| Estimación original | 5 h |
| Etiquetas | `must` · `incertidumbre-alta` · `R2` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero que el sistema compruebe el descanso mínimo entre turnos y que no haya solapes, para no aprobar cambios que los incumplan.

Prioridad MoSCoW: Must. Incertidumbre: Alta. Estimación tras D-18: 5 h-p.
Predecesoras: US-003 (técnica). El formato de solicitud se acuerda con US-009, sin requerir esa historia terminada.
Cambio D-18 (06/10/2026): sin cambio de hora: los datos de demostración no incluyen esas semanas.

Criterios de aceptación:
- US-012-AC-01: Si entre el fin de un turno y el inicio del siguiente del mismo empleado hay menos de 12 h, el intercambio se marca inválido por RN-01.
- US-012-AC-02: Si el intercambio deja a un empleado con dos turnos solapados o con dos turnos con la misma fecha de inicio, se marca inválido por RN-06.
- US-012-AC-03: Se comprueban los dos empleados, incluidos los turnos anteriores y posteriores a los intercambiados.
- US-012-AC-04: Una petición que se salte la interfaz también es rechazada por el servidor.

Ficha completa: specs/EP-004…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-012 · Módulo de validación: RN-01 y RN-06; incluye acordar con US-009 el formato de solicitud que usan los validadores` | Marcelino (MarvelinoGG) | 2,5 h |
| `US-012 · Pruebas de reglas y casos límite` | Julián (Juliannietoo) | 2,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-003, US-009

### US-013. Validar las horas semanales

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-013. Validar las horas semanales` |
| Épica (principal) | EP-004. Validación de reglas |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-alta` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero que el sistema compruebe que ningún empleado supera 40 h en una semana natural tras el intercambio, para respetar el límite interno de jornada.

Prioridad MoSCoW: Should. Incertidumbre: Alta. Estimación tras D-18: 3 h-p.
Predecesoras: US-003 (técnica), US-012 (técnica). El formato de intercambio se acuerda con US-009, sin requerir esa historia terminada.
Cambio D-18 (06/10/2026): pasa a Should; G02 deja de exigir RN-02 en el MVP.

Criterios de aceptación:
- US-013-AC-01: Si tras el intercambio un empleado supera 40 h en alguna semana natural afectada, el intercambio se marca inválido por RN-02.
- US-013-AC-02: Un turno de noche que cruza de domingo a lunes reparte sus horas entre ambas semanas.
- US-013-AC-03: Se comprueban todas las semanas afectadas de los dos empleados.

Ficha completa: specs/EP-004…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-003, US-012, US-009

### US-014. Validar categoría, servicio y cobertura

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-014. Validar categoría, servicio y cobertura` |
| Épica (principal) | EP-004. Validación de reglas |
| Prioridad | Highest (Más alta) |
| Sprint | IT-3. Goal: Compatibles y reglas |
| Versión de corrección (Fix version) | R2 |
| Responsable (asignado) | Paula (PaulaJCruz) |
| Estimación original | 3 h |
| Etiquetas | `must` · `incertidumbre-media` · `R2` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero que solo se permitan intercambios entre empleados de la misma categoría y servicio y que se mantenga la cobertura mínima, para que ningún turno quede desatendido.

Prioridad MoSCoW: Must. Incertidumbre: Media. Estimación tras D-18: 3 h-p.
Predecesoras: US-003 (técnica), US-012 (técnica). El formato de intercambio se acuerda con US-009, sin requerir esa historia terminada.
Cambio D-18 (06/10/2026): en cada intercambio solo se comprueba RN-03; RN-04 se comprueba al preparar los datos (US-003). Los intercambios siguen siendo uno a uno dentro de la misma categoría y servicio, por lo que la cobertura se conserva.

Criterios de aceptación:
- US-014-AC-01: Un intercambio entre empleados de distinta categoría o servicio se marca inválido por RN-03.
- US-014-AC-02: RN-04 se garantiza con el cuadrante de partida (US-003): un intercambio dentro de la misma categoría y servicio no cambia la cobertura. La comprobación de 3/3/2 se realiza al preparar/restablecer los datos, no por cada intercambio (D-18/D-22).

Ficha completa: specs/EP-004…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-014 · Validación RN-03 en el módulo de reglas` | Paula (PaulaJCruz) | 2 h |
| `US-014 · Casos de prueba de compatibilidad` | Luis (Lucansado) | 0,5 h |
| `US-014 · Pruebas automáticas de RN-03` | Julián (Juliannietoo) | 0,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-003, US-012, US-009

### US-015. Validar la antelación mínima

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-015. Validar la antelación mínima` |
| Épica (principal) | EP-004. Validación de reglas |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como responsable, quiero que no se admitan solicitudes con menos de 48 h de antelación, para tener tiempo de resolverlas.

Prioridad MoSCoW: Should. Incertidumbre: Baja. Estimación tras D-18: 3 h-p.
Predecesoras: US-003 (técnica). El formato de solicitud se acuerda con US-009, sin requerir esa historia terminada.
Cambio D-18 (06/10/2026): pasa a Should; G02 deja de exigir RN-05 en el MVP.

Criterios de aceptación:
- US-015-AC-01: Al registrar una solicitud, el servidor exige al menos 48 h hasta el inicio más temprano de los dos turnos. Exactamente 48 h se admite; 47 h y 59 min se rechaza, indicando RN-05 y la antelación disponible.
- US-015-AC-02: Una solicitud registrada a tiempo puede aceptarse y aprobarse hasta antes de ese inicio, aunque ya resten menos de 48 h. Al llegar el inicio queda Caducada y no puede aceptarse ni aprobarse.
- US-015-AC-03: La caducidad reutiliza el contrato Must de US-009-AC-08, US-010-AC-05 y US-018-AC-07: actualiza el detalle básico, libera ambos turnos y usa la hora del servidor sin depender de que se abra la pantalla. US-015 añade únicamente la comprobación opcional de antelación.

Ficha completa: specs/EP-004…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-003, US-009

### US-016. Ampliar el diagnóstico de reglas

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-016. Ampliar el diagnóstico de reglas` |
| Épica (principal) | EP-004. Validación de reglas |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 2 h |
| Etiquetas | `should` · `incertidumbre-baja` |

**Descripción** (copiar y pegar):

```text
Como empleado, quiero ver juntas todas las reglas incumplidas y orientaciones para corregir mi propuesta, para encontrar otra opción más fácilmente.

Prioridad MoSCoW: Should. Incertidumbre: Baja. Estimación tras D-18: 2 h-p.
Predecesoras: US-012 (funcional), US-013 (funcional), US-014 (funcional), US-015 (funcional)

Criterios de aceptación:
- US-016-AC-01: Si se incumplen varias reglas, se muestran juntas con los resultados que justifican cada fallo.
- US-016-AC-02: Cada fallo incluye una orientación concreta, como buscar un turno que deje al menos 12 h de descanso. La orientación no promete que el intercambio cumpla las demás reglas.

Ficha completa: specs/EP-004…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-012, US-013, US-014, US-015

---

## EP-007. Calidad y entrega

### US-023. Crear el guion mínimo final de instalación y evaluación

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-023. Crear el guion mínimo final de instalación y evaluación` |
| Épica (principal) | EP-007. Calidad y entrega |
| Prioridad | Highest (Más alta) |
| Sprint | IT-6. Goal: Resolución y guion |
| Versión de corrección (Fix version) | R3 · MVP |
| Responsable (asignado) | Julián (Juliannietoo) |
| Estimación original | 0,5 h |
| Etiquetas | `must` · `incertidumbre-baja` · `R3` |

**Descripción** (copiar y pegar):

```text
Como evaluador, quiero un guion paso a paso para instalar y evaluar el producto, para comprobarlo sin ayuda del equipo.

Prioridad MoSCoW: Must. Incertidumbre: Baja. Estimación tras D-18: 2 h-p.
Predecesoras: US-018 (funcional); externa: evaluador ajeno a la implementación. Por partes: la parte 1 necesita US-001, US-002, US-003 y US-009; la parte 2, US-010 y US-018 (D-24, D-27 y D-28)
Cambio D-18 (06/10/2026): guion mínimo de instalación y evaluación al final del proyecto, no en cada release.

Criterios de aceptación:
- US-023-AC-01: Una persona que no ha participado en el desarrollo instala el producto desde un entorno limpio siguiendo solo el guion.
- US-023-AC-02: El guion final incluye preparación del entorno, restablecimiento de datos, cuentas ficticias por rol y los pasos del flujo esencial disponible en la versión final: consultar turnos, proponer, aceptar y resolver solicitudes.
- US-023-AC-03: Una persona ajena a la implementación ejecuta y evalúa la versión final desde el entorno limpio siguiendo solo el guion documentado, sin intervenciones no documentadas, conforme a M04. El guion mínimo se entrega al final, sin exigir esta evaluación en cada release (D-18).

Ficha completa: specs/EP-007…/spec.md del repositorio.
```

**Subtareas** (dentro de la historia → *Añadir subtarea*):

| Resumen | Asignado | Estimación original |
|---|---|---|
| `US-023 · Parte 2: pasos de aceptar y resolver, y validación final con el evaluador externo (coordina el PO)` | Luis (Lucansado) | 0,5 h |

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-018, US-001, US-002, US-003, US-009, US-010

### US-023 · parte 1 (tarea en IT-5)

La historia se cierra en IT-6, pero una parte se hace antes, en IT-5 (excepción explícita de D-24). En Jira una historia solo puede estar en un sprint, así que esta parte va como **tarea** aparte.

| Campo | Valor |
|---|---|
| Tipo | Tarea |
| Resumen | `US-023 · parte 1: entorno, datos, cuentas y pasos de consultar y proponer` |
| Épica (principal) | EP-007. Calidad y entrega |
| Prioridad | Highest (Más alta) |
| Sprint | IT-5. Goal: Respuesta y preparación |
| Versión de corrección | R3 · MVP |
| Asignado | Julián (Juliannietoo) |
| Estimación original | 1,5 h |
| Etiquetas | `must` · `R3` · `parte-1` |

**Descripción** (copiar y pegar):

```text
Parte 1: entorno, restablecimiento de datos, cuentas ficticias y pasos de consultar y proponer (US-023-AC-02).
Preparación de US-023 en IT-5; la historia se cierra en IT-6 (D-24, D-27, D-28).
```

**Enlace:** esta tarea *bloquea* → US-023

### US-024. Prueba de usabilidad y accesibilidad básica

| Campo | Valor |
|---|---|
| Tipo | Historia |
| Resumen | `US-024. Prueba de usabilidad y accesibilidad básica` |
| Épica (principal) | EP-007. Calidad y entrega |
| Prioridad | Medium (Media) |
| Sprint | ninguno: se queda en el **Backlog** |
| Versión | ninguna |
| Responsable (asignado) | sin asignar (no está en el plan) |
| Estimación original | 3 h |
| Etiquetas | `should` · `incertidumbre-media` |

**Descripción** (copiar y pegar):

```text
Como Product Owner, quiero probar el flujo con 3 participantes y revisar la accesibilidad básica, para comprobar M01 y M03 antes de la entrega.

Prioridad MoSCoW: Should. Incertidumbre: Media. Estimación tras D-18: 3 h-p.
Predecesoras: US-010 (funcional), US-018 (funcional), US-023 (funcional); externa: tres participantes ajenos al equipo
Cambio D-18 (06/10/2026): pasa a Should; si cabe, se realiza durante la review final.

Criterios de aceptación:
- US-024-AC-01: Tres participantes ajenos al equipo completan individualmente los pasos de proponer y aceptar un intercambio válido sobre un turno de un compañero compatible utilizando dos cuentas ficticias, hasta dejarlo pendiente de aprobación. Se registran tiempo, ayuda necesaria y resultado. M01 se cumple si los tres terminan en menos de cinco minutos y sin ayuda; se excluye el tiempo de decisión del responsable.
- US-024-AC-02: Los flujos principales se completan con teclado, con foco visible y mensajes que no dependan solo del color; se mide contraste mínimo de 4,5:1 para texto normal y 3:1 para texto grande.
- US-024-AC-03: Para M03, el responsable resuelve tres solicitudes de muestra en menos de un minuto cada una, medido desde que abre el detalle hasta que registra la decisión. Si US-024 no se realiza, M03 queda pendiente de validación, igual que M01 (D-23).

Ficha completa: specs/EP-007…/spec.md del repositorio.
```

**Enlaces** (al final, cuando existan todas las historias): *está bloqueada por* → US-010, US-018, US-023

---

## Tus subtareas de gestión (MGT)

Paula crea las 30 tareas MGT (5 por sprint). Cuando estén, entra en cada una y pulsa *Añadir subtarea* con tu parte. Son 30 subtareas: 5 por sprint.

| Dentro de la tarea | Resumen de tu subtarea | Asignado | Estimación |
|---|---|---|---|
| `MGT IT-1. Sprint planning` | `MGT IT-1. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-1. Dailies (2 × 15 min)` | `MGT IT-1. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-1. Coordinación de roles` | `MGT IT-1. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-1. Sprint review` | `MGT IT-1. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-1. Sprint retrospective` | `MGT IT-1. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-2. Sprint planning` | `MGT IT-2. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-2. Dailies (2 × 15 min)` | `MGT IT-2. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-2. Coordinación de roles` | `MGT IT-2. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-2. Sprint review` | `MGT IT-2. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-2. Sprint retrospective` | `MGT IT-2. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-3. Sprint planning` | `MGT IT-3. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-3. Dailies (2 × 15 min)` | `MGT IT-3. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-3. Coordinación de roles` | `MGT IT-3. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-3. Sprint review` | `MGT IT-3. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-3. Sprint retrospective` | `MGT IT-3. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-4. Sprint planning` | `MGT IT-4. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-4. Dailies (2 × 15 min)` | `MGT IT-4. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-4. Coordinación de roles` | `MGT IT-4. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-4. Sprint review` | `MGT IT-4. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-4. Sprint retrospective` | `MGT IT-4. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-5. Sprint planning` | `MGT IT-5. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-5. Dailies (2 × 15 min)` | `MGT IT-5. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-5. Coordinación de roles` | `MGT IT-5. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-5. Sprint review` | `MGT IT-5. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-5. Sprint retrospective` | `MGT IT-5. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-6. Sprint planning` | `MGT IT-6. Sprint planning · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-6. Dailies (2 × 15 min)` | `MGT IT-6. Dailies (2 × 15 min) · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-6. Coordinación de roles` | `MGT IT-6. Coordinación de roles · Julián` | Julián (Juliannietoo) | 0,5 h |
| `MGT IT-6. Sprint review` | `MGT IT-6. Sprint review · Julián` | Julián (Juliannietoo) | 0,25 h |
| `MGT IT-6. Sprint retrospective` | `MGT IT-6. Sprint retrospective · Julián` | Julián (Juliannietoo) | 0,25 h |

Total de tus horas de gestión: **12 h**.
