# TurnoLibre — Riesgos técnicos

Revisión técnica inicial · Tech Lead (MarvelinoGG) · 29/09/2026 · Valoración de probabilidad e impacto añadida el 30/09/2026 · RT-01 actualizado al alcance de D-22 el 14/10/2026 · RT-04 añadido el 14/10/2026
| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| RT-01 | Complejidad de las reglas de negocio | Media | Alto | Centralizar las reglas vigentes del MVP en un módulo de lógica de negocio y probar cada regla y sus casos límite | Abierto |
| RT-02 | Concurrencia y consistencia en los intercambios | Media | Alto | Validar y confirmar dentro de una transacción y volver a comprobar las reglas justo antes de confirmar | Abierto |
| RT-03 | Control de acceso por roles sin definir | Media | Alto | Definir los permisos de cada rol y comprobar siempre la autorización en el servidor | Abierto |
| RT-04 | Tecnologías autorizadas sin confirmar al empezar la ejecución | Media | Alto | Preguntar al profesor en la sesión del 21/10; si no hay respuesta, empezar IT-001 por las tareas que no dependen de la tecnología (TK-005, TK-006 y la preparación de TK-002) y completar TK-001 cuando se confirme, usando el margen de IT-001 (2,18 h) | Abierto |

**Criterio de valoración:** *probabilidad* = posibilidad de que el riesgo se materialice durante las 6 semanas; *impacto* = efecto sobre los objetivos G01–G04 si ocurre. Un impacto *Alto* significa que compromete un principio de la constitución o la métrica M02.

| ID | Justificación de la valoración |
|---|---|
| RT-01 | Probabilidad media: tras D-22 el MVP valida en el servidor RN-01, RN-03 y RN-06, mientras RN-04 se garantiza al preparar los datos de demostración y RN-02/RN-05 quedan como Should. La reducción de alcance disminuye la complejidad, aunque RN-01 y RN-06 mantienen casos temporales y afectan a los dos empleados del intercambio. Impacto alto: M02 exige que el 100 % de los casos de las reglas vigentes del MVP se resuelvan correctamente. |
| RT-02 | Probabilidad media: con datos de demostración y pocos usuarios es poco frecuente que coincidan dos solicitudes. Impacto alto: si ocurre, podría aprobarse un cambio inválido, justo lo que prohíbe el principio 4 de la constitución. |
| RT-03 | Probabilidad media: se previene definiendo los permisos pronto, en la historia de inicio de sesión. Impacto alto: un fallo sería un problema de seguridad (principio 5 de la constitución). |
| RT-04 | Probabilidad media: el enunciado dice que las tecnologías «se definirán más adelante» y a 14/10 no se han comunicado. Impacto alto: US-001 es la raíz de la cadena crítica y el plan no tiene un sprint de holgura (D-24). |

## RT-01 · Complejidad de las reglas de negocio de los turnos
Tras D-22 y de acuerdo con G02, el MVP comprueba en el servidor RN-01, RN-03 y RN-06. RN-04 se garantiza al preparar y restablecer el cuadrante de demostración mediante US-003, mientras que RN-02 y RN-05 solo se incorporan si se implementan sus historias Should. Aunque el alcance se ha reducido respecto a la definición inicial, la combinación de descanso, compatibilidad y solapes de los dos empleados puede generar casos límite y errores en la lógica de validación.
*Mitigación:* centralizar las reglas vigentes del MVP en un módulo o capa de lógica de negocio y definir pruebas específicas para cada regla y sus casos límite.

## RT-02 · Concurrencia y consistencia en los intercambios de turnos
Dos solicitudes de intercambio pueden afectar a los mismos turnos a la vez. Aunque ambas sean válidas al comprobarse, la aprobación de una puede invalidar la otra, lo que provocaría estados inconsistentes o problemas de cobertura.
*Mitigación:* validar y confirmar los intercambios de forma consistente, con transacciones y una nueva comprobación de las reglas antes de la confirmación definitiva.

## RT-03 · Definición insuficiente del control de acceso por roles
La constitución distingue entre empleado y responsable, pero no especifica qué acciones puede realizar cada uno. Esto podría permitir operaciones no autorizadas o diferencias entre la interfaz y el servidor.
*Mitigación:* definir los permisos de cada rol y comprobar siempre la autorización en el servidor.

## RT-04 · Tecnologías autorizadas sin confirmar
Las tecnologías autorizadas para el proyecto todavía no están confirmadas al inicio de la planificación de la ejecución. Como US-001 constituye la base técnica del producto y se encuentra al comienzo de la cadena crítica, un retraso en esta decisión podría afectar al arranque de IT-001 y propagarse a las iteraciones posteriores.
*Mitigación:* consultar al profesor en la sesión del 21/10. Si la decisión sigue pendiente, avanzar primero con las tareas de IT-001 que no dependan del stack tecnológico (TK-005 y TK-006) y con la preparación posible de TK-002. TK-001 se completará en cuanto se confirmen las tecnologías, utilizando si fuera necesario el margen disponible de 2,18 h en IT-001.