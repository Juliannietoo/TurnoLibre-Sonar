# Audit report v01

Agente auditor de TurnoLibre (AG-02) · modo INITIAL · informe consultivo. Las decisiones sobre cada hallazgo corresponden al equipo y se registran en la Wiki, «Uso de agentes».

## 1. Metadatos de la ejecución

| Campo | Valor |
|---|---|
| Repositorio y commit revisado | `C:\GPS_GC02`, rama `main`, commit **20d453b**, árbol de trabajo limpio (los ficheros en disco se tratan como ese commit) |
| Wiki (decisiones humanas) | Clon local `C:\GPS_GC02_wiki`, commit **90565b6** |
| Fecha de ejecución | 14/10/2026 (fecha del entorno de ejecución; hora no registrada) |
| Modo | INITIAL (no hay informe de auditoría previo) |
| Enfoque | Completo: riesgos, planes de ProjectLibre, viabilidad de la asignación, secuencia y coste |
| Fichero del agente | `.github/agents/project-auditor.agent.md` (contrato) y `.claude/agents/project-auditor.md` (adaptación a Claude Code) |
| Herramienta | Claude Code (subagente general-purpose cargado con las instrucciones de .claude/agents/project-auditor.md, porque el agente se creó durante la sesión y no estaba registrado) |
| Modelo | claude-opus-5-5 |
| Idioma | Español (es-ES); IDs, estados y severidades como en el contrato |
| Herramientas usadas | Solo lectura y búsqueda (Read, Glob, Grep) y una escritura: este informe. Sin comandos, sin web, sin otros agentes |

## 2. Manifiesto de fuentes y limitaciones

| Fuente | Versión / referencia | Lectura |
|---|---|---|
| `.specify/memory/constitution.md` | v1.1, 13/10/2026 | Completa |
| `specs/product/goals.md` | Restricciones D-26 | Completa |
| `specs/product/catalogo.md` | requisitos-v1-revisado (D-24/D-25) | Completa |
| `specs/EP-001…EP-007/spec.md` | Cabeceras 14/10/2026 | Predecesoras de todas las historias (búsqueda); US-023 (EP-007) leída en detalle |
| `docs/risks/technical-risks.md` | RT-01…RT-04 (RT-04 añadido el 14/10/2026) | Completa |
| `docs/organization/capacity.md` | D-21/D-24/D-25 | Completa |
| `docs/organization/company.md` | Revisión D-26 | Completa |
| `docs/quality/definition-of-ready.md` | v1.0 | Completa |
| `docs/quality/definition-of-done.md` | v1.1 | Completa |
| `docs/planning/extracts/TurnoLibre_H3_extracto-v4.md` | Extracto del libro v4 | Completo (sustituye al .xlsx, ver limitaciones) |
| `docs/planning/projectlibre/TurnoLibre_plan_por_sprints.xml` | MS Project XML (SaveVersion 14) | Completo: calendario, 59 tareas, 79 enlaces, 4 recursos, 154 asignaciones |
| `docs/planning/projectlibre/TurnoLibre_plan_por_epicas.xml` | MS Project XML | Calendario, tareas y recursos completos; asignaciones y enlaces comparados con el plan por sprints (154 asignaciones y 79 enlaces en ambos) |
| `docs/reviews/initial-planning/initial-planning-review-v02.md` | RECHECK AG-03 | Búsqueda de estados (DEFERRED, PARTIALLY_RESOLVED) |
| `docs/reviews/requirements/`, `initial-planning-review-v01.md` | Informes AG-01 v01/v02 y AG-03 v01 | No leídos íntegros; su contenido y su decisión humana se tomaron del resumen trazado en «Uso de agentes» |
| Wiki: `Registro-de-decisiones.md` | D-01…D-26 | Completa (en especial D-19, D-21, D-24, D-25, D-26) |
| Wiki: `Uso-de-agentes.md` | R-01…R-30 | Completa |
| Wiki: `Planificacion-H3.md`, `Planificacion-H4.md` | — | Completas |

**Limitaciones**
- El libro `docs/planning/TurnoLibre_H3_planificacion.xlsx` (versión 4) no se puede leer con estas herramientas: se revisa el **extracto v4**. Las comprobaciones «libro = extracto» se dan por ciertas según declara el extracto («los valores son los que calculan sus fórmulas»); no se han verificado las fórmulas.
- Los ficheros `.pod` son binarios y no se han revisado. Todo lo dicho sobre ProjectLibre se refiere al XML de origen; lo que ProjectLibre muestre tras la importación (jerarquía, costes recalculados, camino crítico) es **NOT_ASSESSABLE** desde aquí.
- La fecha de ejecución procede del entorno (14/10/2026). No se ha ejecutado git, por lo que no se ha comprobado la fecha del commit.
- Los cálculos de carga semanal de ProjectLibre por semana natural suponen el reparto uniforme del trabajo que implican las unidades fijas del XML.

## 3. Resultado y resumen

**Resultado: CONSISTENT_WITH_NON_BLOCKING_FINDINGS.** Hallazgos bloqueantes: **0**. Hallazgos: 3 MAJOR, 6 MINOR y 2 QUESTION (11 en total).

Conclusión principal: el libro (extracto v4), los dos XML de ProjectLibre, `company.md`, `goals.md` y la Wiki coinciden en horas, asignaciones y coste. Recalculado de forma independiente: 46 h de historias + 54 h de gestión = **100 h**; personal **1.996,88 €**; precio **3.737,53 € con IVA**; ninguna persona supera su capacidad efectiva en ningún sprint y ninguna supera 6 h menos ausencias en ninguna semana de sprint. Las dos vistas tienen las mismas 154 asignaciones y los mismos 79 enlaces. Todas las predecesoras del catálogo para las Must están en el plan, salvo matices de modelado.

Los problemas relevantes son tres, ninguno bloqueante:
1. **UID duplicados** en los dos XML (AUD-v01-001): el formato exige UID únicos; el efecto en los `.pod` no se puede comprobar.
2. **El tratamiento de RT-04 no coincide con el plan** (AUD-v01-002): ProjectLibre hace depender TK-006 y TK-002 de TK-001, y el margen de 2,18 h que cita es del equipo, no del TL (0,48 h).
3. **Riesgos de plan sin registrar** (AUD-v01-003): evaluador externo de US-023/M04, margen mínimo en IT-002 y cierre de US-018/US-023 en el último sprint sin holgura.

## 4. Riesgos

### 4.1 Registro `technical-risks.md`

| ID | Situación | Evento | Consecuencia | Tratamiento | Probabilidad | Impacto | Responsable | Estado | Huecos |
|---|---|---|---|---|---|---|---|---|---|
| RT-01 Reglas de negocio | Sí | Sí | Sí (G02, M02) | Sí (módulo central + pruebas por regla) | Media (texto) | Alto (texto) | No por riesgo (autor del documento: TL) | No | Sin responsable ni estado (AUD-v01-004) |
| RT-02 Concurrencia | Sí | Sí | Sí (principio 4, M02) | Sí (transacción + revalidación en US-018) | Media (texto) | Alto (texto) | No | No | Idem |
| RT-03 Control de acceso | Sí | Sí | Sí (principio 5) | Sí (permisos + pruebas de acceso indebido) | Media (texto) | Alto (texto) | No | No | Idem |
| RT-04 Tecnologías sin confirmar | Sí | Sí | Sí (IT-001, sin sprint de holgura) | Sí, pero no coincide con el plan | Media (texto) | Alto (texto) | No (la acción del 21/10 es del TL según R-12) | No | Tratamiento incoherente con ProjectLibre y con la capacidad del TL (AUD-v01-002) |

Las cuatro fichas tienen los cuatro elementos (situación, evento, consecuencia y tratamiento). La reserva del 10 % de `company.md` se justifica con RT-01…RT-04. El residuo de RT-01 señalado por AG-01 (R-02) ya no aparece: el texto actual se refiere a D-22.

### 4.2 Riesgos visibles en el plan y no registrados

| Riesgo visible | Evidencia | ¿En el registro? |
|---|---|---|
| Evaluador externo de US-023 / M04 | Catálogo §6 «Evaluador externo de US-023: lo identifican PO y QA antes de planificar IT-005 (18/11/2026)»; R-13 «Pendiente de aplicar»; IPR-v01-004 DEFERRED en el informe AG-03 v02; parte 2 de US-023 el 30/11, último día laborable antes de la entrega | No |
| Margen mínimo en IT-002 (semana con 4 exámenes/entregas) | Extracto §4: PO 0,10 h, TL 0,13 h, QA 0,20 h, SM 0,35 h; equipo 0,78 h. Planificación H3 §7: «Poco margen en IT-002» | No |
| Cierre de US-018 (incertidumbre alta, 6,5 h) y de US-023 en IT-006 sin sprint de holgura | Planificación H3 §7 y H4 §5 («No hay ningún sprint de holgura»); IT-006 incluye la entrega de la práctica 4 de GPS (27/11) | Solo en parte: RT-02 trata la consistencia técnica de US-018, no el riesgo de plazo |

## 5. ProjectLibre (XML de origen de los `.pod`)

| Comprobación | Plan por sprints | Plan por épicas | Resultado |
|---|---|---|---|
| Calendario definido | «TurnoLibre (lunes a viernes, 8 h)», 08–12 y 13–17, sábado y domingo no laborables; 21/10/2026 08:00 → 01/12/2026 17:00 | Igual | OK. Sin excepciones (festivos): ver pregunta 6. `WeekStartDay` = 1 (lunes): ver AUD-v01-007 |
| Recursos con capacidad y coste | 4 recursos, `MaxUnits` 1, tarifas 19,50 / 24,75 / 15,75 / 20,25 €/h = `company.md`; capacidad por sprint en las notas | Igual | OK según la convención declarada (100 %, tope semanal en el libro). Notas del TL con 2,12 h en lugar de 2,13 h (AUD-v01-008) |
| Tareas con ID, trabajo y duración | US-XXX, TK-001…TK-007, MGT IT-X, IT-X. Goal; `Work` = estimación consensuada (5, 3, 3, 3, 3, 8, 3, 5, 3, 8, 2 h); duraciones en días | Mismas tareas hoja; resúmenes EP-001…EP-005 y EP-007 | OK. MSPDI no tiene campo de estimación separado: se usa `Work` |
| Identificadores únicos (UID) | UID 1003 repetido (IT-1 y US-003) | UID 1008 ×2, 1012 ×2, 1017 ×2, 1019 ×3 | **Defecto** (AUD-v01-001) |
| Dependencias aplicadas | 79 enlaces: FS entre historias y dentro de cada sprint; SS de dailies y coordinación con la planning | 79 enlaces, mismos pares | OK, con matices en US-001 → US-003 (AUD-v01-005) y US-023 parte 1 (AUD-v01-006) |
| Asignaciones según el esfuerzo | 154 asignaciones; horas por persona y tarea = extracto §3 | Las mismas 154 (tarea, recurso, unidades, trabajo) | OK |
| Tareas de gestión MGT | 5 por sprint (planning, dailies, coordinación, review, retrospectiva): 9 h/sprint, 54 h | Agrupadas en «Gestión (Management)» | OK. Nombre «Coordinación de roles» frente a «Coordinación del rol» en el extracto (sin efecto) |
| Hitos | R1 03/11 17:00, R2 17/11 17:00, R3 01/12 17:00 (D-19) | En «Gestión › Hitos de release» | OK |
| Dos vistas con las mismas tareas, trabajo y coste | Total 100 h (17 + 15 + 20 + 17 + 15 + 16) | Total 100 h (Gestión 54 + Historias 46: EP-001 11, EP-002 6, EP-003 11, EP-004 8, EP-005 8, EP-007 2) | OK. Coste almacenado en los campos `Cost` con otro redondeo (AUD-v01-009) |

## 6. Viabilidad de la asignación

### 6.1 Capacidad efectiva recalculada (h)

`efectiva = max(0, 6 − ausencias − 1,5 − coordinación) × (1 − margen)`

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---|---|---|---|---|---|---|
| Lucansado (PO) | 3 × 0,80 = 2,40 | 2 × 0,80 = 1,60 | 4 × 0,80 = 3,20 | 2,40 | 2,40 | 2,40 | 14,40 |
| PaulaJCruz (SM) | 2,5 × 0,90 = 2,25 | 1,5 × 0,90 = 1,35 | 3,5 × 0,90 = 3,15 | 2,25 | 2,25 | 2,25 | 13,50 |
| MarvelinoGG (TL) | 3,5 × 0,85 = 2,975 | 2,5 × 0,85 = 2,125 | 2,975 | 2,125 | 2,125 | 2,125 | 14,45 |
| Juliannietoo (QA) | 3 × 0,85 = 2,55 | 2 × 0,85 = 1,70 | 4 × 0,85 = 3,40 | 2,55 | 2,55 | 2,55 | 15,30 |
| Equipo | 10,175 | 6,775 | 12,725 | 9,325 | 9,325 | 9,325 | **57,65** |

Conciliación: 144 − 36 (reuniones) − 18 (coordinación) − 22 (ausencias) − 10,35 (margen: PO 3,60 + SM 1,50 + TL 2,55 + QA 2,70) = **57,65 h**. Coincide con `capacity.md` y el extracto.

### 6.2 Carga de historias frente a capacidad (h asignadas / capacidad; diferencia)

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---|---|---|---|---|---|---|
| PO | 1,5 / 2,40 (0,90) | 1,5 / 1,60 (**0,10**) | 2,5 / 3,20 (0,70) | 2 / 2,40 (0,40) | 1 / 2,40 (1,40) | 2 / 2,40 (0,40) | 10,5 / 14,40 |
| SM | 1,5 / 2,25 (0,75) | 1 / 1,35 (0,35) | 3 / 3,15 (0,15) | 2 / 2,25 (0,25) | 1 / 2,25 (1,25) | 1,5 / 2,25 (0,75) | 10 / 13,50 |
| TL | 2,5 / 2,975 (0,475) | 2 / 2,125 (**0,125**) | 2,5 / 2,975 (0,475) | 2 / 2,125 (0,125) | 2 / 2,125 (0,125) | 1,5 / 2,125 (0,625) | 12,5 / 14,45 |
| QA | 2,5 / 2,55 (**0,05**) | 1,5 / 1,70 (0,20) | 3 / 3,40 (0,40) | 2 / 2,55 (0,55) | 2 / 2,55 (0,55) | 2 / 2,55 (0,55) | 13 / 15,30 |

Sobrecargas: **0**. Trabajo Must sin asignar: **0 h** (cada historia suma su estimación: US-001 5, US-003 3, US-002 3, US-005 3, US-006 3, US-012 5, US-014 3, US-009 8, US-010 3, US-018 1,5 + 6,5, US-023 1,5 + 0,5). Los mismos valores salen de las asignaciones del XML.

### 6.3 Horas totales en ProjectLibre por semana de sprint (historias + MGT) frente a 6 h − ausencias

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 |
|---|---|---|---|---|---|---|
| PO (MGT 2 h/sprint) | 3,5 / 5 | 3,5 / 4 | 4,5 / 6 | 4 / 5 | 3 / 5 | 4 / 5 |
| SM (MGT 2,5 h) | 4 / 5 | 3,5 / 4 | 5,5 / 6 | 4,5 / 5 | 3,5 / 5 | 4 / 5 |
| TL (MGT 2,5 h) | 5 / 6 | 4,5 / 5 | 5 / 6 | 4,5 / 5 | 4,5 / 5 | 4 / 5 |
| QA (MGT 2 h) | 4,5 / 5 | 3,5 / 4 | 5 / 6 | 4 / 5 | 4 / 5 | 4 / 5 |

Ninguna semana de sprint supera la disponibilidad nominal. Las horas MGT por persona y sprint (1,5 h de reuniones + coordinación) son exactamente las que descuenta la capacidad, como declara D-26: no hay doble cómputo. Por semana natural (lunes–domingo), la vista por defecto de ProjectLibre, la SM suma ≈ 6,17 h del 09/11 al 15/11 (AUD-v01-007).

### 6.4 Coste: libro (extracto) / ProjectLibre XML / `company.md`

| Persona | Horas (historias + MGT) | Tarifa | Coste recalculado | Extracto | `company.md` | XML (tarifa × trabajo) |
|---|---|---|---|---|---|---|
| PO | 10,5 + 12 = 22,5 | 19,50 € | 438,75 € | 438,75 € | 438,75 € | 438,75 € |
| SM | 10 + 15 = 25 | 24,75 € | 618,75 € | 618,75 € | 618,75 € | 618,75 € |
| TL | 12,5 + 15 = 27,5 | 15,75 € | 433,125 € | 433,13 € | 433,13 € | 433,125 € |
| QA | 13 + 12 = 25 | 20,25 € | 506,25 € | 506,25 € | 506,25 € | 506,25 € |
| Total | **100 h** | | **1.996,875 €** | 1.996,88 € | 1.996,88 € | 1.996,875 € (suma de los campos `Cost`: 1.996,97 €, AUD-v01-009) |

Coste por sprint recalculado (MGT = 180,75 €/sprint; historias IT-001…IT-006 = 156,375 / 115,875 / 223,125 / 160,50 / 116,25 / 140,25 €): **337,13 · 296,63 · 403,88 · 341,25 · 297,00 · 321,00 €**. Coincide con el extracto y la Wiki H4.

Presupuesto recalculado: personal 1.996,875 + equipos 115,38 (4.000 € ÷ 4 años × 6/52) + software 30,00 + gastos generales 15 % 299,53 = **2.441,79 €**; reserva 10 % 244,18 → 2.685,97; margen 15 % 402,90 → **3.088,87 € sin IVA**; IVA 21 % 648,66 → **3.737,53 €**. Coincide con `company.md`, `goals.md`, D-26 y Planificación H4.

Nota (pregunta 5): si se consumiera todo el margen de capacidad sin comprometer (PO 3,90 h, SM 3,50, TL 1,95, QA 2,30), las horas asignadas aumentarían en 11,65 h, con 239,96 € más de personal (275,95 € con gastos generales). La reserva del 10 % (244,18 €) cubre el personal, pero no los gastos generales asociados.

## 7. Secuencia

### 7.1 Predecesoras del catálogo frente al plan (FS salvo indicación)

| Historia | Predecesoras (catálogo / ficha) | Enlaces en ProjectLibre | Resultado |
|---|---|---|---|
| US-001 | Externa: tecnologías autorizadas | TK-001 ← planning IT-1; sin hito externo | Externa no modelada; cubierta por RT-04 (AUD-v01-002) |
| US-003 | US-001 (técnica) | Solo TK-006 ← TK-001; TK-005 ← planning; TK-007 ← TK-006. US-003 empieza el 22/10, igual que US-001 | Parcial a nivel de tarea (AUD-v01-005) |
| US-002 | US-001, US-003 | ← planning IT-2, TK-004, TK-007 (y por transitividad toda IT-1) | OK |
| US-005 | US-002, US-003 | ← US-002, TK-007; 02/11 tras US-002 (29–30/10) | OK |
| US-006 | US-005 | ← planning IT-3, US-005 | OK |
| US-012 | US-003 (formato con US-009 sin requerirla) | ← planning IT-3, TK-007 | OK |
| US-014 | US-003, US-012 | ← US-012, TK-007; 09/11 tras US-012 (05–06/11) | OK |
| US-009 | US-006, US-005, US-003 | ← planning IT-4, US-006, US-005, TK-007 | OK |
| US-010 | US-009 | ← planning IT-5, US-009 | OK |
| US-018 | US-010, US-012, US-014 | Parte 1 ← US-012, US-014 (preparación, D-24); parte 2 ← parte 1, US-010 | OK con la excepción de D-24 |
| US-023 | US-018 (parte 2); parte 1 solo US-001…US-003 (D-24); externa: evaluador | Parte 1 ← planning IT-5, US-002; parte 2 ← US-018 parte 2, parte 1 | OK según D-24; la parte 1 describe «aceptar» (US-010) en paralelo a US-010 (AUD-v01-006). Evaluador no modelado (AUD-v01-003) |

No hay ninguna tarea que empiece antes de que termine su predecesora FS en el XML. Todos los enlaces son FS (tipo 1) o SS (tipo 3, solo dailies y coordinación), sin desfases.

### 7.2 Camino crítico, hitos, holgura y reservas
- **Cadena de dependencias Must** (catálogo, Planificación H3/H4): US-001 → US-003 → US-002 → US-005 → US-006 → US-009 → US-010 → US-018 → US-023. En ProjectLibre el tramo US-001 → US-003 es paralelo (AUD-v01-005).
- **Camino crítico en ProjectLibre:** cada sprint está encadenado (planning → historias → review → retrospectiva → planning siguiente) y termina el martes. El fin calculado (01/12/2026 17:00) coincide con el fin de D-19: **holgura total del proyecto = 0 días**. Las duraciones en días (por ejemplo, 3 h de trabajo en 3 días) son convención del equipo, así que el camino crítico de ProjectLibre refleja la estructura de sprints más que el esfuerzo. La holgura real está en horas (§6.2).
- **Hitos:** R1 03/11, R2 17/11 y R3 01/12, alineados con D-19.
- **Reservas:** 11,65 h de capacidad sin comprometer (2,18 · 0,78 · 1,73 · 1,33 · 3,33 · 2,33 h por sprint), márgenes individuales (10,35 h) y reserva económica del 10 %. El margen de equipo no es transferible sin reasignar tareas: los márgenes individuales mínimos son QA 0,05 h (IT-001), PO 0,10 h y TL 0,125 h (IT-002) y TL 0,125 h (IT-004 e IT-005).
- **Excepción DoR «cabe en un sprint»:** US-018 y US-023 tienen la excepción explícita de D-24, reflejada en el plan.

## 8. Hallazgos

### 8.1 Índice

| ID | Categoría | Severidad | Bloqueante | Resumen |
|---|---|---|---|---|
| AUD-v01-001 | ProjectLibre | MAJOR | NO | UID de tarea duplicados en los dos XML de origen de los `.pod` |
| AUD-v01-002 | Riesgos / Secuencia | MAJOR | NO | El tratamiento de RT-04 contradice las dependencias del plan y cita un margen de equipo que el TL no tiene |
| AUD-v01-003 | Riesgos | MAJOR | NO | Riesgos de plan visibles (evaluador externo, margen de IT-002, cierre en IT-006) sin registrar |
| AUD-v01-004 | Riesgos | MINOR | NO | El registro no tiene responsable ni estado por riesgo; probabilidad e impacto solo en texto |
| AUD-v01-005 | Secuencia | MINOR | NO | US-001 → US-003 solo se modela como TK-001 → TK-006; la Wiki afirma FS entre historias |
| AUD-v01-006 | Secuencia | MINOR | NO | La parte 1 de US-023 describe el paso «aceptar» de US-010, que se desarrolla en paralelo y sin enlace |
| AUD-v01-007 | Viabilidad / ProjectLibre | MINOR | NO | La semana de ProjectLibre empieza en lunes: la SM suma 6,17 h en la semana natural 09–15/11 |
| AUD-v01-008 | ProjectLibre | MINOR | NO | Notas del recurso TL con 2,12 h en lugar de 2,13 h (regresión de R-15) |
| AUD-v01-009 | Coste | MINOR | NO | Los campos `Cost` del XML redondean de otra forma: suman 1.996,97 € frente a 1.996,88 € |
| AUD-v01-010 | Trazabilidad | MINOR | NO | R-12 sigue «Pendiente de aplicar» aunque RT-04 ya está registrado |
| AUD-v01-011 | Trazabilidad | QUESTION | NO | D-26, el extracto v4, `company.md` y el contrato del auditor tienen fecha 15/10/2026, posterior a esta ejecución |

### 8.2 Registros detallados

#### AUD-v01-001 · UID de tarea duplicados en los XML de ProjectLibre
- **Categoría:** ProjectLibre · **Severidad:** MAJOR · **Bloqueante:** NO
- **Evidencia:**
  - `TurnoLibre_plan_por_sprints.xml`, línea 37: `<Task><UID>1003</UID><ID>1</ID><Name>IT-1. Goal: Base técnica y datos</Name>`; línea 61: `<Task><UID>1003</UID><ID>10</ID><Name>US-003. Cargar los datos de demostración</Name>`.
  - `TurnoLibre_plan_por_epicas.xml`: UID 1008 en «Gestión (Management)» (l. 37) y «Hitos de release» (l. 152); UID 1012 en «EP-001…» (l. 165) y «US-003…» (l. 186); UID 1017 en «EP-005…» (l. 230) y «US-018. Resolver una solicitud» (l. 232); UID 1019 en «Historias de usuario» (l. 163), «EP-007…» (l. 244) y «US-023…» (l. 246).
  - Todos son tareas resumen. Ningún `PredecessorUID` ni `TaskUID` de asignación apunta a un UID ≥ 1000.
- **Impacto:** el formato MS Project XML identifica cada tarea por su UID. Con duplicados, el importador puede sobrescribir o confundir tareas resumen (jerarquía, totales de resumen o nombres). Como ningún enlace ni asignación las usa, es probable que las tareas hoja, las horas y el coste no cambien, pero no se puede confirmar sin abrir los `.pod`. Además, cualquier reimportación o regeneración hereda el defecto.
- **Acción recomendada:** generar los XML con UID únicos en las tareas resumen. Comprobar en ProjectLibre que las dos vistas muestran la jerarquía completa (IT-1…IT-6 y US-001/US-003 en sprints; Gestión, Hitos, EP-001…EP-007, US-018 y US-023 en épicas) con 100 h y 1.996,88 €, y volver a guardar los `.pod` si hace falta.
- **Confianza:** HIGH en la duplicación (lectura directa). MEDIUM en el impacto, porque los `.pod` no son revisables.
- **Rol sugerido:** SM (genera los planes), con revisión del TL.

#### AUD-v01-002 · El tratamiento de RT-04 no coincide con el plan
- **Categoría:** Riesgos / Secuencia · **Severidad:** MAJOR · **Bloqueante:** NO
- **Evidencia:**
  - `technical-risks.md`, RT-04, tratamiento: «avanzar con las tareas de IT-001 que no dependan del stack (TK-005, TK-006 y la preparación posible de TK-002) y completar TK-001 cuando se confirme, utilizando si fuera necesario el margen de IT-001 (2,18 h)».
  - Los dos XML: TK-006 (UID 7) tiene `PredecessorUID` 4 (TK-001) y 5 (TK-005); TK-002 (UID 6) tiene `PredecessorUID` 4 (TK-001); TK-003 y TK-004 dependen de TK-002, y TK-007 de TK-006. Si TK-001 se retrasa, ProjectLibre desplaza todo IT-001 menos TK-005.
  - Extracto §4: 2,18 h es el margen del **equipo** en IT-001. TK-001 es del TL (MarvelinoGG), cuyo margen individual es 2,98 − 2,50 = **0,48 h** (QA 0,05 h). Para usar más margen hay que reasignar trabajo a PO (0,90 h) o SM (0,75 h), o se rompe la regla «No se puede sobreasignar tareas».
- **Impacto:** el plan de contingencia de la raíz de la cadena crítica no puede ejecutarse tal como está modelado, y la holgura que cita no es utilizable por quien hace la tarea. Un retraso de TK-001 tendría más efecto del que indica el registro.
- **Acción recomendada (opciones condicionadas, a decidir por el equipo):** (a) quitar en ProjectLibre la dependencia TK-001 → TK-006, o explicar por qué el script de carga necesita el stack (en cuyo caso RT-04 no debería citar TK-006); (b) precisar en RT-04 quién absorbería horas extra de TK-001 y con qué margen individual, o qué tarea se reasignaría.
- **Confianza:** HIGH (enlaces y cifras leídos directamente).
- **Rol sugerido:** TL (riesgos y TK-001), con la SM para el plan.

#### AUD-v01-003 · Riesgos de plan visibles y no registrados
- **Categoría:** Riesgos · **Severidad:** MAJOR · **Bloqueante:** NO
- **Evidencia:**
  - Catálogo §6: «Evaluador externo de US-023: lo identifican PO y QA antes de planificar IT-005 (18/11/2026)»; Uso de agentes R-13: «Pendiente de aplicar: Lucansado (PO) y Juliannietoo (QA)»; informe AG-03 v02: IPR-v01-004 **DEFERRED**. En ProjectLibre, US-023 parte 2 cae el 30/11, el último día laborable antes del hito R3 (01/12).
  - Planificación H3 §7, «Riesgos que quedan»: US-018 en el último sprint, evaluador externo y «Poco margen en IT-002 (0,78 h), semana con cuatro exámenes y entregas». Extracto §4: PO 0,10 h y TL 0,13 h de margen en IT-002.
  - Planificación H4 §5: «No hay ningún sprint de holgura»; «Riesgos ligados al camino crítico: RT-04 … y RT-02».
  - `technical-risks.md` solo contiene RT-01…RT-04, todos técnicos.
- **Impacto:** M04/G04 y el cierre de una Must (US-023) dependen de una persona externa sin identificar, sin respuesta registrada si no aparece. Las otras dos exposiciones de calendario tampoco tienen dueño, disparador ni tratamiento. La reserva del 10 % se justifica solo con riesgos técnicos.
- **Acción recomendada:** registrar estos riesgos con situación, evento, consecuencia y tratamiento, más probabilidad, impacto, responsable y estado. Por ejemplo: fecha límite para confirmar el evaluador y alternativa si no hay; respuesta prevista si una persona pierde horas en IT-002; criterio de recorte si US-018 no cierra a tiempo. Revisar si cambia la justificación de la reserva.
- **Confianza:** HIGH.
- **Rol sugerido:** TL (registro de riesgos) con PO y QA (evaluador) y SM (calendario).

#### AUD-v01-004 · Registro de riesgos sin responsable ni estado
- **Categoría:** Riesgos · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** `technical-risks.md`: la tabla principal tiene las columnas ID, Riesgo, Situación, Evento, Consecuencia y Tratamiento. La probabilidad y el impacto solo aparecen en el texto de «Justificación de la valoración» («Probabilidad media… Impacto alto»). No hay responsable ni estado por riesgo (la cabecera solo indica «Tech Lead (MarvelinoGG)» como autor de la revisión).
- **Impacto:** no se puede seguir quién vigila cada riesgo ni si está abierto, mitigado o materializado durante la ejecución, que empieza el 21/10.
- **Acción recomendada:** añadir columnas de probabilidad, impacto, responsable y estado (con fecha de revisión).
- **Confianza:** HIGH.
- **Rol sugerido:** TL.

#### AUD-v01-005 · US-001 → US-003 solo a nivel de tarea
- **Categoría:** Secuencia · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** catálogo y EP-001: US-003 tiene «Predecesoras: US-001 (técnica)». En los XML, US-003 (resumen) empieza el 22/10, igual que US-001. TK-005 solo depende de la planning, TK-006 depende de TK-001 y TK-005, y TK-007 de TK-006: falta el enlace con TK-002…TK-004. Sin embargo, Planificación H4 §3 dice «Fin a comienzo entre historias según el catálogo», y H4 §5 y el catálogo §3 presentan la cadena crítica como US-001 → US-003.
- **Impacto:** el refinamiento a nivel de tarea es razonable (el cuadrante se puede diseñar sin entorno), pero no está documentado y la Wiki describe una secuencia que el plan no aplica. Quien lea el plan puede esperar una relación FS que no existe.
- **Acción recomendada:** confirmar que es un refinamiento intencionado y documentarlo (en la Wiki H4 o en la nota de US-003), o añadir los enlaces que falten si US-003 necesita algo más de US-001 (por ejemplo, el entorno de TK-003 para validar la carga).
- **Confianza:** HIGH en la evidencia; la intención del equipo es desconocida.
- **Rol sugerido:** SM y TL.

#### AUD-v01-006 · US-023 parte 1 describe «aceptar» en paralelo a US-010
- **Categoría:** Secuencia · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** extracto §3 (D-25, R-30): «Parte 1: guion de instalación con las cuentas de prueba y los pasos de consultar, proponer y aceptar (US-023-AC-02)». La ficha EP-007 dice que la parte 1 «solo necesita US-001, US-002 y US-003 (D-24)». En ProjectLibre, US-023 parte 1 (UID 39) y US-010 «Responder a una propuesta» (UID 37) ocupan las mismas fechas (19/11–23/11) y no están enlazadas. US-023 parte 1 solo depende de la planning IT-5 y de US-002.
- **Impacto:** el paso «aceptar» del guion se redacta mientras se implementa. Puede requerir retrabajo en IT-006, cuando QA tiene 0,55 h de margen y la parte 2 la hace el PO con 0,5 h.
- **Acción recomendada:** decidir si (a) la parte 1 redacta «aceptar» al final de IT-005 con un enlace FS desde US-010, (b) ese paso pasa a la parte 2, o (c) se acepta el riesgo y se documenta. Actualizar la nota de predecesoras de US-023 para que refleje R-30.
- **Confianza:** MEDIUM (depende de cómo se organice el trabajo dentro del sprint).
- **Rol sugerido:** QA (dueño de la parte 1) y PO.

#### AUD-v01-007 · Semana de ProjectLibre (lunes) distinta de la semana de sprint (miércoles)
- **Categoría:** Viabilidad / ProjectLibre · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** XML: `<WeekStartDay>1</WeekStartDay>` (lunes); D-02/D-19: sprints de miércoles a martes. Con las unidades del XML, la SM (PaulaJCruz) suma en la semana natural del lunes 09/11 al domingo 15/11: lunes 2,63 h (US-006 0,33 + US-014 2,00 + daily 0,10 + coordinación 0,20); martes 0,80 h (review y retrospectiva IT-3); miércoles 0,80 h (planning IT-4); jueves y viernes 0,97 h cada uno (US-009 0,67 + daily + coordinación). Total **≈ 6,17 h**, por encima de las 6 h nominales, en una semana con una entrega (13/11). Por semanas de sprint no hay exceso (IT-003 5,5/6 h; IT-004 4,5/5 h).
- **Impacto:** el uso de recursos por semana de ProjectLibre muestra una sobreasignación aparente que contradice el «0 sobrecargas» del libro y puede confundir a un evaluador. El contrato pide informar si las horas semanales de ProjectLibre superan la capacidad.
- **Acción recomendada:** poner la semana de ProjectLibre en miércoles (`WeekStartDay` = 3) para que coincida con los sprints, o explicar en la Wiki H4 que el control semanal es por semana de sprint.
- **Confianza:** MEDIUM (supone reparto uniforme; no se ha visto la vista de uso de recursos de los `.pod`).
- **Rol sugerido:** SM.

#### AUD-v01-008 · Notas del recurso TL con 2,12 h
- **Categoría:** ProjectLibre · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** los dos XML, recurso UID 3: «IT-002: 2,12 h, … IT-004: 2,12 h, IT-005: 2,12 h, IT-006: 2,12 h». El extracto §1 y `capacity.md` dicen 2,13 h. R-15 (IPR-v01-006) se aceptó para unificar el redondeo a la mitad hacia arriba (valor exacto 2,125 h).
- **Impacto:** inconsistencia de presentación; reabre un hallazgo ya resuelto.
- **Acción recomendada:** usar 2,13 h en las notas al regenerar los XML.
- **Confianza:** HIGH.
- **Rol sugerido:** SM.

#### AUD-v01-009 · Redondeo de los campos `Cost` del XML
- **Categoría:** Coste · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** el XML guarda, por ejemplo, `<Cost>10.12</Cost>` (QA 0,5 h), `23.62` (TL 1,5 h), `37.12` (SM 1,5 h), `50.62` (QA 2,5 h) y `3.94` (TL 0,25 h). El extracto §3 dice 10,13, 23,63, 37,13 y 50,63 €. Recalculando la desviación de cada una de las 154 asignaciones, los campos `Cost` suman **1.996,97 €** (+0,12 € en MGT, −0,025 € en historias) frente a 1.996,875 € = 1.996,88 €.
- **Impacto:** pequeño (0,09 €). ProjectLibre suele recalcular el coste con tarifa × trabajo, pero si muestra los valores importados, el total no coincidiría con `company.md`.
- **Acción recomendada:** comprobar el coste total que muestran los `.pod` (1.996,88 €) y, al regenerar, escribir los costes con el mismo redondeo que el libro, o no incluirlos.
- **Confianza:** MEDIUM (comportamiento de importación no verificable).
- **Rol sugerido:** SM.

#### AUD-v01-010 · Estado de R-12 desactualizado
- **Categoría:** Trazabilidad · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:** Uso de agentes, R-12 (IPR-v01-003): «Aceptada. El TL lo pregunta al profesor en la sesión del 21/10 y se añade como riesgo», con «Pendiente de aplicar: MarvelinoGG (TL)». `technical-risks.md`: «RT-04 añadido el 14/10/2026». El commit 9fae570 se titula «docs: añadido del RT-04».
- **Impacto:** el registro de recomendaciones no refleja que la parte «se añade como riesgo» ya se aplicó; la pregunta del 21/10 sigue pendiente.
- **Acción recomendada:** actualizar la columna «Cambio / referencia» de R-12 (RT-04 aplicado; pregunta del 21/10 pendiente).
- **Confianza:** HIGH.
- **Rol sugerido:** SM.

#### AUD-v01-011 · Fechas posteriores a la ejecución
- **Categoría:** Trazabilidad · **Severidad:** QUESTION · **Bloqueante:** NO
- **Evidencia:** Registro de decisiones, D-26: fecha «15/10/2026» y «Equipo (OK por el grupo, 15/10/2026)». Extracto v4: «versión 4, 15/10/2026». `company.md`: «recalculó … el 15/10/2026 por D-26». Contrato del auditor: «configurado por el equipo el 15/10/2026». Esta ejecución tiene fecha 14/10/2026 según el entorno.
- **Impacto:** si D-26 aún no está aprobada, el coste de 3.737,53 € y los planes de ProjectLibre se presentan como decididos antes de tiempo. Si la fecha es una errata, la trazabilidad de la decisión (fecha y autor, constitución) queda imprecisa.
- **Acción recomendada:** confirmar la fecha real de aprobación de D-26 y corregir las fechas, o dejar D-26 como pendiente hasta la votación.
- **Confianza:** MEDIUM (fecha tomada del entorno; no se ha consultado la fecha del commit).
- **Rol sugerido:** SM.

## 9. Preguntas para el equipo

1. **(AUD-v01-001)** Al abrir los `.pod`, ¿aparecen todas las tareas resumen con su nombre y jerarquía (en especial IT-1 frente a US-003 en sprints, y EP-005/US-018 y EP-007/US-023 en épicas) y los totales de 100 h y 1.996,88 €? ¿Se regenerarán los XML con UID únicos?
2. **(AUD-v01-002)** ¿Necesita TK-006 (script de carga) la tecnología autorizada? Si TK-001 se retrasa o hay retrabajo, ¿quién absorbe las horas extra, si el TL solo tiene 0,48 h de margen en IT-001?
3. **(AUD-v01-003)** ¿Cuál es la fecha límite para confirmar al evaluador externo de US-023 y qué se hará si no hay nadie disponible el 30/11? ¿Se registrarán también el margen de IT-002 y el cierre de US-018 en IT-006 como riesgos?
4. **(AUD-v01-006)** ¿El paso «aceptar» del guion (US-023 parte 1) se redacta después de terminar US-010 dentro de IT-005, o se acepta redactarlo en paralelo?
5. **(Coste)** ¿La reserva del 10 % (244,18 €) pretende cubrir el uso del margen de capacidad? Consumir las 11,65 h costaría 239,96 € de personal y 275,95 € con gastos generales.
6. **(Calendario)** ¿Se ha comprobado el calendario laboral y académico del periodo? El calendario de ProjectLibre no tiene festivos. Por ejemplo, el 01/11/2026 es domingo y US-005 está programada solo el lunes 02/11. No se afirma que sea festivo; solo se pide confirmarlo.
7. **(AUD-v01-011)** ¿D-26 está aprobada ya o se aprobará el 15/10/2026?
8. **(AUD-v01-007)** ¿Se ajustará la semana de ProjectLibre a miércoles o se documentará que el control semanal es por semana de sprint?

## 10. Correspondencia RECHECK

No aplica: modo INITIAL, sin informe de auditoría previo.

## 11. Cierre

Esta es una auditoría consultiva. No se ha modificado ninguna fuente, plan, estimación ni decisión humana. No se ha aprobado ninguna línea base ni puerta de calidad.

*This is an advisory audit. No source, plan, estimate or human decision was changed. No baseline or gate was approved.*
