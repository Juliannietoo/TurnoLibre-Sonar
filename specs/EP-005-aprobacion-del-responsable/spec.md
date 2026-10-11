# EP-005 — Aprobación del responsable

**Objetivos:** G03
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** resolución de solicitudes aceptadas por ambos empleados (S-02) y consulta básica de decisiones del servicio (S-03). No incluye delegación de la aprobación ni aprobación automática.

## Resultado de la épica

El responsable resuelve cada solicitud con las reglas ya comprobadas en menos de 1 minuto (métrica M03), y el cuadrante se actualiza sin inconsistencias.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-017 — Consultar solicitudes y decisiones del servicio

> **Cambio D-18 (06/10/2026):** fusionada en US-018 (una sola pantalla para consultar las pendientes y resolverlas). Se conserva el identificador.

> Como responsable, quiero consultar las solicitudes pendientes y las decisiones anteriores de mi servicio, para resolver cambios y comprobar su resultado.

- **Necesidad:** hoy el responsable comprueba las reglas a mano.
- **Objetivo:** G03 · S-02/S-03
- **Prioridad:** Fusionada en US-018 (antes Must) — *valor:* la consulta de pendientes se integra con la resolución en una sola pantalla (D-18); *riesgo:* medio; *dependencias:* no se planifica como predecesora independiente de US-018; su alcance y esfuerzo están incluidos en ella.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 5 · SM 5 · TL 5 · QA 5); sin estimación propia tras D-18 (fusionada en US-018).
- **Incertidumbre:** Media
- **Predecesoras:** — (fusionada en US-018)
- **Plan inicial:** fusionada en US-018

**Criterios de aceptación**
- US-017-AC-01: El responsable dispone de una lista de solicitudes Aceptadas de su servicio, ordenadas por el inicio más próximo, y de una lista básica de las que ya aprobó o rechazó. No accede a solicitudes de otros servicios.
- US-017-AC-02: Cada solicitud muestra empleados, turnos y el resultado de cada regla (cumple / incumple).
- US-017-AC-03: Si no hay solicitudes pendientes, se muestra un mensaje que lo indica.
- US-017-AC-04: El detalle de una decisión conserva los turnos originales, solicitante y destinatario, fechas de propuesta y aceptación, responsable, fecha y resultado de la decisión y motivo del rechazo cuando proceda. Este historial básico está disponible sin US-020.

- **Reglas y límites:** Solo solicitudes del servicio; información completa de RN-01…RN-06. Se aplican los límites comunes de la épica.
- NFR: El servidor impide consultar otro servicio; la lista vacía tiene un mensaje explícito.

---

### US-018 — Resolver una solicitud  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** una sola pantalla para consultar las pendientes y resolverlas (absorbe US-017); se mantiene el registro básico de la decisión y el resultado visible para ambos empleados.

> Como responsable, quiero aprobar o rechazar con motivo una solicitud, para mantener el cuadrante correcto y que los empleados conozcan el resultado.

- **Necesidad:** decisión final con trazabilidad de quién aprobó qué y cuándo.
- **Objetivo:** G03 · M03 y G02 (revalidación antes de aprobar)
- **Prioridad:** Must — *valor:* cierra el flujo completo; *riesgo:* alto (RT-02, concurrencia); *dependencias:* predecesora de las vistas ampliadas de estado e historial y de la prueba del flujo completo.
- **Estimación:** consenso del 06/10/2026: **8 h-p** (individuales: PO 7 · SM 8 · TL 8 · QA 8).
- **Incertidumbre:** Alta
- **Predecesoras:** US-010 (funcional), US-012 (funcional), US-014 (funcional)
- **Plan inicial:** por replanificar tras D-18: ajustar carga por sprint y tareas individuales según D-21 (ver catálogo, apartado 4)

**Criterios de aceptación**
- US-018-AC-01: Al aprobar una solicitud válida, los turnos se intercambian en el calendario de ambos empleados, la solicitud pasa a *Aprobada* y se cierran las publicaciones de los turnos afectados.
- US-018-AC-02: Al rechazar, es obligatorio escribir un motivo, que ven ambos empleados. La solicitud pasa a *Rechazada*, se liberan ambos turnos y las publicaciones que sigan vigentes vuelven a estar disponibles.
- US-018-AC-03: Antes de aprobar se repite la validación completa; si ahora incumple una regla, no se aprueba y se muestra el motivo.
- US-018-AC-04: El botón *Aprobar* está desactivado si la solicitud incumple alguna regla.
- US-018-AC-05: Cada decisión queda registrada con fecha, hora y responsable.
- US-018-AC-06: La decisión actualiza el detalle básico de los empleados (US-009) y el historial del responsable (US-017). Repetir una aprobación o enviarla desde dos pestañas produce un único intercambio y una única decisión; una solicitud ya terminada no puede volver a resolverse.

**Reglas:** RN-01 a RN-06 (revalidación); RN-05 (no se aprueban solicitudes caducadas).

**Verificación y restricciones**
- NFR: NFR-001 (autorización exclusiva en servidor para el responsable del servicio, RT-03), NFR-004 (interfaz y controles accesibles con teclado), NFR-005 (motivo de rechazo obligatorio y visible; regla indicada si falla revalidación), NFR-006 (revalidación completa de reglas en < 500 ms), NFR-007 (aprobación y permuta de cuadrante como transacción atómica ACID; control de concurrencia, RT-02) y NFR-009 (compatibilidad en navegadores).
- Métrica M03: el responsable decide en menos de 1 minuto desde que abre el detalle.

**Ejemplos**
- Solicitud Ana ↔ Luis válida → aprobada → Ana ve la mañana del viernes y Luis la tarde del jueves.

**Casos límite**
- Dos solicitudes aceptadas afectan al mismo empleado; al aprobar la primera, la segunda deja de cumplir RN-01: la segunda no puede aprobarse.
- Si ambas se aprueban simultáneamente, el resultado también debe cumplir todas las reglas: no pueden confirmarse dos decisiones que juntas dejen un cuadrante inválido.
- El responsable abre una solicitud y, mientras decide, un empleado la cancela: se rechaza la aprobación y no se modifica el cuadrante (si se incorpora US-011).
- Rechazo con motivo vacío o solo espacios: no se permite.

**Supuestos**
- La decisión conserva los datos originales de la solicitud; las consultas básicas no necesitan las vistas ampliadas de EP-006.
- Un único responsable por servicio (A-02), pero puede tener la aplicación abierta en dos pestañas.

---
