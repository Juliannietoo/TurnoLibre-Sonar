# EP-004 — Validación de reglas

**Objetivos:** G02
**Línea base:** requisitos-v0-borrador · revisión 01/10/2026 · reglas de [reglas de negocio](../product/business-rules.md) v0.2
**Límites:** comprobación en el servidor de RN-01 a RN-06 sobre el cuadrante resultante de los dos empleados (S-02). No incluye reglas de convenios reales ni cómputo anual de jornada.

## Resultado de la épica

Ningún intercambio que incumpla una regla puede aprobarse, y el empleado entiende por qué (métrica M02, principio 4 de la constitución).

**Criterio común:** la aprobación comprueba todas las reglas en el servidor. Cada fallo identifica la regla y el motivo con los datos relevantes; esta explicación básica está incluida en US-012…US-015. La reutilización técnica de validadores queda a revisión del TL.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-012 — Validar descanso mínimo y solapes  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** sin cambio de hora: los datos de demostración no incluyen esas semanas.

> Como responsable, quiero que el sistema compruebe el descanso mínimo entre turnos y que no haya solapes, para no aprobar cambios que los incumplan.

- **Necesidad:** el descanso entre turnos es el error más frecuente de los cambios pactados informalmente.
- **Objetivo:** G02 · M02
- **Prioridad:** Must — *valor:* regla central del dominio; *riesgo:* alto (RT-01), conviene abordarla pronto; *dependencias:* crea el módulo de validación que reutilizan US-013 y US-014.
- **Estimación:** consenso del 06/10/2026: **8 h-p** (individuales: PO 7 · SM 8 · TL 8 · QA 8); revisada por D-18: **5 h-p**, votada por el equipo.
- **Incertidumbre:** Alta
- **Predecesoras:** US-009 (funcional), US-003 (técnica)
- **Plan inicial:** IT-003 · R2

**Criterios de aceptación**
- US-012-AC-01: Si entre el fin de un turno y el inicio del siguiente del mismo empleado hay menos de 12 h, el intercambio se marca inválido por RN-01.
- US-012-AC-02: Si el intercambio deja a un empleado con dos turnos solapados o con dos turnos con la misma fecha de inicio, se marca inválido por RN-06.
- US-012-AC-03: Se comprueban los dos empleados, incluidos los turnos anteriores y posteriores a los intercambiados.
- US-012-AC-04: Una petición que se salte la interfaz también es rechazada por el servidor.

**Reglas:** RN-01 (12 h), RN-06 (sin solapes; la noche cuenta en la fecha en que empieza).

**Verificación y restricciones**
- Pruebas automatizadas con todos los casos de [reglas de negocio](../product/business-rules.md) para RN-01 y RN-06.
- NFR: NFR-001 (validación forzosa en el servidor sin posibilidad de omisión), NFR-005 (mensajes claros con indicación de RN-01/RN-06 y horas de descanso resultantes) y NFR-006 (tiempo de validación < 500 ms).

**Ejemplos** (de [reglas de negocio](../product/business-rules.md))

| Caso | Resultado |
|---|---|
| Ana, noche del lunes (acaba martes 08:00) → recibe mañana del martes | Inválido, 0 h de descanso |
| Ana, noche del lunes → recibe tarde del martes | Inválido, 7 h |
| Ana, noche del lunes → recibe noche del martes | Cumple RN-01, 14 h; el intercambio debe superar también las demás reglas |

**Casos límite**
- Exactamente 12 h de descanso (válido).
- Turno de noche del domingo que termina el lunes: el descanso se mide desde su fin real del lunes, no desde la fecha de inicio.
- Si se conoce que no existe un turno anterior, no se inventa uno; se comprueba el siguiente. Si faltan datos necesarios para validar un turno existente, se bloquea la aprobación y se indica el dato ausente.

**Supuestos**
- Los horarios de turno son fijos (M 08–15, T 15–22, N 22–08).

---

### US-013 — Validar las horas semanales  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** pasa a Should; G02 deja de exigir RN-02 en el MVP.

> Como responsable, quiero que el sistema compruebe que ningún empleado supera 40 h en una semana natural tras el intercambio, para respetar el límite interno de jornada.

- **Necesidad:** cambiar una mañana (7 h) por una noche (10 h) puede superar el límite sin que nadie lo note.
- **Objetivo:** G02 · M02
- **Prioridad:** Should (antes Must) — *valor:* G02 exige cubrir RN-01 a RN-06; *riesgo:* alto por el reparto de la noche entre semanas; *dependencias:* reutiliza el módulo de US-012.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 6 · SM 5 · TL 8 · QA 5); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Alta
- **Predecesoras:** US-009 (funcional), US-003 (técnica), US-012 (técnica) Reutilización de US-012 a revisar por TL.
- **Plan inicial:** sin compromiso; tras las Must

**Criterios de aceptación**
- US-013-AC-01: Si tras el intercambio un empleado supera 40 h en alguna semana natural afectada, el intercambio se marca inválido por RN-02.
- US-013-AC-02: Un turno de noche que cruza de domingo a lunes reparte sus horas entre ambas semanas.
- US-013-AC-03: Se comprueban todas las semanas afectadas de los dos empleados.

**Reglas:** RN-02 (40 h por semana natural, lunes a domingo).

**Verificación y restricciones**
- Pruebas automatizadas con los casos de RN-02 de [reglas de negocio](../product/business-rules.md).

**Ejemplos**
- Ana tiene 38 h; cede una mañana (7 h) y recibe una noche (10 h) → 41 h → inválido.
- Ana tiene 38 h; cede una noche (10 h) y recibe una tarde (7 h) → 35 h → cumple RN-02, sujeto a las demás reglas.

**Casos límite**
- Exactamente 40 h (válido).
- Semana con retraso de una hora: 30 h de otros turnos más una noche de 11 h dentro de esa semana suman 41 h y se rechazan; 29 h más esa noche suman 40 h y cumplen RN-02.
- Noche del domingo: 2 h cuentan en la semana del domingo y 8 h en la siguiente.
- Intercambio entre turnos de semanas distintas: se revisan las dos semanas.

**Supuestos**
- Solo cuentan horas de turno; no hay horas extra ni guardias.
- Los ejemplos de noches de 10 h corresponden a noches ordinarias. Se suman horas realmente transcurridas, repartidas por semanas locales de Europe/Madrid: una noche con retraso de una hora aporta 11 h y con adelanto, 9 h. El TL concreta su implementación.
- NFR: NFR-001 (validación en servidor), NFR-005 (mensajes de rechazo claros indicando horas acumuladas y superación de 40 h de RN-02) y NFR-006 (cálculo determinista en < 500 ms).

---

### US-014 — Validar categoría, servicio y cobertura  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** en cada intercambio solo se comprueba RN-03; RN-04 se comprueba al preparar los datos (US-003). Los intercambios siguen siendo uno a uno dentro de la misma categoría y servicio, por lo que la cobertura se conserva.

> Como responsable, quiero que solo se permitan intercambios entre empleados de la misma categoría y servicio y que se mantenga la cobertura mínima, para que ningún turno quede desatendido.

- **Necesidad:** que un turno quede sin el personal mínimo es el riesgo más grave para el hospital.
- **Objetivo:** G02 · M02
- **Prioridad:** Must — *valor:* protege la cobertura; *riesgo:* medio; *dependencias:* reutiliza el módulo de US-012.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 4 · SM 5 · TL 5 · QA 5); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Media
- **Predecesoras:** US-009 (funcional), US-003 (técnica), US-012 (técnica) Reutilización de US-012 a revisar por TL.
- **Plan inicial:** por replanificar tras D-18 (ver catálogo, apartado 4)

**Criterios de aceptación**
- US-014-AC-01: Un intercambio entre empleados de distinta categoría o servicio se marca inválido por RN-03.
- US-014-AC-02: Si tras el intercambio alguna franja de un servicio queda por debajo de 3/3/2, se marca inválido por RN-04.

**Reglas:** RN-03, RN-04 (mañana 3, tarde 3, noche 2 por servicio).

**Verificación y restricciones**
- Pruebas automatizadas con los casos de RN-03 y RN-04.

**Ejemplos**
- Una enfermera y un celador intentan intercambiar → inválido por RN-03.
- Dos empleados de la misma categoría y servicio intercambian y se conserva 3/3/2 → cumple RN-03/RN-04, sujeto a las demás reglas.
- Dos empleados compatibles intentan intercambiar con un cuadrante que solo tiene una persona en una noche afectada → RN-04 bloquea la aprobación e indica el déficit.

**Casos límite**
- Con RN-03 cumplida, un intercambio uno a uno no cambia la cobertura; RN-04 protege frente a datos inconsistentes (cuadrante que ya estaba por debajo del mínimo).
- Cobertura exactamente 3/3/2: cumple RN-04; 3/3/1: incumple RN-04. Una categoría o servicio inexistente impide validar la solicitud.

**Supuestos**
- El cuadrante inicial cumple 3/3/2 (US-003).
- NFR: NFR-001 (validación forzosa en servidor), NFR-005 (mensajes claros con motivo y regla ante categoría distinta o déficit de cobertura) y NFR-006 (rendimiento de validación en < 500 ms). Datos incompletos bloquean la aprobación con motivo.

---

### US-015 — Validar la antelación mínima

> **Cambio D-18 (06/10/2026):** pasa a Should; G02 deja de exigir RN-05 en el MVP.

> Como responsable, quiero que no se admitan solicitudes con menos de 48 h de antelación, para tener tiempo de resolverlas.

- **Necesidad:** evitar cambios de última hora imposibles de gestionar.
- **Objetivo:** G02 · M02
- **Prioridad:** Should (antes Must) — *valor:* garantiza el plazo de G02; *riesgo:* bajo; *dependencias:* debe estar disponible al registrar una propuesta en US-009.
- **Estimación:** consenso del 06/10/2026: **3 h-p** (individuales: PO 2 · SM 3 · TL 3 · QA 2).
- **Incertidumbre:** Baja
- **Predecesoras:** US-003 (técnica) El formato de solicitud se acuerda con US-009, sin requerir esa historia terminada.
- **Plan inicial:** sin compromiso; tras las Must

**Criterios de aceptación**
- US-015-AC-01: Al registrar una solicitud, el servidor exige al menos 48 h hasta el inicio más temprano de los dos turnos. Exactamente 48 h se admite; 47 h y 59 min se rechaza, indicando RN-05 y la antelación disponible.
- US-015-AC-02: Una solicitud registrada a tiempo puede aceptarse y aprobarse hasta antes de ese inicio, aunque ya resten menos de 48 h. Al llegar el inicio queda Caducada y no puede aceptarse ni aprobarse.
- US-015-AC-03: La caducidad actualiza el detalle básico de ambos empleados y libera los turnos; solo las publicaciones que aún sean futuras quedan disponibles. La comprobación usa la hora del servidor y no depende de que alguien abra la pantalla.

**Reglas:** RN-05.
- NFR: Plazos comprobados con la hora del servidor, aunque se manipule el navegador.

---

### US-016 — Ampliar el diagnóstico de reglas

> Como empleado, quiero ver juntas todas las reglas incumplidas y orientaciones para corregir mi propuesta, para encontrar otra opción más fácilmente.

- **Necesidad:** ampliar la explicación básica que ya devuelve cada validación.
- **Objetivo:** G01 y G02
- **Prioridad:** Should — *valor:* mejora la autonomía (G01); *riesgo:* bajo; *dependencias:* necesita todas las validaciones. El mensaje básico con regla y motivo forma parte de las Must.
- **Estimación:** consenso del 06/10/2026: **2 h-p** (individuales: PO 2 · SM 5 · TL 2 · QA 2).
- **Incertidumbre:** Baja
- **Predecesoras:** US-012 (funcional), US-013 (funcional), US-014 (funcional), US-015 (funcional)
- **Plan inicial:** candidata IT-006 · R3, solo si hay capacidad después de las Must.

**Criterios de aceptación**
- US-016-AC-01: Si se incumplen varias reglas, se muestran juntas con los resultados que justifican cada fallo.
- US-016-AC-02: Cada fallo incluye una orientación concreta, como buscar un turno que deje al menos 12 h de descanso. La orientación no promete que el intercambio cumpla las demás reglas.

**Verificación y restricciones**
- NFR: mensajes accesibles y comprensibles (usabilidad).

- **Reglas y límites:** RN-01…RN-06; no añade reglas ni sustituye los mensajes básicos. Se aplican los límites comunes de la épica.
