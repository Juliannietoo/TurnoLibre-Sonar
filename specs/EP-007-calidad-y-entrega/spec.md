# EP-007 — Calidad y entrega

**Objetivos:** G04 (y evidencias de M01, M03, M04)
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** documentación de instalación y evaluación, y validación con usuarios. Las pruebas automatizadas de cada historia no están aquí: las exige la Definition of Done de cada historia.

## Resultado de la épica

Un tercero instala y evalúa cada release sin ayuda, y se dispone de evidencias de usabilidad.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-023 — Crear el guion inicial de instalación y evaluación

> **Cambio D-18 (06/10/2026):** guion mínimo de instalación y evaluación al final del proyecto, no en cada release.

> Como evaluador, quiero un guion paso a paso para instalar y evaluar el producto, para comprobarlo sin ayuda del equipo.

- **Necesidad:** métrica M04.
- **Objetivo:** G04 · M04
- **Prioridad:** Must — *valor:* aporta el guion mínimo de instalación al final que exigen G04 y M04 tras D-18; *riesgo:* bajo; *dependencias:* necesita el flujo completo (US-018) y una persona ajena a la implementación que lo valide.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 4 · SM 5 · TL 3 · QA 3); revisada por D-18: **2 h-p**, votada por el equipo.
- **Incertidumbre:** Baja
- **Predecesoras:** US-001 (técnica), US-003 (técnica), US-002 (funcional), US-005 (funcional); externa: evaluador ajeno a la implementación
- **Plan inicial:** por replanificar tras D-18 (ver catálogo, apartado 4)

**Criterios de aceptación**
- US-023-AC-01: Una persona que no ha participado en el desarrollo instala el producto desde un entorno limpio siguiendo solo el guion.
- US-023-AC-02: El guion incluye acceso por rol y consulta del calendario con las cuentas de demostración de R1, preparación del entorno y restablecimiento de los datos.
- US-023-AC-03: Quedan identificadas las instrucciones que se ampliarán con las funciones de R2/R3. Cada release debe volver a instalarse y evaluarse desde un entorno limpio según M04; ese esfuerzo se incluye en las historias del incremento correspondiente.

- **Reglas y límites:** Cuentas y datos ficticios; evaluación de las funciones disponibles de cada release. Se aplican los límites comunes de la épica.
- NFR: NFR-003 (datos 100 % ficticios) y NFR-008 (instalación reproducible desde cero en < 10 min según guion documentado).

---

### US-024 — Prueba de usabilidad y accesibilidad básica

> **Cambio D-18 (06/10/2026):** pasa a Should; si cabe, se realiza durante la review final.

> Como Product Owner, quiero probar el flujo con 3 participantes y revisar la accesibilidad básica, para comprobar M01 y M03 antes de la entrega.

- **Necesidad:** Obtener evidencia medible de autonomía de los empleados y rapidez del responsable.
- **Objetivo:** G01, G03 y G04 · M01/M03

- **Prioridad:** Should (antes Must) — *valor:* aporta evidencia de M01 y M03; pasa a Should por D-18 y, si no se hace, M01 queda pendiente; *riesgo:* medio, requiere coordinar participantes; *dependencias:* necesita el flujo completo. La prueba con tres participantes se realiza durante la review final si se incorpora.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 3 · SM 5 · TL 5 · QA 3); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Media
- **Predecesoras:** US-010 (funcional), US-018 (funcional), US-023 (funcional); externa: tres participantes ajenos al equipo
- **Plan inicial:** sin compromiso; si cabe, en la review final

**Criterios de aceptación**
- US-024-AC-01: Tres participantes ajenos al equipo completan individualmente los pasos de publicar, proponer y aceptar un intercambio válido utilizando dos cuentas ficticias, hasta dejarlo pendiente de aprobación. Se registran tiempo, ayuda necesaria y resultado. M01 se cumple si los tres terminan en menos de cinco minutos y sin ayuda; se excluye el tiempo de decisión del responsable.
- US-024-AC-02: Los flujos principales se completan con teclado, con foco visible y mensajes que no dependan solo del color; se mide contraste mínimo de 4,5:1 para texto normal y 3:1 para texto grande.
- US-024-AC-03: Para M03, el responsable resuelve tres solicitudes de muestra en menos de un minuto cada una, medido desde que abre el detalle hasta que registra la decisión.

La muestra de tres participantes sustituye la meta anterior de cuatro éxitos entre cinco participantes, por decisión del PO del 01/10/2026. Con tres personas se exige el éxito de las tres para conservar un umbral de al menos el 80 %.

- **Reglas y límites:** M01: tres éxitos de tres en menos de 5 min; M03: tres decisiones de menos de 1 min. Se aplican los límites comunes de la épica.
- NFR: NFR-003 (datos ficticios sin identificación de participantes), NFR-004 (accesibilidad básica WCAG 2.1 AA) y NFR-009 (compatibilidad en navegadores).
