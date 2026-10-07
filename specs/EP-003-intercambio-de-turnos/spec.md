# EP-003 — Intercambio de turnos

**Objetivos:** G01
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** intercambio uno a uno entre dos empleados (S-01) y consulta básica del estado de cada solicitud propia (S-03). No incluye cesiones sin contrapartida, intercambios en cadena ni notificaciones externas (EX-04).

## Resultado de la épica

Dos empleados pueden acordar un intercambio sin ayuda y dejarlo pendiente de aprobación (métrica M01).

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-007 — Publicar un turno para cambiar

> **Cambio D-18 (06/10/2026):** fuera de esta versión; la propuesta se hace directamente sobre un turno compatible (US-006 + US-009). Se conserva el identificador.

> Como empleado, quiero publicar un turno que quiero cambiar, para que mis compañeros compatibles lo vean.

- **Necesidad:** hoy los cambios se anuncian por mensajería informal.
- **Objetivo:** G01 · S-01
- **Prioridad:** Won't, fuera de esta versión (antes Must) — *valor:* la propuesta directa la sustituye (D-18); *riesgo:* bajo; *dependencias:* ninguna Must depende de ella.
- **Estimación:** consenso del 06/10/2026: **3 h-p** (individuales: PO 3 · SM 3 · TL 2 · QA 3).
- **Incertidumbre:** Baja
- **Predecesoras:** US-005 (funcional)
- **Plan inicial:** fuera de esta versión

**Criterios de aceptación**
- US-007-AC-01: El empleado puede publicar uno de sus turnos futuros desde el calendario.
- US-007-AC-02: No puede publicar un turno pasado ni uno ya publicado.
- US-007-AC-03: El turno publicado aparece marcado en su calendario.

**Verificación y restricciones**
- Reglas: el turno debe pertenecer al empleado y comenzar en el futuro. Las 48 h de RN-05 se comprueban al registrar una solicitud de intercambio en US-009, mediante US-015.
- NFR: Autorización de propiedad en servidor; los reintentos no duplican publicaciones.

---

### US-008 — Ver los turnos publicados compatibles

> **Cambio D-18 (06/10/2026):** fuera de esta versión; la propuesta se hace directamente sobre un turno compatible (US-006 + US-009). Se conserva el identificador.

> Como empleado, quiero ver los turnos publicados por compañeros compatibles, para encontrar un cambio posible.

- **Necesidad:** encontrar contrapartida sin preguntar uno a uno.
- **Objetivo:** G01 · S-01
- **Prioridad:** Won't, fuera de esta versión (antes Must) — *valor:* US-006 la cubre tras D-18; *riesgo:* bajo; *dependencias:* necesitaría US-007.
- **Estimación:** consenso del 06/10/2026: **3 h-p** (individuales: PO 3 · SM 3 · TL 3 · QA 3).
- **Incertidumbre:** Baja
- **Predecesoras:** US-007 (funcional)
- **Plan inicial:** fuera de esta versión

**Criterios de aceptación**
- US-008-AC-01: Solo se listan turnos de empleados de la misma categoría y servicio (RN-03).
- US-008-AC-02: No aparecen turnos pasados, los propios ni aquellos que ya estén implicados en una solicitud activa.
- US-008-AC-03: Si no hay turnos compatibles, se muestra un mensaje que lo explica.

**Verificación y restricciones**
- Reglas: RN-03.
- NFR: Listado utilizable con teclado; no expone turnos fuera del servicio/categoría permitidos.

---

### US-009 — Proponer un intercambio  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** propuesta directa sobre un turno de un compañero compatible, sin publicación previa; se mantiene una única propuesta activa por turno.

> Como empleado, quiero proponer un intercambio ofreciendo uno de mis turnos a cambio de uno publicado, para cambiar un turno que no puedo hacer.

- **Necesidad:** formalizar el acuerdo entre dos empleados para que quede registrado y pueda validarse.
- **Objetivo:** G01 (autonomía) y G02 (la propuesta es el objeto sobre el que se validan las reglas).
- **Prioridad:** Must — *valor:* núcleo del producto; *riesgo:* medio, concentra los cambios de estado; *dependencias:* predecesora de aceptación, validaciones, estado y cancelación.
- **Estimación:** consenso del 06/10/2026: **8 h-p** (individuales: PO 7 · SM 8 · TL 5 · QA 8).
- **Incertidumbre:** Media
- **Predecesoras:** US-008 (funcional), US-015 (funcional), US-003 (técnica)
- **Plan inicial:** por replanificar tras D-18: con 8 h-p no cabe en ningún sprint desde IT-003 (ver catálogo, apartado 4)

**Criterios de aceptación**
- US-009-AC-01: Dado un turno publicado compatible, el empleado elige uno de sus turnos futuros y confirma; la solicitud queda en estado *Propuesta*.
- US-009-AC-02: Ambos empleados pueden abrir el detalle de su solicitud desde su calendario, con los dos turnos, el estado actual y la siguiente acción disponible. Solo sus participantes y el responsable del servicio pueden acceder a ella; el servidor rechaza el acceso de otros usuarios.
- US-009-AC-03: Ninguno de los dos turnos puede formar parte de otra solicitud activa. Una solicitud está activa mientras está en estado Propuesta o Aceptada, pendiente de aprobación. Si alguno está ocupado, el sistema rechaza la nueva propuesta y explica el motivo.
- US-009-AC-04: No se puede proponer sobre un turno propio.
- US-009-AC-05: Al registrar la propuesta se comprueban RN-03 y RN-05: misma categoría y servicio, y al menos 48 h hasta el inicio más temprano de los dos turnos. Si falla una, no se crea la solicitud ni se reservan los turnos; se indica la regla y el motivo.
- US-009-AC-06: Si llegan dos propuestas simultáneas sobre el mismo turno, solo una se registra. La otra no ocupa turnos ni crea una solicitud y recibe un mensaje indicando que el turno ya no está disponible.
- US-009-AC-07: El detalle básico sigue siendo accesible cuando la solicitud termina; muestra el estado final, quién realizó la última acción y cuándo, y el motivo si hubo rechazo del responsable. Esta consulta forma parte del flujo esencial y funciona sin US-019.

**Reglas:** RN-03 (compatibilidad), RN-05 (antelación), RN-01, RN-02, RN-04 y RN-06 se validan en EP-004.

**Estados:** la publicación está Disponible, Ocupada por una solicitud o Cerrada. La solicitud nace como Propuesta; pasa a Aceptada (pendiente de aprobación), Aprobada o Rechazada. Puede quedar Caducada al comenzar el primero de sus turnos, o Cancelada si se incorpora US-011. Publicada describe una oferta de turno, no una solicitud.

**Verificación y restricciones**
- NFR: NFR-001 (autorización por rol: solo empleados participantes o su responsable acceden), NFR-004 (interfaz accesible por teclado), NFR-005 (mensajes claros con regla y motivo ante rechazo por RN-03 o RN-05), NFR-007 (creación atómica y consistente ante concurrencia, RT-02) y NFR-009 (compatibilidad de navegadores).
- Restricción: intercambio uno a uno, sin cesiones.

**Ejemplos**
- Ana publica su tarde del jueves; Luis ofrece su mañana del viernes → solicitud *Propuesta* entre Ana y Luis.

**Casos límite**
- Dos empleados proponen a la vez sobre el mismo turno publicado: solo una propuesta puede quedar activa.
- El turno publicado se cancela mientras Luis está proponiendo.
- Luis ofrece un turno que empieza en menos de 48 h: RN-05 rechaza la propuesta sin reservar los turnos.

**Supuestos**
- Cada turno admite una sola propuesta activa. El turno publicado y el ofrecido quedan reservados hasta resolver la solicitud. Si se rechaza o cancela, se liberan; si se aprueba, se cierran las publicaciones de ambos turnos. Una publicación liberada puede recibir otra propuesta si aún cumple las condiciones para intercambiarse.
- No se permite contraoferta: si no interesa, se rechaza y se propone de nuevo.

---

### US-010 — Responder a una propuesta

> Como empleado, quiero aceptar o rechazar una propuesta recibida, para cerrar el acuerdo con mi compañero.

- **Necesidad:** el acuerdo requiere el consentimiento de los dos empleados.
- **Objetivo:** G01 · M01/S-03
- **Prioridad:** Must — *valor:* cierra la parte del empleado del flujo (M01); *riesgo:* bajo; *dependencias:* predecesora de la bandeja del responsable.
- **Estimación:** consenso del 06/10/2026: **3 h-p** (individuales: PO 3 · SM 5 · TL 3 · QA 3).
- **Incertidumbre:** Baja
- **Predecesoras:** US-009 (funcional), US-015 (funcional)
- **Plan inicial:** por replanificar tras D-18 (ver catálogo, apartado 4)

**Criterios de aceptación**
- US-010-AC-01: Al aceptar, la solicitud pasa a *Aceptada* y queda pendiente de aprobación.
- US-010-AC-02: Al rechazar, la solicitud pasa a *Rechazada*, se liberan ambos turnos y las publicaciones que sigan vigentes vuelven a estar disponibles.
- US-010-AC-03: Una propuesta solo puede aceptarse antes del inicio más temprano de sus turnos. Puede aceptarse a menos de 48 h de ese inicio si se registró con la antelación exigida; al llegar el inicio queda Caducada.
- US-010-AC-04: Solo el destinatario de una propuesta puede responderla. Su respuesta se refleja en el detalle básico de ambos empleados con fecha y autor; repetir la misma acción no cambia dos veces el estado.

**Verificación y restricciones**
- Reglas: RN-05.
- NFR: Respuesta autorizada e indivisible; el reintento no duplica la aceptación.

---

### US-011 — Cancelar una publicación o propuesta

> Como empleado, quiero cancelar mi publicación o propuesta mientras no esté aprobada, para retirar un cambio que ya no necesito.

- **Necesidad:** los planes cambian; sin cancelación quedan solicitudes huérfanas.
- **Objetivo:** G01 · S-01
- **Prioridad:** Should — *valor:* medio; *riesgo:* bajo; *dependencias:* ninguna historia depende de ella.
- **Estimación:** consenso del 06/10/2026: **3 h-p** (individuales: PO 3 · SM 3 · TL 2 · QA 3).
- **Incertidumbre:** Baja
- **Predecesoras:** US-007 (funcional), US-009 (funcional)
- **Plan inicial:** sin sprint asignado (entra si hay capacidad)

**Criterios de aceptación**
- US-011-AC-01: El autor puede retirar su publicación Disponible; cualquiera de los dos participantes puede cancelar una solicitud Propuesta o Aceptada antes de aprobarse. Cancelar registra autor y fecha y actualiza el detalle básico de ambos.
- US-011-AC-02: No se puede cancelar una solicitud Aprobada, Rechazada o Caducada, ni actuar sobre publicaciones o solicitudes ajenas.
- US-011-AC-03: Cancelar una solicitud libera ambos turnos; las publicaciones que sigan vigentes vuelven a estar disponibles. Cancelar una publicación la retira del listado.

- **Reglas y límites:** Solo autor de publicación o participante de solicitud; estados permitidos. Se aplican los límites comunes de la épica.
- NFR: Cancelación autorizada e indivisible; las solicitudes ajenas no se modifican.
