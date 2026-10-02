# EP-007 — Calidad y entrega

**Objetivos:** G04 (y evidencias de M01, M03, M04)
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** documentación de instalación y evaluación, y validación con usuarios. Las pruebas automatizadas de cada historia no están aquí: las exige la Definition of Done de cada historia.

## Resultado de la épica

Un tercero instala y evalúa cada release sin ayuda, y se dispone de evidencias de usabilidad.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales se describen aquí por su comportamiento; QA asignará los IDs del catálogo compartido.

## Historias

### US-023 — Crear el guion inicial de instalación y evaluación

> Como evaluador, quiero un guion paso a paso para instalar y evaluar el producto, para comprobarlo sin ayuda del equipo.

- **Necesidad:** métrica M04.
- **Objetivo:** G04 · M04
- **Prioridad:** Must — *valor:* permite evaluar R1 y sirve de base para las demás releases; *riesgo:* bajo; *dependencias:* necesita el entorno, los datos y las funciones de R1.
- **Estimación:** PO individual: **4 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker.
- **Incertidumbre:** Baja
- **Predecesoras:** US-001 (técnica), US-003 (técnica), US-002 (funcional), US-005 (funcional); externa: evaluador ajeno a la implementación
- **Plan inicial:** IT-002 · R1. Se actualiza y verifica en R2/R3 dentro de las tareas de entrega de cada incremento, sin mantener esta historia abierta tres sprints.

**Criterios de aceptación**
- US-023-AC-01: Una persona que no ha participado en el desarrollo instala el producto desde un entorno limpio siguiendo solo el guion.
- US-023-AC-02: El guion incluye acceso por rol y consulta del calendario con las cuentas de demostración de R1, preparación del entorno y restablecimiento de los datos.
- US-023-AC-03: Quedan identificadas las instrucciones que se ampliarán con las funciones de R2/R3. Cada release debe volver a instalarse y evaluarse desde un entorno limpio según M04; ese esfuerzo se incluye en las historias del incremento correspondiente.

- **Reglas y límites:** Cuentas y datos ficticios; evaluación de las funciones disponibles de cada release. Se aplican los límites comunes de la épica.
- NFR: Instalación desde cero con pasos y versiones documentados; datos totalmente ficticios.

---

### US-024 — Prueba de usabilidad y accesibilidad básica

> Como Product Owner, quiero probar el flujo con 3 participantes y revisar la accesibilidad básica, para comprobar M01 y M03 antes de la entrega.

- **Necesidad:** Obtener evidencia medible de autonomía de los empleados y rapidez del responsable.
- **Objetivo:** G01, G03 y G04 · M01/M03

- **Prioridad:** Must — *valor:* demuestra el cumplimiento de M01 y M03; *riesgo:* medio, requiere coordinar participantes; *dependencias:* necesita el flujo completo. Se reduce la muestra a tres personas para acotar el esfuerzo.
- **Estimación:** PO individual: **3 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker.
- **Incertidumbre:** Media
- **Predecesoras:** US-010 (funcional), US-018 (funcional), US-023 (funcional); externa: tres participantes ajenos al equipo
- **Plan inicial:** IT-006 · R3; preparar participantes y guion antes de la prueba.

**Criterios de aceptación**
- US-024-AC-01: Tres participantes ajenos al equipo completan individualmente los pasos de publicar, proponer y aceptar un intercambio válido utilizando dos cuentas ficticias, hasta dejarlo pendiente de aprobación. Se registran tiempo, ayuda necesaria y resultado. M01 se cumple si los tres terminan en menos de cinco minutos y sin ayuda; se excluye el tiempo de decisión del responsable.
- US-024-AC-02: Los flujos principales se completan con teclado, con foco visible y mensajes que no dependan solo del color; se mide contraste mínimo de 4,5:1 para texto normal y 3:1 para texto grande.
- US-024-AC-03: Para M03, el responsable resuelve tres solicitudes de muestra en menos de un minuto cada una, medido desde que abre el detalle hasta que registra la decisión.

La muestra de tres participantes sustituye la meta anterior de cuatro éxitos entre cinco participantes, por decisión del PO del 01/10/2026. Con tres personas se exige el éxito de las tres para conservar un umbral de al menos el 80 %.

- **Reglas y límites:** M01: tres éxitos de tres en menos de 5 min; M03: tres decisiones de menos de 1 min. Se aplican los límites comunes de la épica.
- NFR: Prueba con datos ficticios; evidencias sin identificación personal de participantes.
