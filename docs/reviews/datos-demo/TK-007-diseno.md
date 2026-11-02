# TK-007 · Comprobación del diseño de cuadrante

Trazabilidad: GC02-186 · US-003-AC-02 · RN-01, RN-02, RN-04 y RN-06.

Resultado del diseño: **CORRECTO**.

16 empleados; 240 asignaciones; 30 fechas, incluidos los dos días de guarda.

Se comprueban las semanas centrales completas. Los días de guarda permiten comprobar descansos en los extremos y repartir la noche del domingo anterior.

| Empleado | 2026-11-02 | 2026-11-09 | 2026-11-16 | 2026-11-23 |
|---|---:|---:|---:|---:|
| empleado01 | 21 h | 28 h | 21 h | 28 h |
| empleado02 | 21 h | 28 h | 21 h | 28 h |
| empleado03 | 21 h | 28 h | 21 h | 28 h |
| empleado04 | 28 h | 21 h | 28 h | 21 h |
| empleado05 | 28 h | 21 h | 28 h | 21 h |
| empleado06 | 28 h | 21 h | 28 h | 21 h |
| empleado07 | 21 h | 28 h | 21 h | 28 h |
| empleado08 | 21 h | 28 h | 21 h | 28 h |
| empleado09 | 21 h | 28 h | 21 h | 28 h |
| empleado10 | 28 h | 21 h | 28 h | 21 h |
| empleado11 | 28 h | 21 h | 28 h | 21 h |
| empleado12 | 28 h | 21 h | 28 h | 21 h |
| empleado13 | 38 h | 32 h | 38 h | 32 h |
| empleado14 | 38 h | 32 h | 38 h | 32 h |
| empleado15 | 32 h | 38 h | 32 h | 38 h |
| empleado16 | 32 h | 38 h | 32 h | 38 h |

Descanso mínimo observado: 38.0 h.

La cobertura usa empleados distintos por fecha y franja. Las horas se calculan con tiempo UTC realmente transcurrido y semanas locales Europe/Madrid.

## Pendiente de integración

Esta evidencia valida el JSON de diseño. TK-007 continúa pendiente de comprobar que el comando de Django de TK-006 carga y restablece esos mismos datos sin pérdidas ni duplicados. No acredita US-003-AC-03 ni completa la historia US-003.
