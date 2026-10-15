# EP-007 — Calidad y entrega

**Objetivos:** G04 (y evidencias de M01, M03, M04)
**Línea base documental:** requisitos-v1-revisado · revisión 14/10/2026 (D-18/D-21/D-22/D-23/D-24; decisiones en Uso de agentes)
**Límites:** documentación de instalación y evaluación, y validación con usuarios. Las pruebas automatizadas de cada historia no están aquí: las exige la Definition of Done de cada historia.

## Resultado de la épica

Un tercero instala y evalúa la versión final siguiendo el guion mínimo sin ayuda. Si se realiza la prueba Should US-024, se obtienen las evidencias de M01 y M03; si no, ambas métricas quedan pendientes de validación (D-18/D-23).

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-023 — Crear el guion mínimo final de instalación y evaluación

> **Cambio D-18 (06/10/2026):** guion mínimo de instalación y evaluación al final del proyecto, no en cada release.

> Como evaluador, quiero un guion paso a paso para instalar y evaluar el producto, para comprobarlo sin ayuda del equipo.

- **Necesidad:** métrica M04.
- **Objetivo:** G04 · M04
- **Prioridad:** Must — *valor:* aporta el guion mínimo de instalación al final que exigen G04 y M04 tras D-18; *riesgo:* bajo; *dependencias:* necesita el flujo completo (US-018) y una persona ajena a la implementación que lo valide.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 4 · SM 5 · TL 3 · QA 3); revisada por D-18: **2 h-p**, votada por el equipo.
- **Incertidumbre:** Baja
- **Predecesoras:** US-018 (funcional); externa: evaluador ajeno a la implementación. La dependencia de US-018 se aplica a la parte 2 (validación final); la parte 1 (guion de instalación) solo necesita US-001, US-002 y US-003 (D-24)
- **Plan inicial:** IT-005 (parte 1: entorno, restablecimiento de datos, cuentas ficticias y pasos de consultar y proponer, 1,5 h) e IT-006 (parte 2: pasos de aceptar y resolver, y validación con el evaluador externo, 0,5 h) · R3. Excepción explícita a «cabe en un sprint» (D-24). El paso «aceptar» va en la parte 2 porque US-010 se desarrolla en IT-005 a la vez que la parte 1 (AUD-v01-006, D-27)

**Criterios de aceptación**
- US-023-AC-01: Una persona que no ha participado en el desarrollo instala el producto desde un entorno limpio siguiendo solo el guion.
- US-023-AC-02: El guion final incluye preparación del entorno, restablecimiento de datos, cuentas ficticias por rol y los pasos del flujo esencial disponible en la versión final: consultar turnos, proponer, aceptar y resolver solicitudes.
- US-023-AC-03: Una persona ajena a la implementación ejecuta y evalúa la versión final desde el entorno limpio siguiendo solo el guion documentado, sin intervenciones no documentadas, conforme a M04. El guion mínimo se entrega al final, sin exigir esta evaluación en cada release (D-18).

- **Reglas y límites:** Cuentas y datos ficticios; instalación y evaluación de las funciones de la versión final. Se aplican los límites comunes de la épica.
- NFR: NFR-003 (datos 100 % ficticios) y NFR-008 (instalación reproducible desde cero en < 10 min según guion documentado).

---

### US-024 — Prueba de usabilidad y accesibilidad básica

> **Cambio D-18 (06/10/2026):** pasa a Should; si cabe, se realiza durante la review final.

> Como Product Owner, quiero probar el flujo con 3 participantes y revisar la accesibilidad básica, para comprobar M01 y M03 antes de la entrega.

- **Necesidad:** Obtener evidencia medible de autonomía de los empleados y rapidez del responsable.
- **Objetivo:** G01, G03 y G04 · M01/M03

- **Prioridad:** Should (antes Must) — *valor:* aporta evidencia de M01 y M03; pasa a Should por D-18 y, si no se hace, M01 y M03 quedan pendientes de validación (D-23); *riesgo:* medio, requiere coordinar participantes; *dependencias:* necesita el flujo completo. La prueba con tres participantes se realiza durante la review final si se incorpora.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 3 · SM 5 · TL 5 · QA 3); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Media
- **Predecesoras:** US-010 (funcional), US-018 (funcional), US-023 (funcional); externa: tres participantes ajenos al equipo
- **Plan inicial:** sin compromiso; si cabe, en la review final

**Criterios de aceptación**
- US-024-AC-01: Tres participantes ajenos al equipo completan individualmente los pasos de proponer y aceptar un intercambio válido sobre un turno de un compañero compatible utilizando dos cuentas ficticias, hasta dejarlo pendiente de aprobación. Se registran tiempo, ayuda necesaria y resultado. M01 se cumple si los tres terminan en menos de cinco minutos y sin ayuda; se excluye el tiempo de decisión del responsable.
- US-024-AC-02: Los flujos principales se completan con teclado, con foco visible y mensajes que no dependan solo del color; se mide contraste mínimo de 4,5:1 para texto normal y 3:1 para texto grande.
- US-024-AC-03: Para M03, el responsable resuelve tres solicitudes de muestra en menos de un minuto cada una, medido desde que abre el detalle hasta que registra la decisión. Si US-024 no se realiza, M03 queda pendiente de validación, igual que M01 (D-23).

La muestra de tres participantes sustituye la meta anterior de cuatro éxitos entre cinco participantes, por decisión del PO del 01/10/2026. Con tres personas se exige el éxito de las tres para conservar un umbral de al menos el 80 %.

- **Reglas y límites:** M01: tres éxitos de tres en menos de 5 min; M03: tres decisiones de menos de 1 min. Se aplican los límites comunes de la épica.
- NFR: NFR-003 (datos ficticios sin identificación de participantes), NFR-004 (accesibilidad básica WCAG 2.1 AA) y NFR-009 (compatibilidad en navegadores).
