# TurnoLibre — Riesgos técnicos

Revisión técnica inicial · Tech Lead (MarvelinoGG) · 29/09/2026 · Valoración de probabilidad e impacto añadida el 30/09/2026 
| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| RT-01 | Complejidad de las reglas de negocio | Alta | Alto | Centralizar las reglas en un módulo de lógica de negocio y probar cada regla y sus casos límite | Abierto |
| RT-02 | Concurrencia y consistencia en los intercambios | Media | Alto | Validar y confirmar dentro de una transacción y volver a comprobar las reglas justo antes de confirmar | Abierto |
| RT-03 | Control de acceso por roles sin definir | Media | Alto | Definir los permisos de cada rol y comprobar siempre la autorización en el servidor | Abierto |

**Criterio de valoración:** *probabilidad* = posibilidad de que el riesgo se materialice durante las 6 semanas; *impacto* = efecto sobre los objetivos G01–G04 si ocurre. Un impacto *Alto* significa que compromete un principio de la constitución o la métrica M02.

| ID | Justificación de la valoración |
|---|---|
| RT-01 | Probabilidad alta: son 6 reglas con casos que se cruzan (noches que pasan de una semana a otra, dos empleados afectados). Impacto alto: la métrica M02 exige que el 100 % de los casos se resuelvan correctamente. |
| RT-02 | Probabilidad media: con datos de demostración y pocos usuarios es poco frecuente que coincidan dos solicitudes. Impacto alto: si ocurre, podría aprobarse un cambio inválido, justo lo que prohíbe el principio 4 de la constitución. |
| RT-03 | Probabilidad media: se previene definiendo los permisos pronto, en la historia de inicio de sesión. Impacto alto: un fallo sería un problema de seguridad (principio 5 de la constitución). |

## RT-01 · Complejidad de las reglas de negocio de los turnos
La constitución establece que deben comprobarse reglas como el descanso mínimo, el límite de horas o la cobertura antes de aprobar cualquier intercambio. A medida que aumenten las reglas y sus combinaciones, la lógica de validación puede volverse difícil de mantener y probar.
*Mitigación:* centralizar las reglas en un módulo o capa de lógica de negocio y definir pruebas específicas para cada regla y sus casos límite.

## RT-02 · Concurrencia y consistencia en los intercambios de turnos
Dos solicitudes de intercambio pueden afectar a los mismos turnos a la vez. Aunque ambas sean válidas al comprobarse, la aprobación de una puede invalidar la otra, lo que provocaría estados inconsistentes o problemas de cobertura.
*Mitigación:* validar y confirmar los intercambios de forma consistente, con transacciones y una nueva comprobación de las reglas antes de la confirmación definitiva.

## RT-03 · Definición insuficiente del control de acceso por roles
La constitución distingue entre empleado y responsable, pero no especifica qué acciones puede realizar cada uno. Esto podría permitir operaciones no autorizadas o diferencias entre la interfaz y el servidor.
*Mitigación:* definir los permisos de cada rol y comprobar siempre la autorización en el servidor.