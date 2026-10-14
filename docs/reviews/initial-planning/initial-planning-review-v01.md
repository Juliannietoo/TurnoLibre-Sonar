# Initial planning review v01

## 1. Metadatos de ejecución

- Proyecto: TurnoLibre (empresa ficticia MedSwap; cliente ficticio Hospital Comarcal Vega Alta).
- Agente: AG-03, Planning Agent (*initial-planning-reviewer*). Contrato: `.github/agents/initial-planning-reviewer.agent.md` (adaptación D-20, 07/10/2026), leído íntegramente.
- Modo: **CONSISTENCY**, a petición del equipo, que aporta una hipótesis de planificación humana ya construida.
- Commit revisado: **45d6b38** (rama `main`, repositorio `C:\GPS_GC02`). Se consideran los ficheros en disco como ese commit. Wiki: clon local `C:\GPS_GC02_wiki` (solo `Registro-de-decisiones.md` y `Uso-de-agentes.md`); no se ha indicado el commit de la Wiki.
- Libro de planificación: `docs/planning/TurnoLibre_H3_planificacion.xlsx`. La herramienta no puede leer ficheros .xlsx. **Se ha revisado el extracto** `docs/planning/extracts/TurnoLibre_H3_extracto-v1.md` (versión 1, 14/10/2026), que declara contener los mismos datos y los valores calculados por las fórmulas. No se ha podido comprobar que el extracto coincida con el libro ni revisar sus fórmulas.
- Alcance revisado: las 11 historias Must del catálogo V1 tras D-18 (US-001, 002, 003, 005, 006, 009, 010, 012, 014, 018 y 023; 46 h-p), en un horizonte de 6 iteraciones (IT-001 a IT-006, del 21/10/2026 al 01/12/2026, 3 releases; D-19), con 4 personas a 6 h/semana (D-21). Should, Could y Won't sin compromiso.
- Versiones de las fuentes: catálogo y fichas `requisitos-v1-revisado` (revisión 13/10/2026); constitución v1.1 (13/10/2026); DoD v1.1; DoR v1.0; NFR v1.1; reglas de negocio v0.2 con nota D-18; riesgos técnicos con RT-01 actualizado el 14/10/2026; `capacity.md` y `company.md` según D-21; revisiones de requisitos v01 (INITIAL) y v02 (RECHECK, NO_BLOCKING_FINDINGS_IN_REVIEWED_SCOPE).
- Decisiones humanas de referencia: D-18, D-19, D-21, D-22 y D-23 (Registro de decisiones de la Wiki); decisiones de planificación de SM y TL del 14/10/2026 según la cabecera del extracto.
- Versión del informe: v01 (primer informe de este directorio; no es un RECHECK).
- Fecha: 14/10/2026.
- Herramienta: Claude Code (subagente initial-planning-reviewer). Modelo: claude-opus-5-5.
- Idioma: español (es-ES); los IDs, estados y severidades se mantienen como en el contrato.

## 2. Resumen

**Resultado consultivo: READY_WITH_NON_BLOCKING_QUESTIONS.**
**Hallazgos bloqueantes: 0.** Hay 14 hallazgos: 5 MAJOR y 9 MINOR, ninguno bloqueante.

Conclusión principal: en el extracto, la hipótesis humana es aritméticamente coherente con las fuentes. Coinciden la capacidad por persona e iteración (57,65 h), el alcance Must (46 h-p) con las estimaciones tras D-18, el coste (923,25 € de horas asignadas dentro de un personal presupuestado de 2.889,00 €) y el precio (5.307,88 € con IVA). Ninguna persona supera su capacidad efectiva en ninguna iteración y no queda trabajo Must sin asignar. Las dudas no impiden revisar la hipótesis, pero conviene resolverlas antes de comprometer cada sprint. Afectan a la secuencia de dependencias (US-023 empieza antes de que termine US-018), a una historia Must repartida entre dos sprints (US-018), a dos dependencias externas sin confirmar (tecnologías autorizadas y evaluador externo), a la falta de iteraciones de holgura en la cadena crítica y a una discrepancia sobre las horas de reunión entre el Team Charter y `capacity.md`.

Este resultado indica si las entradas permiten revisar y usar la hipótesis. **No es una aprobación del plan ni demuestra que el calendario sea viable.**

## 3. Inventario de evidencias y matriz de compatibilidad

| Dimensión | Estado | Evidencia | Límite |
|---|---|---|---|
| Alcance y prioridades | COMPATIBLE | Extracto §2 frente a `catalogo.md` §2 y tabla D-18: 11 Must = 46 h-p; MoSCoW e incertidumbre iguales en las 24 filas; US-017 fusionada; US-007/008/022 fuera de versión. | La tabla de plan del catálogo (§4 y columna Plan) y el «Plan inicial» de las fichas no se han actualizado (IPR-v01-007). |
| Madurez de requisitos / DoR | PARCIAL | Las 11 Must tienen ID, épica, objetivo, criterios de aceptación, MoSCoW, estimación, incertidumbre y NFR en sus fichas; v02 de requisitos sin bloqueos. | DoR C15/C20 (dependencias que no bloqueen; preguntas abiertas) siguen sin evidencia para US-001, US-023 y el contrato de validadores (IPR-v01-003, 004, 013). Ninguna historia se declara Ready. |
| Cobertura y unidades de las estimaciones | COMPATIBLE | La suma de horas asignadas por historia coincide con sus h-p (§5.2). Las unidades son horas-persona frente a horas por persona y sprint. | IT-002 a IT-006 se reparten por historia, no por tareas. |
| Capacidad efectiva | COMPATIBLE CON DUDA | Recalculada con la fórmula del equipo: 57,65 h, igual que `capacity.md`. | Discrepancia de redondeo de presentación (IPR-v01-006). El Team Charter fija una sesión de 2 h frente a 1 h de eventos en `capacity.md` (IPR-v01-005). |
| Horizonte y duración | COMPATIBLE | 21/10/2026 (miércoles) – 01/12/2026 (martes), 6 iteraciones de una semana y 3 releases de 2 iteraciones (D-19). | La cadena Must ocupa las 6 iteraciones sin ninguna iteración de holgura (IPR-v01-003). |
| Dependencias y capacidades | PARCIAL | Las predecesoras del extracto coinciden con el catálogo. El libro informa de 0 incumplimientos con su propia regla. | Inicio de US-023 antes de que termine US-018. La secuencia dentro del sprint no es visible. Las capacidades técnicas de cada persona no están documentadas (IPR-v01-001, 012). |
| Coste | COMPATIBLE | Tarifas de `company.md`; coste por persona e iteración recalculado; desglose de presupuesto recalculado (§7). | El coste planificado de las 46 h es una parte del personal nominal pagado (144 h), no un coste adicional. |
| Supuestos e incertidumbre | PARCIAL | Pendientes declarados en el extracto §6; RT-01 a RT-03 abiertos; M01/M03 quedarán pendientes de validación sin US-024 (D-23). | Dos dependencias externas sin confirmar (IPR-v01-003, 004). La revisión técnica de la caducidad (R-04) sigue pendiente (IPR-v01-013). |
| Planificación y viabilidad | COMPATIBLE A NIVEL AGREGADO | 0 sobreasignaciones persona × iteración; las 46 h están asignadas; la holgura del equipo es de 11,65 h. | La viabilidad temporal dentro de cada sprint y la de las tareas futuras quedan para el equipo; hay holguras individuales mínimas (IPR-v01-014). |

## 4. Hallazgos

### IPR-v01-001 · Dependencias · MAJOR · Bloqueante: NO

- **Fuente/ID:** extracto §2, §3 y §4 (regla del libro); `catalogo.md` §2 y §3 (US-023 depende funcionalmente de US-018); EP-007 US-023 (dependencias y AC-02/AC-03).
- **Evidencia observada:** la parte 1 de US-023 («guion de instalación con las cuentas de prueba», 1,50 h de QA) está en IT-005, pero US-018, su predecesora funcional, termina en IT-006. El libro usa la regla «cada predecesora empieza y termina en la misma iteración o antes» e informa de 0 incumplimientos. Además, hay dependencias resueltas dentro de la misma iteración sin secuencia visible: US-002 → US-005 (funcional, IT-002), US-012 → US-014 (técnica, IT-003) y US-010 → US-018 parte 1 (IT-005).
- **Impacto:** la regla no detecta que un sucesor empiece antes de que termine su predecesor, que es lo que exige una dependencia funcional. US-023-AC-02 exige incluir en el guion el flujo de la versión final, incluida la resolución de solicitudes. En sprints de una semana con 1–3 h por persona, una dependencia dentro del mismo sprint obliga a encadenar tareas que el libro no muestra.
- **Acción recomendada:** confirmar si la parte 1 de US-023 solo necesita US-001/US-003 (instalación y cuentas) y la parte que depende de US-018 está en IT-006. Si es así, registrarlo. Revisar la regla del libro para que compare el fin de la predecesora con el inicio del sucesor y mostrar la secuencia dentro del sprint de las dependencias en la misma iteración.
- **Pregunta o decisión:** ¿La parte 1 de US-023 depende de US-018? ¿Se acepta empezar US-023 antes de que termine US-018 y con qué justificación?
- **Rol propuesto:** SM y TL (con el PO para el alcance de US-023).

### IPR-v01-002 · Tamaño y DoR · MAJOR · Bloqueante: NO

- **Fuente/ID:** extracto, cabecera y §3 (US-018 parte 1 en IT-005 y parte 2 en IT-006; US-023 repartida 1,5 + 0,5 h); DoR, Planificación («Cabe en un sprint; si no cabe, se divide»); `catalogo.md` §6, decisión del TL (US-009/US-018 caben en un sprint de equipo y se descomponen en tareas, sin dividir la historia).
- **Evidencia observada:** US-018 (Must, incertidumbre Alta, 8 h-p) se ejecuta en dos sprints sin dividirse en historias. El diseño de la transacción (1,50 h, TL) se adelanta a IT-005 por decisión de SM y TL del 14/10. US-023 (2 h-p) también se reparte entre dos sprints.
- **Impacto:** la parte de IT-005 no puede cumplir la DoD ni formar un incremento por sí sola. La historia arrastra trabajo entre sprints. Con una sola historia en dos sprints es más difícil comprobar la DoR («cabe en un sprint») y seguir la DoD. La decisión se aparta de la del TL en el catálogo §6. Es una contrapartida que decide el equipo: adelantar el diseño reduce el riesgo RT-02 a cambio de que la historia no cierre dentro de un sprint.
- **Acción recomendada:** registrar de forma explícita cómo se trata ese trabajo adelantado (por ejemplo, como tarea preparatoria de US-018 aceptada a sabiendas o como otra forma que decida el equipo) y cómo se informa en la review de IT-005. El agente no elige la opción.
- **Pregunta o decisión:** ¿Acepta el equipo que US-018 y US-023 abarquen dos sprints, en contra de la regla de tamaño de la DoR y de la decisión anterior del TL? ¿Dónde queda registrado?
- **Rol propuesto:** TL y SM, con conformidad del PO.

### IPR-v01-003 · Dependencia externa y horizonte · MAJOR · Bloqueante: NO

- **Fuente/ID:** extracto, cabecera y §6 (TK-001 condicionada); `catalogo.md` §2, §3 y §6 (US-001: dependencia externa de las tecnologías autorizadas); `goals.md`, Restricciones («se definirán más adelante»); DoR C15.
- **Evidencia observada:** la confirmación de las tecnologías autorizadas sigue pendiente. US-001 es la raíz del grafo y está en IT-001, que empieza el 21/10/2026, dentro de 7 días. La cadena crítica Must (US-001 → US-003 → US-002 → US-005 → US-006 → US-009 → US-010 → US-018 → US-023) ocupa IT-001 a IT-006 sin ninguna iteración libre.
- **Impacto:** mientras falte la confirmación, US-001 no cumple el criterio de la DoR «dependencias … no bloquean el sprint». Cualquier retraso de US-001 se propaga a toda la cadena. Las 11,65 h de holgura son horas, no semanas de calendario, y no compensan un retraso de la cadena.
- **Acción recomendada:** obtener y registrar la confirmación antes del Sprint Planning de IT-001. Si no llega, que el equipo decida de antemano qué partes de US-001 pueden avanzar y cómo se trata el riesgo de calendario.
- **Pregunta o decisión:** ¿Quién solicita la confirmación al profesorado y en qué fecha? ¿Qué decide el equipo si no se ha recibido el 21/10?
- **Rol propuesto:** TL (dependencia técnica), con seguimiento de la SM.

### IPR-v01-004 · Dependencia externa y calendario final · MAJOR · Bloqueante: NO

- **Fuente/ID:** extracto §3 (US-023 parte 2, 0,50 h de QA, IT-006) y §6; EP-007 US-023-AC-01/AC-03; `goals.md` M04 y G04; NFR-008.
- **Evidencia observada:** la persona evaluadora externa no está identificada. La validación de M04 está prevista en IT-006 (25/11–01/12), la misma semana en que termina US-018, de la que depende. En esa semana también vence la entrega de la práctica 4 de GPS (27/11, `capacity.md`). La holgura de QA en IT-006 es de 0,05 h.
- **Impacto:** G04 y M04 dependen de una persona ajena al equipo y de que US-018 esté terminada en esa misma semana. Si cualquiera de las dos cosas falla, la Must US-023 no puede cerrarse dentro del horizonte.
- **Acción recomendada:** identificar a la persona evaluadora, confirmar su disponibilidad en una fecha concreta de IT-006 posterior al cierre previsto de US-018 y registrarlo antes de planificar IT-005.
- **Pregunta o decisión:** ¿Quién es la persona evaluadora? ¿Qué día de IT-006 puede hacer la evaluación? ¿Qué ocurre con la release R3 si no está disponible?
- **Rol propuesto:** PO (stakeholders y M04) y QA (ejecución del guion).

### IPR-v01-005 · Capacidad (conflicto de fuentes) · MAJOR · Bloqueante: NO

- **Fuente/ID:** `team-charter.md`, acuerdos 4 y 5 (planning, review y retrospectiva en la sesión presencial del miércoles de 17:30 a 19:30, más 2 dailies de 15 min); `capacity.md` («Las reuniones incluyen una hora de planning/review/retrospectiva y dos dailies de 15 minutos», 1,5 h/semana); D-08, D-09 y D-21.
- **Evidencia observada:** el Team Charter reserva una sesión semanal de 2 h para los eventos, mientras que `capacity.md` y el extracto descuentan 1 h de eventos más 0,5 h de dailies. Ninguna fuente aclara si la segunda hora de la sesión es tiempo de trabajo incluido en las 6 h.
- **Impacto:** la diferencia es de 1 h por persona y semana (24 h nominales en el horizonte). Solo para indicar la magnitud del conflicto, y no como escenario alternativo: si esa hora se descontara como reunión, la fórmula y los márgenes declarados darían 6 × (0,80 + 0,90 + 0,85 + 0,85) = 20,40 h efectivas menos. Esa cifra supera la holgura de 11,65 h y haría que las asignaciones actuales superasen la capacidad. Se marca como no bloqueante porque la fuente más reciente y específica (D-21, `capacity.md`) fija 1,5 h de forma explícita y la cifra coincide con D-08.
- **Acción recomendada:** confirmar y registrar cuánto dura cada evento dentro de la sesión del miércoles y si el resto de la sesión es trabajo productivo incluido en las 6 h. Alinear el Team Charter o `capacity.md` según lo que se decida.
- **Pregunta o decisión:** ¿La sesión de 17:30 a 19:30 consume 1 h o 2 h de reuniones por persona y semana?
- **Rol propuesto:** SM.

### IPR-v01-006 · Aritmética (redondeo de presentación) · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto §1 y §4; `capacity.md` (tabla por sprint); `catalogo.md` §4.
- **Evidencia observada:** la capacidad exacta del TL en IT-002 a IT-006 es (6 − 1 − 1,5 − 1) × 0,85 = 2,125 h. El extracto muestra 2,12 y `capacity.md`, 2,13. Ocurre lo mismo con el equipo en IT-003 (12,725 h: 12,72 frente a 12,73) y en IT-004 a IT-006 (9,325 h: 9,32 frente a 9,33). En el coste, 23,625 € aparece como 23,62 y 39,375 € como 39,38. Los totales (57,65 h, 923,25 €) son exactos en ambas fuentes.
- **Impacto:** no cambia ninguna comprobación; solo produce cifras distintas entre documentos.
- **Acción recomendada:** usar un criterio de redondeo único para presentar las cifras o indicar en el libro que los valores se calculan sin redondear.
- **Pregunta o decisión:** ninguna de alcance.
- **Rol propuesto:** SM.

### IPR-v01-007 · Versiones de fuentes · MINOR · Bloqueante: NO

- **Fuente/ID:** `catalogo.md` §2 (columna Plan), §4 (plan provisional D-21) y §6; «Plan inicial» de EP-002 US-006 (IT-002), EP-003/005/007 («por replanificar»); extracto §2.
- **Evidencia observada:** el extracto pone US-006 en IT-003, US-014 en IT-003, US-018 en IT-005 e IT-006 y US-023 en IT-005 e IT-006. El catálogo y las fichas mantienen el plan provisional de D-21 (US-006 en IT-002, US-014 en IT-005, US-018 y US-023 en IT-006) y señalan IT-002 e IT-006 como sobrecargados.
- **Impacto:** hay dos planes en las fuentes. El agente no decide cuál prevalece. El catálogo deja el plan de H3 a cargo de SM y TL, pero ese plan todavía no está reflejado.
- **Acción recomendada:** cuando el equipo acepte la hipótesis, actualizar la columna Plan, el §4 y el §6 del catálogo y el «Plan inicial» de las fichas, o enlazar el libro como fuente vigente del plan.
- **Pregunta o decisión:** ¿Qué artefacto es la fuente vigente del plan por iteración?
- **Rol propuesto:** SM (con revisión del alcance por el PO).

### IPR-v01-008 · Trazabilidad de decisiones · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto, cabecera («Decisiones de planificación SM/TL (14/10/2026)»); Wiki, Registro de decisiones (última entrada: D-23); Team Charter, acuerdo 11; constitución, Standards.
- **Evidencia observada:** las cuatro decisiones de planificación (dividir US-023, adelantar el diseño de US-018, no comprometer US-011 y condicionar TK-001) solo aparecen en la cabecera del extracto.
- **Impacto:** se pierde la trazabilidad de decisiones relevantes, que además se apartan de la decisión anterior del TL en el catálogo §6 (IPR-v01-002).
- **Acción recomendada:** registrarlas en la Wiki con fecha, autor, motivo y artefactos afectados. El agente no les asigna ningún ID.
- **Pregunta o decisión:** ¿Se registran como decisión formal en el Registro de decisiones?
- **Rol propuesto:** SM.

### IPR-v01-009 · Coherencia tarea–criterio · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto §3, TK-007 («Comprobar que el cuadrante cumple RN-01, RN-03, RN-04 y RN-06»); EP-001 US-003-AC-02 (el cuadrante cumple RN-01, RN-02, RN-04 y RN-06; hay empleados compatibles para RN-03 y fechas para RN-05).
- **Evidencia observada:** la tarea no incluye RN-02 y añade RN-03, que no es una propiedad del cuadrante sino de cada pareja de un intercambio.
- **Impacto:** puede quedar sin verificar parte de US-003-AC-02 (RN-02 y la preparación de casos para RN-03 y RN-05) y, con ello, la DoD de US-003.
- **Acción recomendada:** alinear la descripción de TK-007 con US-003-AC-02.
- **Pregunta o decisión:** ninguna de alcance.
- **Rol propuesto:** PO (responsable de la tarea), con QA.

### IPR-v01-010 · Dependencia no declarada · MINOR · Bloqueante: NO

- **Fuente/ID:** EP-002 US-005-AC-03 («Los turnos implicados en una solicitud pendiente aparecen marcados»); extracto §2 (US-005 en IT-002 y US-009 en IT-004); `goals.md` S-04 (solicitudes ficticias); EP-001 US-003-AC-01/02 (no mencionan solicitudes).
- **Evidencia observada:** US-005 se planifica en IT-002, pero las solicitudes se crean con US-009 en IT-004. Ni el catálogo ni la ficha de US-003 indican si los datos de demostración incluyen solicitudes pendientes.
- **Impacto:** puede que US-005-AC-03 no pueda verificarse en IT-002, lo que impediría cumplir la DoD de US-005 en su sprint.
- **Acción recomendada:** aclarar si los datos de demostración de US-003 incluyen solicitudes pendientes o si existe una dependencia de US-005 respecto al modelo de solicitud de US-009. En ese caso, registrarla.
- **Pregunta o decisión:** ¿Cómo se verificará US-005-AC-03 en IT-002?
- **Rol propuesto:** PO y TL.

### IPR-v01-011 · DoR (criterios de aceptación) · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto §3 (tareas del PO «… y criterios de aceptación» en US-005, US-009, US-010 y US-018, dentro de su sprint); DoR, Aceptación y Uso (la historia no entra en el sprint sin criterios identificados).
- **Evidencia observada:** los criterios ya existen en las fichas (US-005-AC-01 a 03, US-009-AC-01 a 08, US-010-AC-01 a 05, US-018-AC-01 a 07). El nombre de las tareas puede leerse como redacción de criterios durante el sprint.
- **Impacto:** si las tareas consisten en redactar o cambiar criterios, no se cumple la DoR al entrar en el sprint. Si consisten en verificarlos o validarlos, no hay conflicto.
- **Acción recomendada:** precisar el contenido de esas tareas (por ejemplo, verificar los criterios o validarlos como PO) al detallarlas por tareas.
- **Pregunta o decisión:** ¿Qué trabajo incluyen las tareas «criterios de aceptación» del PO?
- **Rol propuesto:** PO.

### IPR-v01-012 · Cobertura de la DoD y capacidades · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto §3; DoD (pruebas automatizadas, revisión en PR por otro miembro, despliegue en demostración); Team Charter, acuerdo 15; EP-005 US-018-AC-03/06/07 y NFR-007; `company.md` («Todos los miembros participan en el desarrollo»).
- **Evidencia observada:** US-003, US-006 y US-010 no tienen una tarea explícita de pruebas automatizadas. Ninguna historia tiene horas explícitas de revisión de PR o despliegue. En US-018, la lógica de servidor (revalidación, permuta atómica, rechazo por regla y comprobación de caducidad) solo aparece como «Parte 2: implementación de la transacción», con 0,50 h del TL en IT-006. El resto se reparte entre la pantalla, el flujo y los criterios del PO, y las pruebas de QA. Ninguna fuente documenta las capacidades técnicas de cada persona (por ejemplo, la validación RN-03 asignada a la SM).
- **Impacto:** no puede comprobarse que las horas asignadas cubran la DoD ni quién implementa la lógica de servidor de US-018. El agente no valora si las estimaciones son suficientes.
- **Acción recomendada:** confirmar que las pruebas, la revisión de PR y el despliegue están incluidos en las horas de cada tarea e identificar quién implementa la lógica de servidor de US-018 al detallar IT-005 e IT-006.
- **Pregunta o decisión:** ¿Dónde está, dentro de las 8 h-p de US-018, la implementación de AC-03, AC-06 y AC-07?
- **Rol propuesto:** TL y QA.

### IPR-v01-013 · Prerrequisitos técnicos pendientes · MINOR · Bloqueante: NO

- **Fuente/ID:** Wiki, Uso de agentes (R-04: «La revisión técnica posterior de la caducidad a cargo de MarvelinoGG (TL) sigue pendiente»); requisitos v02 §8 y §9 (contrato del formato de solicitud entre US-012/014/015 y US-009 sin evidencia); extracto §2 (US-012/014 en IT-003 y US-009 en IT-004).
- **Evidencia observada:** los validadores (IT-003) se construyen antes que US-009 (IT-004) y dependen de un formato de solicitud acordado, pero el plan no tiene ninguna tarea para acordarlo ni consta que exista. La revisión técnica de la caducidad (US-009-AC-08, US-010-AC-05 y US-018-AC-07) dentro de las 8/3/8 h-p sigue pendiente.
- **Impacto:** si no se acuerda el contrato, US-009 podría tener que rehacer trabajo de los validadores. Si la revisión de la caducidad cambiara las estimaciones, cambiaría la carga de IT-004 a IT-006.
- **Acción recomendada:** registrar el acuerdo del formato de solicitud antes de planificar IT-003 (04/11) y la revisión técnica de la caducidad antes de planificar IT-004 (11/11).
- **Pregunta o decisión:** ¿Confirma el TL, tras la revisión técnica, que la caducidad cabe en 8/3/8 h-p?
- **Rol propuesto:** TL.

### IPR-v01-014 · Holgura individual y cuellos de botella · MINOR · Bloqueante: NO

- **Fuente/ID:** extracto §4; `catalogo.md` §2 (US-012 y US-018 con incertidumbre Alta); `technical-risks.md` (RT-01 y RT-02).
- **Evidencia observada:** no hay ninguna sobreasignación. Las holguras individuales mínimas son: QA, 0,05 h en IT-001 y en IT-006; PO, 0,10 h en IT-002; TL, 0,12 h en IT-002 e IT-004; SM, 0,15 h en IT-003. En IT-006, QA lleva las pruebas de US-018 (Alta, RT-02) y la parte 2 de US-023 con 0,05 h de holgura, mientras el TL conserva 1,62 h.
- **Impacto:** el margen individual ya está descontado en la capacidad, así que la regla de la asignatura se cumple. Aun así, cualquier desviación de QA en IT-006 afecta directamente a la release final, porque no queda ninguna iteración después.
- **Acción recomendada:** que SM y QA decidan con antelación cómo actuar si las pruebas de US-018 se desvían. El agente no propone reasignaciones.
- **Pregunta o decisión:** ¿Qué se hará si QA no puede absorber una desviación en IT-006?
- **Rol propuesto:** SM y QA.

## 5. Observaciones aritméticas y de capacidad

**Unidades:** estimaciones en horas-persona (h-p); capacidad en horas por persona e iteración (h); coste en euros (€). Fórmula del equipo: `efectiva = max(0, nominal − ausencias − reuniones − coordinación) × (1 − margen)`, con nominal 6 h y reuniones 1,5 h por semana.

### 5.1 Capacidad recalculada (h, sin redondear)

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| PO (coord. 0,5; margen 20 %) | (6−1−1,5−0,5)×0,80 = 2,40 | 2,0×0,80 = 1,60 | 4,0×0,80 = 3,20 | 2,40 | 2,40 | 2,40 | 14,40 |
| SM (coord. 1; margen 10 %) | 2,5×0,90 = 2,25 | 1,5×0,90 = 1,35 | 3,5×0,90 = 3,15 | 2,25 | 2,25 | 2,25 | 13,50 |
| TL (coord. 1; margen 15 %) | 3,5×0,85 = 2,975 | 2,5×0,85 = 2,125 | 2,975 | 2,125 | 2,125 | 2,125 | 14,45 |
| QA (coord. 0,5; margen 15 %) | 3,0×0,85 = 2,55 | 2,0×0,85 = 1,70 | 4,0×0,85 = 3,40 | 2,55 | 2,55 | 2,55 | 15,30 |
| **Equipo** | 10,175 | 6,775 | 12,725 | 9,325 | 9,325 | 9,325 | **57,65** |

Las ausencias del extracto coinciden con `capacity.md`. La conciliación es 144 − 36 − 18 − 22 − 10,35 = 57,65 h. Las fechas son correctas: el 21/10/2026 es miércoles y el 01/12/2026, martes.

### 5.2 Carga asignada (h), recalculada desde el extracto §3

| Persona | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total | ¿Supera la capacidad? |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| PO | 1,50 | 1,50 | 2,50 | 2,00 | 1,50 | 2,00 | 11,00 | No |
| SM | 1,50 | 1,00 | 3,00 | 2,00 | 1,50 | 2,00 | 11,00 | No |
| TL | 2,50 | 2,00 | 2,50 | 2,00 | 1,50 | 0,50 | 11,00 | No |
| QA | 2,50 | 1,50 | 3,00 | 2,00 | 1,50 | 2,50 | 13,00 | No |
| **Equipo** | 8,00 | 6,00 | 11,00 | 8,00 | 6,00 | 7,00 | **46,00** | No |

- Horas por historia, iguales a las h-p tras D-18: US-001 = 1,5+1,5+1,0+1,0 = 5; US-003 = 1,0+1,5+0,5 = 3; US-002 = 3; US-005 = 3; US-006 = 3; US-012 = 5; US-014 = 3; US-009 = 8; US-010 = 3; US-018 = 1,5+0,5+2+2+2 = 8; US-023 = 1,5+0,5 = 2. Total: 46 h-p, igual a las 11 Must del catálogo.
- Holgura del equipo: 57,65 − 46,00 = 11,65 h, igual que en el catálogo (D-21). Por iteración: 2,175 · 0,775 · 1,725 · 1,325 · 3,325 · 2,325 h.
- Se cumple la regla de la asignatura («No se puede sobreasignar tareas») en las 24 combinaciones de persona e iteración.
- **Exclusiones:** Should, Could y Won't (US-011, 013, 015, 016, 019, 020, 024; US-004, 021; US-007, 008, 022) y US-017, fusionada.
- **Desconocidos:** el reparto por tareas de IT-002 a IT-006, la secuencia dentro de cada sprint, las capacidades técnicas de cada persona y si las horas incluyen pruebas, revisión de PR y despliegue (IPR-v01-012).
- **Límite del control agregado:** que no haya sobreasignación por persona e iteración no demuestra que el orden dentro de una semana de trabajo sea viable ni que las estimaciones sean adecuadas. Sin US-024, M01 y M03 quedarán pendientes de validación, como ya decidió D-23.

## 6. Observaciones de dependencias y capacidades

- **Tipos de dependencia (catálogo §3):** técnicas, de US-001 a US-002/US-003 y de US-003 a US-002/005/009/012/014; funcionales, de US-002 a US-005, de US-005 a US-006, de US-006 a US-009, de US-009 a US-010, de US-010/012/014 a US-018 y de US-018 a US-023; técnica, de US-012 a US-014. Las predecesoras del extracto coinciden con el catálogo. No se observan ciclos.
- **Externas sin resolver:** las tecnologías autorizadas (US-001; IPR-v01-003) y la persona evaluadora ajena a la implementación (US-023 y M04; IPR-v01-004). El contrato del formato de solicitud entre los validadores y US-009 tampoco consta como cerrado (IPR-v01-013).
- **Ubicación de cada historia frente a sus predecesoras:** todas las predecesoras terminan en una iteración anterior o en la misma, salvo US-023, que empieza en IT-005 cuando US-018 termina en IT-006 (IPR-v01-001). Hay dependencias dentro de la misma iteración en IT-002 (US-002 → US-005), IT-003 (US-012 → US-014) e IT-005 (US-010 → US-018 parte 1).
- **Cadena crítica:** ocupa las seis iteraciones sin ninguna iteración de holgura (IPR-v01-003).
- **Cuellos de botella que pueden afirmarse con la evidencia:** QA en IT-001 e IT-006 (0,05 h de holgura) y la concentración del trabajo de incertidumbre Alta de US-018 en la última iteración (IPR-v01-014). Las capacidades de cada persona no pueden evaluarse con las fuentes disponibles.
- No se ha generado ningún calendario ni secuencia alternativa.

## 7. Resultado de coste

- **Tarifas** (`company.md`, verificadas por D-17 y mantenidas por D-21): PO 19,50 €/h, SM 24,75 €/h, TL 15,75 €/h, QA 20,25 €/h.
- **Coste de las horas asignadas (recalculado):** PO 11 × 19,50 = 214,50 €; SM 11 × 24,75 = 272,25 €; TL 11 × 15,75 = 173,25 €; QA 13 × 20,25 = 263,25 €. Total: **923,25 €**. Por iteración: 156,375 · 115,875 · 223,125 · 160,50 · 120,375 · 147,00 €, que también suman 923,25 €.
- **Presupuesto** (D-21; recalculado): personal 144 h nominales = 2.889,00 €; equipos 4 × 1.000 € / 4 años × 6/52 = 115,38 €; software 30,00 €; gastos generales 15 % = 433,35 €; coste 3.467,73 €; reserva 10 % = 346,77 €; margen 15 % sobre 3.814,50 € = 572,18 €; precio sin IVA 4.386,68 €; IVA 21 % = 921,20 €; **precio 5.307,88 € con IVA**. Coincide con `company.md`, `goals.md` y D-21.
- **Supuestos:** se paga la jornada nominal completa (144 h), no solo la capacidad efectiva. El coste de las horas asignadas es una parte del personal presupuestado, no un coste adicional.
- **Desconocidos:** el efecto de IPR-v01-005 no se refleja en el coste, porque las horas nominales pagadas no cambian. La revisión del presupuesto queda prevista en H4 (`company.md`).

## 8. Preguntas y acciones sugeridas

| # | Pregunta o acción | Rol propuesto | Momento de validación | Bloqueante |
|---|---|---|---|---|
| 1 | Confirmar las tecnologías autorizadas y, si no llegan a tiempo, decidir qué hacer con TK-001 y US-001 (IPR-v01-003). | TL; seguimiento de la SM | Antes del Sprint Planning de IT-001 (21/10/2026) | NO |
| 2 | Confirmar cuántas horas de reunión consume la sesión del miércoles (1 h o 2 h) y alinear el Team Charter y `capacity.md` (IPR-v01-005). | SM | Antes del 21/10/2026 | NO |
| 3 | Confirmar si la parte 1 de US-023 depende de US-018, revisar la regla de dependencias del libro y mostrar la secuencia dentro de los sprints (IPR-v01-001). | SM y TL; PO para el alcance | Antes de planificar IT-005 (18/11/2026) | NO |
| 4 | Decidir y registrar cómo se trata que US-018 y US-023 abarquen dos sprints (IPR-v01-002) y registrar las decisiones de planificación del 14/10 (IPR-v01-008). | TL y SM; conformidad del PO | Al aceptar la hipótesis, antes de IT-001 | NO |
| 5 | Identificar a la persona evaluadora externa y fijar una fecha de IT-006 posterior al cierre de US-018 (IPR-v01-004). | PO y QA | Antes de planificar IT-005 (18/11/2026) | NO |
| 6 | Registrar el contrato del formato de solicitud de los validadores y la revisión técnica de la caducidad pendiente de R-04 (IPR-v01-013). | TL | IT-003 (04/11/2026) e IT-004 (11/11/2026) | NO |
| 7 | Aclarar cómo se verifica US-005-AC-03 en IT-002 (IPR-v01-010) y alinear TK-007 con US-003-AC-02 (IPR-v01-009). | PO y TL; QA | Antes de IT-001 (TK-007) y de IT-002 (US-005) | NO |
| 8 | Precisar las tareas «criterios de aceptación» (IPR-v01-011) y confirmar la cobertura de pruebas, PR y despliegue y la lógica de servidor de US-018 (IPR-v01-012). | PO; TL y QA | Al detallar cada iteración por tareas | NO |
| 9 | Decidir cuál es la fuente vigente del plan y actualizar el catálogo y las fichas (IPR-v01-007); unificar el redondeo (IPR-v01-006). | SM; PO | Tras aceptar la hipótesis | NO |
| 10 | Decidir con antelación qué hacer si hay desviaciones de QA en IT-006 (IPR-v01-014). | SM y QA | Antes de planificar IT-006 (25/11/2026) | NO |

Estas son propuestas: no son decisiones aprobadas, estimaciones nuevas ni asignaciones de sprint o de personas.

## 9. Matriz de disposición RECHECK

No aplica: es el primer informe del Planning Agent (modo CONSISTENCY, no RECHECK).

## 10. Consejo final y límites

- **Preparación:** READY_WITH_NON_BLOCKING_QUESTIONS para revisar y usar la hipótesis humana de planificación inicial del H3 (11 Must, 46 h-p, IT-001 a IT-006). No hay hallazgos bloqueantes. Se recomienda resolver las preguntas 1 y 2 antes del 21/10/2026.
- **Límites:** se ha revisado el extracto Markdown, no el libro .xlsx ni sus fórmulas. Las capacidades técnicas de cada persona, la secuencia dentro de los sprints, el reparto por tareas de IT-002 a IT-006 y la idoneidad de las estimaciones no se han evaluado. No hay acceso al estado real de las dependencias externas. Este resultado no demuestra que el calendario sea viable.
- **Fuentes sin cambios:** no se ha modificado ningún requisito, prioridad, estimación, cifra de capacidad, DoR/DoD, dependencia, supuesto, decisión, plan ni fichero de la Wiki. **Solo se ha creado este informe nuevo** (`docs/reviews/initial-planning/initial-planning-review-v01.md`).
- **Sin aprobación:** este informe es consultivo. No compromete alcance, no aprueba ningún plan ni línea base, no supera ninguna puerta de calidad, no selecciona candidatas para sprints y no asigna recursos.
