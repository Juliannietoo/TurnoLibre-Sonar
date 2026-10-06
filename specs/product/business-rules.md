# TurnoLibre — Reglas de negocio

Versión 0.2 · 24/09/2026 · Validada por Lucansado (Product Owner) el 28/09/2026 tras la revisión de PaulaJCruz ([PR #1](https://github.com/UniExtremadura/TurnoLibre_GC02/pull/1)).

> **Ajuste de alcance D-18 (06/10/2026):** las seis reglas se mantienen definidas, pero en el MVP se comprueban en el servidor **RN-01, RN-03 y RN-06**; **RN-04** se garantiza al preparar el cuadrante de demostración (los intercambios uno a uno dentro de la misma categoría y servicio no alteran la cobertura); **RN-02 y RN-05** pasan a Should (US-013, US-015). Los datos de demostración no incluyen semanas con cambio de hora (supuesto A-05 de `goals.md`).

Reglas que el sistema comprueba **en el servidor** antes de que un intercambio pueda aprobarse (constitución, principio 4). Son reglas **ficticias**, definidas por el equipo e **inspiradas** en la normativa laboral española, simplificadas para el proyecto. No describen por sí solas el régimen laboral de un hospital real: el [art. 34.1 del Estatuto de los Trabajadores](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430) expresa las 40 h semanales como promedio en cómputo anual; aquí RN-02 fija deliberadamente un máximo estricto en cada semana natural.

## Turnos del Hospital Comarcal Vega Alta (ficticio)
| Turno | Horario | Duración |
|---|---|---|
| Mañana (M) | 08:00 – 15:00 | 7 h |
| Tarde (T) | 15:00 – 22:00 | 7 h |
| Noche (N) | 22:00 – 08:00 (del día siguiente) | 10 h |

Los horarios y las semanas naturales se interpretan en la zona **Europe/Madrid**. Las duraciones de la tabla corresponden a días sin cambio de hora. RN-01, RN-02 y RN-05 usan tiempo realmente transcurrido: una noche con retraso de una hora dura 11 h y con adelanto dura 9 h. RN-06 utiliza la fecha local de inicio. Precisión del PO para H2, 01/10/2026.

## Reglas
| ID | Regla | Valor | Referencia |
|---|---|---|---|
| RN-01 | Descanso mínimo entre el fin de un turno y el inicio del siguiente del mismo empleado | **12 h** | Estatuto de los Trabajadores, art. 34.3 |
| RN-02 | Horas máximas por empleado en una semana natural (lunes a domingo) | **40 h** | Límite interno ficticio, más estricto que el promedio anual del ET art. 34.1 |
| RN-03 | Solo pueden intercambiar turno dos empleados de la **misma categoría profesional y el mismo servicio** | — | Garantiza que la cobertura por perfil no cambia |
| RN-04 | Tras el intercambio, cada turno de cada servicio mantiene su **cobertura mínima** | Mañana 3 · Tarde 3 · Noche 2 empleados por servicio | Valores ficticios de la organización |
| RN-05 | Antelación mínima de la solicitud respecto al primero de los turnos afectados | **48 h** | Da tiempo al responsable para resolver |
| RN-06 | Un empleado no puede tener dos turnos que se solapen, ni dos turnos con la misma fecha de inicio | — | Coherencia del calendario |

## Criterios de aplicación
- Se comprueba el cuadrante resultante **de ambos empleados**, incluidos los turnos anteriores y posteriores a los intercambiados. La validación se repite antes de la aprobación del responsable, por si el cuadrante ha cambiado.
- RN-02 suma horas efectivamente trabajadas dentro de cada semana natural. Un turno de noche que cruza el domingo se reparte entre ambas semanas. Se comprueban todas las semanas afectadas para los dos empleados.
- RN-04 se calcula por servicio, fecha y franja; el conjunto de datos de demostración debe partir de un cuadrante que cumpla 3/3/2. En una semana sin cambio de hora supone 434 h de cobertura por servicio (436 h con retraso de una hora y 432 h con adelanto) y un mínimo teórico de 11 empleados si ninguno supera 40 h. En un intercambio uno a uno dentro del mismo servicio y categoría, la cobertura debe permanecer igual; la comprobación protege también frente a datos inconsistentes.
- RN-05 se mide al registrar la solicitud respecto al inicio más temprano de los dos turnos. La aceptación y la aprobación deben ocurrir antes de ese inicio; las solicitudes caducadas no pueden aprobarse.
- RN-06 asigna a la noche la fecha en que empieza (22:00), aunque termine al día siguiente. Esta regla se aplica además de RN-01.

## Casos de ejemplo
| Caso | Resultado | Motivo |
|---|---|---|
| Ana (noche del lunes, termina el martes a las 08:00) acepta la mañana del martes de Luis | Rechazado | RN-01: solo hay 0 h de descanso |
| Ana acepta la tarde del martes de Luis tras su noche del lunes | Rechazado | RN-01: 7 h de descanso (08:00 → 15:00) |
| Ana acepta la noche del martes de Luis tras su noche del lunes | Válido | RN-01: 14 h de descanso (08:00 → 22:00) |
| Ana (38 h en la semana) cede una mañana (7 h) y recibe una noche (10 h) en la misma semana | Rechazado | RN-02: 38 − 7 + 10 = 41 h > 40 h |
| Una enfermera y un celador intercambian turnos | Rechazado | RN-03: categorías distintas |
| Solicitud creada 24 h antes del turno | Rechazado | RN-05: antelación inferior a 48 h |

Estos casos forman la base de la suite de casos de regla de la métrica M02 (`goals.md`).

## Mensajes al usuario
Cada rechazo indica **qué regla** se incumple y **por qué** en lenguaje claro (p. ej. "Entre tu turno de noche y este turno solo tendrías 7 h de descanso; el mínimo es 12 h"), según la experiencia *Recuperable* de `mission.md`.
