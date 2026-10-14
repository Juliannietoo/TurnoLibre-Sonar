# Capacidad del equipo

## Plan vigente · D-21, 07/10/2026

**6 h semanales por persona**, durante seis sprints de miércoles a martes, del **21/10/2026 al 01/12/2026**, en tres releases. El PO adopta la opción propuesta por la SM para mantener las **46 h-p Must** de D-18. Se mantienen dos dailies y 1,5 h de reuniones semanales. Esta decisión actualiza la dedicación de D-07 y mantiene las fechas de D-19.

La SM comunica una capacidad de **37,25 h con 5 h semanales** para el nuevo periodo. Añadir 1 h semanal por persona aporta **6 × (0,80 + 0,90 + 0,85 + 0,85) = 20,40 h efectivas**, resultando **57,65 h**. Las cifras se suman sin redondear; las tablas muestran dos decimales.

## Ausencias y disponibilidad individual

Se aplica el criterio comunicado por la SM: 1 h de descuento en semanas con uno o dos exámenes/entregas y 2 h con tres o más. El PO utiliza las mismas ausencias que la SM (6 h en el periodo); TL contempla GPS/PBD y QA también SO.

El desglose de ausencias corresponde al publicado por la SM el 07/10/2026 (D-19). Se mantienen esos descuentos al ampliar la dedicación a 6 h. El festivo del 12/10 queda fuera del periodo.

| Rol | IT-001 | IT-002 | IT-003 | IT-004 | IT-005 | IT-006 | Total ausencias |
|---|---:|---:|---:|---:|---:|---:|---:|
| PO | 1 h | 2 h | 0 h | 1 h | 1 h | 1 h | 6 h |
| SM | 1 h | 2 h | 0 h | 1 h | 1 h | 1 h | 6 h |
| TL | 0 h | 1 h | 0 h | 1 h | 1 h | 1 h | 4 h |
| QA | 1 h | 2 h | 0 h | 1 h | 1 h | 1 h | 6 h |

| Rol | Nominal semanal | Reuniones | Coordinación | Margen sobre neta | Motivo del margen |
|---|---:|---:|---:|---:|---|
| PO | 6 h | 1,5 h | 0,5 h | 20 % | Carga de otras actividades |
| SM | 6 h | 1,5 h | 1 h | 10 % | Exámenes conocidos descontados aparte; reserva para imprevistos |
| TL | 6 h | 1,5 h | 1 h | 15 % | Incertidumbre técnica y carga de otras actividades |
| QA | 6 h | 1,5 h | 0,5 h | 15 % | Incidencias de pruebas/despliegue e imprevistos |

La coordinación cubre refinamiento del PO; actas y seguimiento de SM; dependencias y riesgos de TL; y calidad/entornos de QA. La sesión semanal de los miércoles dura 2 h (17:30–19:30): se descuenta 1 h de ceremonias (planning, review y retrospectiva) y la otra hora es trabajo del proyecto con el profesor, que cuenta como capacidad (IPR-005, D-24). Las reuniones incluyen una hora de planning/review/retrospectiva y dos dailies de 15 minutos.

**Exámenes y entregas en el periodo de ejecución:**

| Sprint | Periodo | Fecha | Evento | PO | SM | TL | QA |
|---|---|---|---|:-:|:-:|:-:|:-:|
| IT-001 | 21/10–27/10 | 27/10 | Parcial de SO | ✓ | ✓ | | ✓ |
| IT-002 | 28/10–03/11 | 28/10 | Examen práctico 1 de PBD | ✓ | ✓ | ✓ | ✓ |
| | | 29/10 | Examen práctico 1 de SO | ✓ | ✓ | | ✓ |
| | | 30/10 | Entrega de la práctica 2 de GPS | ✓ | ✓ | ✓ | ✓ |
| | | 03/11 | Parcial 1 de IS | ✓ | ✓ | | |
| IT-003 | 04/11–10/11 | — | Sin exámenes ni entregas | | | | |
| IT-004 | 11/11–17/11 | 13/11 | Entrega de la práctica 3 de GPS | ✓ | ✓ | ✓ | ✓ |
| IT-005 | 18/11–24/11 | 18/11 | Examen práctico 2 de PBD | ✓ | ✓ | ✓ | ✓ |
| IT-006 | 25/11–01/12 | 27/11 | Entrega de la práctica 4 de GPS | ✓ | ✓ | ✓ | ✓ |

## Capacidad efectiva por persona y sprint

`efectiva = max(0, nominal − ausencias − reuniones − coordinación) × (1 − margen individual)`.

| Sprint | Periodo 2026 | PO | SM | TL | QA | Equipo |
|---|---|---:|---:|---:|---:|---:|
| IT-001 | 21/10–27/10 | 2,40 h | 2,25 h | 2,98 h | 2,55 h | **10,18 h** |
| IT-002 | 28/10–03/11 | 1,60 h | 1,35 h | 2,13 h | 1,70 h | **6,78 h** |
| IT-003 | 04/11–10/11 | 3,20 h | 3,15 h | 2,98 h | 3,40 h | **12,73 h** |
| IT-004 | 11/11–17/11 | 2,40 h | 2,25 h | 2,13 h | 2,55 h | **9,33 h** |
| IT-005 | 18/11–24/11 | 2,40 h | 2,25 h | 2,13 h | 2,55 h | **9,33 h** |
| IT-006 | 25/11–01/12 | 2,40 h | 2,25 h | 2,13 h | 2,55 h | **9,33 h** |
| **Total** | **6 semanas** | 14,40 h | 13,50 h | 14,45 h | 15,30 h | **57,65 h** |

**Conciliación:** 144 h nominales − 36 h de reuniones − 18 h de coordinación − 22 h de ausencias − 10,35 h de reserva = **57,65 h efectivas**. Las ausencias se descuentan una sola vez, antes del margen.

## Uso en la planificación

Las Must suman **46 h-p**: quedan **11,65 h** de capacidad sin comprometer. Las Should siguen siendo opcionales; no se incorporan automáticamente.

El encaje total no demuestra que el plan por sprint sea viable. Con el reparto actual, IT-002 tiene 9 h-p frente a 6,775 h disponibles e IT-006 tiene 10 h-p frente a 9,325 h. SM/TL deben redistribuir la carga respetando dependencias y preparar las tareas de H3. Una historia de 5 u 8 h-p requiere varias personas: ninguna tarea individual puede superar la disponibilidad de su responsable en ese sprint. El máximo individual del nuevo plan es 3,40 h, no las 2,55 h del escenario de 5 h semanales. Se mantiene WIP 2.

Referencia histórica: el periodo anterior tenía 46,35 h de capacidad; el nuevo periodo con 5 h semanales tendría 37,25 h. El detalle vigente es el de D-21.
