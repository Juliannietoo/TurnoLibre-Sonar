# TurnoLibre — Objetivos

## Objetivos
| ID | Objetivo | Resultado esperado |
|---|---|---|
| G01 | Autonomía del empleado | El empleado completa un intercambio de turno de principio a fin sin ayuda externa. |
| G02 | Cumplimiento de reglas | Ningún cambio que incumpla las reglas de descanso, horas o cobertura llega a aprobarse. |
| G03 | Control ágil del responsable | El responsable resuelve solicitudes con la información y validaciones ya disponibles. |
| G04 | Incremento revisable | Un tercero puede instalar, ejecutar y evaluar cada release de forma estable. |

## Indicadores de éxito
| ID | Objetivo | Meta |
|---|---|---|
| M01 | G01 | Al menos 4 de 5 participantes de prueba completan un intercambio en menos de 5 minutos y sin ayuda. |
| M02 | G02 | El 100 % de los casos de prueba que violan una regla son rechazados o marcados por el sistema (suite de casos de regla). |
| M03 | G03 | El responsable resuelve una solicitud en menos de 1 minuto en pruebas con 3 solicitudes de muestra. |
| M04 | G04 | Una persona que no ha implementado el producto sigue el guion de instalación y evaluación sin intervenciones no documentadas. |
| M05 | Todos | No hay defectos bloqueantes abiertos al cierre de cada release. |

> Metas propuestas: el equipo puede ajustarlas, pero deben seguir siendo medibles.

## Alcance incluido
- **S-01:** flujo esencial de intercambio de un turno entre dos empleados (publicar, proponer, aceptar).
- **S-02:** aprobación o rechazo por el responsable, con validación automática de reglas.
- **S-03:** calendario de turnos y consulta del estado e historial de solicitudes.
- **S-04:** conjunto controlado de empleados, turnos y solicitudes completamente ficticios.
- **S-05:** gestión mínima de datos de demostración (alta de turnos y empleados) imprescindible para probar el producto.

## Exclusiones
- **EX-01:** nóminas, fichaje, control horario y vacaciones.
- **EX-02:** integración con sistemas de RR. HH. o con software hospitalario real.
- **EX-03:** generación automática del cuadrante mensual completo.
- **EX-04:** notificaciones por correo, SMS o push reales (solo avisos dentro de la aplicación).
- **EX-05:** aplicación móvil nativa.

## Supuestos
- **A-01:** las reglas de negocio de los intercambios son las definidas por el equipo en [`business-rules.md`](business-rules.md): descanso mínimo de 12 h entre turnos, máximo de 40 h por semana, intercambio solo entre empleados de la misma categoría y servicio, cobertura mínima por turno y solicitud con 48 h de antelación.
- **A-02:** hay un único centro y un único responsable de planificación por servicio.
- **A-03:** los usuarios disponen de un navegador moderno.
- **A-04:** cada miembro dedica 5 h/semana durante las 6 semanas: 120 h brutas y ≈ 75 h disponibles para el backlog (cálculo en `docs/organization/capacity.md`).

## Restricciones
- Prohibido usar datos personales, laborales o sanitarios reales.
- Ejecución de **6 semanas** (del 23/09/2026 al 03/11/2026), en **3 releases de 2 semanas**, con sprints de **1 semana que comienzan en miércoles**.
- Equipo de **4 personas** a 5 h/semana cada una; coste directo de personal estimado en **3.780 €** (cálculo en `docs/organization/company.md`).
- Uso de las tecnologías y convenciones aprobadas por la asignatura (se definirán más adelante).

## Trazabilidad
Misión → objetivos → épicas → historias → tareas → código y pruebas → evidencias.
Una épica que no contribuya a ningún objetivo queda fuera del alcance hasta que se apruebe un cambio en este documento.

## Gestión de cambios
Cualquier modificación de un objetivo, métrica, alcance, exclusión, supuesto o restricción requiere:
1. Revisión por parte del equipo.
2. Decisión explícita del Product Owner.
3. Registro de la decisión.
4. Revisión del roadmap, las especificaciones, Jira y la capacidad.
5. Actualización de todas las referencias afectadas.
