# Requirements review v02

## 1. Metadatos de ejecución

- Agente: AG-01 — Requirements Agent / requirements-reviewer.
- Contrato: .github/agents/requirements-reviewer.agent.md, leído íntegramente; adaptación del profesorado de 07/10/2026 (D-20), sin otra versión numérica declarada. Guía: docs/agents/README.md.
- Modo: RECHECK. Informe previo: docs/reviews/requirements/requirements-report-v01.md (INITIAL sobre db086ad9a307a5c05c7e3422d3a6183eb659f415).
- Commit suministrado y snapshot de fuentes: **dda3ce4c38383c43eb5d1ed3ba6703cd37b251ec**. El asistente de documentación confirmó previamente main publicado y limpio y cargó las 16 fuentes en memoria; el revisor examinó ese snapshot sin editar las fuentes.
- Integración anterior al snapshot: constitución 7584e5a; QA 752e8a1; PO 9568fe0; sincronización NFR 810e2a0; formato de catálogo dda3ce4. Son actuaciones del equipo/asistente de documentación anteriores a esta revisión.
- Registro humano: Uso-de-agentes.md y Registro-de-decisiones.md de la Wiki, commit **4b049c285ba95feb71a1b59b716d80f6452a330a**; D-22 para R-01…R-06 y D-23 para R-07…R-09. No se equipara aceptación humana a corrección comprobada.
- Línea base documental declarada: requisitos-v1-revisado, revisión 13/10/2026; constitución, DoD y NFR v1.1. El identificador documental no implica aprobación de un gate.
- Fecha: 13/10/2026, Europe/Madrid; hora exacta no registrada.
- Herramienta: ChatGPT / Codex desktop. Modelo: GPT-6 (familia indicada por el entorno; ID/variante exacto no disponible).
- Alcance: catálogo completo EP-001…EP-007 / US-001…US-024 y consistencia transversal; muestra detallada US-002, US-009, US-012, US-013, US-014 y US-018. **US-013 es Should diferida**, sin compromiso de implementación MVP.
- Idioma: español, es-ES; estados e IDs conforme al contrato. Salida nueva: docs/reviews/requirements/requirements-report-v02.md. El directorio contenía solo v01; v02 se crea sin sobreescribirlo.

## 2. Manifiesto de fuentes y limitaciones

Se leyeron íntegramente las fuentes siguientes y sus secciones en contexto:

| Fuente | Secciones / uso |
|---|---|
| .specify/memory/constitution.md | Principios, estándares, gates, gobierno e historial v1.1/D-22. |
| specs/product/mission.md | Experiencia, problema, usuarios, valor y misión. |
| specs/product/goals.md | G01–G04, M01–M05, S-01…S-05, exclusiones, supuestos, restricciones, trazabilidad y cambios D-18/D-22/D-23. |
| specs/product/business-rules.md | Nota de alcance, turnos, RN-01…RN-06, aplicación, ejemplos y mensajes. |
| specs/product/catalogo.md | Las 24 filas, estimaciones, D-18/D-21, grafo, plan provisional, historial y pendientes. |
| specs/product/non-functional-requirements.md | NFR-001…009: métricas, verificación, historias afectadas y protocolo NFR-006. |
| docs/quality/definition-of-ready.md | Los 21 criterios reales y regla de uso, v1.0. |
| docs/quality/definition-of-done.md | Todas las condiciones, especialmente reglas MVP en servidor y evidencia, v1.1. |
| docs/risks/technical-risks.md | RT-01…03: tabla, valoración, justificaciones y mitigaciones. |
| specs/EP-001-base-del-producto/spec.md | US-001…004; detalle US-002, bloqueo fuera de versión y datos de un servicio. |
| specs/EP-002-calendario-de-turnos/spec.md | US-005/006; lista y nuevo AC-03 vacío/error. |
| specs/EP-003-intercambio-de-turnos/spec.md | US-007…011; detalle US-009, estados, reserva, caducidad y respuesta. |
| specs/EP-004-validacion-de-reglas/spec.md | US-012…016; detalle US-012/013/014, alcance común y separación de US-015. |
| specs/EP-005-aprobacion-del-responsable/spec.md | US-017 fusionada y detalle US-018; revalidación, decisión y caducidad. |
| specs/EP-006-estado-e-historial/spec.md | US-019…022; ampliaciones frente al detalle básico. |
| specs/EP-007-calidad-y-entrega/spec.md | US-023/024; guion final y M01/M03 si se difiere la prueba. |
| docs/reviews/requirements/requirements-report-v01.md | Metadatos, seis hallazgos, DoR, tres candidatos y límites del INITIAL. |
| Wiki / Uso-de-agentes.md | R-01…09, decisiones, commits de aplicación y seguimiento RECHECK. |
| Wiki / Registro-de-decisiones.md | Decisiones D-01…D-23; especialmente D-18/D-21/D-22/D-23. |
| .github/agents/requirements-reviewer.agent.md | Contrato completo y límites de ejecución. |
| docs/agents/README.md | Guía de ejecución y registro de herramienta/modelo. |

No faltó ninguna fuente esencial para valorar la coherencia documental del alcance revisado. Precedencia: constitución > objetivos > reglas > catálogo > fichas; las notas fechadas prevalecen sobre texto anterior del mismo fichero. Los criterios de US-002 marcados fuera de versión, US-007/008 y el catálogo §5 histórico no restauran funciones MVP.

No se inspeccionaron código, datasets efectivos, planes técnicos, tareas, Excel, Jira, pruebas ejecutadas ni la Wiki completa. No se ejecutaron comandos, tests o instalaciones en la fase de revisor; no se consultó la web ni se verificó normativa laboral real. La preparación/publicación anterior de fuentes y la publicación posterior del informe pertenecen al asistente de documentación.

MET acredita documentación para el criterio indicado, no comportamiento implementado. La terminación de predecesoras, el acuerdo técnico de entrada a validadores, la autorización de tecnologías y el reparto final por persona/sprint no son evaluables con estas fuentes. La revisión técnica posterior de Marcelino (TL) sobre la caducidad no se da por realizada; se distingue de la conformidad previa con estimaciones mencionada en el registro humano.

## 3. Valoración del alcance revisado

**NO_BLOCKING_FINDINGS_IN_REVIEWED_SCOPE**, limitado a la coherencia de los requisitos documentados en el snapshot y a la muestra indicada.

Los bloqueos iniciales REQ-v01-001/003/004 tienen resolución comprobable en gobierno, NFR y criterios Must. REQ-v01-005/006 también quedan resueltos documentalmente. Las tres preguntas candidatas cuentan con decisión humana D-23 y texto aplicado. REQ-v01-002 queda **PARTIALLY_RESOLVED** por un resto no bloqueante en la descripción histórica de RT-01: las historias operativas ya reflejan D-18, pero ese documento todavía atribuye a la constitución la comprobación de horas/cobertura antes de toda aprobación.

Ese residuo no impide interpretar US-012/014/018: constitución v1.1, G02, DoD y fichas coinciden expresamente y prevalecen. No se detectó otro bloqueo documental en la muestra. No se declara Ready/Done ninguna historia, ni aprobado el catálogo, la planificación o la línea base. Las 13 celdas NOT_ASSESSABLE de la DoR delimitan preparación para sprint y evidencia externa; no ocultan una fuente esencial de requisitos inaccesible.

## 4. Matriz de cobertura

| Dimensión | Alcance examinado | Resultado / referencia |
|---|---|---|
| Claridad y consistencia | Gobierno, G02, RN, NFR, misión y siete fichas | Reglas vigentes, mensajes y caducidad alineados; resto menor RT-01 dentro de REQ-v01-002 (§5). |
| Cobertura y alcance | G01–G04/M01–M05, actores, 24 historias y exclusiones | Objetivos cubiertos por épicas/historias; R-07…09 aplicadas; M01/M03 pueden quedar pendientes sin promover US-024 a Must (§7). |
| Elementos de especificación | AC, RN, NFR, casos positivos/negativos, reservas y límites | Caducidad Must y revalidación fallida tienen resultados observables; trazabilidad/protocolo corregidos (§5/§6). |
| Tamaño y granularidad / INVEST | Muestra detallada, prioridades, horas y D-21 | Se mantienen consensos y decisión TL sobre historias de 8 h-p; consulta/resolución fusionada conserva un resultado vertical. No se exige dividir ni reestimar (§8). |
| Aceptación y DoR | 21 criterios reales × seis historias | 126 celdas con evidencia; US-013 separada como diferida. Preparación efectiva para sprint no certificada (§6). |
| Dependencias y supuestos | Grafo, predecesoras, contratos comunes, A-01…05 y RT | No se observó ciclo Must; contrato compartido no equivale a historia terminada. Pendientes D-21 y revisión técnica posterior conservados (§8/§9). |

## 5. Hallazgos y evidencia de revalidación

Se conservan los seis IDs originales. La severidad de la tabla es la del INITIAL, no una afirmación de bloqueo actual. El resto de RT-01 se agrupa en el problema de propagación D-18 ya identificado, sin duplicarlo con un nuevo ID.

| ID previo / registro | Severidad inicial | Estado RECHECK | Bloqueo actual | Confianza |
|---|---|---|---|---|
| REQ-v01-001 / R-01 | CRITICAL | RESOLVED | No | HIGH |
| REQ-v01-002 / R-02 | MINOR | PARTIALLY_RESOLVED | No | HIGH |
| REQ-v01-003 / R-03 | MAJOR | RESOLVED | No | HIGH |
| REQ-v01-004 / R-04 | MAJOR | RESOLVED | No, como contrato documental | HIGH |
| REQ-v01-005 / R-05 | MINOR | RESOLVED | No | HIGH |
| REQ-v01-006 / R-06 | QUESTION | RESOLVED | No | HIGH |

### REQ-v01-001 — Gobierno y reglas MVP: RESOLVED

- Decisión: R-01 aceptada con cambios por el equipo, D-22. Evidencia anterior: constitución v1.0/DoD exigían validación completa frente a G02/D-18 reducido (v01 §5).
- Evidencia actual: .specify/memory/constitution.md, principio 4: «las reglas vigentes del MVP», definidas por G02; historial 1.1 fechado 13/10/2026 con aprobación del equipo y justificación RN-04. docs/quality/definition-of-done.md, Implementación: «vigentes del MVP (G02)». specs/product/goals.md, G02/M02: RN-01/03/06 en servidor y RN-04 en cuadrante de partida; RN-02/05 Should. business-rules.md y EP-004/EP-005, Reglas, coinciden.
- Observación/impacto: existe la modificación de gobierno antes ausente y la DoD la refleja. US-014-AC-02 y US-018 Reglas ya no exigen RN-04 por permuta ni RN-02/05 obligatorias.
- Acción sugerida: conservar D-22 y estas referencias en la trazabilidad; la ejecución de validaciones y pruebas se comprobará en desarrollo. No se requiere otra decisión de alcance para resolver este conflicto.
- Confianza HIGH: comparación directa de ambos lados y registro humano. Bloqueo documental actual: no.

### REQ-v01-002 — Propagación D-18: PARTIALLY_RESOLVED

- Decisión: R-02 aceptada, D-22; corrección de decisiones ya tomadas en D-18, manteniendo IDs.
- Evidencia corregida: mission.md, Experiencia/Propuesta de valor, elimina publicación. EP-001, US-002-AC-06…08 quedan «fuera de esta versión por D-18», casos y supuestos no exigen bloqueo; US-003-AC-01 fija 1 servicio. EP-002, US-005 lista con navegación por mes, sin cuadrícula. EP-003, US-009/010 separan RN-05 opcional, US-011 cancela solicitudes. EP-004, US-014-AC-02/Reglas/Casos sitúan RN-04 en US-003. EP-005, US-017/018 usan G02 y no publicaciones. EP-006, US-019-AC-02 solo trata solicitudes. EP-007, US-023 título/AC-03 final, US-024-AC-01 «proponer y aceptar». Catálogo y cabeceras comparten requisitos-v1-revisado.
- Residuo comprobado: docs/risks/technical-risks.md, descripción «RT-01 · Complejidad…»: «La constitución establece que deben comprobarse… el límite de horas o la cobertura antes de aprobar cualquier intercambio». Su justificación conserva «son 6 reglas». En contraste, constitución v1.1/G02 y US-014-AC-02 establecen RN-02 Should y cobertura garantizada al preparar datos. El documento se presenta como revisión inicial de 29/09/2026; no distingue dentro de esa explicación el mandato antiguo del vigente.
- Observación/impacto: se corrigieron todos los restos operativos enumerados en v01; queda una explicación de riesgo anterior que puede inducir a valorar o probar el MVP como seis validadores obligatorios. La fecha y la precedencia resuelven la interpretación actual: MINOR, sin bloqueo independiente para las historias detalladas.
- Acción sugerida al TL/equipo: actualizar la descripción/justificación de RT-01 para referir G02/D-22, RN-04 inicial y RN-02/05 opcionales, o identificar expresamente ese fragmento como histórico. Conservar el riesgo y su mitigación; no cambiar probabilidad/impacto ni estimaciones sin decisión humana.
- Confianza HIGH: el residuo y las fuentes que lo sustituyen son explícitos. Bloqueo actual: no. No se editó el documento de riesgos durante este RECHECK.

### REQ-v01-003 — Mensajes de error NFR-005: RESOLVED

- Decisión: R-03 aceptada con cambios, D-22.
- Evidencia actual: non-functional-requirements.md, NFR-005 métrica y verificación, exige RN/motivo para rechazos de negocio; otros errores tienen motivo sin RN y credenciales genéricas. EP-001 US-002-AC-03 conserva «Usuario o contraseña incorrectos». EP-003 US-009-AC-03/06 explica indisponibilidad; AC-05 sí indica RN-03. EP-005 US-018-AC-02/03 y casos distinguen rechazo manual, regla incumplida y motivo manual vacío.
- Observación/impacto: el cuantificador anterior ya no obliga a inventar una RN para autenticación, reserva o entrada. La verificación central comprueba separadamente esas clases de errores.
- Acción sugerida: trasladar esas clases a evidencias de pruebas; no se afirma que estén implementadas. Confianza HIGH por textos concordantes y decisión trazada. Bloqueo actual: no.

### REQ-v01-004 — Caducidad Must independiente de US-015: RESOLVED

- Decisión: R-04 aceptada con cambios, D-22; caducidad al primer inicio y mínimo opcional de 48 h separados.
- Evidencia actual: EP-003 US-009-AC-08 y US-010-AC-05, EP-005 US-018-AC-07: «Con la hora del servidor», Caducada, liberación de ambos turnos y prohibición de aceptar/aprobar. US-009 exige actualizar detalle sin depender de abrir pantalla y consistencia ante repetición/concurrencia. US-018 comprueba el límite aunque el detalle se abriese antes; AC-03 comprueba caducidad antes de revalidar. EP-004 US-015-AC-03 reutiliza el contrato Must y añade solo antelación; business-rules.md, aplicación RN-05, coincide.
- Observación/impacto: los efectos esenciales ya están en Must; diferir US-015 no difiere caducidad ni liberación. Se especifica el resultado sin elegir un planificador técnico.
- Acción sugerida: Marcelino debe realizar la revisión técnica posterior encomendada y confirmar su encaje en las 8/3/8 h-p; las pruebas futuras deben cubrir el instante de inicio y peticiones repetidas/concurrentes. D-22 registra conformidad previa con las horas, que no acredita esa revisión posterior ni una implementación.
- Confianza HIGH: criterios explícitos y referenciados en las tres historias. Bloqueo de interpretación documental actual: no; revisión técnica/evidencia de ejecución pendientes.

### REQ-v01-005 — Referencias NFR: RESOLVED

- Decisión: R-05 aceptada, D-22.
- Evidencia actual: EP-001 US-003 Verificación añade NFR-003/008; EP-002 US-006 añade NFR-003/004/009. Catálogo NFR incluye US-003 en NFR-008 y US-006 en NFR-004/009. EP-004 US-012/013/014 sustituye el uso impropio de NFR-001 por «validación en servidor (constitución, principio 4)», conservando NFR-005/006.
- Observación/impacto: queda trazada la aplicación señalada en v01 y se distingue autorización por rol de validación RN. No se inventan endpoints de validadores ni requisitos adicionales.
- Acción sugerida: mantener esos IDs en pruebas/planes cuando se elaboren. Confianza HIGH por cotejo ficha/catálogo. Bloqueo actual: no.

### REQ-v01-006 — Protocolo NFR-006: RESOLVED

- Decisión: R-06 aceptada con cambios, D-22: mediana < 500 ms y p95 < 1 s, 30 validaciones con datos de demostración.
- Evidencia actual: non-functional-requirements.md, NFR-006 métrica/verificación y Notas, coincide con EP-004 US-012/013/014 y EP-005 US-018 Verificación. Se mide el motor completo de ambos cuadrantes en servidor, del inicio al resultado; se conservan las 30 duraciones y se documentan entorno/configuración y cálculo de mediana/p95 para repetir la comprobación.
- Observación/impacto: 500 ms ya no tiene una estadística incierta ni contradice el percentil. Las fichas remiten al protocolo central. Documentar el entorno usado permite comparar evidencias; no se afirma que exista una medición ni que el umbral se cumpla.
- Acción sugerida: QA debe aportar ese registro durante verificación. Confianza HIGH por criterio central y resúmenes alineados. Bloqueo actual: no.

## 6. Matriz de DoR

C01…C21 son etiquetas de este informe para los criterios reales, en su orden original; no modifican la DoR. Referencias: K = .specify/memory/constitution.md; G = specs/product/goals.md; B = specs/product/business-rules.md; C = specs/product/catalogo.md; N = specs/product/non-functional-requirements.md. P2 = EP-001/US-002; P9 = EP-003/US-009; P12/P13/P14 = EP-004/US-012/013/014; P18 = EP-005/US-018 (rutas completas en §2).

La matriz valora documentación y conserva US-013 como **Should diferida**. La evaluación de tamaño individual no aprueba carga conjunta ni reparto personal. En C20, la interpretación funcional queda aclarada, pero no se acredita que todos los pendientes de preparación para sprint estén resueltos.

| Criterio real de la DoR | US-002 Must | US-009 Must | US-012 Must | US-013 Should diferida | US-014 Must | US-018 Must |
|---|---|---|---|---|---|---|
| C01 — La historia tiene un identificador único y estable (US-XXX). | MET — P2, encabezado US-002; C §2. | MET — P9, encabezado US-009; C §2. | MET — P12, encabezado US-012; C §2. | MET — P13, encabezado US-013; C §2. | MET — P14, encabezado US-014; C §2. | MET — P18, encabezado US-018; C §2. |
| C02 — Está asociada a una épica (EP-XXX). | MET — P2 en EP-001. | MET — P9 en EP-003. | MET — P12 en EP-004. | MET — P13 en EP-004. | MET — P14 en EP-004. | MET — P18 en EP-005. |
| C03 — Está trazada al menos a un objetivo del producto (G01–G04). | MET — P2 Objetivo G04; K principio 5. | MET — P9 Objetivo G01/G02. | MET — P12 Objetivo G02/M02. | MET — P13 Objetivo G02/M02, Should. | MET — P14 Objetivo G02/M02. | MET — P18 Objetivo G03/M03 y G02. |
| C04 — El usuario o stakeholder está identificado (empleado, responsable, evaluador…). | MET — P2 enunciado: usuario con rol. | MET — P9 enunciado: empleado. | MET — P12 enunciado: responsable. | MET — P13 enunciado: responsable. | MET — P14 enunciado: responsable. | MET — P18 enunciado: responsable. |
| C05 — La capacidad esperada está descrita con claridad. | MET — P2 enunciado y AC-01…05/09: acceso identificado. | MET — P9 enunciado y AC-01: propuesta directa. | MET — P12 enunciado y AC: descanso/solapes. | MET — P13 enunciado y AC: jornada semanal. | MET — P14 enunciado y AC: RN-03 y cobertura inicial. | MET — P18 enunciado y AC: resolver y registrar resultado. |
| C06 — El valor o beneficio se entiende. | MET — P2 Necesidad: identidad y trazabilidad. | MET — P9 Necesidad: formalizar y validar acuerdo. | MET — P12 Necesidad: impedir descanso insuficiente. | MET — P13 Necesidad: detectar exceso de horas. | MET — P14 Necesidad: conservar personal mínimo. | MET — P18 Necesidad: decisión final trazable. |
| C07 — El alcance y los límites están claros (qué entra y qué no). | MET — P2 Límites/Supuestos; AC-06…08 fuera de versión. | MET — P9 Límites/Reglas: uno a uno, RN-05 opcional. | MET — P12 Límites/Reglas; G A-05 sin cambio de hora. | MET — P13 D-18/Plan: diferida; no extras/guardias. | MET — P14 AC-02/Reglas: RN-04 inicial, no por permuta. | MET — P18 Límites/Reglas: servicio propio, reglas G02, caducidad Must. |
| C08 — Tiene criterios de aceptación identificados (US-XXX-AC-01…). | MET — P2 AC-01…09; 06…08 conservados fuera de versión. | MET — P9 AC-01…08. | MET — P12 AC-01…04. | MET — P13 AC-01…03. | MET — P14 AC-01…02. | MET — P18 AC-01…07. |
| C09 — Los criterios son observables y verificables, incluidos los casos de error. | MET — P2 AC-03/05/09 y N NFR-005: errores genéricos/autorización. | MET — P9 AC-03/05/06/08: reservas, RN y caducidad. | MET — P12 AC-01…04/Casos límite: 12 h, datos ausentes, servidor. | MET — P13 AC/Casos: 40 h, domingo, dos semanas. | MET — P14 AC/Casos: incompatibilidad, 3/3/2 y preparación inicial. | MET — P18 AC-02/03/06/07: motivo, rechazo por RN, concurrencia y límite temporal. |
| C10 — Describen el comportamiento esperado, no una implementación concreta. | MET — P2 AC describen sesión, permisos e invalidación. | MET — P9 AC describen propuesta, acceso, reservas y estados. | MET — P12 AC describen comprobación y rechazo, sin algoritmo. | MET — P13 AC describen límite/reparto semanal, sin algoritmo. | MET — P14 AC describen compatibilidad/conservación de cobertura. | MET — P18 AC describen resultado indivisible, sin elegir mecanismo técnico. |
| C11 — Si afecta a un intercambio o a su validación, indica qué reglas de negocio (RN-01–RN-06) aplica y sus precondiciones. | NOT_APPLICABLE — P2 trata acceso; no intercambio ni validación RN. | MET — P9 Reglas/AC-05/08: RN-03, G02 y caducidad; RN-05 condicional. | MET — P12 Reglas/AC-03: RN-01/06, vecinos y ambos empleados. | MET — P13 Reglas/AC: RN-02, semanas y ambos empleados, si se incorpora. | MET — P14 Reglas/AC-02: RN-03; RN-04 precondición de US-003. | MET — P18 Reglas/AC-03/07: RN-01/03/06, RN-04 inicial, Should condicionales. |
| C12 — Tiene prioridad MoSCoW asignada y justificada. | MET — P2 Prioridad Must: identidad y RT-03. | MET — P9 Prioridad Must: núcleo del producto. | MET — P12 Prioridad Must: regla central y RT-01. | MET — P13 Prioridad Should: D-18; K/G permiten diferirla. | MET — P14 Prioridad Must: compatibilidad y cobertura. | MET — P18 Prioridad Must: cierre del flujo y RT-02. |
| C13 — Tiene una estimación consensuada en horas-persona. | MET — P2 Estimación/C §2: 3 h-p votadas tras D-18. | MET — P9 Estimación/C §2: 8 h-p consensuadas. | MET — P12 Estimación/C §2: 5 h-p tras D-18. | MET — P13 Estimación/C §2: 3 h-p tras D-18. | MET — P14 Estimación/C §2: 3 h-p tras D-18. | MET — P18 Estimación/C §2: 8 h-p; US-017 absorbida. |
| C14 — Tiene indicada la incertidumbre (Baja / Media / Alta). | MET — P2 Incertidumbre: Media. | MET — P9 Incertidumbre: Media. | MET — P12 Incertidumbre: Alta. | MET — P13 Incertidumbre: Alta. | MET — P14 Incertidumbre: Media. | MET — P18 Incertidumbre: Alta. |
| C15 — Sus predecesoras y dependencias (funcionales, técnicas y externas) son conocidas y no bloquean el sprint. | NOT_ASSESSABLE — P2 conoce US-001/003; C §6 tecnología y §4 reparto pendientes; terminación no revisada. | NOT_ASSESSABLE — P9 conoce US-006/003; C D-21 mantiene replanificación; disponibilidad no acreditada. | NOT_ASSESSABLE — P12 conoce US-003/contrato US-009; no se acredita disponibilidad/acuerdo técnico. | NOT_ASSESSABLE — P13 conoce US-003/012 y contrato US-009; Should sin sprint comprometido. | NOT_ASSESSABLE — P14 conoce US-003/012 y contrato US-009; no se acredita disponibilidad/reparto. | NOT_ASSESSABLE — P18 conoce US-010/012/014; C §4/§6 provisional; predecesoras no verificadas. |
| C16 — Cabe en un sprint; si no cabe, se divide. | MET — C §4: 3 h-p ≤ 6,78 h; carga conjunta IT-002 pendiente. | MET — C §4/§6: 8 h-p ≤ 9,33 h de equipo; reparto individual pendiente. | MET — C §4: 5 h-p ≤ 12,73 h de IT-003. | NOT_ASSESSABLE — P13: 3 h-p; Should sin sprint elegido para comparar carga. | MET — C §4: 3 h-p ≤ 9,33 h de IT-005. | MET — C §4/§6: 8 h-p ≤ 9,33 h; carga conjunta IT-006 pendiente. |
| C17 — Se han identificado los requisitos no funcionales que le aplican (NFR-XXX). | MET — P2 Verificación: NFR-001/002/004/005/009; NFR-003 en Restricción. | MET — P9 Verificación: NFR-001/004/005/007/009; privacidad común. | MET — P12 Verificación: NFR-005/006; servidor referido a K principio 4. | MET — P13 Supuestos: NFR-005/006; servidor referido a K principio 4. | MET — P14 Supuestos: NFR-005/006; servidor referido a K principio 4. | MET — P18 Verificación: NFR-001/004/005/006/007/009. |
| C18 — Se conocen las restricciones técnicas, organizativas o de proyecto relevantes. | MET — P2 Límites/Verificación: cuentas ficticias, roles, hashing, sin registro/recuperación. | MET — P9 Límites/Supuestos: uno a uno, sin contraofertas, reserva única. | MET — P12 Supuestos/Casos: horarios fijos, datos necesarios; G A-05/B zona horaria. | MET — P13 Supuestos/Reglas: solo turnos, semanas Europe/Madrid; G A-05. | MET — P14 Supuestos/AC-02: cuadrante inicial válido y permuta compatible. | MET — P18 Verificación/Supuestos: responsable por servicio, atomicidad, dos pestañas. |
| C19 — Solo utiliza datos ficticios o sintéticos y cumple las restricciones de privacidad (principio 5 de la constitución). | MET — P2 Restricción NFR-003 y límites comunes EP-001; sin inspección de datos. | MET — P9 aplicación común datos ficticios; AC-02 privacidad de participantes. | MET — P12 aplicación común ficticia; límites sin convenios reales. | MET — P13 aplicación común ficticia; límite interno de jornada. | MET — P14 aplicación común ficticia; US-003 como precondición. | MET — P18 aplicación común ficticia; NFR-001 acceso por servicio. |
| C20 — No hay preguntas sin resolver que impidan entender o planificar la historia. | NOT_ASSESSABLE — D-22 resuelve interpretación; tecnología y reparto para sprint siguen pendientes (C §4/§6). | NOT_ASSESSABLE — D-22/D-23 resuelven flujo; replanificación y revisión técnica posterior R-04 pendientes. | NOT_ASSESSABLE — reglas claras; disponibilidad del contrato/predecesoras para sprint no acreditada. | NOT_ASSESSABLE — D-18/D-22 aclaran Should; incorporación y planificación no decididas. | NOT_ASSESSABLE — D-22 aclara cobertura; contrato y planificación efectiva no acreditados. | NOT_ASSESSABLE — D-22/D-23 aclaran resultado; reparto y revisión técnica posterior R-04 pendientes. |
| C21 — Cualquier supuesto importante o duda no bloqueante está documentado en la ficha. | MET — P2 Supuestos: responsable único, sin bloqueo ni recuperación. | MET — P9 Supuestos/Estados: reserva única, liberación y sin contraoferta. | MET — P12 Supuestos/Casos: horarios fijos; distingue turno inexistente de datos ausentes. | MET — P13 Supuestos: horas efectivas/semanas locales; G A-05 limita demostración. | MET — P14 Supuestos: cuadrante inicial 3/3/2; datos completos para validar. | MET — P18 Supuestos/Casos: datos originales, historial básico, un responsable/dos pestañas. |

Balance de las 126 celdas: **112 MET, 1 NOT_APPLICABLE y 13 NOT_ASSESSABLE**. No se identificó NOT_MET de interpretación documental en la muestra actual. C15/C20 y C16 de US-013 siguen sin evidencia suficiente de preparación efectiva. Ninguna combinación de MET sustituye la sesión humana de refinamiento o declara Ready.

## 7. Candidatos, stakeholders y alcance excluido

Las preguntas candidatas del v01 no tenían IDs REQ propios; se preserva su referencia §7 y su registro humano R-07…09. No se crean nuevas historias ni decisiones.

| Candidato del v01 | Decisión y evidencia actual | Resultado / límite |
|---|---|---|
| IN_SCOPE_CANDIDATE — US-006 sin turnos compatibles, R-07 | D-23; EP-002 US-006-AC-03: consulta correcta sin turnos muestra mensaje de lista vacía; fallo muestra motivo y no se presenta como vacío. | RESOLVED. Precisa el flujo G01 existente sin restaurar US-008 ni añadir filtros. |
| IN_SCOPE_CANDIDATE — M03 si se difiere US-024, R-08 | D-23; goals.md M03, resultado EP-005/EP-007, US-018 Verificación y US-024 Prioridad/AC-03: M03 pendiente de validación si no se realiza US-024, igual que M01. | RESOLVED por condición humana explícita. Se conservan tres decisiones, cada una < 1 min; no se promete evidencia alternativa ni se declara la métrica superada. |
| SCOPE_UNCLEAR — revalidación fallida US-018, R-09 | D-23; US-018-AC-03: si sigue Aceptada y no caducó, regla incumplida produce Rechazada con RN/motivo, libera reservas y no permuta; actualización indivisible. US-009 Estados/AC-07 y business-rules Aplicación conservan ese detalle. | RESOLVED. «Por regla» es motivo del estado Rechazada, no un estado global nuevo. El rechazo manual exige texto; el rechazo por regla registra explicación del servidor. |
| OUT_OF_SCOPE — cambio de hora para demostración | G A-05/D-18; ejemplo futuro en US-013 Should. | Sigue excluido del dataset MVP; no exige implementar esa mejora para cerrar el flujo Must. |
| OUT_OF_SCOPE — RR. HH. real, generación automática, notificaciones externas y móvil nativo | G EX-02/03/04/05. | No se recomiendan como omisiones necesarias. |

Se revisaron empleado, responsable, evaluador y participantes opcionales de US-024; no se confirmó otro stakeholder necesario. Las mejoras US-011/013/015/016/019/020/024 mantienen Should. US-007/008/022 quedan fuera de versión, US-017 fusionada y US-004/021 Could. El estado/historial básico sigue disponible sin las vistas ampliadas de EP-006.

## 8. Dependencias, supuestos y trazabilidad

- **Predecesoras:** C §2/§3 y fichas mantienen la cadena Must US-001 → US-003 → US-002 → US-005 → US-006 → US-009 → US-010 → US-018 → US-023; validadores US-012/014 alimentan US-018. No se observó ciclo en el grafo Must. Una dependencia explícita no obliga por sí sola a dividir una historia.
- **Contrato compartido:** US-012/013/014/015 acuerdan formato de solicitud con US-009 sin exigir esa historia terminada. No se encontró constancia de esquema/acuerdo técnico ya cerrado en C §2/§6 ni Predecesoras/Supuestos de esas fichas; no se afirma que no exista en otra ubicación. C15 queda NOT_ASSESSABLE, sin inventar una dependencia circular.
- **Externas:** autorización de tecnologías para US-001 está pendiente en C §6; evaluador para US-023; tres participantes solo si se incorpora US-024. No se verificó disponibilidad efectiva.
- **Secuenciación:** asignaciones iniciales y preferencia por riesgo no sustituyen predecesoras funcionales/técnicas; el plan D-21 sigue provisional. No se revisan ni modifican planes/TK.
- **Desacoplamiento:** US-009/010/018 incluyen estado y registro básicos; US-017 absorbida no añade esfuerzo separado; US-019/020 amplían presentación. Caducidad Must ya no depende de US-015 y las métricas M01/M03 no convierten US-024 en requisito Must.

C §4 conserva IT-002: 9 h-p frente a 6,78 h, e IT-006: 10 h-p frente a 9,33 h; total Must 46 h-p frente a 57,65 h. Son desequilibrios ya reconocidos por D-21. SM/TL deben redistribuir, respetar capacidades personales y preparar tareas. C §6 recoge que US-009/018 de 8 h-p caben individualmente en un sprint de equipo de 9,33 h; no prueba que el reparto esté aprobado ni que se haya revisado técnicamente la nueva caducidad. Se conservan 24 IDs, prioridades y consensos; el agente no genera estimaciones.

| Supuesto / restricción | Resultado documental |
|---|---|
| G A-01 y B RN-01…06 | Las seis reglas quedan definidas; G02/K/D-22 delimitan cuáles se validan en MVP. Definición no equivale a seis validadores obligatorios. |
| G A-02 y P18 Supuestos | Un responsable por servicio; dos pestañas hacen relevante RT-02. No se añade otro aprobador. |
| G A-03, NFR-009 y US-006 | Navegadores modernos y compatibilidad trazada; implementación no comprobada. |
| G A-04 y C D-21 | Capacidad/ausencias/reparto referenciados, sin verificar cálculos externos ni asignaciones. |
| G A-05 y B zona horaria | Demo sin cambio de hora; fechas/semanas locales Europe/Madrid y límites temporales mantienen su interpretación. |
| P14 / US-003 | Cuadrante inicial 3/3/2; permuta uno a uno compatible conserva cobertura. Dataset efectivo no inspeccionado. |
| NFR-003 / K principio 5 | Datos ficticios exigidos en todas las épicas; no se auditó repositorio, base de datos o logs. |

Las hipótesis sobre motor de base de datos, ORM, planificador de caducidad, alojamiento o algoritmo de reserva son **UNCONFIRMED**. Las fuentes exigen atomicidad/concurrencia como resultados; no eligen aquí una implementación. No se confirma una dependencia técnica sin evidencia.

La trazabilidad necesidad → objetivos → épicas → historias → AC/RN/NFR y decisiones D-22/D-23 es inspeccionable en las fuentes leídas. El enlace hasta plan, tareas, código y pruebas queda fuera de alcance. Los commits citados en Uso de agentes identifican la aplicación; este informe comprueba además el texto actual. RT-01 conserva el residuo descrito en REQ-v01-002.

## 9. Preguntas y actuaciones humanas pendientes

1. **TL/equipo — REQ-v01-002:** ¿se actualiza la explicación de RT-01 a G02/D-22 o se identifica expresamente como histórico el mandato constitucional anterior? Es precisión no bloqueante; la revisión no cambia su valoración de riesgo.
2. **Marcelino (TL) — seguimiento R-04:** revisar técnicamente US-009-AC-08, US-010-AC-05 y US-018-AC-07 y confirmar el encaje en 8/3/8 h-p, como se ha encargado. El criterio documental queda claro; no se inventa su confirmación posterior.
3. **SM/TL — D-21 y C15/C20:** aportar redistribución de IT-002/IT-006, reparto por persona, confirmación tecnológica y estado/acuerdo de predecesoras y contrato de validadores antes del compromiso de sprint. Son pendientes conocidos; no bloqueos de interpretación nuevos.
4. **QA, durante implementación:** aportar evidencias de NFR-005/006/007 y caducidad; para rendimiento, registrar las 30 duraciones, entorno y cálculo acordado. M01/M03 se validarán solo si se ejecuta US-024; si no, siguen pendientes conforme a D-23.

Las tres preguntas candidatas iniciales ya están respondidas y no se reabren. No se exige respuesta interactiva para persistir este informe consultivo; tampoco se afirma que esos pendientes estén completados.

## 10. Crosswalk RECHECK

| Referencia anterior | Registro / decisión humana | Evidencia revisada actual | Estado y motivo |
|---|---|---|---|
| REQ-v01-001 | R-01; aceptada con cambios, D-22 | K v1.1 principio 4/historial; DoD v1.1; G02/M02; P14/P18 Reglas | RESOLVED: modificación de gobierno explícita y alcance coincidente. |
| REQ-v01-002 | R-02; aceptada, D-22/D-18 | Misión; P2/US-003; US-005/006; P9/US-010/011; P14; US-017/P18; US-019; US-023/024; C línea base; RT-01 | PARTIALLY_RESOLVED: restos operativos corregidos; explicación constitucional anterior en riesgos aún visible como se detalla en §5. No bloqueante. |
| REQ-v01-003 | R-03; aceptada con cambios, D-22 | NFR-005 métrica/verificación; P2-AC-03; P9-AC-03/05/06; P18-AC-02/03 | RESOLVED: RN/motivo en negocio, otros errores sin RN y credenciales genéricas. |
| REQ-v01-004 | R-04; aceptada con cambios, D-22 | P9-AC-08; US-010-AC-05; P18-AC-07/03; US-015-AC-03; B Aplicación | RESOLVED documentalmente: caducidad y liberación en Must; revisión técnica posterior pendiente, no atribuida al TL. |
| REQ-v01-005 | R-05; aceptada, D-22 | US-003/006 NFR; NFR-004/008/009 listas; P12/P13/P14 referencias | RESOLVED: IDs sincronizados y autorización separada de validación RN. |
| REQ-v01-006 | R-06; aceptada con cambios, D-22 | NFR-006 métrica/verificación/Notas; P12/P13/P14/P18 Verificación | RESOLVED como protocolo: mediana/p95/30, alcance temporal y registro de condiciones; sin mediciones efectuadas. |
| v01 §7, US-006, IN_SCOPE_CANDIDATE | R-07; aceptada por PO, D-23 | US-006-AC-03 | RESOLVED: vacío explícito distinto de fallo de consulta. |
| v01 §7, M03/US-024, IN_SCOPE_CANDIDATE | R-08; aceptada por PO, D-23 | G M03; EP-005/007; P18 métrica; US-024-AC-03 | RESOLVED: pendiente sin US-024; umbral y prioridad conservados. |
| v01 §7, US-018, SCOPE_UNCLEAR | R-09; aceptada por PO, D-23 | P18-AC-03; P9 Estados/AC-07; B Aplicación | RESOLVED: Rechazada por regla, RN/motivo, liberación sin permuta, efecto indivisible. |

Resumen de hallazgos formales v01: **5 RESOLVED y 1 PARTIALLY_RESOLVED**; los tres candidatos adicionales están **RESOLVED**. Ningún hallazgo previo se declara JUSTIFIABLY_REJECTED o DEFERRED por la sola aceptación de una propuesta. El informe v01 se conserva sin cambios; los estados RECHECK son valoración del revisor y no reemplazan decisiones humanas.

## 11. Cierre explícito

Durante esta ejecución AG-01 las fuentes y registros humanos fueron de solo lectura. Se creó únicamente este informe nuevo; no se ejecutaron comandos, pruebas o instalaciones, no se editaron requisitos, estimaciones, prioridades o planes y no se aprobó una línea base o puerta de calidad. Las actuaciones de documentación anteriores al snapshot y la publicación posterior son distintas de la revisión consultiva.

"This is an advisory review. No source requirement, priority, estimate, plan or human decision was changed. No baseline or gate was approved."
