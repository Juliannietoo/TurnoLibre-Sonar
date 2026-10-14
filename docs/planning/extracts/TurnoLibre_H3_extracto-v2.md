# TurnoLibre · Extracto de la planificación inicial H3 (v2)

Extracto en Markdown de `docs/planning/TurnoLibre_H3_planificacion.xlsx` (versión 2, 14/10/2026) para el Planning Agent (AG-03), que no puede leer ficheros .xlsx. Mismos datos que el libro; los valores son los que calculan sus fórmulas.

- Horizonte: 6 iteraciones de una semana (miércoles a martes), 21/10/2026–01/12/2026, 3 releases (D-19).
- Dedicación: 6 h/semana por persona (D-21). Capacidad: `efectiva = max(0, nominal − ausencias − reuniones − coordinación) × (1 − margen)`.
- Alcance comprometido: las 11 historias Must del catálogo V1 (46 h-p, estimación consensuada tras D-18). Should, Could y Won't sin compromiso.
- Regla del enunciado: ninguna persona puede tener asignadas más horas que su capacidad efectiva en una iteración.
- Decisiones de planificación SM/TL (14/10/2026): US-023 se divide en 1,5 h (IT-005) y 0,5 h (IT-006) y mantiene su dependencia de US-018; el diseño de la transacción de US-018 (1,5 h, TL) se adelanta a IT-005 dentro de sus 8 h-p; US-011 no se compromete; TK-001 queda condicionada a las tecnologías autorizadas.
- Cambios de la versión 2 (D-24, decisiones del equipo sobre el informe v01 del Planning Agent): excepción explícita a «cabe en un sprint» para US-018 y US-023, cuya parte de IT-005 es preparación; la dependencia US-023 → US-018 se aplica a la parte 2 (validación final) y la parte 1 solo necesita US-001 a US-003 (IPR-001/002). TK-007 comprueba RN-01, RN-02, RN-04 y RN-06 (IPR-009). US-005-AC-03 pasa a US-009 como US-009-AC-09 y US-009 añade US-005 como predecesora (IPR-010). Tareas del PO renombradas (IPR-011). US-018 en IT-006: TL 1,5 · QA 2 · SM 1,5 · PO 1,5 (IPR-012). Parte 2 de US-023 al PO (IPR-014). De la sesión de los miércoles (2 h) se descuenta 1 h de ceremonias; la otra hora es trabajo del proyecto (IPR-005).

## 1. Capacidad efectiva por persona e iteración (h)

| Persona | Rol | Coordinación | Margen | Ausencias por iteración | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Lucansado | PO | 0,50 h | 20 % | 1 · 2 · 0 · 1 · 1 · 1 | 2,40 | 1,60 | 3,20 | 2,40 | 2,40 | 2,40 | 14,40 |
| PaulaJCruz | SM | 1,00 h | 10 % | 1 · 2 · 0 · 1 · 1 · 1 | 2,25 | 1,35 | 3,15 | 2,25 | 2,25 | 2,25 | 13,50 |
| MarvelinoGG | TL | 1,00 h | 15 % | 0 · 1 · 0 · 1 · 1 · 1 | 2,98 | 2,13 | 2,98 | 2,13 | 2,13 | 2,13 | 14,45 |
| Juliannietoo | QA | 0,50 h | 15 % | 1 · 2 · 0 · 1 · 1 · 1 | 2,55 | 1,70 | 3,40 | 2,55 | 2,55 | 2,55 | 15,30 |
| **Equipo** | | | | | **10,18** | **6,78** | **12,73** | **9,33** | **9,33** | **9,33** | **57,65** |

Nominal: 6 h × 4 personas × 6 semanas = 144 h. Reuniones 1,5 h/semana por persona.

## 2. Catálogo y plan por historia

| ID | Historia | Épica | MoSCoW | Incert. | h-p | Iteración | Predecesoras del plan | Horas asignadas |
|---|---|---|---|---|---|---|---|---|
| US-001 | Preparar el entorno base | EP-001 | Must | Media | 5 | IT-001 | — | 5,00 |
| US-002 | Iniciar sesión con rol | EP-001 | Must | Media | 3 | IT-002 | US-001, US-003 | 3,00 |
| US-003 | Cargar los datos de demostración | EP-001 | Must | Media | 3 | IT-001 | US-001 | 3,00 |
| US-004 | Mantener los turnos del cuadrante | EP-001 | Could | Media | 5 | Sin compromiso | — | — |
| US-005 | Consultar mi calendario de turnos | EP-002 | Must | Baja | 3 | IT-002 | US-002, US-003 | 3,00 |
| US-006 | Consultar los turnos de compañeros compatibles | EP-002 | Must | Baja | 3 | IT-003 | US-005 | 3,00 |
| US-007 | Publicar un turno para cambiar | EP-003 | Won't | Baja | 3 | Fuera de versión | — | — |
| US-008 | Ver los turnos publicados compatibles | EP-003 | Won't | Baja | 3 | Fuera de versión | — | — |
| US-009 | Proponer un intercambio | EP-003 | Must | Media | 8 | IT-004 | US-006, US-005, US-003 | 8,00 |
| US-010 | Responder a una propuesta | EP-003 | Must | Baja | 3 | IT-005 | US-009 | 3,00 |
| US-011 | Cancelar una solicitud de intercambio | EP-003 | Should | Baja | 3 | Sin compromiso (si hay adelanto) | — | — |
| US-012 | Validar descanso mínimo y solapes | EP-004 | Must | Alta | 5 | IT-003 | US-003 | 5,00 |
| US-013 | Validar las horas semanales | EP-004 | Should | Alta | 3 | Sin compromiso | — | — |
| US-014 | Validar categoría, servicio y cobertura | EP-004 | Must | Media | 3 | IT-003 | US-003, US-012 | 3,00 |
| US-015 | Validar la antelación mínima | EP-004 | Should | Baja | 3 | Sin compromiso | — | — |
| US-016 | Ampliar el diagnóstico de reglas | EP-004 | Should | Baja | 2 | Sin compromiso | — | — |
| US-017 | Consultar solicitudes y decisiones del servicio | EP-005 | Fusionada | Media | — | Fusionada en US-018 | — | — |
| US-018 | Resolver una solicitud | EP-005 | Must | Alta | 8 | IT-005 (diseño) · IT-006 | US-010, US-012, US-014 | 8,00 |
| US-019 | Consultar una vista unificada de mis solicitudes | EP-006 | Should | Baja | 3 | Sin compromiso | — | — |
| US-020 | Consultar una cronología ampliada de intercambios | EP-006 | Should | Baja | 3 | Sin compromiso | — | — |
| US-021 | Recibir avisos dentro de la aplicación | EP-006 | Could | Media | 3 | Sin compromiso | — | — |
| US-022 | Filtrar el historial | EP-006 | Won't | Baja | 2 | Fuera de versión | — | — |
| US-023 | Crear el guion mínimo final de instalación y evaluación | EP-007 | Must | Baja | 2 | IT-005 · IT-006 | US-018 | 2,00 |
| US-024 | Prueba de usabilidad y accesibilidad básica | EP-007 | Should | Media | 3 | Sin compromiso | — | — |

## 3. Asignación por persona e iteración

IT-001 está detallada por tareas (TK); el resto, por historia.

| Historia | Tarea | Descripción | Persona | Iteración | Horas | Coste (€) |
|---|---|---|---|---|---|---|
| US-001 | TK-001 | Crear la estructura técnica y arquitectónica básica del proyecto con la tecnología autorizada (condicionada a su confirmación) | MarvelinoGG | IT-001 | 1,50 | 23,63 |
| US-001 | TK-002 | Integración continua: compilar y pasar las pruebas en cada push; bloquear la integración si falla | Juliannietoo | IT-001 | 1,50 | 30,38 |
| US-001 | TK-003 | Entorno de demostración y documentación del despliegue | Juliannietoo | IT-001 | 1,00 | 20,25 |
| US-001 | TK-004 | Prueba de humo y revisión de la base técnica | MarvelinoGG | IT-001 | 1,00 | 15,75 |
| US-003 | TK-005 | Diseñar el cuadrante ficticio: 1 servicio, categorías, cobertura 3/3/2, sin cambio de hora | Lucansado | IT-001 | 1,00 | 19,50 |
| US-003 | TK-006 | Script de carga y restablecimiento de los datos en un paso | PaulaJCruz | IT-001 | 1,50 | 37,13 |
| US-003 | TK-007 | Comprobar que el cuadrante cumple RN-01, RN-02, RN-04 y RN-06 (US-003-AC-02) | Lucansado | IT-001 | 0,50 | 9,75 |
| US-002 | — | Autenticación y roles en el servidor | MarvelinoGG | IT-002 | 2,00 | 31,50 |
| US-002 | — | Pruebas de acceso y autorización | Juliannietoo | IT-002 | 1,00 | 20,25 |
| US-005 | — | Calendario en lista: revisión y aceptación del PO | Lucansado | IT-002 | 1,50 | 29,25 |
| US-005 | — | Pantalla del calendario | PaulaJCruz | IT-002 | 1,00 | 24,75 |
| US-005 | — | Pruebas y accesibilidad con teclado | Juliannietoo | IT-002 | 0,50 | 10,13 |
| US-006 | — | Consulta de turnos compatibles y lista vacía | Lucansado | IT-003 | 2,00 | 39,00 |
| US-006 | — | Pantalla de turnos compatibles | PaulaJCruz | IT-003 | 1,00 | 24,75 |
| US-012 | — | Módulo de validación: RN-01 y RN-06 | MarvelinoGG | IT-003 | 2,50 | 39,38 |
| US-012 | — | Pruebas de reglas y casos límite | Juliannietoo | IT-003 | 2,50 | 50,63 |
| US-014 | — | Validación RN-03 en el módulo de reglas | PaulaJCruz | IT-003 | 2,00 | 49,50 |
| US-014 | — | Casos de prueba de compatibilidad | Lucansado | IT-003 | 0,50 | 9,75 |
| US-014 | — | Pruebas automáticas de RN-03 | Juliannietoo | IT-003 | 0,50 | 10,13 |
| US-009 | — | Reserva de turnos y transacción de la propuesta | MarvelinoGG | IT-004 | 2,00 | 31,50 |
| US-009 | — | Pruebas de concurrencia y caducidad | Juliannietoo | IT-004 | 2,00 | 40,50 |
| US-009 | — | Flujo de propuesta: revisión y aceptación del PO | Lucansado | IT-004 | 2,00 | 39,00 |
| US-009 | — | Pantalla de propuesta | PaulaJCruz | IT-004 | 2,00 | 49,50 |
| US-010 | — | Aceptar o rechazar: revisión y aceptación del PO | Lucansado | IT-005 | 1,50 | 29,25 |
| US-010 | — | Pantalla de respuesta | PaulaJCruz | IT-005 | 1,50 | 37,13 |
| US-018 | — | Parte 1: diseño de la transacción y la revalidación (mitigación del riesgo, decisión del TL) | MarvelinoGG | IT-005 | 1,50 | 23,63 |
| US-023 | — | Parte 1: guion de instalación con las cuentas de prueba | Juliannietoo | IT-005 | 1,50 | 30,38 |
| US-018 | — | Parte 2: implementación de la transacción y la revalidación | MarvelinoGG | IT-006 | 1,50 | 23,63 |
| US-018 | — | Pruebas de revalidación, caducidad y concurrencia | Juliannietoo | IT-006 | 2,00 | 40,50 |
| US-018 | — | Pantalla de pendientes y decisión con motivo | PaulaJCruz | IT-006 | 1,50 | 37,13 |
| US-018 | — | Flujo de decisión: revisión y aceptación del PO | Lucansado | IT-006 | 1,50 | 29,25 |
| US-023 | — | Parte 2: paso de aprobación y validación con el evaluador externo (coordina el PO) | Lucansado | IT-006 | 0,50 | 9,75 |

## 4. Carga frente a capacidad (h)

| Persona | Concepto | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total |
|---|---|---|---|---|---|---|---|---|
| Lucansado | Capacidad | 2,40 | 1,60 | 3,20 | 2,40 | 2,40 | 2,40 | 14,40 |
| Lucansado | Asignada | 1,50 | 1,50 | 2,50 | 2,00 | 1,50 | 2,00 | 11,00 |
| Lucansado | Diferencia | 0,90 | 0,10 | 0,70 | 0,40 | 0,90 | 0,40 | 3,40 |
| PaulaJCruz | Capacidad | 2,25 | 1,35 | 3,15 | 2,25 | 2,25 | 2,25 | 13,50 |
| PaulaJCruz | Asignada | 1,50 | 1,00 | 3,00 | 2,00 | 1,50 | 1,50 | 10,50 |
| PaulaJCruz | Diferencia | 0,75 | 0,35 | 0,15 | 0,25 | 0,75 | 0,75 | 3,00 |
| MarvelinoGG | Capacidad | 2,98 | 2,13 | 2,98 | 2,13 | 2,13 | 2,13 | 14,45 |
| MarvelinoGG | Asignada | 2,50 | 2,00 | 2,50 | 2,00 | 1,50 | 1,50 | 12,00 |
| MarvelinoGG | Diferencia | 0,48 | 0,13 | 0,48 | 0,13 | 0,63 | 0,63 | 2,45 |
| Juliannietoo | Capacidad | 2,55 | 1,70 | 3,40 | 2,55 | 2,55 | 2,55 | 15,30 |
| Juliannietoo | Asignada | 2,50 | 1,50 | 3,00 | 2,00 | 1,50 | 2,00 | 12,50 |
| Juliannietoo | Diferencia | 0,05 | 0,20 | 0,40 | 0,55 | 1,05 | 0,55 | 2,80 |
| **Equipo** | Capacidad | 10,18 | 6,78 | 12,73 | 9,33 | 9,33 | 9,33 | 57,65 |
| **Equipo** | Asignada | 8,00 | 6,00 | 11,00 | 8,00 | 6,00 | 7,00 | 46,00 |
| **Equipo** | Margen | 2,18 | 0,78 | 1,73 | 1,33 | 3,33 | 2,33 | 11,65 |

Sobrecargas persona × iteración: **0**. Trabajo Must sin asignar: **0 h**. Dependencias incumplidas según el libro: **0** (regla: cada predecesora empieza y termina en la misma iteración o antes).

## 5. Coste

| Persona | Rol | Coste/hora | Horas asignadas | Coste planificado | Horas nominales | Coste nominal |
|---|---|---|---|---|---|---|
| Lucansado | PO | 19,50 € | 11,00 | 214,50 € | 36 | 702,00 € |
| PaulaJCruz | SM | 24,75 € | 10,50 | 259,88 € | 36 | 891,00 € |
| MarvelinoGG | TL | 15,75 € | 12,00 | 189,00 € | 36 | 567,00 € |
| Juliannietoo | QA | 20,25 € | 12,50 | 253,13 € | 36 | 729,00 € |
| **Total** | | | 46,00 | 916,50 € | 144 | 2889,00 € |

| Iteración | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 |
|---|---|---|---|---|---|---|
| Coste planificado (€) | 156,38 | 115,88 | 223,13 | 160,50 | 120,38 | 140,25 |

Presupuesto (company.md, D-21): personal 2.889,00 € (144 h nominales) · equipos 115,38 € · software 30,00 € · gastos generales 15 % 433,35 € · coste 3.467,73 € · reserva 10 % 346,77 € · margen 15 % 572,18 € · precio sin IVA 4.386,68 € · IVA 21 % 921,20 € · **precio 5.307,88 € con IVA**.

## 6. Pendientes conocidos

- Tecnologías autorizadas por la asignatura sin confirmar (dependencia externa de US-001; TK-001 condicionada).
- Evaluador externo para US-023 (IT-006).
- Las iteraciones IT-002 a IT-006 se detallarán por tareas al planificar cada una.
