# Audit report v02

Agente auditor de TurnoLibre (AG-02) · modo RECHECK · informe consultivo. Las decisiones sobre cada hallazgo corresponden al equipo y se registran en la Wiki, «Uso de agentes».

## 1. Metadatos de la ejecución

| Campo | Valor |
|---|---|
| Repositorio y commit revisado | `C:\GPS_GC02`, rama `main`, commit **424ab4e** («H4: correcciones de la auditoría v01 (D-27), plan v5 y planes de ProjectLibre regenerados»), árbol de trabajo limpio (los ficheros en disco se tratan como ese commit) |
| Wiki (decisiones humanas) | Clon local `C:\GPS_GC02_wiki`, commit **74069c3** (indicado por quien lanza el agente; no verificado con git) |
| Fecha de ejecución | 15/10/2026 (fecha del entorno de ejecución; hora no registrada) |
| Modo | RECHECK |
| Informe previo | `docs/reviews/audit/audit-report-v01.md` (INITIAL, commit 20d453b) |
| Decisiones humanas de entrada | D-26 y D-27 (Registro de decisiones); R-31 a R-41 (Uso de agentes, correspondencia uno a uno con AUD-v01-001 … AUD-v01-011); R-12; acta del 15/10/2026 |
| Enfoque | Completo: riesgos, planes de ProjectLibre, viabilidad de la asignación, secuencia y coste, con correspondencia de los 11 hallazgos de v01 |
| Fichero del agente | `.github/agents/project-auditor.agent.md` (contrato) |
| Herramienta | Claude Code (subagente project-auditor) |
| Modelo | claude-opus-5-5 |
| Idioma | Español (es-ES); IDs, estados y severidades como en el contrato |
| Herramientas usadas | Solo lectura y búsqueda (Read, Glob, Grep) y una escritura: este informe. Sin comandos, sin web, sin otros agentes |

## 2. Manifiesto de fuentes y limitaciones

| Fuente | Versión / referencia | Lectura |
|---|---|---|
| `.github/agents/project-auditor.agent.md` | Cabecera «configurado por el equipo el 14/10/2026» | Completa |
| `docs/reviews/audit/audit-report-v01.md` | INITIAL, commit 20d453b | Completa |
| `docs/planning/extracts/TurnoLibre_H3_extracto-v5.md` | Libro versión 5, 15/10/2026 (sustituye al .xlsx) | Completo |
| `docs/planning/projectlibre/TurnoLibre_plan_por_sprints.xml` | MS Project XML (SaveVersion 14), regenerado tras v01 | Completo: cabecera, calendario, 60 tareas (incluida la tarea proyecto UID 0), 80 enlaces, 4 recursos, 154 asignaciones |
| `docs/planning/projectlibre/TurnoLibre_plan_por_epicas.xml` | MS Project XML, regenerado tras v01 | Cabecera, calendario, recursos, UID de las 71 tareas, trabajo de los resúmenes, tareas de EP-005/EP-007 completas; 154 asignaciones (tarea, recurso, unidades, trabajo) comparadas una a una con el plan por sprints; 80 enlaces (recuento y pares de US-018/US-023) |
| `docs/risks/technical-risks.md` | RT-01 … RT-07 («RT-04 corregido y RT-05 a RT-07 añadidos el 15/10/2026») | Completa |
| `specs/EP-007-calidad-y-entrega/spec.md` | Cabecera «revisión 14/10/2026» | US-023 y US-024 (búsqueda) |
| `specs/product/catalogo.md` | requisitos-v1-revisado | §3 (cadena crítica), §4, §6, §7 y fila de US-023 |
| `docs/organization/company.md` | Revisión D-26 (14/10/2026) | Completa |
| `docs/organization/capacity.md` | D-21/D-24/D-25 | Completa |
| Wiki: `Registro-de-decisiones.md` | D-01 … D-27 | Completa (en especial D-26 y D-27) |
| Wiki: `Uso-de-agentes.md` | R-01 … R-41 | Completa (en especial R-12, R-13 y R-31 … R-41) |
| Wiki: `Actas.md` | Acta del 15/10/2026 | Completa |
| Wiki: `Planificacion-H4.md`, `Planificacion-H3.md` | — | Completas |
| `.specify/memory/constitution.md`, `goals.md`, DoR, DoD, informes AG-01/AG-03 | — | No releídos en esta ejecución: no han cambiado por D-27 según el registro y su contenido se comprobó en v01 |

**Limitaciones**
- El libro `docs/planning/TurnoLibre_H3_planificacion.xlsx` (versión 5) no se puede leer con estas herramientas: se revisa el **extracto v5** y se da por cierto que reproduce los valores de las fórmulas, como declara el propio extracto.
- Los ficheros `TurnoLibre_plan_por_sprints.pod` y `TurnoLibre_plan_por_epicas.pod` existen en `docs/planning/projectlibre/`, pero son binarios: lo que ProjectLibre muestra tras la reimportación (jerarquía, coste calculado, primer día de la semana, camino crítico) es **NOT_ASSESSABLE** desde aquí. Todo lo dicho sobre ProjectLibre se refiere a los XML de origen.
- No se ha ejecutado git: no se verifican los commits 424ab4e y 74069c3, ni la fecha de los `.pod`.
- La interpretación de `<WeekStartDay>3</WeekStartDay>` como miércoles sigue el esquema MSPDI (0 = domingo). No se ha comprobado que ProjectLibre lo respete al importar.

## 3. Resultado y resumen

**Resultado: CONSISTENT_WITH_NON_BLOCKING_FINDINGS.** Hallazgos bloqueantes: **0**.

Correspondencia de los 11 hallazgos de v01: **8 RESOLVED** (001, 003, 004, 007, 008, 009, 010, 011) y **3 PARTIALLY_RESOLVED** (002, 005, 006). Hallazgos nuevos: **2 MINOR** (AUD-v02-001 y AUD-v02-002). Siguen abiertos: 1 MAJOR (AUD-v01-002, parcial) y 4 MINOR (AUD-v01-005 y AUD-v01-006 parciales, y los dos nuevos).

Conclusión principal: las correcciones de D-27 están aplicadas y comprobadas en los XML regenerados. Los UID son únicos, la semana empieza en miércoles, las notas del TL dicen 2,13 h, no hay campos `Cost` y US-023 parte 2 depende de US-010. El registro de riesgos tiene RT-05 … RT-07 con los cuatro elementos y con probabilidad, impacto, responsable y estado. Las cifras no cambian: **46 h de historias + 54 h de gestión = 100 h**; personal **1.996,88 €**; precio **3.737,53 € con IVA**. No hay sobrecargas por sprint ni por semana de ProjectLibre. Las 154 asignaciones son idénticas en las dos vistas y en el extracto v5. No hay ningún FS incumplido.

Queda un problema relevante, que no es bloqueante. El tratamiento corregido de **RT-04** cita bien el margen del TL (0,48 h), pero ahora mueve TK-001 y TK-006 (3 h) a los márgenes de IT-002 e IT-003, que suman **2,50 h de equipo**. El TL tiene ahí **0,60 h** y la SM **0,50 h**: el plan de contingencia sigue sin caber en la capacidad (AUD-v01-002, PARTIALLY_RESOLVED). Además, RT-04, RT-06 y RT-07 reclaman los mismos márgenes sin orden de prioridad (AUD-v02-001).

## 4. Riesgos

### 4.1 Registro `technical-risks.md` (estado actual)

| ID | Situación | Evento | Consecuencia | Tratamiento | Probabilidad | Impacto | Responsable | Estado | Huecos |
|---|---|---|---|---|---|---|---|---|---|
| RT-01 Reglas de negocio | Sí | Sí | Sí (G02, M02) | Sí | Media | Alto | MarvelinoGG (TL) | Abierto | — |
| RT-02 Concurrencia | Sí | Sí | Sí (principio 4, M02) | Sí (transacción + revalidación, US-018) | Media | Alto | MarvelinoGG (TL) | Abierto | — |
| RT-03 Control de acceso | Sí | Sí | Sí (principio 5) | Sí | Media | Alto | Juliannietoo (QA) | Abierto | — |
| RT-04 Tecnologías sin confirmar | Sí | Sí | Sí | Sí, corregido; coherente con los enlaces TK-001 → TK-002/TK-006 del XML | Media | Alto | MarvelinoGG (TL) | Abierto | Los márgenes de destino no bastan para 3 h y no se dice quién hace el trabajo (AUD-v01-002) |
| RT-05 Evaluador externo | Sí | Sí | Sí (US-023, G04/M04) | Sí: identificar antes del 18/11, persona de reserva y fecha del 30/11 (coincide con US-023 parte 2 en el XML) | Media | Alto | Lucansado (PO) | Abierto | — |
| RT-06 Poco margen en IT-002 | Sí (6,78 h para 6 h; PO 0,10 h, TL 0,13 h) | Sí | Sí | Sí | Media | Medio | PaulaJCruz (SM) | Abierto | Usa los márgenes de IT-001 e IT-003, también reclamados por RT-04 (AUD-v02-001) |
| RT-07 Cierre en el último sprint | Sí | Sí | Sí (G03, G04) | Sí: diseño en IT-005, márgenes de IT-005 (3,33 h) e IT-006 (2,33 h), US-011 sin compromiso y criterio de priorización | Media | Alto | MarvelinoGG (TL) | Abierto | Ver pregunta 4 (qué cuenta como cierre de US-023 si US-018 no está) |

Comprobaciones adicionales:
- Las cifras citadas en los riesgos coinciden con el extracto v5 §4: margen del TL en IT-001 2,98 − 2,50 = 0,48 h; IT-002 6,78 h para 6 h; márgenes de equipo 2,18 · 0,78 · 1,73 · 1,33 · 3,33 · 2,33 h; TL 1,5 h en US-018 parte 1 (IT-005).
- `company.md` justifica ahora la reserva del 10 % con «RT-01 a RT-07».
- Los riesgos ligados al camino crítico que cita Planificación H4 §5 (RT-04, RT-06, RT-07, RT-05 y RT-02) están todos registrados.

### 4.2 Riesgos visibles en el plan y no registrados
No se encuentran riesgos nuevos sin registrar. Los tres que señaló v01 (evaluador externo, margen de IT-002 y cierre en IT-006) son ahora RT-05, RT-06 y RT-07.

## 5. ProjectLibre (XML de origen de los `.pod`)

| Comprobación | Plan por sprints | Plan por épicas | Resultado |
|---|---|---|---|
| Calendario definido | «TurnoLibre (lunes a viernes, 8 h)», 08–12 y 13–17; 21/10/2026 08:00 → 01/12/2026 17:00; `WeekStartDay` = 3 (miércoles) | Igual | OK. Sin excepciones de calendario; D-27 confirma que no hay festivos en el periodo |
| Recursos con capacidad y coste | 4 recursos, `MaxUnits` 1, tarifas 19,5 / 24,75 / 15,75 / 20,25 €/h = `company.md`; notas con capacidad por sprint (TL 2,98 / 2,13 h) | Igual | OK (convención declarada: tope semanal en el libro) |
| Tareas con ID, trabajo y duración | IT-X. Goal, MGT IT-X, US-XXX, TK-001…TK-007, hitos; `Work` = estimación consensuada | Mismas tareas hoja; resúmenes Gestión, Hitos, Historias, EP-001…EP-005, EP-007 | OK |
| Identificadores únicos (UID) | Tareas resumen 1001–1008, hojas e hitos 1–51, proyecto 0: **sin repeticiones** | Resúmenes 1001–1019, hojas e hitos 1–51, proyecto 0: **sin repeticiones**; las tareas hoja tienen el mismo UID en las dos vistas | OK (AUD-v01-001 resuelto) |
| Dependencias aplicadas | 80 enlaces: los 79 de v01 más US-010 (UID 37) → US-023 parte 2 (UID 46), FS | 80 enlaces; US-018 y US-023 con los mismos pares | OK |
| Asignaciones según el esfuerzo | 154 asignaciones = filas del extracto v5 §3 (34 de historias + 120 MGT) | Las mismas 154 (tarea, recurso, unidades, trabajo) | OK |
| Coste | Sin campos `Cost` en tareas ni asignaciones; tarifa × trabajo = 1.996,875 € | Igual | OK (AUD-v01-009 resuelto en el XML) |
| Tareas de gestión MGT | 5 por sprint, 9 h/sprint, 54 h | Agrupadas en «Gestión (Management)», 54 h | OK |
| Hitos | R1 03/11 17:00, R2 17/11 17:00, R3 01/12 17:00 | En «Hitos de release» | OK (D-19) |
| Dos vistas con las mismas tareas, trabajo y coste | Total 100 h (17 + 15 + 20 + 17 + 15 + 16) | Total 100 h (Gestión 54 + Historias 46: EP-001 11, EP-002 6, EP-003 11, EP-004 8, EP-005 8, EP-007 2) | OK |
| `.pod` reimportados | Existen | Existen | NOT_ASSESSABLE (binarios) |

## 6. Viabilidad de la asignación

### 6.1 Capacidad efectiva recalculada (h)
Sin cambios respecto a v01 (mismas ausencias, reuniones, coordinación y márgenes en `capacity.md` y el extracto v5): PO 14,40 · SM 13,50 · TL 14,45 · QA 15,30 → **57,65 h**. Por sprint: 10,175 · 6,775 · 12,725 · 9,325 · 9,325 · 9,325 h. Conciliación: 144 − 36 − 18 − 22 − 10,35 = 57,65 h.

### 6.2 Carga de historias frente a capacidad
Las asignaciones del extracto v5 y de los dos XML son las de v01 (D-27 solo cambia el texto de las partes de US-023 y un enlace, no las horas):

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---|---|---|---|---|---|---|
| PO | 1,5 / 2,40 | 1,5 / 1,60 | 2,5 / 3,20 | 2 / 2,40 | 1 / 2,40 | 2 / 2,40 | 10,5 / 14,40 |
| SM | 1,5 / 2,25 | 1 / 1,35 | 3 / 3,15 | 2 / 2,25 | 1 / 2,25 | 1,5 / 2,25 | 10 / 13,50 |
| TL | 2,5 / 2,975 | 2 / 2,125 | 2,5 / 2,975 | 2 / 2,125 | 2 / 2,125 | 1,5 / 2,125 | 12,5 / 14,45 |
| QA | 2,5 / 2,55 | 1,5 / 1,70 | 3 / 3,40 | 2 / 2,55 | 2 / 2,55 | 2 / 2,55 | 13 / 15,30 |

Sobrecargas: **0**. Trabajo Must sin asignar: **0 h**. Margen de equipo: 2,18 · 0,78 · 1,73 · 1,33 · 3,33 · 2,33 = **11,65 h**.

### 6.3 Horas en ProjectLibre por semana (historias + MGT) frente a 6 h − ausencias
Con `WeekStartDay` = 3, la semana de ProjectLibre coincide con la del sprint (miércoles a martes), así que la tabla por semana es la de v01 §6.3: el máximo es TL 5/6 h (IT-001 e IT-003) y SM 5,5/6 h (IT-003). **Ninguna semana supera la disponibilidad nominal.** El exceso aparente de 6,17 h de la SM en la semana natural 09–15/11 ya no aparece si ProjectLibre aplica el inicio de semana importado (no verificable en el `.pod`).

### 6.4 Coste: libro (extracto v5) / XML / `company.md` / Wiki

| Persona | Horas | Tarifa | Recalculado | Extracto v5 | `company.md` | XML (tarifa × trabajo) | Planificación H4 |
|---|---|---|---|---|---|---|---|
| PO | 22,5 | 19,50 € | 438,75 € | 438,75 € | 438,75 € | 438,75 € | 438,75 € |
| SM | 25 | 24,75 € | 618,75 € | 618,75 € | 618,75 € | 618,75 € | 618,75 € |
| TL | 27,5 | 15,75 € | 433,125 € | 433,13 € | 433,13 € | 433,125 € | 433,13 € |
| QA | 25 | 20,25 € | 506,25 € | 506,25 € | 506,25 € | 506,25 € | 506,25 € |
| Total | **100 h** | | **1.996,875 €** | 1.996,88 € | 1.996,88 € | 1.996,875 € | 1.996,88 € |

Coste por sprint: 337,13 · 296,63 · 403,88 · 341,25 · 297,00 · 321,00 € (coincide con el extracto v5 y con H4). Presupuesto: 1.996,875 + 115,38 + 30,00 + 299,53 = 2.441,79 €; reserva 244,18 € → 2.685,97 €; margen 402,90 € → 3.088,87 €; IVA 648,66 € → **3.737,53 €**. Coincide en todas las fuentes.

Sobre la reserva (D-27): consumir las 11,65 h de margen costaría 239,96 € de personal (PO 3,90 × 19,50 + SM 3,50 × 24,75 + TL 1,95 × 15,75 + QA 2,30 × 20,25). Con el 15 % de gastos generales serían 275,95 €. La reserva es de 244,18 € y además se justifica con RT-01 … RT-07 (pregunta 5).

### 6.5 Viabilidad del tratamiento de RT-04 (recalculado)
Si no hay respuesta el 21/10, RT-04 mueve TK-001 (TL, 1,5 h) y TK-006 (SM, 1,5 h) «al margen de IT-002 o a IT-003»:

| Persona | Horas que se mueven | Margen IT-002 | Margen IT-003 | Margen disponible | Déficit |
|---|---|---|---|---|---|
| TL (TK-001) | 1,50 h | 0,125 h | 0,475 h | 0,60 h | **0,90 h** |
| SM (TK-006) | 1,50 h | 0,35 h | 0,15 h | 0,50 h | **1,00 h** |
| Equipo | 3,00 h | 0,775 h | 1,725 h | 2,50 h | **0,50 h** |

Además, TK-002 (resto), TK-003, TK-004 y TK-007 dependen en el XML de TK-001 o de TK-006 (2,5 h más, aparte de la preparación de TK-002), y US-002 tiene FS desde TK-004 y TK-007.

## 7. Secuencia

### 7.1 Predecesoras del catálogo frente al plan
Sin cambios respecto a v01 §7.1, salvo:

| Historia | Predecesoras (catálogo / ficha) | Enlaces en ProjectLibre | Resultado |
|---|---|---|---|
| US-003 | US-001 (técnica) | TK-006 ← TK-001 y TK-005; TK-007 ← TK-006; TK-005 en paralelo | Refinamiento a nivel de tarea, explicado ahora en Planificación H4 §3 (AUD-v01-005) |
| US-023 parte 1 | Ficha: «solo necesita US-001, US-002 y US-003» | ← planning IT-5, US-002 | Los pasos «consultar y proponer» (US-005/US-006/US-009) quedan cubiertos por la cadena de sprints (US-009 → review/retro IT-4 → planning IT-5), pero la nota de predecesoras no lo refleja (AUD-v01-006) |
| US-023 parte 2 | US-018 (funcional); D-27: también US-010 | ← US-018 parte 2, US-023 parte 1, **US-010** | OK. US-010 termina el 23/11 y la parte 2 empieza el 30/11 |

No hay ninguna tarea que empiece antes de que termine su predecesora FS. Los tipos de enlace son FS (1) o SS (3, solo dailies y coordinación), sin desfases.

### 7.2 Camino crítico, hitos, holgura y reservas
- **Cadena Must:** US-001 → US-003 → US-002 → US-005 → US-006 → US-009 → US-010 → US-018 → US-023 (catálogo §3, H3, H4). En ProjectLibre, US-001 → US-003 es TK-001 → TK-006, como documenta ahora H4.
- **Fin calculado:** 01/12/2026 17:00 = hito R3 = fin de D-19. **Holgura total del proyecto: 0 días.** Los hitos R1 03/11, R2 17/11 y R3 01/12 no cambian.
- **Reservas:** 11,65 h de capacidad sin comprometer, márgenes individuales (10,35 h) y reserva económica del 10 %. Los tratamientos de riesgo reclaman ahora: IT-001 (RT-06), IT-002 (RT-04), IT-003 (RT-04 y RT-06), IT-005 e IT-006 (RT-07). Los márgenes individuales más pequeños siguen siendo QA 0,05 h (IT-001), PO 0,10 h y TL 0,125 h (IT-002) y TL 0,125 h (IT-004 e IT-005).

## 8. Hallazgos

### 8.1 Índice (hallazgos abiertos tras el RECHECK)

| ID | Categoría | Severidad | Bloqueante | Estado | Resumen |
|---|---|---|---|---|---|
| AUD-v01-002 | Riesgos / Viabilidad | MAJOR | NO | PARTIALLY_RESOLVED | La contingencia corregida de RT-04 mueve 3 h a márgenes que suman 2,50 h (TL 0,60 h, SM 0,50 h) |
| AUD-v01-005 | Secuencia / Documentación | MINOR | NO | PARTIALLY_RESOLVED | Refinamiento documentado en H4 §3, pero la frase quedó mal montada |
| AUD-v01-006 | Secuencia / Documentación | MINOR | NO | PARTIALLY_RESOLVED | «Aceptar» pasa a la parte 2 y hay enlace con US-010, pero la nota de predecesoras de US-023 no se actualizó |
| AUD-v02-001 | Riesgos / Reservas | MINOR | NO | Nuevo | RT-04, RT-06 y RT-07 reclaman los mismos márgenes sin prioridad ni cuantía |
| AUD-v02-002 | Trazabilidad | MINOR | NO | Nuevo | Registros sin sincronizar tras D-27 (acta, fechas, versión del Excel, R-13, cabecera de EP-007) |

Los hallazgos AUD-v01-001, 003, 004, 007, 008, 009, 010 y 011 están RESOLVED (ver §10).

### 8.2 Registros detallados

#### AUD-v01-002 · La contingencia de RT-04 sigue sin caber en la capacidad (PARTIALLY_RESOLVED)
- **Categoría:** Riesgos / Viabilidad · **Severidad:** MAJOR · **Bloqueante:** NO
- **Decisión humana:** R-32, aceptada con cambios (D-27): «sin tecnología confirmada, IT-001 solo hace TK-005 y la preparación de TK-002; TK-001 y TK-006 pasan a IT-002/IT-003 y se replanifican».
- **Evidencia:**
  - Lo corregido: `technical-risks.md`, RT-04 dice «El margen individual del TL en IT-001 es de 0,48 h, así que el retrabajo no puede absorberlo solo él». TK-006 ya no se presenta como independiente del stack y se mueve con TK-001, lo que coincide con el XML (TK-006, UID 7, `PredecessorUID` 4 y 5).
  - Lo pendiente: RT-04 dice «TK-001 y TK-006 pasan al margen de IT-002 o a IT-003, que es el sprint con más hueco (1,73 h), y el PO y la SM replanifican US-002 y US-005 en la planning de IT-002». Extracto v5 §1 y §3: TK-001 = TL 1,5 h; TK-006 = SM 1,5 h. Extracto v5 §4: márgenes TL 0,13 h (IT-002) y 0,48 h (IT-003); SM 0,35 h y 0,15 h; equipo 0,78 h y 1,73 h. Recalculado en §6.5: déficit de 0,90 h (TL), 1,00 h (SM) y 0,50 h a nivel de equipo.
  - IT-003 no es el sprint con más hueco del plan: IT-005 tiene 3,33 h, IT-006 2,33 h e IT-001 2,18 h. Solo lo es entre IT-002 e IT-003.
  - En el XML, TK-002 (UID 6) depende de TK-001; TK-003 y TK-004 dependen de TK-002; TK-007 de TK-006; y US-002 (UID 16) depende de TK-004 y TK-007. La contingencia arrastra estas tareas (2,5 h más, aparte de la preparación de TK-002).
- **Impacto:** con la regla «No se puede sobreasignar tareas», la contingencia solo funciona si se reasigna trabajo a PO o QA (con las competencias necesarias) o si se retrasa alguna historia. RT-04 lo admite de forma genérica («se replanifican»), pero no dice qué se recorta ni quién hace el trabajo, y presenta como suficiente un margen que no lo es.
- **Acción recomendada (opciones, a decidir por el equipo):** (a) indicar en RT-04 qué personas absorberían las horas de TK-001/TK-006 en IT-002/IT-003 y con qué margen individual, o qué tarea o historia se aplaza; (b) corregir «el sprint con más hueco» o aclarar que se refiere a IT-002/IT-003; (c) valorar si alguna parte de la contingencia debe usar el margen de IT-005, teniendo en cuenta que RT-07 lo reserva (ver AUD-v02-001).
- **Confianza:** HIGH (cifras y enlaces leídos directamente).
- **Rol sugerido:** TL (RT-04), con la SM y el PO para la replanificación.

#### AUD-v01-005 · Refinamiento US-001 → US-003 documentado con una frase corrupta (PARTIALLY_RESOLVED)
- **Categoría:** Secuencia / Documentación · **Severidad:** MINOR · **Bloqueante:** NO
- **Decisión humana:** R-35, aceptada con cambios: «Es intencionado: TK-005 (diseño del cuadrante) no necesita el entorno. Se aclara en Planificación H4».
- **Evidencia:** Planificación H4 §3, fila «Dependencias»: «Fin a comienzo entre historias según el catálogo. En IT-1 la dependencia US-001 → US-003 se modela entre tareas (TK-001 → TK-006), porque el diseño del cuadrante (TK-005) no necesita el entorno y puede hacerse en paralelo (por ejemplo US-006 → US-009 → US-010 → US-018 → US-023) y dentro de cada sprint: planning → historias → …». El ejemplo de la cadena entre historias quedó dentro de la explicación de TK-005, y la frase no se entiende. La intención y los enlaces del XML (TK-006 ← TK-001, TK-005) coinciden.
- **Impacto:** bajo. La explicación existe, pero un evaluador puede leer que la cadena US-006 → … → US-023 corre en paralelo.
- **Acción recomendada:** volver a redactar la fila. Por ejemplo: «Fin a comienzo entre historias según el catálogo (por ejemplo US-006 → US-009 → …) y dentro de cada sprint … En IT-1, US-001 → US-003 se modela entre tareas (TK-001 → TK-006) porque TK-005 no necesita el entorno».
- **Confianza:** HIGH.
- **Rol sugerido:** SM.

#### AUD-v01-006 · Nota de predecesoras de US-023 sin actualizar (PARTIALLY_RESOLVED)
- **Categoría:** Secuencia / Documentación · **Severidad:** MINOR · **Bloqueante:** NO
- **Decisión humana:** R-36, aceptada con cambios: «"Aceptar" pasa a la parte 2, que además depende de US-010».
- **Evidencia:**
  - Aplicado: EP-007, «Plan inicial»: parte 1 «consultar y proponer», parte 2 «aceptar y resolver», con la nota de AUD-v01-006/D-27. Extracto v5 §3 y nombres de UID 39/46 en los dos XML. Enlace FS UID 37 (US-010) → UID 46 en los dos XML.
  - Pendiente: EP-007, «Predecesoras»: «la parte 1 (guion de instalación) solo necesita US-001, US-002 y US-003 (D-24)». La parte 1 documenta también «consultar y proponer» (US-005, US-006 y US-009), y la parte 2 depende ahora también de US-010, pero la línea de predecesoras no lo menciona. El catálogo (fila de US-023) mantiene el mismo texto. En v01 ya se recomendó «Actualizar la nota de predecesoras de US-023 para que refleje R-30».
- **Impacto:** bajo. El plan es correcto (la cadena de sprints garantiza el orden), pero la ficha y el catálogo declaran menos predecesoras de las que el plan aplica.
- **Acción recomendada:** actualizar la línea «Predecesoras» de EP-007 y la fila del catálogo: parte 1 tras US-009 (por la cadena de sprints) y parte 2 tras US-018 y US-010.
- **Confianza:** HIGH.
- **Rol sugerido:** PO (ficha y catálogo), con QA.

#### AUD-v02-001 · Varios riesgos reclaman los mismos márgenes
- **Categoría:** Riesgos / Reservas · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:**
  - RT-04: TK-001 y TK-006 «pasan al margen de IT-002 o a IT-003».
  - RT-06: «Adelantar trabajo con el margen de IT-001 (2,18 h) si sobra; … terminar lo pendiente con el margen de IT-003 (1,73 h) antes de empezar US-006».
  - RT-07: «se reserva el margen de IT-005 (3,33 h) e IT-006 (2,33 h)». Planificación H4 §5: «IT-5 tiene 3,33 h y se reserva para el riesgo de US-018».
  - D-27: «La reserva del 10 % cubre el uso del margen de capacidad (11,65 h ≈ 240 € de personal)». `company.md`: la misma reserva (244,18 €) se justifica con «RT-01 a RT-07».
  - Márgenes individuales de IT-003 (extracto v5 §4): PO 0,70 · SM 0,15 · TL 0,48 · QA 0,40 h. En IT-001: QA 0,05 h.
- **Impacto:** si RT-04 y RT-06 se materializan a la vez (los dos afectan al arranque: RT-04 en IT-001 y RT-06 en IT-002), el margen de IT-003 (1,73 h) se cuenta dos veces. En ese caso no cubre ni RT-04 sola (§6.5). Además, el margen de IT-001 que RT-06 quiere usar es el que queda libre si RT-04 bloquea TK-001, pero solo para quien no dependa de la tecnología. Sin un orden de prioridad, el equipo descubriría el conflicto durante la ejecución.
- **Acción recomendada:** indicar en el registro (o en Planificación H4 §5) qué margen asigna a cada riesgo y qué riesgo tiene prioridad si coinciden. Comprobar que la suma de lo reclamado en cada sprint no supera su margen, persona a persona.
- **Confianza:** MEDIUM (depende de que los riesgos coincidan; las cifras son exactas).
- **Rol sugerido:** TL (registro de riesgos), con la SM (plan).

#### AUD-v02-002 · Registros sin sincronizar tras D-27
- **Categoría:** Trazabilidad · **Severidad:** MINOR · **Bloqueante:** NO
- **Evidencia:**
  1. Acta del 15/10/2026: «- [ ] SM: reimportar los XML en ProjectLibre y guardar los `.pod` · 15/10» sigue sin marcar. En cambio, R-31 dice «XML regenerados … y `.pod` reimportados», D-27 «regenerados … y reimportados» y Planificación H4 §6 «XML regenerados y reimportados».
  2. Uso de agentes: «Ejecución AG-02 · auditoría INITIAL · 15/10/2026». El informe v01 registra como fecha de ejecución el 14/10/2026 (fecha del entorno).
  3. `company.md`, «Coste directo de personal»: «`TurnoLibre_H3_planificacion.xlsx`, versión 4». El libro vigente es la versión 5 (Planificación H4, extracto v5); las horas y el coste no cambian.
  4. Uso de agentes, R-13 (evaluador externo): «Pendiente de aplicar: Lucansado (PO) y Juliannietoo (QA)». La parte «registrar» ya está aplicada como RT-05 (mismo patrón que R-12 en AUD-v01-010). La identificación (antes del 18/11) sigue pendiente.
  5. EP-007, cabecera: «revisión 14/10/2026 (D-18/D-21/D-22/D-23/D-24 …)», aunque el «Plan inicial» de US-023 se cambió el 15/10 por D-27. El historial del catálogo (§7) no tiene ninguna entrada de D-27.
- **Impacto:** bajo, pero afecta al objetivo del enunciado de «conservar trazabilidad de las decisiones». En concreto, el punto 1 deja sin constancia en el acta la reimportación de los `.pod`, que esta auditoría no puede verificar.
- **Acción recomendada:** marcar o fechar la acción del acta cuando se compruebe la reimportación; unificar la fecha de la ejecución AG-02 INITIAL; citar la versión 5 en `company.md`; actualizar la columna «Cambio / referencia» de R-13 (RT-05 registrado; identificación pendiente hasta el 18/11); actualizar la cabecera de EP-007 y añadir D-27 al historial del catálogo.
- **Confianza:** HIGH (lectura directa).
- **Rol sugerido:** SM, con el PO para EP-007 y el catálogo.

## 9. Preguntas para el equipo

1. **(AUD-v01-002)** Si el 21/10 no hay respuesta sobre la tecnología, ¿quién hace TK-001 (1,5 h) y TK-006 (1,5 h) en IT-002/IT-003, si el TL solo tiene 0,60 h y la SM 0,50 h de margen en esos dos sprints y el equipo 2,50 h? ¿Qué historia o tarea se aplazaría?
2. **(AUD-v02-001)** Si RT-04 y RT-06 se materializan juntos, ¿cuál tiene prioridad sobre el margen de IT-003 (1,73 h)?
3. **(AUD-v02-002)** Al abrir los `.pod` reimportados, ¿se ve la jerarquía completa en las dos vistas, 100 h, 1.996,88 € y la semana empezando en miércoles? ¿Se marcará la acción del acta del 15/10?
4. **(RT-07)** Si a mitad de IT-006 US-018 no está terminada y «se valida el guion con lo disponible», ¿se considera cerrada US-023, cuando US-023-AC-02 exige el paso «resolver» y M04 la evaluación de la versión final?
5. **(Coste, D-27)** La reserva de 244,18 € cubre el personal de las 11,65 h de margen (239,96 €), pero no sus gastos generales (275,95 € en total), y además se justifica con RT-01 … RT-07. ¿Se acepta conscientemente que la reserva no cubre las dos cosas a la vez?
6. **(AUD-v01-006)** ¿Se actualizará la línea «Predecesoras» de US-023 en EP-007 y en el catálogo para incluir US-009 (parte 1) y US-010 (parte 2)?

## 10. Correspondencia RECHECK

| ID v01 | Severidad v01 | Decisión humana | Evidencia actual | Estado |
|---|---|---|---|---|
| AUD-v01-001 | MAJOR | R-31 Aceptada (D-27): XML con UID únicos y `.pod` reimportados | Los dos XML tienen UID de tarea únicos (resúmenes 1001–1008 / 1001–1019, hojas 1–51); hojas con el mismo UID en las dos vistas. Lo que muestran los `.pod` no es verificable | **RESOLVED** (en el XML; los `.pod` son NOT_ASSESSABLE) |
| AUD-v01-002 | MAJOR | R-32 Aceptada con cambios (D-27): RT-04 reescrito | Margen del TL (0,48 h) citado bien y TK-006 coherente con el XML; la contingencia mueve 3 h a márgenes de 2,50 h (TL 0,60, SM 0,50) y llama a IT-003 «el sprint con más hueco» | **PARTIALLY_RESOLVED** |
| AUD-v01-003 | MAJOR | R-33 Aceptada (D-27): RT-05 … RT-07 | RT-05, RT-06 y RT-07 con situación, evento, consecuencia, tratamiento, probabilidad, impacto, responsable y estado; reserva justificada con RT-01 … RT-07 | **RESOLVED** |
| AUD-v01-004 | MINOR | R-34 Aceptada (D-27): columnas nuevas | Tabla con columnas de probabilidad, impacto, responsable y estado en los siete riesgos | **RESOLVED** |
| AUD-v01-005 | MINOR | R-35 Aceptada con cambios: intencionado, se aclara en H4 | Explicación presente en H4 §3, pero la frase está corrupta | **PARTIALLY_RESOLVED** |
| AUD-v01-006 | MINOR | R-36 Aceptada con cambios: «aceptar» a la parte 2, con dependencia de US-010 | Aplicado en EP-007 (plan inicial), extracto v5 y los dos XML (enlace 37 → 46); la línea «Predecesoras» de EP-007 y el catálogo no se actualizaron | **PARTIALLY_RESOLVED** |
| AUD-v01-007 | MINOR | R-37 Aceptada: semana de miércoles a martes | `<WeekStartDay>3</WeekStartDay>` en los dos XML; H4 §3 lo documenta; ninguna semana supera la capacidad. Efecto en los `.pod` no verificable | **RESOLVED** |
| AUD-v01-008 | MINOR | R-38 Aceptada: 2,13 h | Notas del TL en los dos XML: «IT-002: 2,13 h, … IT-006: 2,13 h» | **RESOLVED** |
| AUD-v01-009 | MINOR | R-39 Aceptada: sin coste por asignación | No hay ningún `<Cost>` en los XML; tarifa × trabajo = 1.996,875 € = 1.996,88 € | **RESOLVED** |
| AUD-v01-010 | MINOR | R-40 Aceptada: R-12 aplicada | R-12: «Aplicada: RT-04 en technical-risks.md (14/10) y corregido el 15/10 (R-32)». La pregunta del 21/10 sigue visible como pendiente en el acta del 14/10 y en RT-04 (Abierto) | **RESOLVED** (el mismo patrón aparece en R-13: AUD-v02-002) |
| AUD-v01-011 | QUESTION | R-41 Aceptada: D-26 fechada el 14/10/2026 | D-26 «14/10/2026» en el Registro, `company.md`, el extracto v5 y la cabecera del contrato del auditor | **RESOLVED** (la fecha de la ejecución v01 en la Wiki difiere del informe: AUD-v02-002) |

Respuestas de D-27 a las preguntas de v01 sin hallazgo propio: festivos (pregunta 6: «sin festivos entre el 21/10 y el 01/12; el lunes 2/11 no es festivo», decisión del equipo y no verificada por el auditor) y reserva (pregunta 5: decisión registrada en D-27, con la matización de la pregunta 5 de este informe).

## 11. Cierre

Esta es una auditoría consultiva. No se ha modificado ninguna fuente, plan, estimación ni decisión humana. No se ha aprobado ninguna línea base ni puerta de calidad.

*This is an advisory audit. No source, plan, estimate or human decision was changed. No baseline or gate was approved.*
