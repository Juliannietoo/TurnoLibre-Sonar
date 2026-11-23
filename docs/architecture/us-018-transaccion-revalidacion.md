# US-018 · Diseño de la transacción y la revalidación

Trazabilidad: GC02-177 · US-018 (GC02-176) · US-018-AC-01 a US-018-AC-07 · RN-01, RN-03 y RN-06 · D-24, D-27 y D-28.

Este documento prepara la implementación de US-018 en IT-6. El objetivo es definir cómo resolver una solicitud aceptada de forma consistente, revalidando las reglas vigentes inmediatamente antes de aprobar y evitando decisiones o intercambios duplicados.

## Estado de partida

US-018 solo puede resolver una solicitud que se encuentre en estado `ACEPTADA`.

La solicitud conserva las reservas creadas al proponer el intercambio. Antes de cualquier decisión se debe aplicar la caducidad existente mediante `caducar_vencidas()`.

Si alguno de los turnos ya ha comenzado, la solicitud habrá pasado a `CADUCADA`, sus reservas se habrán liberado y no podrá aprobarse ni rechazarse de nuevo como solicitud pendiente.

## Revalidación antes de aprobar

La aprobación no debe confiar únicamente en las comprobaciones realizadas al crear la propuesta. Las reglas se vuelven a evaluar sobre el estado actual del cuadrante justo antes de modificar los turnos.

Se reutilizan los validadores ya existentes:

- RN-03: `validar_compatibilidad(turno_a, turno_b)`.
- RN-01 y RN-06: `validar_descanso_y_solapes(turno_a, turno_b)`.

RN-04 no requiere una validación adicional en este punto. El módulo de compatibilidad documenta que la cobertura no cambia con una permuta uno a uno entre empleados de la misma categoría y servicio.

Los validadores devuelven objetos `Incumplimiento`, con:

- `regla`: regla o condición incumplida.
- `empleado`: empleado afectado.
- `mensaje`: explicación del incumplimiento.

Estos datos permiten registrar de forma trazable el rechazo automático exigido por US-018-AC-03.

## Flujo de resolución

El flujo previsto para el servicio de resolución es:

1. Ejecutar `caducar_vencidas()`.
2. Recuperar el estado actual de la solicitud.
3. Comprobar que continúa en estado `ACEPTADA`.
4. Si el responsable decide rechazar:
   - exigir un motivo;
   - pasar la solicitud a `RECHAZADA`;
   - registrar responsable, fecha y motivo;
   - eliminar las reservas de ambos turnos.
5. Si el responsable decide aprobar:
   - revalidar RN-03;
   - revalidar RN-01 y RN-06;
   - si existe algún incumplimiento, rechazar por regla sin modificar el cuadrante;
   - si no existen incumplimientos, intercambiar los empleados de los dos turnos;
   - pasar la solicitud a `APROBADA`;
   - registrar responsable y fecha;
   - eliminar las reservas asociadas.

La resolución completa debe ejecutarse como una única operación atómica.

## Rechazo por regla

Si la revalidación detecta uno o más incumplimientos, el cuadrante no se modifica.

La solicitud pasa de `ACEPTADA` a `RECHAZADA` y debe conservar información suficiente para explicar la decisión. Como mínimo se registrará la regla incumplida y su mensaje.

El primer `Incumplimiento` puede utilizarse como causa principal de la decisión. La implementación de IT-6 deberá mantener el formato compatible con los campos actuales de `SolicitudIntercambio`, especialmente `ultima_accion`, `autor_ultima_accion`, `fecha_ultima_accion` y `motivo_ultima_accion`.

Las reservas de los dos turnos se eliminan dentro de la misma transacción.

## Aprobación

Si la solicitud sigue `ACEPTADA` y ninguna regla falla, la aprobación realiza una permuta uno a uno:

- `turno_ofrecido` pasa al empleado destinatario.
- `turno_solicitado` pasa al empleado proponente.

Los dos cambios de turno y el cambio de estado de la solicitud deben pertenecer a la misma transacción.

Solo después de realizar correctamente la permuta la solicitud pasa a `APROBADA`.

Las reservas dejan de ser necesarias una vez terminada la solicitud y se eliminan en la misma operación.

## Atomicidad

La resolución debe envolverse en `transaction.atomic()`.

Dentro de la transacción deben quedar incluidos:

- comprobación efectiva del estado pendiente;
- revalidación de reglas;
- intercambio de los empleados de ambos turnos, cuando proceda;
- actualización de la solicitud;
- registro del responsable, fecha y motivo;
- liberación de las reservas.

No debe existir un estado observable en el que solo uno de los dos turnos haya cambiado de empleado o en el que el cuadrante se haya modificado pero la solicitud continúe `ACEPTADA`.

Ante una excepción, la transacción debe revertirse completa.

## Concurrencia e idempotencia

US-018-AC-06 exige que dos pestañas o dos peticiones concurrentes no puedan producir dos intercambios.

La transición debe realizarse únicamente desde el estado `ACEPTADA`.

La implementación de IT-6 debe utilizar una actualización condicionada por el estado actual o un mecanismo equivalente dentro de la transacción para garantizar que solo una petición adquiere el derecho a resolver la solicitud.

Una vez que la primera petición haya terminado:

- otra aprobación no debe volver a intercambiar los turnos;
- un rechazo posterior no debe sustituir una aprobación;
- una aprobación posterior no debe sustituir un rechazo;
- una solicitud `CADUCADA`, `RECHAZADA` o `APROBADA` no puede resolverse de nuevo.

Una repetición de la misma petición debe producir el estado ya alcanzado sin repetir sus efectos sobre el cuadrante.

## Caducidad

La caducidad se comprueba al inicio de cada resolución mediante `caducar_vencidas()`.

Esto es necesario aunque el responsable haya abierto previamente la pantalla cuando los turnos todavía eran futuros.

Si al recibir la petición alguno de los turnos ya ha comenzado:

1. la solicitud pasa a `CADUCADA`;
2. las reservas se liberan;
3. no se ejecuta la revalidación destinada a aprobar;
4. no se modifica el cuadrante;
5. la petición de resolución no puede cambiar posteriormente ese estado.

## Contrato previsto para IT-6

La implementación de la parte 2 debe exponer un único punto de entrada para resolver una solicitud.

El contrato deberá recibir, como mínimo:

- responsable que toma la decisión;
- solicitud;
- decisión de aprobar o rechazar;
- motivo cuando el rechazo sea manual.

El servicio será responsable de aplicar caducidad, comprobar el estado, revalidar, intercambiar los turnos cuando proceda y registrar el resultado.

El nombre definitivo del servicio se fijará al comenzar la implementación de GC02-187 para mantener coherencia con los módulos `propuestas.py` y `respuestas.py`.

## Casos que deberá cubrir GC02-188

La implementación deberá permitir probar al menos:

- aprobación válida;
- rechazo manual con motivo;
- rechazo manual sin motivo;
- rechazo automático por RN-03;
- rechazo automático por RN-01;
- rechazo automático por RN-06;
- solicitud caducada justo antes de aprobar;
- solicitud ya terminada;
- repetición de una aprobación;
- dos aprobaciones concurrentes;
- aprobación y rechazo concurrentes;
- conservación del cuadrante cuando falla una regla;
- intercambio correcto de los dos empleados cuando la aprobación es válida;
- liberación de ambas reservas al terminar la solicitud.

## Alcance de GC02-177

GC02-177 no implementa todavía el servicio de resolución.

Su resultado es este diseño, que reduce la incertidumbre de US-018 antes de IT-6 y deja definidas:

- la reutilización de los validadores existentes;
- la secuencia de revalidación;
- los efectos de aprobar y rechazar;
- la frontera de la transacción;
- el tratamiento de caducidad;
- los requisitos de concurrencia e idempotencia;
- los principales casos que deberá verificar GC02-188.

La implementación corresponde a GC02-187 en IT-6.