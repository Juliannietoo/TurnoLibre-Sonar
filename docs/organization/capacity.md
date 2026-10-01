# Capacidad del equipo

Periodo de ejecución: **6 semanas** (6 sprints de 1 semana, de miércoles a martes), del **23/09/2026** al **03/11/2026**, en 3 releases de 2 semanas.

## Revisión individual del 01/10/2026

El PO ha confirmado su reparto semanal y la recuperación de la hora del festivo 12/10. A fecha 01/10/2026 no tiene exámenes ni entregas importantes previstos entre el 23/09 y el 03/11. No se han comunicado otros descuentos de disponibilidad; si aparece alguno, se actualizará la semana afectada. Queda pendiente la revisión individual de los otros tres roles y la capacidad total del equipo.

| Rol | Nominal semanal | Reuniones | Coordinación del rol | Margen sobre la neta | Efectiva antes de ausencias | Estado |
|---|---|---|---|---|---|---|
| Product Owner | 5 h | 1,5 h | 0,5 h | 20 % | 2,4 h | Reparto confirmado; sin exámenes ni entregas importantes previstos |
| Scrum Master | 5 h (hipótesis H1) | Pendiente | Pendiente | Pendiente | Pendiente | Revisión individual por SM |
| Tech Lead | 5 h (hipótesis H1) | Pendiente | Pendiente | Pendiente | Pendiente | Revisión individual por TL |
| DevOps / QA | 5 h (hipótesis H1) | Pendiente | Pendiente | Pendiente | Pendiente | Revisión individual por QA |

## Capacidad del PO

Semanal: **5 − 1,5 − 0,5 = 3 h netas**. Reserva: **3 × 20 % = 0,6 h**. Capacidad efectiva base: **2,4 h por sprint**.

El margen del 20 % responde a la carga de otras actividades y ha sido confirmado por el PO; no se aplica automáticamente a los demás roles. Las 1,5 h de reuniones incluyen una hora de planning/review/retrospectiva y dos dailies de 15 minutos. La media hora de coordinación individual del PO se descuenta aparte.

| Sprint | Periodo | Nominal base | Reuniones | Coordinación | Reserva base | Efectiva base | Descuentos por ausencias declaradas |
|---|---|---|---|---|---|---|---|
| IT-001 | 23/09–29/09 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas |
| IT-002 | 30/09–06/10 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas |
| IT-003 | 07/10–13/10 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas; hora del 12/10 reubicada el 13/10 |
| IT-004 | 14/10–20/10 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas |
| IT-005 | 21/10–27/10 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas |
| IT-006 | 28/10–03/11 | 5 h | 1,5 h | 0,5 h | 0,6 h | 2,4 h | 0 h declaradas |
| **Total base** | **6 semanas** | **30 h** | **9 h** | **3 h** | **3,6 h** | **14,4 h** | **0 h declaradas** |

El bloque de una hora del lunes 12/10 se traslada al martes 13/10, de 13:30 a 14:30, dentro de IT-003. La hora de las dailies y cualquier cambio de reunión se acuerdan con el equipo. Esta tabla expresa disponibilidad planificada, no horas ya realizadas.

## Cálculo definitivo y uso

Por persona y sprint: `efectiva = max(0, nominal − ausencias − reuniones − coordinación) × (1 − margen individual)`.

Las ausencias se aplican a la semana afectada; si obligan a cancelar o mover una reunión, se recalcula el tiempo de eventos para evitar descontar las mismas horas dos veces. Después se suman las capacidades efectivas de todos los miembros para contrastarlas con las horas-persona consensuadas del backlog. Cada margen debe justificarse individualmente.

Como referencia histórica, H1 suponía 120 h nominales para el equipo y 75,6 h efectivas (aproximadas a 75 h), descontando 1,5 h de reuniones y un 10 % común, sin coordinación individual. Ese cálculo se sustituirá por los datos personales confirmados; no es la capacidad definitiva para H2.
