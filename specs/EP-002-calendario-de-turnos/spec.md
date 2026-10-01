# EP-002 — Calendario de turnos

**Objetivos:** G01
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026
**Límites:** consulta del calendario propio y de turnos compatibles. No incluye generación automática del cuadrante (EX-03) ni control horario o fichaje (EX-01).

## Resultado de la épica

El empleado sabe en todo momento qué turnos tiene y cuáles podría intercambiar.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales se describen aquí por su comportamiento; QA asignará los IDs del catálogo compartido.

## Historias

### US-005 — Consultar mi calendario de turnos

> Como empleado, quiero ver mi calendario mensual de turnos, para saber qué días trabajo y qué turno puedo ofrecer.

- **Necesidad:** es el punto de partida de cualquier intercambio.
- **Objetivo:** G01 · S-03
- **Prioridad:** Must — *valor:* primer paso del flujo esencial (G01); *riesgo:* bajo; *dependencias:* predecesora de publicar un turno.
- **Estimación:** pendiente de Planning Poker (h-p)
- **Incertidumbre:** Baja
- **Predecesoras:** US-002 (funcional), US-003 (técnica)
- **Plan inicial:** IT-002 · R1

**Criterios de aceptación**
- US-005-AC-01: El empleado ve sus turnos del mes actual con fecha, franja (M/T/N) y servicio.
- US-005-AC-02: Puede avanzar y retroceder de mes.
- US-005-AC-03: Los turnos implicados en una solicitud pendiente aparecen marcados.

**Verificación y restricciones**
- NFR: accesibilidad del calendario (navegable con teclado, no depende solo del color).
- Restricción: el turno de noche se muestra en la fecha en que empieza (criterio de RN-06).

- **Reglas y límites:** Solo calendario propio; RN-06 fecha el turno nocturno por su inicio. Se aplican los límites comunes de la épica.

---

### US-006 — Consultar los turnos de compañeros compatibles

> Como empleado, quiero ver los turnos de compañeros de mi categoría y servicio, para saber con quién podría cambiar aunque no los hayan publicado.

- **Necesidad:** facilita encontrar un cambio antes de publicar.
- **Objetivo:** G01 · S-03
- **Prioridad:** Could — *valor:* medio, US-008 ya muestra los turnos publicados; *riesgo:* expone el cuadrante de otros (privacidad); *dependencias:* ninguna historia depende de ella.
- **Estimación:** pendiente de Planning Poker (h-p)
- **Incertidumbre:** Baja
- **Predecesoras:** US-005 (funcional)
- **Plan inicial:** fuera del plan salvo capacidad sobrante

**Criterios de aceptación**
- US-006-AC-01: Solo se muestran compañeros de la misma categoría y servicio (RN-03).
- US-006-AC-02: No se muestran datos personales más allá del nombre ficticio y el turno.

**Verificación y restricciones**
- Reglas: RN-03.
- NFR: privacidad (mínimo de datos visibles).
