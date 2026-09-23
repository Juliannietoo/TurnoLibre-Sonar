# TurnoLibre — Constitución del proyecto

Versión 1.0 · Fecha: **[COMPLETAR]**

## Core Principles

### 1. Especificación y trazabilidad
Toda funcionalidad debe estar especificada antes de implementarse. Debe poder seguirse la cadena:
Necesidad → requisito → plan → tareas → código → pruebas.
No se implementa nada que no esté justificado por una especificación aprobada.

### 2. Disciplina de alcance del MVP
El equipo se centra en lo necesario para un producto mínimo viable. Toda ampliación de alcance debe estar justificada, priorizada, con su impacto en plazo, coste y capacidad evaluado, y quedar registrada como decisión humana del Product Owner.

### 3. Calidad y comportamiento verificable
Los requisitos son claros, medibles y comprobables. Cada funcionalidad incluye criterios de aceptación, tratamiento de errores, pruebas y cumplimiento de la Definition of Done. No está terminada solo porque funcione en el caso ideal.

### 4. Reglas laborales explícitas y validadas
Las reglas de negocio de los turnos (descanso mínimo, límite de horas, cobertura) se documentan como requisitos verificables y se validan siempre en el servidor. Ningún intercambio puede aprobarse si incumple una regla vigente.

### 5. Seguridad, privacidad y datos sintéticos
Solo se usan datos ficticios. No se emplean datos personales, laborales ni sanitarios reales. Se validan las entradas, se controla el acceso por rol (empleado / responsable) y la seguridad se considera desde la especificación hasta las pruebas.

## Development and Documentation Standards
- `spec.md` explica qué y por qué; `plan.md` explica cómo; `tasks.md` descompone el trabajo ejecutable.
- Las decisiones importantes se registran (fecha, autor, motivo) y los artefactos mantienen trazabilidad entre sí.
- Usabilidad y accesibilidad: flujos principales y mensajes de error comprensibles para usuarios diversos.

## Quality Gates and Delivery Workflow
Antes de aprobar una especificación, un plan o una implementación se comprueba que:
- Cumple esta constitución y respeta el alcance acordado.
- Mantiene la trazabilidad y define criterios verificables.
- Considera calidad, pruebas, seguridad y accesibilidad.
- No contiene decisiones importantes sin justificar.

## Governance
- La constitución prevalece sobre el resto de documentos del proyecto.
- Toda modificación debe estar justificada, aprobada explícitamente, registrar fecha y nueva versión, e indicar qué documentos quedan afectados.
- Las excepciones son explícitas, justificadas, aprobadas y, si es posible, temporales.

### Historial de versiones
| Versión | Fecha | Cambio | Aprobado por |
|---|---|---|---|
| 1.0 | **[COMPLETAR]** | Versión inicial | Equipo |
