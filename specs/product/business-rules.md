# TurnoLibre — Reglas de negocio

Versión 0.1 · 23/09/2026 · Propuesta pendiente de validación por el Product Owner.

Reglas que el sistema comprueba **en el servidor** antes de que un intercambio pueda aprobarse (constitución, principio 4). Son reglas **ficticias**, definidas por el equipo e **inspiradas** en la normativa laboral española, simplificadas para el proyecto.

## Turnos del Hospital Comarcal Vega Alta (ficticio)
| Turno | Horario | Duración |
|---|---|---|
| Mañana (M) | 08:00 – 15:00 | 7 h |
| Tarde (T) | 15:00 – 22:00 | 7 h |
| Noche (N) | 22:00 – 08:00 (del día siguiente) | 10 h |

## Reglas
| ID | Regla | Valor | Referencia |
|---|---|---|---|
| RN-01 | Descanso mínimo entre el fin de un turno y el inicio del siguiente del mismo empleado | **12 h** | Estatuto de los Trabajadores, art. 34.3 |
| RN-02 | Horas máximas por empleado en una semana natural (lunes a domingo) | **40 h** | Jornada máxima ordinaria, ET art. 34.1 (simplificada a cómputo semanal) |
| RN-03 | Solo pueden intercambiar turno dos empleados de la **misma categoría profesional y el mismo servicio** | — | Garantiza que la cobertura por perfil no cambia |
| RN-04 | Tras el intercambio, cada turno de cada servicio mantiene su **cobertura mínima** | Mañana 3 · Tarde 3 · Noche 2 empleados | Valores ficticios de la organización |
| RN-05 | Antelación mínima de la solicitud respecto al primero de los turnos afectados | **48 h** | Da tiempo al responsable para resolver |
| RN-06 | Un empleado no puede tener dos turnos que se solapen, ni dos turnos el mismo día | — | Coherencia del calendario |

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
