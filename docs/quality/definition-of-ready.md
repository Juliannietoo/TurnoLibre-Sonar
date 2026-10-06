# TurnoLibre — Definition of Ready (DoR)

Versión 1.0 · 30/09/2026 · Responsable: Juliannietoo (DevOps/QA)

Responde a la pregunta: *¿tenemos información suficiente para aceptar esta historia como candidata a entrar en un sprint?*
No significa saberlo todo, sino saber lo suficiente para asumir el trabajo con confianza.

## Identificación y trazabilidad
- [ ] La historia tiene un identificador único y estable (`US-XXX`).
- [ ] Está asociada a una épica (`EP-XXX`).
- [ ] Está trazada al menos a un objetivo del producto (`G01`–`G04`).

## Valor y alcance
- [ ] El usuario o stakeholder está identificado (empleado, responsable, evaluador…).
- [ ] La capacidad esperada está descrita con claridad.
- [ ] El valor o beneficio se entiende.
- [ ] El alcance y los límites están claros (qué entra y qué no).

## Aceptación
- [ ] Tiene criterios de aceptación identificados (`US-XXX-AC-01`…).
- [ ] Los criterios son observables y verificables, incluidos los casos de error.
- [ ] Describen el comportamiento esperado, no una implementación concreta.
- [ ] Si afecta a un intercambio o a su validación, indica qué reglas de negocio (`RN-01`–`RN-06`) aplica y sus precondiciones.

## Planificación
- [ ] Tiene prioridad MoSCoW asignada y justificada.
- [ ] Tiene una estimación consensuada en horas-persona.
- [ ] Tiene indicada la incertidumbre (Baja / Media / Alta).
- [ ] Sus predecesoras y dependencias (funcionales, técnicas y externas) son conocidas y no bloquean el sprint.
- [ ] Cabe en un sprint; si no cabe, se divide.

## Restricciones
- [ ] Se han identificado los requisitos no funcionales que le aplican (`NFR-XXX`).
- [ ] Se conocen las restricciones técnicas, organizativas o de proyecto relevantes.
- [ ] Solo utiliza datos ficticios o sintéticos y cumple las restricciones de privacidad (principio 5 de la constitución).

## Cuestiones abiertas
- [ ] No hay preguntas sin resolver que impidan entender o planificar la historia.
- [ ] Cualquier supuesto importante o duda no bloqueante está documentado en la ficha.

## Uso
El Product Owner y el equipo de desarrollo revisan y verifican el cumplimiento de la DoR durante las sesiones de refinamiento previas a cada Sprint Planning. Toda historia que no cumpla íntegramente estas condiciones no puede entrar en el sprint ni ser comprometida en el Sprint Backlog hasta que se resuelvan sus dudas o bloqueos.