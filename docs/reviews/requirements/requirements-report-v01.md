# Requirements review v01

## 1. Metadatos de ejecución

- Agente: AG-01 — Requirements Agent / requirements-reviewer.
- Contrato leído íntegramente: .github/agents/requirements-reviewer.agent.md, adaptación del profesorado fechada 07/10/2026 (D-20). No declara otra versión numérica.
- Guía consultada: docs/agents/README.md (D-20, 07/10/2026). Esta ejecución utiliza su contrato en ChatGPT / Codex desktop, con acceso local para persistir el informe.
- Modo: INITIAL.
- Commit suministrado: db086ad9a307a5c05c7e3422d3a6183eb659f415 (abreviado db086ad). El coordinador confirmó HEAD y árbol limpio antes de la lectura. Las 16 fuentes de producto se cargaron en memoria antes de cualquier corrección posterior y se revisaron desde ese snapshot.
- Línea base declarada en los documentos revisados: requisitos-v0-borrador. El catálogo incorpora D-18 (06/10/2026) y D-21 (07/10/2026); las cabeceras de las épicas conservan revisión 01/10/2026.
- Fecha: 12/10/2026, Europe/Madrid. No se registró una hora exacta.
- Herramienta real: ChatGPT / Codex desktop. Modelo: GPT-6, familia indicada por el entorno; identificador o variante exacta no disponible. No se atribuye otra variante.
- Alcance: catálogo completo (EP-001…EP-007, US-001…US-024), consistencia transversal de los siete spec.md y detalle de US-002, US-009, US-012, US-013, US-014 y US-018. US-013 es Should diferida; no se trata como compromiso del MVP.
- Idioma: español (es-ES); IDs, severidades y estados se conservan conforme al contrato.
- Informe nuevo: docs/reviews/requirements/requirements-report-v01.md. Se comprobó que el directorio no contenía informes previos. La creación se realiza sin sobreescritura.

## 2. Manifiesto de fuentes y limitaciones

Se leyeron completos los siguientes ficheros, no solo resultados de búsqueda:

| Fuente | Papel y secciones examinadas |
|---|---|
| .specify/memory/constitution.md | Gobierno, principios 1–5, estándares, puertas de calidad, Governance e historial; v1.0, 23/09/2026. |
| specs/product/mission.md | Idea, experiencia, problema, usuarios, propuesta de valor y misión. |
| specs/product/goals.md | G01–G04, M01–M05, S-01…S-05, EX-01…EX-05, A-01…A-05, restricciones, trazabilidad y gestión de cambios; precisiones D-18/D-21. |
| specs/product/business-rules.md | Nota D-18, tabla de turnos, RN-01…RN-06, criterios de aplicación, ejemplos y mensajes; v0.2 y ajustes posteriores. |
| specs/product/catalogo.md | Las 24 filas, estimaciones individuales/consenso/tras D-18, notas D-18/D-21, criterio MoSCoW, grafo, plan provisional, decisiones históricas y pendientes. |
| specs/product/non-functional-requirements.md | NFR-001…NFR-009 completos, métricas, verificación, historias afectadas y notas; v1.0, 02/10/2026. |
| docs/risks/technical-risks.md | RT-01…RT-03, valoración, justificaciones y mitigaciones. |
| docs/quality/definition-of-ready.md | Todos los 21 criterios reales y regla de uso; v1.0, 30/09/2026. |
| docs/quality/definition-of-done.md | Todas las condiciones de finalización, especialmente validación en servidor, privacidad, evidencia y aceptación; v1.0, 30/09/2026. |
| specs/EP-001-base-del-producto/spec.md | Cabecera, límites y US-001…US-004; US-002 en detalle. |
| specs/EP-002-calendario-de-turnos/spec.md | Cabecera, límites y US-005…US-006. |
| specs/EP-003-intercambio-de-turnos/spec.md | Cabecera, límites y US-007…US-011; US-009 en detalle. |
| specs/EP-004-validacion-de-reglas/spec.md | Criterio común y US-012…US-016; US-012, US-013 y US-014 en detalle. |
| specs/EP-005-aprobacion-del-responsable/spec.md | Límites, US-017 fusionada y US-018 en detalle. |
| specs/EP-006-estado-e-historial/spec.md | Límites y US-019…US-022. |
| specs/EP-007-calidad-y-entrega/spec.md | Límites, US-023 y US-024. |
| .github/agents/requirements-reviewer.agent.md | Contrato de ejecución completo, incluidas precedencia, severidades, 11 secciones y persistencia. |
| docs/agents/README.md | Identidad AG-01, guía ChatGPT y registro humano en Uso de agentes. |

No faltó ninguna fuente esencial configurada. No se examinó código, datos de demostración reales del repositorio, pruebas, planes, tareas, Jira, Excel, documentación organizativa enlazada ni la Wiki completa. D-18 y D-21 se conocen por las notas explícitas de las fuentes leídas; no se verificaron sus entradas originales en la Wiki. No se ejecutaron comandos, tests ni instalaciones, ni se consultó la web. Esta revisión interna no valida normativa laboral real.

Precedencia aplicada: constitution > goals.md > business-rules.md > catalogo.md > spec.md; una nota fechada prevalece sobre texto anterior del mismo fichero. Por tanto, las decisiones históricas del catálogo, apartado 5, no se confunden con el alcance vigente. La precedencia permite identificar muchos restos D-18, pero no autoriza que un documento subordinado exceptúe la constitución.

En los hallazgos de ausencia, la afirmación se limita a «no encontrado en las fuentes revisadas» y a las secciones indicadas. No se afirma que el artefacto no exista en otra ubicación. MET en la DoR acredita documentación suficiente para ese criterio, no implementación, ejecución de pruebas, aprobación humana ni cumplimiento de la DoD.

## 3. Valoración del alcance revisado

**NEEDS_REFINEMENT.**

Hay bloqueos confirmados para fijar una interpretación compartida de la especificación:

1. REQ-v01-001: la constitución mantiene validación obligatoria en servidor de las reglas laborales vigentes, mientras D-18 elimina RN-02 del MVP y traslada RN-04 a la preparación de datos. La DoD exige RN-01…RN-06 en servidor. Afecta a la definición del alcance conjunto de validación y aprobación, principalmente US-014 y US-018, y al contrato del flujo de US-009. Se requiere decisión humana de gobierno; este informe no restituye reglas ni aprueba una excepción.
2. REQ-v01-003: NFR-005 exige identificar una RN en toda validación fallida, incluida US-002, mientras el acceso exige mensajes genéricos. También hay errores de reserva y motivo vacío sin RN correspondiente. Afecta a US-002, US-009 y US-018.
3. REQ-v01-004: el flujo Must declara Caducada y prohíbe aprobar fuera de plazo, pero la liberación autónoma con hora del servidor está especificada solo en US-015 Should. Afecta al contrato de estados y reservas de US-009/010/018.

REQ-v01-002 y REQ-v01-005 son problemas documentales con impacto limitado, sin bloqueo independiente. REQ-v01-006 es una pregunta, no un defecto confirmado ni una razón para bloquear por sí sola.

US-012 tiene criterios propios claros para RN-01/RN-06; no se confunde con la ausencia de RN-02. US-013 se evalúa como mejora diferida, sin exigir implementarla en el MVP por decisión del agente. Tampoco se consideran bloqueos nuevos los desequilibrios IT-002/IT-006 ni la tecnología pendiente: ya están expresamente admitidos en D-21 y el apartado 6 del catálogo, y limitan la valoración de preparación para un sprint.

Esta valoración solo cubre el snapshot y la muestra indicada. No declara que todas las historias sean Ready, que el catálogo esté completo, que el equipo haya aceptado cambios o que una línea base esté aprobada.

## 4. Matriz de cobertura de la revisión

| Dimensión | IDs y fuentes inspeccionados | Resultado | Referencias |
|---|---|---|---|
| Claridad y consistencia | EP-001…EP-007, US-001…US-024, constitución, goals, reglas, catálogo, NFR y DoD | Conflicto de gobierno; restos D-18; mensajes y caducidad con interpretación pendiente. | REQ-v01-001…REQ-v01-004; REQ-v01-006 |
| Cobertura y alcance | G01–G04, M01–M05, S-01…S-05, exclusiones, empleados/responsable/evaluador, catálogo completo | Todos los objetivos tienen épicas e historias; M01 puede quedar pendiente según D-18. Preguntas acotadas para descubrimiento de turnos y evidencia M03. | Secciones 7 y 9; REQ-v01-002 |
| Elementos de especificación | Muestra US-002/009/012/013/014/018, RN-01…RN-06, NFR-001…NFR-009, RT-01…RT-03 | Hay escenarios positivos, negativos y límites; faltan precisión del contrato temporal Must y coherencia de NFR aplicables. | REQ-v01-003…REQ-v01-006 |
| Tamaño y granularidad / INVEST | Muestra detallada, estimaciones tras D-18, grafo y decisión TL del catálogo §6 | Los 8 h-p de US-009/018 caben individualmente en sprints de 9,33 h de equipo, conforme al TL. La consulta/resolución fusionada de US-018 es un resultado vertical; no se exige dividir ni reestimar. La DoR de dependencias sigue limitada por el plan provisional. | Secciones 6 y 8 |
| Aceptación y DoR | Los 21 criterios reales, aplicados a cada una de las seis historias detalladas | 126 comprobaciones documentadas; MET incluye evidencia, las no evaluables se explican y US-013 queda separada como diferida. No hay evaluación de DoD de implementación. | Sección 6; REQ-v01-001/003/004/005 |
| Dependencias y supuestos | Catálogo §2/§3/§4/§6; fichas, A-01…A-05 y riesgos | Grafo Must sin ciclo observado; se distingue contrato compartido de predecesora terminada. Hay tecnología externa pendiente y redistribución conocida D-21. | Sección 8; REQ-v01-004 |

## 5. Hallazgos

### Índice compacto

| ID | Severidad | Categoría | Afectación principal | Bloqueo en el alcance detallado | Confianza |
|---|---|---|---|---|---|
| REQ-v01-001 | CRITICAL | Gobierno y alcance de reglas | G02, RN-02/RN-04/RN-05; US-009/014/018; US-013 diferida | Sí: alcance conjunto y aprobación sin excepción constitucional identificada | HIGH |
| REQ-v01-002 | MINOR | Propagación documental D-18 | Misión, EP-001…EP-005 y EP-007; varios IDs preservados | No independiente: la precedencia resuelve la mayoría de restos | HIGH |
| REQ-v01-003 | MAJOR | Verificabilidad de mensajes NFR | NFR-005; US-002/009/018 | Sí: criterios de error incompatibles o sin RN aplicable | HIGH |
| REQ-v01-004 | MAJOR | Estado, plazo y reservas | US-009/010/018 frente a US-015 Should | Sí: contrato temporal Must insuficientemente separado de RN-05 opcional | HIGH |
| REQ-v01-005 | MINOR | Trazabilidad de NFR | US-003/006 y US-012/013/014 | No: precisión de referencias, sin inventar nuevas obligaciones | HIGH |
| REQ-v01-006 | QUESTION | Medición de rendimiento | NFR-006; US-012/013/014/018 | No: aclaración del protocolo y relación de umbrales | MEDIUM |

### REQ-v01-001 — Recorte D-18 sin alineación con el mandato superior de validación

- **Severidad / categoría:** CRITICAL · gobierno y consistencia de alcance.
- **Evidencia del mandato:** .specify/memory/constitution.md, Core Principles §4: «descanso mínimo, límite de horas, cobertura» se «validan siempre en el servidor» y «Ningún intercambio puede aprobarse si incumple una regla vigente». Governance: «La constitución prevalece» y toda modificación debe aprobarse explícitamente, fecharse y versionarse. docs/quality/definition-of-done.md, Implementación y Reglas de Negocio: «RN-01 a RN-06» estrictamente en servidor.
- **Evidencia del recorte:** specs/product/goals.md, G02: RN-01/RN-03/RN-06 en MVP, RN-04 en el cuadrante de partida, RN-02/RN-05 Should. specs/product/business-rules.md, nota D-18: esas mismas restricciones, manteniendo las seis reglas definidas. specs/EP-004-validacion-de-reglas/spec.md, notas US-013/014: RN-02 sale de G02; por intercambio «solo se comprueba RN-03» y RN-04 se lleva a US-003. specs/EP-005-aprobacion-del-responsable/spec.md, US-018, sigue diciendo revalidación RN-01…RN-06.
- **Observación:** D-18 establece una reducción humana explícita en fuentes subordinadas, pero no se encontró una modificación o excepción constitucional en la constitución leída. Para RN-02 y RN-04 el mandato superior es expreso; para RN-05 también hay discrepancia con la DoD y debe aclararse qué significa «regla vigente» tras declararla Should. La reducción de alcance no puede considerarse una excepción de gobierno aprobada solo por su existencia en goals.
- **Impacto:** no se puede fijar simultáneamente el alcance reducido y afirmar conformidad con la puerta de gobierno actual. US-014/018 y su contrato compartido con US-009 quedan bloqueados para una aceptación coherente. La severidad refleja una frontera documental obligatoria; no implica que se hayan encontrado daños reales o fallos de código.
- **Propuesta:** el PO y equipo deben decidir y documentar la solución de gobierno: adecuar el alcance a la constitución o tramitar la modificación/excepción explícita que permita el MVP reducido, identificando las fuentes afectadas. Después, alinear DoD, G02, reglas y fichas. El agente no elige ninguna opción ni cambia prioridades o estimaciones.
- **Confianza:** HIGH: están presentes ambos lados del conflicto, con textos explícitos y una regla de precedencia.
- **Bloqueo:** sí, para acordar el alcance conjunto de validación/aprobación; no es prueba de incumplimiento de una implementación.

### REQ-v01-002 — Restos operativos de D-18 en la documentación

- **Severidad / categoría:** MINOR · terminología, alcance y mantenimiento.
- **Evidencia vigente:** specs/product/goals.md, S-01/M01/G04/M04; specs/product/catalogo.md, Ajuste D-18; notas fechadas de US-002/003/005/007/008/009/014/017/023/024. Establecen propuesta directa, un servicio, ausencia de bloqueo, RN-04 en datos y guion final.
- **Evidencia anterior aún visible, por grupo:**
  - **Publicación y RN-05:** specs/product/mission.md, experiencia y propuesta de valor («Publicar un turno», «publicación»); specs/EP-003-intercambio-de-turnos/spec.md, US-009 enunciado/AC-01 («turno publicado»), AC-05/reglas/NFR/ejemplos/límites/supuestos (48 h y publicaciones); US-010-AC-02/03 y Reglas (publicaciones, solicitud registrada con antelación exigida, RN-05); US-011 título/enunciado/AC-01…03 (cancelar publicación). specs/EP-005-aprobacion-del-responsable/spec.md, US-018-AC-01/02 («se cierran las publicaciones», «vuelven a estar disponibles»), reglas completas; US-017-AC-02 y Reglas, heredadas por la fusión, muestran todas las RN.
  - **Base y validación:** specs/EP-001-base-del-producto/spec.md, US-002-AC-06…08, verificación, casos límite y supuestos mantienen bloqueo de 5 fallos/15 min frente a nota «sin bloqueo»; US-003-AC-01 exige «al menos 2 servicios» frente a nota «un solo servicio». specs/EP-002-calendario-de-turnos/spec.md, US-005 combina «lista de próximos turnos» con descripción mensual: conviene armonizar el texto, pero no se infiere que una lista no pueda tener filtro por mes. specs/EP-004-validacion-de-reglas/spec.md, límites/criterio común y US-014-AC-02, reglas, pruebas y ejemplos siguen describiendo RN-04 por intercambio, pese a la nota que la lleva a US-003.
  - **Entrega y prueba opcional:** specs/product/catalogo.md, fila US-023, y specs/EP-007-calidad-y-entrega/spec.md, título US-023: «guion inicial» frente a guion final D-18. Resultado de EP-007 y US-023-AC-03/límites exigen cada release frente a nota «no en cada release». US-024-AC-01 aún incluye «publicar» frente a M01 vigente, sin publicación. specs/EP-006-estado-e-historial/spec.md, US-019-AC-02 aún menciona publicaciones sin solicitud.
- **Observación:** es una propagación incompleta ya reconocible por D-18, no una nueva propuesta de producto. La precedencia identifica el alcance vigente en la mayoría de casos. El catálogo §5 está marcado como histórico y no se considera un defecto por conservar decisiones antiguas.
- **Impacto:** riesgo de traducir un criterio anterior a una tarea, prueba o presupuesto vigente; no demuestra que el equipo haya aceptado restaurar esas funciones. El conflicto constitucional y el contrato de caducidad se valoran separadamente en REQ-v01-001/004.
- **Propuesta:** armonizar los textos operativos con la decisión D-18, conservando todos los IDs y el historial claramente identificado. Separar explícitamente las 48 h Should de la caducidad que aparece en Must. Actualizar título y referencia de línea base como operación documental humana, sin declarar una aprobación de calidad. Las correcciones posteriores al snapshot no se dan por verificadas en este INITIAL.
- **Confianza:** HIGH: comparación directa entre notas fechadas y criterios/enunciados anteriores.
- **Bloqueo:** no independiente; la severidad no convierte los restos conocidos en nuevos Must.

### REQ-v01-003 — NFR-005 exige una RN también a errores sin regla de negocio

- **Severidad / categoría:** MAJOR · consistencia y verificabilidad de errores.
- **Evidencia de NFR:** specs/product/non-functional-requirements.md, NFR-005, umbral: «100 % de las validaciones fallidas» indican RN-01…RN-06 y motivo; incluye US-002/009/018 en Historias afectadas.
- **Evidencia del comportamiento:** specs/EP-001-base-del-producto/spec.md, US-002-AC-03: «Usuario o contraseña incorrectos», sin indicar cuál falla; NFR de la ficha pide mensajes «genéricos». specs/EP-003-intercambio-de-turnos/spec.md, US-009-AC-03/06: turno reservado o conflicto concurrente, con motivo, sin RN equivalente. specs/EP-005-aprobacion-del-responsable/spec.md, US-018, caso límite: motivo vacío o solo espacios no permitido. RN-01…RN-06, en business-rules.md, describen turnos y compatibilidad, no autenticación, reservas o validez del texto de rechazo.
- **Observación:** la regla universal de NFR-005 no distingue rechazos de reglas de negocio de errores de acceso/entrada/estado. No existe una RN pertinente en el catálogo leído para esos errores. Asignar arbitrariamente una RN sería inventar reglas; informar qué credencial falla contradiría el criterio de acceso.
- **Impacto:** QA podría exigir una prueba imposible o un mensaje impropio para satisfacer NFR-005, aunque el comportamiento de la historia sea correcto.
- **Propuesta:** someter a decisión una precisión de NFR-005: código RN y motivo para validaciones de reglas aplicables; motivo claro y recuperable para otros errores, preservando los mensajes genéricos de credenciales. No crear nuevas RN solo para satisfacer la redacción actual.
- **Confianza:** HIGH: el cuantificador, las historias afectadas y los contraejemplos están explícitos.
- **Bloqueo:** sí para interpretar y verificar conjuntamente errores/NFR de US-002/009/018.

### REQ-v01-004 — Caducidad del flujo Must dependiente de una ficha Should

- **Severidad / categoría:** MAJOR · límites temporales, estados y reservas.
- **Evidencia Must:** specs/EP-003-intercambio-de-turnos/spec.md, US-009 Estados: «Caducada al comenzar el primero de sus turnos»; AC-03: reserva mientras Propuesta o Aceptada; US-010-AC-03 prohíbe aceptar desde el inicio más temprano. specs/EP-005-aprobacion-del-responsable/spec.md, US-018 Reglas: no se aprueban solicitudes caducadas.
- **Evidencia diferida:** specs/product/goals.md, G02, y catalogo.md, D-18, difieren RN-05/US-015. specs/EP-004-validacion-de-reglas/spec.md, US-015-AC-03 es el lugar que explica que caducar actualiza detalles, libera turnos y se comprueba con hora del servidor «no depende de que alguien abra la pantalla».
- **Búsqueda de ausencia:** se leyeron Estados, AC, reglas, NFR, casos límite y supuestos de US-009/010/018, junto con RN-05 y US-015. No se encontró en esas fichas Must un contrato completo de liberación al caducar ni la separación explícita de ese contrato frente a la validación opcional de 48 h.
- **Observación:** el límite «no aceptar ni aprobar un turno ya iniciado» está presente en Must. El cambio D-18 de RN-05 deja incierto si los efectos de caducidad descritos en US-015 se mantienen como contrato Must, qué sucede con las reservas y cómo se evita depender de una pantalla abierta.
- **Impacto:** dos implementaciones razonables podrían liberar reservas al inicio o solo al ejecutar la mejora Should; también podrían diferir toda caducidad junto con las 48 h. Afecta al estado observable y a la disponibilidad de turnos.
- **Propuesta:** aclarar y ubicar el contrato obligatorio de caducidad, estado final, liberación y rechazo de operaciones tardías en las Must que lo consumen; definir el comportamiento exactamente al inicio con hora del servidor. Mantener separada la mejora de 48 h si así lo decide el equipo. No imponer un proceso técnico concreto de caducidad.
- **Confianza:** HIGH: hay declaraciones Must y efectos definidos exclusivamente en una ficha diferida dentro de las fuentes revisadas.
- **Bloqueo:** sí, en el contrato de US-009/018 y su conexión con US-010; no exige implementar RN-05 completa ni incorporar US-015 automáticamente.

### REQ-v01-005 — Referencias NFR incompletas o con significado distinto

- **Severidad / categoría:** MINOR · trazabilidad.
- **Evidencia normativa documental:** specs/product/non-functional-requirements.md, introducción/notas: las fichas referencian los NFR por ID en Verificación y restricciones; NFR-001 es autorización según rol, NFR-003 datos ficticios/ámbito, NFR-004 accesibilidad de flujos principales y NFR-009 compatibilidad de interfaces.
- **Evidencia de las fichas:** specs/EP-001-base-del-producto/spec.md, US-003, NFR describe datos ficticios y restablecimiento sin ID, aunque figura afectada por NFR-003. specs/EP-002-calendario-de-turnos/spec.md, US-006, solo «privacidad» sin ID; tras D-18 es Must del flujo principal, pero no aparece en Historias afectadas de NFR-004 ni en la enumeración de NFR-009. specs/EP-004-validacion-de-reglas/spec.md, US-012/013/014, etiqueta NFR-001 como «validación en servidor» o «sin posibilidad de omisión», mientras el NFR central especifica autorización por rol.
- **Observación:** privacidad, accesibilidad y compatibilidad tienen fuente general; las referencias no permiten seguir su aplicación con precisión. Comprobar RN en servidor y autorizar una operación por rol son obligaciones distintas, aunque ambas ocurran en servidor.
- **Impacto:** trazabilidad incompleta de pruebas y restricciones; no demuestra ausencia de los comportamientos ni justifica nuevas métricas.
- **Propuesta:** enlazar los IDs ya existentes en las fichas aplicables, revisar las listas afectadas tras D-18 y reservar NFR-001 para autorización; referir las comprobaciones RN a reglas/constitución y NFR pertinentes. Si un validador no expone una operación a usuarios, justificar la aplicabilidad de autorización, sin inventar un endpoint.
- **Confianza:** HIGH: comparación de las definiciones centrales con las referencias y enumeraciones leídas.
- **Bloqueo:** no independiente; US-012/013/014 sí identifican NFR-005/006 y el comportamiento propio de validación.

### REQ-v01-006 — Protocolo de rendimiento NFR-006 por concretar

- **Severidad / categoría:** QUESTION · medición.
- **Evidencia:** specs/product/non-functional-requirements.md, NFR-006: «Tiempo de respuesta < 500 ms (percentil 95 < 1 s)» para el cuadrante completo de dos empleados con datos de demo, verificado mediante una prueba automatizada. specs/EP-004-validacion-de-reglas/spec.md, US-012/013/014, y specs/EP-005-aprobacion-del-responsable/spec.md, US-018, resumen solo «< 500 ms».
- **Búsqueda de ausencia:** NFR-006, fichas detalladas en Verificación y restricciones y DoD leídas no concretan si 500 ms es máximo, media u otra medida, cómo se relaciona con p95, entorno de referencia o punto de inicio/fin de la medición. No se revisaron planes ni pruebas donde pudiera existir el protocolo.
- **Observación:** no se afirma que los dos límites sean incompatibles; uno puede resultar redundante. La interpretación de «tiempo de respuesta» debe confirmarse para que las evidencias sean comparables.
- **Impacto:** pruebas con medidas diferentes podrían producir conclusiones diferentes sin una modificación de umbrales.
- **Propuesta:** QA/TL deben concretar el protocolo y significado de los límites existentes, sin que el agente invente carga, entorno o cifras nuevas.
- **Confianza:** MEDIUM: falta detalle en el ámbito leído, pero puede estar definido en artefactos no examinados.
- **Bloqueo:** no; aclaración de medición, no defecto confirmado de comportamiento.

## 6. Matriz DoR: seis historias por los 21 criterios reales

Los números C01…C21 siguientes son etiquetas de lectura del informe, no nuevos IDs del proyecto. Reproducen, en su orden, los 21 criterios de docs/quality/definition-of-ready.md. Estados: MET, NOT_MET, NOT_ASSESSABLE, NOT_APPLICABLE.

**Historias comprometidas como Must:** US-002, US-009, US-012, US-014 y US-018. **Historia diferida:** US-013 (Should, sin sprint comprometido), mostrada expresamente como tal. Evaluar su ficha no la incorpora al MVP.

Referencias de evidencia usadas en cada celda:

| Abreviatura | Fuente exacta y ámbito |
|---|---|
| P2 | specs/EP-001-base-del-producto/spec.md, US-002, incluidos enunciado, metadatos, AC, límites comunes EP-001, verificación, casos límite y supuestos. |
| P9 | specs/EP-003-intercambio-de-turnos/spec.md, US-009 y límites comunes EP-003. Los criterios US-010 se citan con ese ID. |
| P12 / P13 / P14 / P15 | specs/EP-004-validacion-de-reglas/spec.md, US-012 / US-013 / US-014 / US-015, respectivamente; incluye criterio común y límites EP-004. |
| P18 | specs/EP-005-aprobacion-del-responsable/spec.md, US-018, nota de fusión y límites comunes EP-005. |
| K | .specify/memory/constitution.md, principio 4 y Governance. |
| G | specs/product/goals.md, ID indicado. |
| B | specs/product/business-rules.md, tabla de turnos, reglas, zona y criterios de aplicación. |
| C | specs/product/catalogo.md, apartado indicado, con D-18/D-21 y notas históricas distinguidas. |
| N | specs/product/non-functional-requirements.md, NFR indicado. |

MET siempre aporta texto o sección concreta. Los criterios de planificación no certifican un Sprint Backlog: la capacidad de una historia aislada se distingue de la carga conjunta y el reparto individual; estado/terminación de predecesoras no se examinó. Las cuestiones de implementación, datos, tests y DoD quedan fuera de esta matriz documental.

| Criterio real DoR | US-002 Must | US-009 Must | US-012 Must | US-013 Should diferida | US-014 Must | US-018 Must |
|---|---|---|---|---|---|---|
| C01 — La historia tiene un identificador único y estable (US-XXX). | MET — P2, título US-002. | MET — P9, título US-009. | MET — P12, título US-012. | MET — P13, título US-013. | MET — P14, título US-014. | MET — P18, título US-018. |
| C02 — Está asociada a una épica (EP-XXX). | MET — P2, cabecera EP-001. | MET — P9, cabecera EP-003. | MET — P12, cabecera EP-004. | MET — P13, cabecera EP-004. | MET — P14, cabecera EP-004. | MET — P18, cabecera EP-005. |
| C03 — Está trazada al menos a un objetivo del producto (G01–G04). | MET — P2, Objetivo G04. | MET — P9, Objetivo G01/G02. | MET — P12, Objetivo G02/M02. | MET — P13, Objetivo G02/M02. | MET — P14, Objetivo G02/M02. | MET — P18, Objetivo G03/M03 y G02. |
| C04 — El usuario o stakeholder está identificado (empleado, responsable, evaluador…). | MET — P2, enunciado usuario y roles empleado/responsable. | MET — P9, enunciado empleado. | MET — P12, enunciado responsable. | MET — P13, enunciado responsable. | MET — P14, enunciado responsable. | MET — P18, enunciado responsable. |
| C05 — La capacidad esperada está descrita con claridad. | MET — P2, iniciar sesión con cuenta ficticia y rol. | MET — P9, D-18: proponer directamente dos turnos. | MET — P12, AC-01/02: descanso y solapes. | MET — P13, AC-01/02: 40 h y reparto semanal. | MET — P14, nota D-18/AC-01: compatibilidad. | MET — P18, enunciado/AC-01/02: resolver con motivo. |
| C06 — El valor o beneficio se entiende. | MET — P2, Necesidad: identificación y trazabilidad. | MET — P9, Necesidad: formalizar acuerdo verificable. | MET — P12, Necesidad: evitar descanso inválido. | MET — P13, Necesidad y ejemplo 38−7+10=41 h. | MET — P14, Necesidad: personal mínimo/cobertura. | MET — P18, Necesidad: decisión final trazable. |
| C07 — El alcance y los límites están claros (qué entra y qué no). | MET — P2, límites EP-001 y nota D-18 sin bloqueo; restos REQ-v01-002 resueltos por precedencia. | NOT_MET — P9 Estados frente a P15-AC-03 diferida; REQ-v01-004. | MET — P12, RN-01/RN-06 y nota sin cambio de hora. | MET — P13, RN-02/no extras; G A-05 limita demo sin cambio de hora; Should separada. | NOT_MET — P14 D-18/RN-04 frente a K §4; REQ-v01-001. | NOT_MET — P18 Reglas y G G02; P15-AC-03 diferida; REQ-v01-001/004. |
| C08 — Tiene criterios de aceptación identificados (US-XXX-AC-01…). | MET — P2, AC-01…09; D-18 desplaza AC-06…08 del MVP. | MET — P9, AC-01…07; remanentes REQ-v01-002. | MET — P12, AC-01…04. | MET — P13, AC-01…03. | MET — P14, AC-01…02; AC-02 debe armonizarse. | MET — P18, AC-01…06. |
| C09 — Los criterios son observables y verificables, incluidos los casos de error. | NOT_MET — P2-AC-03 frente a N NFR-005; REQ-v01-003. | NOT_MET — P9-AC-03/06, Estados y N NFR-005; REQ-v01-003/004. | MET — P12-AC-01…04, casos de 12 h, sin turno anterior y datos ausentes. | MET — P13-AC-01…03, ejemplos 41/35 h y límites 40 h/domingo. | NOT_MET — P14-AC-02 por intercambio frente a D-18 y K §4; REQ-v01-001. | NOT_MET — P18 casos motivo vacío, Reglas/caducidad y N NFR-005; REQ-v01-001/003/004. |
| C10 — Describen el comportamiento esperado, no una implementación concreta. | MET — P2-AC-01…05/09 describen sesión, navegación, rechazo e invalidación. | MET — P9-AC-01…07 describen propuesta, permisos, reservas y resultados concurrentes. | MET — P12-AC-01…04 describen validez y rechazo en servidor. | MET — P13-AC-01…03 describen límite y reparto, sin algoritmo. | MET — P14-AC-01/02 describen compatibilidad/cobertura, sin algoritmo. | MET — P18-AC-01…06 describen permuta, estado, motivo, registro y unicidad. |
| C11 — Si afecta a un intercambio o a su validación, indica qué reglas de negocio (RN-01–RN-06) aplica y sus precondiciones. | NOT_APPLICABLE — P2 trata acceso, no intercambio ni su validación; sí le aplica control por rol. | NOT_MET — P9 RN-03/RN-05 y Estados no separan plazo Must de P15 opcional; REQ-v01-004. | MET — P12 Reglas RN-01/RN-06, ambos empleados/vecinos y datos necesarios. | MET — P13 Reglas RN-02, ambos empleados, semanas locales y reparto dominical. | NOT_MET — P14 nota/Reglas RN-03/RN-04 y K §4; precondición de cobertura depende de REQ-v01-001. | NOT_MET — P18 RN-01…06 y caducidad frente a G G02/P15; REQ-v01-001/004. |
| C12 — Tiene prioridad MoSCoW asignada y justificada. | MET — P2 Prioridad Must: identidad/RT-03. | MET — P9 Prioridad Must: núcleo del flujo. | MET — P12 Prioridad Must: RN central/RT-01. | MET — P13 Prioridad Should: nota D-18 y reutilización; conflicto superior en REQ-v01-001 no se da por aprobado. | MET — P14 Prioridad Must: protege compatibilidad/cobertura. | MET — P18 Prioridad Must: cierre del flujo/RT-02. |
| C13 — Tiene una estimación consensuada en horas-persona. | MET — P2 Estimación y C §2: 3 h-p votadas tras D-18. | MET — P9 Estimación/C §2: consenso 8 h-p. | MET — P12 Estimación/C §2: 5 h-p tras D-18. | MET — P13 Estimación/C §2: 3 h-p tras D-18. | MET — P14 Estimación/C §2: 3 h-p tras D-18. | MET — P18 Estimación/C §2 y D-18: 8 h-p fusionada. |
| C14 — Tiene indicada la incertidumbre (Baja / Media / Alta). | MET — P2 Incertidumbre Media. | MET — P9 Incertidumbre Media. | MET — P12 Incertidumbre Alta. | MET — P13 Incertidumbre Alta. | MET — P14 Incertidumbre Media. | MET — P18 Incertidumbre Alta. |
| C15 — Sus predecesoras y dependencias (funcionales, técnicas y externas) son conocidas y no bloquean el sprint. | NOT_ASSESSABLE — P2 conoce US-001/003; C §6 deja tecnología externa pendiente y §4 IT-002 provisional; estado de predecesoras no revisado. | NOT_ASSESSABLE — P9 conoce US-006/003; replanificación D-21 y disponibilidad efectiva no acreditadas en fuentes leídas. | NOT_ASSESSABLE — P12 conoce US-003 y contrato con US-009; no se revisó estado de predecesora/contrato acordado. | NOT_ASSESSABLE — P13 conoce US-003/012 y contrato US-009; Should sin sprint comprometido. | NOT_ASSESSABLE — P14 conoce US-003/012 y contrato US-009; plan por redistribuir, sin estado de terminación revisado. | NOT_ASSESSABLE — P18 conoce US-010/012/014; plan provisional y estado de predecesoras no acreditados. |
| C16 — Cabe en un sprint; si no cabe, se divide. | MET — 3 h-p individualmente ≤ 6,78 h IT-002 en C §4; el total de 9 h aún requiere reparto D-21. | MET — 8 h-p ≤ 9,33 h; C §6 decisión TL permite tareas entre varias personas, sin exigir división de historia. | MET — 5 h-p ≤ 12,73 h IT-003 en C §4. | NOT_ASSESSABLE — 3 h-p y Should documentadas; no hay sprint elegido para comprobar su incorporación/carga. | MET — 3 h-p ≤ 9,33 h IT-005 en C §4; sin afirmar reparto individual aprobado. | MET — 8 h-p ≤ 9,33 h; C §6 decisión TL. Total IT-006 con US-023 de 10 h sigue pendiente. |
| C17 — Se han identificado los requisitos no funcionales que le aplican (NFR-XXX). | MET — P2 Verificación: NFR-001/002/004/005/009 y privacidad NFR-003; precisión de errores REQ-v01-003. | MET — P9 Verificación: NFR-001/004/005/007/009. | MET — P12 Verificación: NFR-005/006 y mención NFR-001; significado de esta última en REQ-v01-005. | MET — P13 Supuestos/NFR: NFR-005/006 y mención NFR-001; ubicación/semántica en REQ-v01-005. | MET — P14 Supuestos/NFR: NFR-005/006 y mención NFR-001; precisión REQ-v01-005. | MET — P18 Verificación: NFR-001/004/005/006/007/009. |
| C18 — Se conocen las restricciones técnicas, organizativas o de proyecto relevantes. | MET — P2 límites sin registro/recuperación, roles, cuentas ficticias y hashing; tecnología externa pendiente se trata en criterio 15. | MET — P9 límites uno a uno, sin cesiones/contraofertas; NFR-007 concurrencia. | MET — P12 horarios fijos, ambos empleados, servidor; G A-05 y B Europe/Madrid. | MET — P13 no extras/guardias y semanas lunes-domingo Europe/Madrid; G A-05 para demo. | MET — P14 intercambio uno a uno compatible y cuadrante inicial 3/3/2; cuestión de gobierno separada. | MET — P18 responsable por servicio, servidor, decisión atómica y concurrencia entre pestañas. |
| C19 — Solo utiliza datos ficticios o sintéticos y cumple las restricciones de privacidad (principio 5 de la constitución). | MET — P2 cuenta ficticia/NFR-003, límites comunes EP-001; valoración documental, sin inspección de datos. | MET — P9 aplicación común datos ficticios y AC-02 acceso participantes/responsable. | MET — P12 aplicación común datos ficticios y límites sin convenios reales. | MET — P13 aplicación común datos ficticios; reglas internas de jornada. | MET — P14 aplicación común datos ficticios, un solo servicio de demo según C D-18. | MET — P18 aplicación común datos ficticios y NFR-001 acceso del responsable de servicio. |
| C20 — No hay preguntas sin resolver que impidan entender o planificar la historia. | NOT_MET — N NFR-005 frente a P2-AC-03; REQ-v01-003. | NOT_MET — contrato del flujo/mensajes/plazo en REQ-v01-001/003/004. | MET — P12 fija reglas propias, fronteras y datos ausentes; preguntas NFR-006 no bloqueantes. | NOT_MET — prioridad diferida y mandato superior RN-02 pendientes de resolver en REQ-v01-001; no se convierte en Must. | NOT_MET — RN-04 inicial frente a validación en servidor; REQ-v01-001. | NOT_MET — gobierno, mensajes y caducidad; REQ-v01-001/003/004. |
| C21 — Cualquier supuesto importante o duda no bloqueante está documentado en la ficha. | MET — P2 Supuestos: responsable único y sin recuperación; D-18 desplaza supuesto antiguo de bloqueo. | MET — P9 Supuestos: reserva única y sin contraoferta; restos de publicaciones en REQ-v01-002. | MET — P12 Supuestos: horarios fijos; Casos límite distingue datos ausentes de turno inexistente. | MET — P13 Supuestos: solo horas de turno, semanas locales; escenarios cambio de hora no exigidos en demo A-05. | MET — P14 Supuestos: cuadrante inicial 3/3/2 y datos completos. | MET — P18 Supuestos: datos originales conservados, consultas básicas sin EP-006 y responsable único con dos pestañas. |

Ninguna fila MET ni combinación de filas constituye aprobación humana. La DoR exige cumplimiento íntegro para entrar en sprint; este informe no declara Ready a ninguna historia. Los NOT_ASSESSABLE de dependencias no inventan un bloqueo técnico: delimitan la evidencia disponible.

## 7. Candidatos de omisión y preguntas de stakeholders

No se han confirmado nuevos actores necesarios más allá de empleado, responsable, evaluador y los participantes de prueba ya declarados. Se separan los siguientes candidatos de los defectos de la sección 5; ninguno queda aprobado ni añade una nueva historia.

| Clasificación | Candidato y evidencia del alcance | Pregunta humana / límite |
|---|---|---|
| IN_SCOPE_CANDIDATE | Estado sin compañeros/turnos compatibles en US-006. G01 y S-01 requieren encontrar el turno sobre el que proponer. EP-002 US-006-AC-01/02 limita compatibilidad y privacidad, pero no describe vacío/error. EP-003 US-008-AC-03 sí describe el vacío, pero US-008 está fuera de versión. No se encontró ese comportamiento en la ficha US-006 leída. | ¿Qué ve el empleado si no hay ningún turno compatible y cómo distingue ausencia de datos de un fallo? Refinar el comportamiento del flujo existente, sin restaurar publicaciones ni inventar filtros. No bloquea una muestra detallada distinta por sí solo. |
| IN_SCOPE_CANDIDATE | Evidencia M03 si US-024 no se incorpora. Goals M03 exige tres decisiones de muestra, cada una < 1 min; US-018 referencia M03; US-024-AC-03 explica la prueba, pero US-024 es Should. | ¿En qué evidencia de US-018 o del guion final se registrarán las tres decisiones si se difiere US-024? El resultado ya está acordado; no se exige la prueba opcional con empleados ni se inventa otra meta. |
| SCOPE_UNCLEAR | Tras una revalidación fallida en US-018-AC-03 se impide aprobar y se muestra el motivo; no se detalla expresamente si la solicitud continúa Aceptada, termina con otro estado o libera sus reservas. Se leyeron Estados de US-009, AC/casos de US-018 y reglas. | ¿El fallo conserva Aceptada y las reservas para otra decisión, o produce una transición terminal? No se propone una transición nueva ni se concluye un defecto de implementación; precisar si el equipo necesita esa decisión. |
| OUT_OF_SCOPE | Tratamiento de semanas con cambio de hora para la demostración, mencionado en US-013 (Should). Goals A-05 y las notas D-18 excluyen esas semanas del MVP. | Mantener los ejemplos como información futura si el equipo lo desea, claramente separados de pruebas exigidas a los datos de esta versión. No convierte el cambio de hora en obligación Must. |
| OUT_OF_SCOPE | Notificaciones externas, integración RR. HH./hospital real, cuadrante generado automáticamente y aplicación móvil nativa. | EX-02/03/04/05 las excluyen. No se proponen como requisitos faltantes. |

La cancelación (US-011), vistas ampliadas (US-019/020), diagnóstico ampliado (US-016), horas semanales (US-013), 48 h (US-015) y prueba con usuarios (US-024) conservan su carácter Should. US-007/008 siguen fuera de esta versión; US-017 continúa fusionada. Un candidato de mejora no se convierte en bloqueo ni compromiso por aparecer aquí.

## 8. Dependencias, supuestos y trazabilidad

### Dependencias explícitas y contratos compartidos

- **Predecesoras de producto/técnicas:** catálogo §2/§3 y fichas: US-001 → US-003 → US-002 → US-005 → US-006 → US-009 → US-010 → US-018 → US-023. US-012 se apoya en US-003; US-014 reutiliza US-012; US-018 necesita US-010/012/014. No se observó un ciclo en el grafo Must leído. Los vínculos directos omitidos en un diagrama resumido no se interpretan automáticamente como dependencia ausente cuando están en el catálogo o son transitivos.
- **Contrato compartido, no prerrequisito de terminación:** US-012/013/014 y US-015 explican que el formato se acuerda con US-009 «sin requerir esa historia terminada». Que US-009 sea el objeto del intercambio no impide desarrollar validadores antes si se acuerda ese contrato. No se encontró en los apartados leídos un esquema de campos o constancia de contrato ya acordado; eso limita el criterio 15, sin inventar un ciclo ni obligar a una tecnología o formato concreto.
- **Preferencia/secuenciación:** plan inicial por iteración y criterio de adelantar riesgo. Son decisiones de planificación del equipo, no nuevas dependencias funcionales impuestas por este informe.
- **Dependencia externa confirmada y pendiente ya declarada:** tecnología autorizada para US-001, catálogo §6/EP-001. Al estar en la raíz del entorno, afecta a la preparación de las sucesoras. No se verificó una confirmación externa en esta revisión.
- **Dependencia externa para la entrega:** evaluador ajeno a la implementación en US-023. Los tres participantes de US-024 solo son exigibles si se incorpora esa Should; su falta no se transforma en bloqueo Must de M01, que D-18 permite dejar pendiente.
- **Desacoplamiento básico/ampliado:** US-009-AC-07, US-010-AC-04 y US-018, incluida US-017 fusionada, mantienen estado y registro básicos. US-019/020 son vistas ampliadas; no son prerrequisitos del resultado básico. El traslado de reglas/estado temporal queda pendiente en REQ-v01-001/004.

### Planificación conocida, sin nuevas estimaciones

El catálogo, revisión D-21, ya admite IT-002 con 9 h-p frente a 6,78 h e IT-006 con 10 h-p frente a 9,33 h. El total Must de 46 h-p cabe en 57,65 h, pero eso no resuelve el reparto por sprint/persona. SM/TL deben redistribuir en H3; no se añade un hallazgo nuevo por ese pendiente declarado.

El TL ha decidido que US-009 y US-018, de 8 h-p, no necesitan dividirse en nuevas historias: caben en varios sprints de equipo y se descompondrán en TK. El informe respeta esa decisión y diferencia capacidad individual, capacidad de equipo y carga conjunta. No crea estimaciones, no modifica Planning Poker ni afirma que las tareas ya estén repartidas. Las cifras individuales históricas y las sumas antiguas no sustituyen el consenso tras D-18.

### Supuestos y límites del snapshot

| Fuente / supuesto | Evidencia y valoración |
|---|---|
| G A-01, reglas definidas RN-01…RN-06 | Las seis reglas siguen documentadas, pero su obligatoriedad MVP está en conflicto de gobierno (REQ-v01-001). Definición no equivale a implementación. |
| G A-02; P2/P18 Supuestos | Un centro y responsable por servicio. Dos pestañas del mismo responsable siguen haciendo pertinente RT-02 y US-018-AC-06. No se añade un segundo aprobador. |
| G A-03; NFR-009 | Navegadores modernos; alcance de compatibilidad ya definido. Falta trazabilidad de la interfaz Must US-006, REQ-v01-005. |
| G A-04 / catálogo D-21 | Capacidad nominal/efectiva y ausencias referidas, con reparto pendiente. No se recalculó capacity.md ni se verificó disponibilidad de personas. |
| G A-05; P12/P13; B zona horaria | Demostración sin semanas de cambio de hora. Europe/Madrid y fecha local de inicio siguen aplicando. Los ejemplos futuros de US-013 no amplían el MVP. |
| P14 US-003 como precondición | El cuadrante inicial debe cumplir 3/3/2; el intercambio compatible uno a uno conserva cobertura. Esto es una justificación de D-18, no aprobación de una excepción constitucional. No se inspeccionó ni validó el dataset. |

Las hipótesis sobre motor de base de datos, ORM, algoritmo de reserva, planificador de caducidad, alojamiento o tecnología de interfaz son **UNCONFIRMED**: no se requieren ni se infieren de las fuentes examinadas. Los NFR y RT-02 sí exigen resultados atómicos y consistentes; no prescriben aquí una implementación elegida por el agente.

### Trazabilidad

Las épicas están vinculadas a objetivos y las 24 historias tienen IDs conservados. La muestra detallada identifica necesidad, objetivo, prioridad, estimación, incertidumbre, predecesoras, AC y supuestos. REQ-v01-005 precisa referencias NFR. La cadena hasta plan, TK, código y evidencias no es evaluable sin esos artefactos; este INITIAL se limita a requisitos. Para decisiones humanas, registrar cada REQ-v01-NNN en Uso de agentes junto con AG-01, entrada/commit, propuesta, justificación, decisión, herramienta y modelo. Aceptar una propuesta no prueba que ya se haya corregido.

## 9. Preguntas para el equipo, por prioridad de interpretación

1. **PO/equipo — REQ-v01-001:** ¿D-18 cuenta con una excepción o modificación constitucional explícita que permita diferir RN-02 y RN-05 y comprobar RN-04 solo en los datos? Si existe, aportar su referencia y versión. Si no, ¿qué solución de gobierno se decide para alinear constitución, DoD y alcance? ¿Qué reglas se consideran «vigentes» para la aprobación?
2. **QA/PO — REQ-v01-003:** ¿Se acepta distinguir rechazos de reglas, que incluyen RN y motivo, de errores de acceso/entrada/reserva sin RN aplicable, manteniendo genéricos los mensajes de credenciales?
3. **PO/TL/QA — REQ-v01-004:** Aunque se difieran las 48 h de RN-05, ¿caducar exactamente al inicio más temprano, impedir aceptar/aprobar y liberar reservas forman parte del flujo Must? ¿Qué estado y detalle se conservan y cómo se verifica con hora del servidor sin depender de abrir una pantalla?
4. **Equipo — REQ-v01-002/005:** ¿Qué textos vigentes se armonizan con D-18 y qué fragmentos se conservan solo como historial? Confirmar que no se restauran bloqueo de acceso, dos servicios, publicación, RN-04 por intercambio o instalación en cada release al corregir las fichas. La navegación mensual de una lista no se declara excluida sin decisión expresa.
5. **SM/TL — pendiente D-21:** ¿Qué redistribución resuelve IT-002/IT-006 respetando personas y predecesoras? ¿Se confirmó la tecnología autorizada y el contrato de entrada común de validadores con US-009? Son pendientes ya declarados, no estimaciones nuevas.
6. **QA/TL — REQ-v01-006:** ¿Qué medida corresponde a < 500 ms, cómo se relaciona con p95 < 1 s y cuál es el protocolo de medición ya acordado? Aportar el artefacto si está definido fuera del alcance leído.
7. **PO/QA — candidatos sección 7:** ¿Qué comportamiento tiene US-006 sin turnos compatibles? ¿Dónde se recoge la evidencia de M03 si US-024 se difiere?
8. **PO/TL — pregunta sección 7:** ¿Una revalidación fallida de US-018 mantiene la solicitud Aceptada y sus reservas, o se produce una transición terminal? Confirmar el resultado antes de concretar pruebas de ese caso.

No se atribuye ninguna respuesta o decisión a un miembro del equipo. Las preguntas se dejan aquí porque esta ejecución no espera una decisión humana interactiva.

## 10. Relación con revisiones anteriores

Modo **INITIAL**. No hay informe anterior ni crosswalk RECHECK. Los antecedentes D-18/D-21 son decisiones y pendientes del proyecto, no hallazgos de un informe anterior.

Las correcciones realizadas después de fijar el snapshot deben revisarse mediante un nuevo informe RECHECK, conservando esta versión sin edición. Ese informe necesita la decisión humana de cada REQ-v01-NNN y las fuentes revisadas; debe distinguir RESOLVED, PARTIALLY_RESOLVED, OPEN, JUSTIFIABLY_REJECTED, DEFERRED o NOT_ASSESSABLE. Una corrección parcial de los restos conocidos no resuelve automáticamente los conflictos de gobierno ni aprueba propuestas nuevas.

## 11. Cierre explícito

Esta ejecución AG-01 ha realizado una revisión consultiva y ha creado únicamente este informe nuevo. No se han modificado fuentes de requisitos por el agente, no se han ejecutado comandos ni pruebas, no se han generado estimaciones y no se han decidido prioridades, planes o excepciones. Las actividades del coordinador o del equipo posteriores al snapshot quedan fuera del resultado INITIAL.

"This is an advisory review. No source requirement, priority, estimate, plan or human decision was changed. No baseline or gate was approved."
