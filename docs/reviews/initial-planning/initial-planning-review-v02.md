# Initial planning review v02

## 1. Metadatos de ejecución

- Proyecto: TurnoLibre (empresa ficticia MedSwap; cliente ficticio Hospital Comarcal Vega Alta).
- Agente: AG-03, Planning Agent (*initial-planning-reviewer*). Contrato: `.github/agents/initial-planning-reviewer.agent.md` (adaptación D-20, 07/10/2026), leído íntegramente antes de la revisión.
- Modo: **RECHECK** del informe `docs/reviews/initial-planning/initial-planning-review-v01.md` (commit revisado 45d6b38), aplicado a la hipótesis de planificación humana vigente con alcance **CONSISTENCY**.
- Commit revisado: **b9c5e27** (rama `main`, repositorio `C:\GPS_GC02`, árbol de trabajo limpio según el equipo). Se consideran los ficheros en disco como ese commit.
- Wiki: clon local `C:\GPS_GC02_wiki`, commit **76f5f57** (dato aportado por el equipo). Páginas leídas: `Registro-de-decisiones.md` (D-24 en particular), `Uso-de-agentes.md` (R-10 a R-23), `Actas.md` (acta del 14/10/2026) y `Planificacion-H3.md`.
- Libro de planificación: `docs/planning/TurnoLibre_H3_planificacion.xlsx` (versión 2). La herramienta no puede leer .xlsx. **Se ha revisado el extracto** `docs/planning/extracts/TurnoLibre_H3_extracto-v2.md` (versión 2, 14/10/2026). El extracto v1 se conserva como entrada del informe v01. No se ha podido comprobar que el extracto coincida con el libro ni revisar sus fórmulas.
- Alcance revisado: las 11 historias Must tras D-18 (US-001, 002, 003, 005, 006, 009, 010, 012, 014, 018 y 023; 46 h-p), IT-001 a IT-006 (21/10/2026–01/12/2026, 3 releases; D-19), 4 personas a 6 h/semana (D-21). Should, Could y Won't sin compromiso.
- Fuentes: `specs/product/goals.md`; `specs/product/catalogo.md` (requisitos-v1-revisado, incluida la fila de historial «plan H3» del 14/10/2026 y el §4); fichas EP-001 a EP-007 (incluido «Plan inicial»); `docs/organization/capacity.md`; `docs/organization/team-charter.md`; `docs/organization/company.md`; `docs/risks/technical-risks.md`; DoR v1.0; DoD v1.1; constitución v1.1; `docs/reviews/requirements/requirements-report-v01.md` y `-v02.md`.
- Decisiones humanas de referencia: D-24 y R-10 a R-23 (aceptación de IPR-v01-001 a IPR-v01-014, correspondencia uno a uno); acta del 14/10/2026.
- Versión del informe: v02 (siguiente número libre; v01 se conserva sin cambios).
- Fecha: 14/10/2026.
- Herramienta: Claude Code (subagente initial-planning-reviewer). Modelo: claude-opus-5-5.
- Idioma: español (es-ES); IDs, estados y severidades como en el contrato.

## 2. Resumen

**Resultado consultivo: READY_WITH_NON_BLOCKING_QUESTIONS.**
**Hallazgos bloqueantes: 0.**

Disposición de los 14 hallazgos de v01: **8 RESOLVED** (002, 005, 006, 008, 009, 010, 011, 014), **4 PARTIALLY_RESOLVED** (001, 007, 012, 013) y **2 DEFERRED** (003, 004). Hay **3 hallazgos nuevos MINOR, no bloqueantes** (IPR-v02-001 a 003).

Conclusión principal: el extracto v2 sigue siendo aritméticamente coherente con las fuentes. La capacidad (57,65 h) no cambia, las 46 h-p Must están asignadas, ninguna persona supera su capacidad en ninguna iteración y el coste planificado baja a 916,50 € dentro del mismo personal presupuestado (2.889,00 €) y del mismo precio (5.307,88 € con IVA). Varias decisiones de D-24 tienen evidencia en las fuentes: la excepción explícita a «cabe en un sprint», la sesión de los miércoles en el Team Charter y en `capacity.md`, el redondeo unificado, el traslado de US-005-AC-03 a US-009-AC-09, el cambio de TK-007 y la redistribución de IT-006. Las dos dependencias externas siguen sin confirmar: el equipo las ha aplazado con responsable y fecha. La de tecnologías tiene fecha el mismo día en que empieza IT-001 y no hay alternativa prevista si no llega. También quedan restos de menor alcance: la regla de dependencias del libro, textos del plan provisional en el catálogo §6 y en `capacity.md`, el contrato del formato de solicitud y las consecuencias del traslado de un criterio de aceptación.

Aceptar una propuesta no se toma como prueba de corrección: el estado de cada hallazgo se basa en la evidencia actual. Este resultado indica que las entradas permiten revisar y usar la hipótesis. **No aprueba el plan ni demuestra que el calendario sea viable**, aunque la página Wiki Planificación H3 §7 lo califique de viable.

## 3. Inventario de evidencias y matriz de compatibilidad

| Dimensión | Estado | Evidencia | Límite |
|---|---|---|---|
| Alcance y prioridades | COMPATIBLE | Extracto v2 §2 frente al catálogo §2 y a la tabla D-18: 11 Must = 46 h-p. MoSCoW, incertidumbre y h-p coinciden en las 24 filas. | La regla de cambio de alcance no se aplica: D-24 declara que no hay cambios de alcance. El traslado de un criterio de aceptación entre historias se trata en IPR-v02-001. |
| Madurez de requisitos / DoR | PARCIAL | Excepción explícita a «cabe en un sprint» para US-018/US-023 (D-24; constitución, Governance: «Las excepciones son explícitas, justificadas, aprobadas y, si es posible, temporales»). TK-007 alineada con US-003-AC-02. Tareas del PO renombradas. | La DoR C15 (dependencias que no bloquean) sigue sin cumplirse para US-001 (tecnologías) ni para US-023 (evaluador). El contrato del formato de solicitud sigue sin evidencia. Ninguna historia se declara Ready. |
| Cobertura y unidades de las estimaciones | COMPATIBLE | La suma de horas por historia coincide con las h-p (§5.2). Las estimaciones están en h-p y la capacidad en h por persona e iteración. | US-009 recibe un criterio de aceptación nuevo sin evidencia de que se haya revisado su estimación (IPR-v02-001). IT-002 a IT-006 se reparten por historia. |
| Capacidad efectiva | COMPATIBLE | Recalculada: 57,65 h. El Team Charter (acuerdo 4) y `capacity.md` coinciden ahora: 1 h de ceremonias, más la otra hora de trabajo del proyecto (D-24). El redondeo de presentación es igual en el extracto v2 y en `capacity.md`. | Las fórmulas del libro no son legibles (NOT_ASSESSABLE). |
| Horizonte y duración | COMPATIBLE | Del 21/10/2026 (miércoles) al 01/12/2026 (martes), 6 iteraciones y 3 releases. | La cadena crítica Must sigue ocupando las 6 iteraciones, sin ninguna iteración de holgura. |
| Dependencias y capacidades | PARCIAL | La dependencia US-023 → US-018 se limita a la parte 2 (catálogo §2, EP-007). US-009 añade US-005 como predecesora (catálogo y EP-003). | La regla del libro no ha cambiado. La columna de predecesoras de US-023 no distingue partes. La secuencia dentro del sprint no es visible. Falta la arista US-005 → US-009 en el diagrama del catálogo §3. El criterio de reparto declarado choca con algunas asignaciones (IPR-v01-001, 012; IPR-v02-001). |
| Coste | COMPATIBLE | Recalculado: 916,50 € de horas asignadas. Presupuesto y precio sin cambios (§7). | — |
| Supuestos e incertidumbre | PARCIAL | La caducidad cabe en 8/3/8 h-p según la confirmación del TL del 14/10, registrada en el acta y en Uso de agentes. | Tecnologías autorizadas: aplazado al 21/10. Evaluador externo: aplazado al 18/11. El riesgo de tecnologías todavía no está en `technical-risks.md`. |
| Planificación y viabilidad | COMPATIBLE A NIVEL AGREGADO | 0 sobreasignaciones. Holgura del equipo: 11,65 h. Holgura mínima individual: QA, 0,05 h en IT-001. | La viabilidad de la secuencia dentro de cada semana y de las tareas aún sin detallar queda para el equipo. |
| Fórmulas del libro .xlsx | NOT_ASSESSABLE | Solo se ha leído el extracto v2. | Hace falta una revisión humana del libro o un extracto de sus fórmulas. |

## 4. Hallazgos

Los restos de los hallazgos de v01 se siguen con su ID original en el apartado 9; no se renumeran. A continuación solo figuran los hallazgos nuevos.

### IPR-v02-001 · Versiones y estimación tras el traslado de un criterio · MINOR · Bloqueante: NO

- **Fuente/ID:** EP-002 (US-005-AC-03 tachado), EP-003 (US-009-AC-09 y predecesora US-005); catálogo §2, §3 (diagrama) y §7 (fila «plan H3», «Sin cambios de alcance, prioridad ni estimación»); cabeceras del catálogo y de las fichas («revisión 13/10/2026»); Uso de agentes R-19 y R-22; requisitos v02 (revisó dda3ce4); constitución, Governance («registrar fecha y nueva versión»); extracto v2 §4 (IT-004).
- **Evidencia observada:** el 14/10 se ha cambiado el contenido de dos fichas: un criterio pasa de US-005 a US-009 y US-009 gana una predecesora. El cambio es posterior al RECHECK de requisitos v02. Las cabeceras del catálogo y de las fichas EP-002 y EP-003 siguen indicando «revisión 13/10/2026», aunque el historial del catálogo sí registra el cambio del 14/10. US-009 mantiene 8 h-p y US-005, 3 h-p. La confirmación del TL de R-22 se refiere a US-009-AC-08 (caducidad), no a AC-09. En IT-004 las holguras son pequeñas: TL 0,125 h y SM 0,25 h. El diagrama del catálogo §3 no muestra la nueva arista US-005 → US-009.
- **Impacto:** el traslado reduce el trabajo de US-005 y aumenta el de US-009 sin ningún registro de que se hayan revisado las estimaciones. Si AC-09 necesita más trabajo del previsto, la presión cae en IT-004, la semana con menos holgura individual del TL. La marca de revisión no permite distinguir el contenido revisado por AG-01 en v02 del cambiado el 14/10.
- **Acción recomendada:** registrar si el equipo confirma que AC-09 cabe en las 8 h-p de US-009 (y si US-005 se mantiene en 3 h-p), actualizar la marca de revisión de las cabeceras afectadas y añadir la arista al diagrama. El equipo decide si el cambio necesita otra revisión de requisitos.
- **Pregunta o decisión:** ¿Se ha comprobado que US-009-AC-09 cabe en la estimación de US-009? ¿Qué identificador o fecha de revisión tienen ahora EP-002, EP-003 y el catálogo?
- **Rol propuesto:** PO (fichas y alcance) y TL (estimación); SM para el versionado.

### IPR-v02-002 · Versiones de fuentes (`capacity.md`) · MINOR · Bloqueante: NO

- **Fuente/ID:** `docs/organization/capacity.md`, apartado «Uso en la planificación»; extracto v2 §4; catálogo §4 (plan del H3).
- **Evidencia observada:** `capacity.md` sigue diciendo «Con el reparto actual, IT-002 tiene 9 h-p frente a 6,775 h disponibles e IT-006 tiene 10 h-p frente a 9,325 h. SM/TL deben redistribuir la carga». En el plan vigente, IT-002 tiene 6 h e IT-006, 7 h, y no hay sobrecargas.
- **Impacto:** quien lea `capacity.md` encontrará un plan anterior que ya se ha sustituido. Es la misma clase de desfase que IPR-v01-007, ahora en otra fuente.
- **Acción recomendada:** marcar ese párrafo como histórico (D-21) o remitir al plan del H3 (D-24).
- **Pregunta o decisión:** ninguna de alcance.
- **Rol propuesto:** SM.

### IPR-v02-003 · Cobertura de US-023-AC-02 entre las dos partes · MINOR · Bloqueante: NO

- **Fuente/ID:** EP-007 US-023-AC-02/AC-03 y «Plan inicial»; extracto v2 §3 (parte 1: «guion de instalación con las cuentas de prueba», QA, IT-005, 1,5 h; parte 2: «paso de aprobación y validación con el evaluador externo (coordina el PO)», PO, IT-006, 0,5 h); `capacity.md` (entrega de la práctica 4 de GPS el 27/11).
- **Evidencia observada:** AC-02 exige que el guion incluya preparación del entorno, restablecimiento de datos, cuentas por rol y los pasos del flujo «consultar turnos, proponer, aceptar y resolver solicitudes». Las descripciones de las dos partes solo mencionan de forma explícita la instalación con las cuentas y el paso de aprobación. Los pasos de consultar, proponer y aceptar no aparecen en ninguna. En IT-006, 0,5 h deben cubrir el paso de aprobación y la coordinación de la evaluación externa (AC-03). Esa evaluación solo puede hacerse después de cerrar US-018 en la misma semana.
- **Impacto:** puede quedar sin responsable una parte de AC-02. La parte 2 concentra en la última semana una tarea dependiente de US-018 y de una persona externa con muy pocas horas.
- **Acción recomendada:** al detallar IT-005 e IT-006 por tareas, indicar qué parte cubre cada paso de AC-02 y si 0,5 h bastan para la parte 2. El agente no propone nuevas horas.
- **Pregunta o decisión:** ¿En qué parte de US-023 se documentan los pasos de consultar, proponer y aceptar?
- **Rol propuesto:** PO y QA.

## 5. Observaciones aritméticas y de capacidad

**Unidades:** estimaciones en h-p; capacidad en h por persona e iteración; coste en €. Fórmula: `efectiva = max(0, nominal − ausencias − reuniones − coordinación) × (1 − margen)`, con nominal 6 h y reuniones 1,5 h por semana (1 h de ceremonias + 0,5 h de dailies; D-24 no cambia el descuento).

### 5.1 Capacidad (h, sin redondear)

Sin cambios respecto a v01 §5.1. PO 14,40 · SM 13,50 · TL 14,45 · QA 15,30. Equipo por iteración: 10,175 · 6,775 · 12,725 · 9,325 · 9,325 · 9,325 = **57,65 h**. Conciliación: 144 − 36 − 18 − 22 − 10,35 = 57,65 h. El extracto v2 y `capacity.md` presentan ahora las mismas cifras redondeadas (2,98 / 2,13 / 10,18 / 6,78 / 12,73 / 9,33).

### 5.2 Carga asignada (h), recalculada desde el extracto v2 §3

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total | Holgura total | ¿Supera la capacidad? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PO | 1,50 | 1,50 | 2,50 | 2,00 | 1,50 | 2,00 | 11,00 | 3,40 | No |
| SM | 1,50 | 1,00 | 3,00 | 2,00 | 1,50 | 1,50 | 10,50 | 3,00 | No |
| TL | 2,50 | 2,00 | 2,50 | 2,00 | 1,50 | 1,50 | 12,00 | 2,45 | No |
| QA | 2,50 | 1,50 | 3,00 | 2,00 | 1,50 | 2,00 | 12,50 | 2,80 | No |
| **Equipo** | 8,00 | 6,00 | 11,00 | 8,00 | 6,00 | 7,00 | **46,00** | **11,65** | No |

- Horas por historia, iguales a las h-p tras D-18: US-001 = 5; US-003 = 1,0 + 1,5 + 0,5 = 3; US-002 = 2 + 1 = 3; US-005 = 1,5 + 1 + 0,5 = 3; US-006 = 2 + 1 = 3; US-012 = 2,5 + 2,5 = 5; US-014 = 2 + 0,5 + 0,5 = 3; US-009 = 4 × 2 = 8; US-010 = 1,5 + 1,5 = 3; US-018 = 1,5 + 1,5 + 2 + 1,5 + 1,5 = 8; US-023 = 1,5 + 0,5 = 2. **Total: 46 h-p.**
- Holguras individuales exactas (h): PO 0,90 · 0,10 · 0,70 · 0,40 · 0,90 · 0,40; SM 0,75 · 0,35 · 0,15 · 0,25 · 0,75 · 0,75; TL 0,475 · 0,125 · 0,475 · 0,125 · 0,625 · 0,625; QA 0,05 · 0,20 · 0,40 · 0,55 · 1,05 · 0,55. Coinciden con el extracto v2 §4, redondeadas a la mitad hacia arriba.
- Cambios respecto a v01, todos en IT-006: SM 2,0 → 1,5; TL 0,5 → 1,5; QA 2,5 → 2,0; PO 2,0 → 2,0 (1,5 de US-018 + 0,5 de US-023). La holgura de QA en IT-006 pasa de 0,05 a 0,55 h; la del TL, de 1,625 a 0,625 h.
- Se cumple «No se puede sobreasignar tareas» en las 24 combinaciones de persona e iteración.
- **Exclusiones:** Should, Could, Won't y US-017 (fusionada).
- **Desconocidos:** el reparto por tareas de IT-002 a IT-006, la secuencia dentro de cada semana, las capacidades técnicas de cada persona y la cobertura de la DoD dentro de cada estimación. Esto último queda para el detalle de cada iteración, según R-21.
- **Límite del control agregado:** que no haya sobreasignación no demuestra que el orden dentro de cada semana sea viable ni que las estimaciones sean adecuadas.

## 6. Observaciones de dependencias y capacidades

- **Tipos (catálogo §2 y §3):** sin cambios respecto a v01, salvo la nueva dependencia funcional US-005 → US-009 (EP-003, catálogo §2). En el plan se cumple (IT-002 → IT-004), pero no figura en el diagrama del §3 (IPR-v02-001). No se observan ciclos.
- **US-023 → US-018:** el equipo limita la dependencia a la parte 2. La parte 1 necesita US-001 a US-003, ya terminadas en IT-001 e IT-002 (catálogo §2, EP-007). La columna «Predecesoras del plan» del extracto sigue indicando solo «US-018» y la regla del libro no ha cambiado. Por eso el «0 incumplimientos» del libro no comprueba la nueva lectura por partes (IPR-v01-001).
- **Dependencias dentro de la misma iteración, sin secuencia visible:** US-002 → US-005 (IT-002, holgura del equipo 0,775 h, semana con cuatro exámenes o entregas), US-012 → US-014 (IT-003) y US-010 → US-018 diseño (IT-005; el diseño no exige que US-010 esté terminada, según la nota de D-24). En IT-006, la parte 2 de US-023 depende del cierre de US-018 en la misma semana y de una persona externa.
- **Externas sin resolver:** tecnologías autorizadas (aplazado al 21/10, TL) y evaluador externo (aplazado al 18/11, PO y QA). El contrato del formato de solicitud entre los validadores (IT-003) y US-009 (IT-004) sigue sin evidencia ni tarea.
- **Capacidades:** la Wiki Planificación H3 §4 declara un criterio de reparto: el TL lleva la arquitectura y la lógica de reglas; QA, el entorno, la integración continua y las pruebas; el PO, los datos y la aceptación; la SM, las pantallas y los scripts. Algunas asignaciones no siguen ese criterio: la SM tiene «Validación RN-03 en el módulo de reglas» (US-014, 2 h) y el PO, «Consulta de turnos compatibles y lista vacía» (US-006, 2 h). US-010 no tiene horas del TL ni de QA para la lógica de servidor de AC-02, AC-04 y AC-05. Se trata en IPR-v01-012. Ninguna fuente documenta las capacidades técnicas individuales.
- **Cadena crítica:** sin cambios; ocupa las seis iteraciones.
- No se ha generado ningún calendario ni secuencia alternativa.

## 7. Resultado de coste

- **Tarifas** (`company.md`): PO 19,50 €/h, SM 24,75 €/h, TL 15,75 €/h, QA 20,25 €/h.
- **Coste de las horas asignadas (recalculado):** PO 11 × 19,50 = 214,50 €; SM 10,5 × 24,75 = 259,875 €; TL 12 × 15,75 = 189,00 €; QA 12,5 × 20,25 = 253,125 €. **Total: 916,50 €**, igual que el extracto v2 §5. Por iteración: 156,375 · 115,875 · 223,125 · 160,50 · 120,375 · 140,25 €, que suman 916,50 €. La diferencia con v01 es de −6,75 € y procede solo de la redistribución de IT-006: −12,375 (SM) + 15,75 (TL) − 10,125 (QA).
- **Presupuesto** (D-21; sin cambios y recalculado en v01): personal 2.889,00 € (144 h nominales); **precio 5.307,88 € con IVA**. Coincide con `company.md` y con el extracto v2.
- **Supuestos:** se paga la jornada nominal completa. El coste de las horas asignadas es una parte del personal presupuestado, no un coste adicional. D-24 no cambia las horas nominales y, por tanto, tampoco el presupuesto.
- **Desconocidos:** ninguno nuevo. La revisión del presupuesto sigue prevista en H4.

## 8. Preguntas y acciones sugeridas

| # | Pregunta o acción | Rol propuesto | Momento de validación | Bloqueante |
|---|---|---|---|---|
| 1 | Decidir **antes** de la sesión del 21/10 qué hará el equipo con TK-001 y US-001 si ese día no se confirman las tecnologías autorizadas. La pregunta al profesor coincide con el Sprint Planning de IT-001. Registrar el riesgo en `technical-risks.md` (IPR-v01-003). | TL; seguimiento de la SM | Antes del 21/10/2026; confirmación el 21/10 | NO |
| 2 | Confirmar que US-009-AC-09 cabe en las 8 h-p de US-009 (y US-005 en 3 h-p); actualizar las cabeceras de revisión del catálogo, EP-002 y EP-003 y el diagrama del §3 (IPR-v02-001). | PO y TL; SM | Antes de planificar IT-002 (28/10/2026) y, como tarde, IT-004 (11/11/2026) | NO |
| 3 | Registrar el acuerdo del formato de solicitud entre los validadores y US-009 (IPR-v01-013). | TL | Antes de planificar IT-003 (04/11/2026) | NO |
| 4 | Ajustar la regla de dependencias del libro (fin de la predecesora frente al inicio del sucesor) o reflejar por partes las predecesoras de US-023; mostrar la secuencia dentro del sprint de US-002 → US-005 y US-012 → US-014 (IPR-v01-001). | SM y TL | Antes de planificar IT-002 (28/10/2026) | NO |
| 5 | Actualizar el catálogo §6 (redistribución pendiente y decisión del TL de no dividir) y el apartado «Uso en la planificación» de `capacity.md` al plan de D-24 (IPR-v01-007, IPR-v02-002). | SM; PO | Próxima actualización documental | NO |
| 6 | Al detallar cada iteración, identificar quién implementa la lógica de servidor de US-010 (AC-02, AC-04 y AC-05) y conciliar el criterio de reparto de la Wiki con las asignaciones de US-006 y US-014 (IPR-v01-012). | TL y QA | Al planificar IT-003 (04/11) e IT-005 (18/11) | NO |
| 7 | Indicar qué parte de US-023 cubre cada paso de AC-02 y si bastan 0,5 h para la parte 2 (IPR-v02-003). | PO y QA | Antes de planificar IT-005 (18/11/2026) | NO |
| 8 | Identificar a la persona evaluadora externa y una fecha de IT-006 posterior al cierre de US-018; decidir qué pasa con R3 si no está disponible (IPR-v01-004). | PO y QA | 18/11/2026 (fecha del acta) | NO |

Estas son propuestas: no son decisiones aprobadas, estimaciones nuevas ni asignaciones de sprint o de personas.

## 9. Matriz de disposición RECHECK

| Hallazgo v01 | Decisión humana | Evidencia nueva o cambiada (b9c5e27 / Wiki 76f5f57) | Estado verificado | Impacto restante |
|---|---|---|---|---|
| IPR-v01-001 Dependencias (US-023 antes de que termine US-018; regla del libro) | R-10, aceptada con cambios (D-24) | El catálogo §2 y EP-007 limitan la dependencia de US-018 a la parte 2; la parte 1 solo necesita US-001 a US-003. El extracto v2 lo recoge en la cabecera. | **PARTIALLY_RESOLVED** | La duda funcional está resuelta y documentada. La regla del libro no ha cambiado («cada predecesora empieza y termina en la misma iteración o antes»). La columna de predecesoras de US-023 no distingue partes. La secuencia dentro del sprint sigue sin verse (US-002 → US-005, US-012 → US-014; US-018 → US-023 parte 2 en IT-006). |
| IPR-v01-002 Tamaño y DoR (US-018/US-023 en dos sprints) | R-11, aceptada con cambios (D-24) | La excepción explícita y justificada está en D-24, en el catálogo §4, en EP-005, en EP-007 y en el extracto v2. Cumple la constitución (Governance: excepciones explícitas, justificadas, aprobadas y temporales). | **RESOLVED** | No se ha registrado cómo se presentará en la review de IT-005 la parte preparatoria. El catálogo §6 mantiene la decisión anterior del TL sin nota (ver IPR-v01-007). |
| IPR-v01-003 Tecnologías autorizadas y cadena sin holgura | R-12, aceptada; «Pendiente de aplicar», TL, 21/10 | Sin cambios en las fuentes. `technical-risks.md` no incluye el riesgo. El acta del 14/10 tiene la acción abierta para el 21/10. TK-001 sigue condicionada. | **DEFERRED** | La confirmación se pedirá el día en que empieza IT-001. Si no llega, no hay una alternativa decidida para US-001, que es la raíz de toda la cadena. Pregunta 1 del §8. |
| IPR-v01-004 Evaluador externo / M04 en IT-006 | R-13, aceptada; «Pendiente de aplicar», PO y QA, 18/11 | Sin cambios en las fuentes. El acta tiene la acción abierta para el 18/11, que coincide con el momento de validación propuesto en v01. | **DEFERRED** | G04/M04 y el cierre de US-023 siguen dependiendo de una persona externa en la última semana, la de la entrega de la práctica 4 de GPS (27/11). |
| IPR-v01-005 Sesión de los miércoles (1 h o 2 h) | R-14, aceptada con cambios (D-24) | Team Charter, acuerdo 4: «De las 2 h, 1 h son ceremonias; la otra hora es trabajo del proyecto (D-24)». `capacity.md` dice lo mismo. Capacidad: 57,65 h. | **RESOLVED** | Ninguno. |
| IPR-v01-006 Redondeo de presentación | R-15, aceptada | El extracto v2 redondea a la mitad hacia arriba (2,98 / 2,13 / 10,18 / 6,78 / 12,73 / 9,33; costes 23,63 / 39,38), igual que `capacity.md`. | **RESOLVED** | Ninguno. |
| IPR-v01-007 Dos planes en las fuentes | R-16, aceptada | Actualizados: catálogo §2 (columna Plan), catálogo §4 (plan del H3; D-21 marcado como sustituido) y «Plan inicial» de EP-001 a EP-007. | **PARTIALLY_RESOLVED** | El catálogo §6 sigue diciendo «Para H3, redistribuir IT-002 e IT-006» y conserva la decisión del TL de no dividir US-009/US-018, sin nota sobre la excepción de D-24. Desfase parecido en `capacity.md` (IPR-v02-002). |
| IPR-v01-008 Trazabilidad de las decisiones SM/TL | R-17, aceptada | D-24 registra las cuatro decisiones con fecha, motivo, autores y artefactos afectados. | **RESOLVED** | Ninguno. |
| IPR-v01-009 TK-007 frente a US-003-AC-02 | R-18, aceptada | Extracto v2: TK-007 comprueba RN-01, RN-02, RN-04 y RN-06 (US-003-AC-02), igual que EP-001. | **RESOLVED** | Ninguno. |
| IPR-v01-010 Verificación de US-005-AC-03 | R-19, aceptada con cambios | EP-002: AC-03 trasladado. EP-003: US-009-AC-09 y predecesora US-005. Catálogo §2 y §7, y extracto v2 §2. | **RESOLVED** | El hallazgo original queda resuelto. Las consecuencias del traslado (estimación, marca de revisión, diagrama) se tratan en IPR-v02-001. |
| IPR-v01-011 Tareas «criterios de aceptación» del PO | R-20, aceptada | Extracto v2: «revisión y aceptación del PO» en US-005, US-009, US-010 y US-018. | **RESOLVED** | Ninguno. |
| IPR-v01-012 Cobertura de la DoD, lógica de servidor de US-018 y capacidades | R-21, aceptada con cambios | En US-018 el TL tiene ahora 1,5 h de diseño en IT-005 y 1,5 h de implementación en IT-006. Según R-21, las pruebas y la revisión van dentro de cada estimación y se detallarán por iteración. La Wiki publica un criterio de reparto. | **PARTIALLY_RESOLVED** | La lógica de servidor de US-018 tiene responsable. La cobertura de la DoD queda para el detalle de cada iteración. US-010 (AC-02, AC-04 y AC-05) no tiene horas del TL ni de QA. La SM (validación RN-03) y el PO (consulta de US-006) tienen tareas fuera del criterio de reparto declarado. Las capacidades técnicas siguen sin documentarse. |
| IPR-v01-013 Caducidad (R-04) y formato de solicitud | R-22, aceptada | El acta del 14/10 y Uso de agentes (R-22 y seguimiento 3) registran la confirmación del TL de que la caducidad cabe en 8/3/8 h-p. | **PARTIALLY_RESOLVED** | La revisión de la caducidad está registrada como confirmación del TL, sin más detalle técnico. El acuerdo del formato de solicitud entre los validadores (IT-003) y US-009 (IT-004) no tiene evidencia ni tarea, y la decisión no lo trata. |
| IPR-v01-014 Holgura de QA en IT-006 | R-23, aceptada con cambios | La parte 2 de US-023 pasa al PO. QA tiene 2,0 h en IT-006 (holgura 0,55 h); el PO, 2,0 h (holgura 0,40 h). | **RESOLVED** | Sigue habiendo holguras individuales mínimas dentro de la regla de la asignatura: QA 0,05 h en IT-001, PO 0,10 h en IT-002, TL 0,125 h en IT-002 e IT-004. La concentración de riesgo en QA en IT-006 ya no existe. |

Los estados de esta matriz son del revisor. Las decisiones humanas (R-10 a R-23, D-24) se citan sin cambios; el agente no crea IDs de decisión ni da por hecho que se aceptará ningún consejo nuevo.

## 10. Consejo final y límites

- **Preparación:** READY_WITH_NON_BLOCKING_QUESTIONS para revisar y usar la hipótesis humana de planificación inicial del H3 (extracto v2; 11 Must, 46 h-p, IT-001 a IT-006). **0 hallazgos bloqueantes.** Se recomienda resolver la pregunta 1 antes del 21/10/2026 y las preguntas 2 y 4 antes de planificar IT-002.
- **Límites:** se ha revisado el extracto Markdown, no el libro .xlsx ni sus fórmulas. La Wiki se ha leído en el clon local, en el commit indicado por el equipo. La confirmación técnica del TL sobre la caducidad solo consta como registro, no como análisis. No se han evaluado las capacidades técnicas de cada persona, la secuencia dentro de los sprints, el reparto por tareas de IT-002 a IT-006 ni la idoneidad de las estimaciones. No hay acceso al estado real de las dependencias externas. **Este resultado no demuestra que el calendario sea viable** ni respalda la valoración de viabilidad de la Wiki Planificación H3 §7.
- **Fuentes sin cambios:** no se ha modificado ningún requisito, prioridad, estimación, cifra de capacidad, DoR/DoD, dependencia, supuesto, decisión, plan, extracto ni fichero de la Wiki. **Solo se ha creado este informe nuevo** (`docs/reviews/initial-planning/initial-planning-review-v02.md`); v01 se conserva sin cambios.
- **Sin aprobación:** este informe es consultivo. No compromete alcance, no aprueba ningún plan ni línea base, no supera ninguna puerta de calidad, no selecciona candidatas para sprints y no asigna recursos.
