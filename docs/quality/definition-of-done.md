# TurnoLibre — Definition of Done (DoD)

Versión 1.1 · 13/10/2026 · Responsable: Juliannietoo (DevOps/QA)

Responde a la pregunta: *¿qué condiciones mínimas debe cumplir cualquier historia para considerarla terminada?*
Una historia está Done cuando cumple todas las condiciones aplicables siguientes.

> [!NOTE]
> Una historia no está terminada solo porque funcione en el caso ideal (Constitución, principio 3). Debe cumplir íntegramente con las validaciones del servidor, pruebas automáticas, control de roles y revisión de código.

## Implementación y Reglas de Negocio
- [ ] La funcionalidad descrita ha sido implementada siguiendo la arquitectura y las convenciones técnicas acordadas.
- [ ] Se validan las entradas y las reglas de negocio vigentes del MVP (G02) estrictamente en el servidor (Constitución, principio 4).
- [ ] Los mensajes de error o rechazo son claros, comprensibles e indican la regla o motivo aplicable.
- [ ] No quedan problemas críticos de implementación ni advertencias bloqueantes sin resolver.

## Criterios de Aceptación
- [ ] Todos los criterios de aceptación aprobados en la historia han sido verificados con evidencia objetiva.
- [ ] El comportamiento implementado coincide exactamente con la especificación y cubre los casos límite acordados.

## Pruebas y Calidad
- [ ] Dispone de pruebas automatizadas ejecutadas (unitarias, integración o interfaz) que cubren tanto los flujos exitosos como las validaciones y errores.
- [ ] Solo utiliza datos ficticios o sintéticos en todos los entornos, sin datos personales ni sanitarios reales (Constitución, principio 5).
- [ ] La suite de pruebas existente continúa pasando al 100% (no se han introducido regresiones).

## Requisitos No Funcionales y Seguridad
- [ ] Se comprueba el control de acceso y autorización por rol (*empleado* y *responsable*) en rutas y acciones sensibles (Constitución, principio 5).
- [ ] Se han respetado las pautas de usabilidad, diseño responsivo y accesibilidad básica acordadas.

## Integración y Despliegue
- [ ] La integración continua (CI) finaliza en verde sin advertencias bloqueantes.
- [ ] El código está integrado en la rama `main`, ejecuta correctamente y se ha desplegado en el entorno de demostración.

## Documentación y Trazabilidad
- [ ] Se mantiene la cadena de trazabilidad completa: necesidad → requisito → plan → tareas → código → pruebas (Constitución, principio 1).
- [ ] La documentación técnica, de usuario o fichas de especificación (`spec.md`, `tasks.md`) afectadas están actualizadas.

## Revisión y Aceptación
- [ ] Ha sido revisada y aprobada en un Pull Request por al menos otro miembro del equipo (Team Charter, acuerdo 15).
- [ ] No quedan comentarios ni hilos bloqueantes de revisión sin resolver.
- [ ] El Product Owner ha validado el incremento frente al valor y alcance esperados.