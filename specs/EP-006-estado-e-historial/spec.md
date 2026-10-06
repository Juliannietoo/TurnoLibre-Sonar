# EP-006 — Vistas ampliadas de estado e historial

**Objetivos:** G01, G03
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** mejoras de presentación del estado y del historial (S-03). La consulta básica ya forma parte de US-009, US-010, US-017 y US-018. No incluye notificaciones por correo, SMS o push (EX-04).

## Resultado de la épica

El empleado puede consultar juntas sus solicitudes y el responsable recorrer una cronología ampliada. Estas mejoras facilitan la consulta de información que ya conserva el flujo básico.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-019 — Consultar una vista unificada de mis solicitudes

> Como empleado, quiero ver todas mis solicitudes juntas y agrupadas por estado, para revisarlas sin abrir cada turno del calendario.

- **Necesidad:** agilizar la consulta cuando existen varias solicitudes.
- **Objetivo:** G01 · S-03
- **Prioridad:** Should — *valor:* mejora la comodidad; *riesgo:* bajo; *dependencias:* utiliza la consulta básica de US-009/010/018 y habilita US-021. Su ausencia no impide conocer el estado de cada solicitud.
- **Estimación:** PO individual: **3 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker.
- **Incertidumbre:** Baja
- **Predecesoras:** US-009 (funcional), US-010 (funcional), US-018 (funcional)
- **Plan inicial:** candidata IT-006, solo si hay capacidad después de las Must.

**Criterios de aceptación**
- US-019-AC-01: El empleado dispone de una pantalla unificada de sus solicitudes, agrupadas en activas (Propuesta y Aceptada) y terminadas (Aprobada, Rechazada, Caducada y, si existe US-011, Cancelada), ordenadas por última actividad.
- US-019-AC-02: Cada elemento muestra los turnos y el estado, y enlaza al detalle básico existente, incluido el motivo de rechazo del responsable. Las publicaciones sin solicitud permanecen en el calendario.

- **Reglas y límites:** Solo solicitudes propias; estados del flujo básico. Se aplican los límites comunes de la épica.
- NFR: Vista navegable con teclado y estados identificados con texto.

---

### US-020 — Consultar una cronología ampliada de intercambios

> Como responsable, quiero ver en una cronología los eventos de cada solicitud de mi servicio, para seguir visualmente su evolución.

- **Necesidad:** facilitar la lectura de la secuencia de acciones ya registrada por el flujo básico.
- **Objetivo:** G03 · S-03
- **Prioridad:** Should — *valor:* mejora la lectura del historial; *riesgo:* bajo; *dependencias:* amplía US-017/018. La lista y el detalle básicos de las decisiones ya están incluidos en US-017.
- **Estimación:** PO individual: **3 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker.
- **Incertidumbre:** Baja
- **Predecesoras:** US-017 (funcional), US-018 (funcional)
- **Plan inicial:** sin sprint asignado (entra si hay capacidad)

**Criterios de aceptación**
- US-020-AC-01: El responsable ve los eventos registrados de una solicitud en orden temporal, con acción, autor y fecha; una propuesta aún no aceptada no muestra una aceptación inventada.
- US-020-AC-02: La cronología coincide con el detalle básico y solo es accesible al responsable del servicio. La cancelación aparece únicamente si se incorpora US-011.

- **Reglas y límites:** Solo solicitudes del servicio; no inventar eventos no ocurridos. Se aplican los límites comunes de la épica.
- NFR: Eventos legibles en orden temporal; acceso limitado por servicio en el servidor.

---

### US-021 — Recibir avisos dentro de la aplicación

> Como empleado, quiero recibir un aviso dentro de la aplicación cuando cambie el estado de una solicitud, para no tener que revisarla constantemente.

- **Necesidad:** Avisar de cambios sin exigir consultas repetidas.
- **Objetivo:** G01

- **Prioridad:** Could — *valor:* comodidad; *riesgo:* medio; *dependencias:* necesita US-019.
- **Estimación:** PO individual: **4 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker.
- **Incertidumbre:** Media
- **Predecesoras:** US-019 (funcional)
- **Plan inicial:** fuera del plan salvo capacidad sobrante

**Criterios de aceptación**
- US-021-AC-01: Al entrar, el empleado ve un indicador con los cambios de estado desde su última visita.

- **Reglas y límites:** Solo cambios en solicitudes del usuario; avisos internos. Se aplican los límites comunes de la épica.
- NFR: Un evento genera como máximo un aviso por destinatario.

---

### US-022 — Filtrar el historial

> Como responsable, quiero filtrar el historial por empleado y fechas, para encontrar un cambio concreto.

- **Necesidad:** Localizar decisiones concretas cuando crezca el historial; el volumen de demostración permite aplazarlo.
- **Objetivo:** G03

- **Prioridad:** Won't — *valor:* bajo con pocos datos; *riesgo:* bajo; *dependencias:* ampliaría US-020 sin ser necesaria para el historial básico.
- **Estimación:** PO individual: **2 h-p**, confirmada el 02/10/2026; consenso pendiente de Planning Poker. Referencia para versión futura; excluida de la entrega.
- **Incertidumbre:** Baja
- **Plan inicial:** fuera de esta versión.
- **Predecesoras:** US-020 (funcional)

**Criterios de aceptación para una versión futura**
- US-022-AC-01: El responsable puede limitar las decisiones de su servicio por empleado y por un intervalo de fechas inclusivo.
- US-022-AC-02: Un intervalo cuyo inicio sea posterior al fin se rechaza con un mensaje; cero coincidencias muestra una lista vacía, sin ocultar un error de permisos.

- **Reglas y límites:** Solo historial del servicio; fuera de esta versión. Se aplican los límites comunes de la épica.
- NFR: El filtro mantiene los permisos de servicio y es utilizable con teclado.
