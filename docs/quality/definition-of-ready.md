# Definition of Ready (DoR)

El *Definition of Ready* responde a la pregunta clave:
> **¿Tiene esta historia de usuario la información y madurez suficiente para entrar en un Sprint y poder cumplir la Definition of Done (DoD)?**

> [!NOTE]
> No implica conocer todos los detalles de implementación por adelantado, sino disponer de la claridad y consenso necesarios para que el equipo asuma el compromiso de desarrollo de forma viable y predecible.

Una Historia de Usuario se considera **Ready** cuando satisface todas las condiciones a continuación:

## Especificación y Trazabilidad
- [ ] Tiene un identificador único y estable (`US-xxx`) asociado a su Épica correspondiente (`EP-xxx`).
- [ ] Es trazable hasta los objetivos del producto (`G01`–`G04`) o métricas del proyecto (Constitución, principio 1).
- [ ] El rol beneficiario (*empleado* o *responsable*) y el valor aportado están claramente identificados.

## Criterios de Aceptación y Comportamiento
- [ ] Los criterios de aceptación están definidos de forma observable y verificable (p. ej. formato *Given-When-Then* o reglas claras de verificación).
- [ ] Describen tanto el flujo principal (camino feliz) como los casos límite y el tratamiento de errores.
- [ ] Establecen el comportamiento funcional esperado sin imponer innecesariamente detalles de implementación interna.

## Reglas de Negocio y Requisitos No Funcionales
- [ ] Se identifican explícitamente las reglas de negocio aplicables (RN-01 a RN-06) y la necesidad de validación en servidor (Constitución, principio 4).
- [ ] Se definen las restricciones de seguridad y control de acceso por rol (Constitución, principio 5).
- [ ] Se indican las restricciones técnicas, de usabilidad o accesibilidad pertinentes para la historia.

## Testabilidad y Datos de Prueba
- [ ] La historia es comprobable y se tiene identificada la estrategia de pruebas requerida (unitarias, integración o interfaz).
- [ ] Se conocen o están disponibles los escenarios con datos ficticios/sintéticos necesarios (Constitución, principio 5).

## Planificación y Dependencias
- [ ] Tiene asignada una prioridad MoSCoW (*Must*, *Should*, *Could*, *Won't*).
- [ ] Dispone de una estimación de esfuerzo consensuada y se ha evaluado su nivel de incertidumbre.
- [ ] El tamaño de la historia está acotado para completarse dentro de un único Sprint.
- [ ] Se conocen las dependencias y predecesoras relevantes (técnicas o funcionales) y no suponen un bloqueo activo.

## Revisión y Consenso
- [ ] Ha sido revisada en sesión de refinamiento por el Product Owner y el equipo.
- [ ] No quedan cuestiones abiertas ni dudas que impidan al equipo iniciar el desarrollo y satisfacer con éxito el DoD.