# EP-005 — Aprobación del responsable

**Objetivos:** G03
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** resolución de solicitudes aceptadas por ambos empleados (S-02) y consulta básica de decisiones del servicio (S-03). No incluye delegación de la aprobación ni aprobación automática.

## Resultado de la épica

El responsable resuelve cada solicitud con las reglas ya comprobadas en menos de 1 minuto (métrica M03), y el cuadrante se actualiza sin inconsistencias.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales se describen aquí por su comportamiento; QA asignará los IDs del catálogo compartido.

## Historias

### US-017 — Consultar solicitudes y decisiones del servicio

> Como responsable, quiero consultar las solicitudes pendientes y las decisiones anteriores de mi servicio, para resolver cambios y comprobar su resultado.

- **Necesidad:** hoy el responsable comprueba las reglas a mano.
- **Objetivo:** G03 · S-02/S-03
- **Prioridad:** Must — *valor:* punto de entrada del responsable (G03); *riesgo:* medio; *dependencias:* predecesora de US-018.
- **Estimación:** pendiente de Planning Poker (h-p)
- **Incertidumbre:** Media
- **Predecesoras:** US-010 (funcional), US-012 (funcional), US-013 (funcional), US-014 (funcional), US-015 (funcional)
- **Plan inicial:** IT-005 · R3

**Criterios de aceptación**
- US-017-AC-01: El responsable dispone de una lista de solicitudes Aceptadas de su servicio, ordenadas por el inicio más próximo, y de una lista básica de las que ya aprobó o rechazó. No accede a solicitudes de otros servicios.
- US-017-AC-02: Cada solicitud muestra empleados, turnos y el resultado de cada regla (cumple / incumple).
- US-017-AC-03: Si no hay solicitudes pendientes, se muestra un mensaje que lo indica.
- US-017-AC-04: El detalle de una decisión conserva los turnos originales, solicitante y destinatario, fechas de propuesta y aceptación, responsable, fecha y resultado de la decisión y motivo del rechazo cuando proceda. Este historial básico está disponible sin US-020.

- **Reglas y límites:** Solo solicitudes del servicio; información completa de RN-01…RN-06. Se aplican los límites comunes de la épica.
- NFR: El servidor impide consultar otro servicio; la lista vacía tiene un mensaje explícito.

---

### US-018 — Resolver una solicitud  *(muestra detallada)*

> Como responsable, quiero aprobar o rechazar con motivo una solicitud, para mantener el cuadrante correcto y que los empleados conozcan el resultado.

- **Necesidad:** decisión final con trazabilidad de quién aprobó qué y cuándo.
- **Objetivo:** G03 · M03 y G02 (revalidación antes de aprobar)
- **Prioridad:** Must — *valor:* cierra el flujo completo; *riesgo:* alto (RT-02, concurrencia); *dependencias:* predecesora del historial y del guion de instalación.
- **Estimación:** pendiente de Planning Poker (h-p)
- **Incertidumbre:** Alta
- **Predecesoras:** US-017 (funcional), US-012 (funcional), US-013 (funcional), US-014 (funcional), US-015 (funcional)
- **Plan inicial:** IT-005 · R3

**Criterios de aceptación**
- US-018-AC-01: Al aprobar una solicitud válida, los turnos se intercambian en el calendario de ambos empleados, la solicitud pasa a *Aprobada* y se cierran las publicaciones de los turnos afectados.
- US-018-AC-02: Al rechazar, es obligatorio escribir un motivo, que ven ambos empleados. La solicitud pasa a *Rechazada*, se liberan ambos turnos y las publicaciones que sigan vigentes vuelven a estar disponibles.
- US-018-AC-03: Antes de aprobar se repite la validación completa; si ahora incumple una regla, no se aprueba y se muestra el motivo.
- US-018-AC-04: El botón *Aprobar* está desactivado si la solicitud incumple alguna regla.
- US-018-AC-05: Cada decisión queda registrada con fecha, hora y responsable.
- US-018-AC-06: La decisión actualiza el detalle básico de los empleados (US-009) y el historial del responsable (US-017). Repetir una aprobación o enviarla desde dos pestañas produce un único intercambio y una única decisión; una solicitud ya terminada no puede volver a resolverse.

**Reglas:** RN-01 a RN-06 (revalidación); RN-05 (no se aprueban solicitudes caducadas).

**Verificación y restricciones**
- NFR: la aprobación y el cambio de cuadrante se confirman o fallan juntos (transacción, RT-02); autorización solo para el responsable del servicio (RT-03).
- Métrica M03: el responsable decide en menos de 1 minuto desde que abre el detalle.

**Ejemplos**
- Solicitud Ana ↔ Luis válida → aprobada → Ana ve la mañana del viernes y Luis la tarde del jueves.

**Casos límite**
- Dos solicitudes aceptadas afectan al mismo empleado; al aprobar la primera, la segunda deja de cumplir RN-01: la segunda no puede aprobarse.
- El responsable abre una solicitud y, mientras decide, un empleado la cancela: se rechaza la aprobación y no se modifica el cuadrante (si se incorpora US-011).
- Rechazo con motivo vacío o solo espacios: no se permite.

**Supuestos**
- La decisión conserva los datos originales de la solicitud; las consultas básicas no necesitan las vistas ampliadas de EP-006.
- Un único responsable por servicio (A-02), pero puede tener la aplicación abierta en dos pestañas.

---
