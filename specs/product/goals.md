# TurnoLibre — Objetivos

Precisiones de G01, G02 y M01–M05 propuestas el 24/09/2026 y validadas por el Product Owner el 28/09/2026 tras la revisión de PaulaJCruz ([PR #1](https://github.com/UniExtremadura/TurnoLibre_GC02/pull/1)). M01 revisada por decisión del PO el 01/10/2026: muestra de tres participantes para reducir el esfuerzo de evaluación; se exige que los tres completen el flujo.

## Objetivos
| ID | Objetivo | Resultado esperado |
|---|---|---|
| G01 | Autonomía del empleado | Los dos empleados completan sin ayuda los pasos que les corresponden hasta dejar la solicitud pendiente de aprobación. |
| G02 | Cumplimiento de reglas | Ningún cambio que incumpla cualquiera de las reglas RN-01 a RN-06 llega a aprobarse. |
| G03 | Control ágil del responsable | El responsable resuelve solicitudes con la información y validaciones ya disponibles. |
| G04 | Incremento revisable | Un tercero puede instalar, ejecutar y evaluar cada release de forma estable. |

## Indicadores de éxito
| ID | Objetivo | Meta |
|---|---|---|
| M01 | G01 | Los 3 participantes de prueba publican, proponen y aceptan un intercambio válido con dos cuentas ficticias hasta el estado «pendiente de aprobación» en menos de 5 minutos cada uno, sin ayuda (3 de 3). El tiempo no incluye la decisión del responsable. |
| M02 | G02 | El 100 % de la suite de casos de RN-01 a RN-06 se resuelve correctamente en el servidor: los casos inválidos quedan bloqueados antes de aprobar y los válidos pueden aprobarse. Incluye casos límite. |
| M03 | G03 | En 3 solicitudes de muestra, el responsable decide cada una en menos de 1 minuto desde que abre el detalle hasta que registra la decisión. |
| M04 | G04 | Una persona ajena a la implementación instala y evalúa cada release desde un entorno limpio siguiendo solo el guion documentado, sin intervenciones no documentadas. |
| M05 | Todos | No hay defectos bloqueantes abiertos al cierre de cada release. Es bloqueante un fallo que impide el flujo principal, la instalación o el bloqueo de un intercambio inválido. |

> Metas propuestas: el equipo puede ajustarlas, pero deben seguir siendo medibles.

## Alcance incluido
- **S-01:** flujo esencial de intercambio de un turno entre dos empleados (publicar, proponer, aceptar).
- **S-02:** aprobación o rechazo por el responsable, con validación automática de reglas.
- **S-03:** calendario de turnos y consulta del estado e historial de solicitudes.
- **S-04:** conjunto controlado de empleados, turnos y solicitudes completamente ficticios.
- **S-05:** preparación mínima de empleados y turnos ficticios mediante carga inicial y restablecimiento de datos. La pantalla de alta y modificación de turnos queda como mejora opcional (decisión del PO del 01/10/2026).

## Exclusiones
- **EX-01:** nóminas, fichaje, control horario y vacaciones.
- **EX-02:** integración con sistemas de RR. HH. o con software hospitalario real.
- **EX-03:** generación automática del cuadrante mensual completo.
- **EX-04:** notificaciones por correo, SMS o push reales (solo avisos dentro de la aplicación).
- **EX-05:** aplicación móvil nativa.

## Supuestos
- **A-01:** las reglas de negocio de los intercambios son las definidas por el equipo en [`business-rules.md`](business-rules.md): descanso mínimo de 12 h entre turnos, máximo interno de 40 h por semana natural, intercambio solo entre empleados de la misma categoría y servicio, cobertura mínima por turno, solicitud con 48 h de antelación y turnos sin solapamientos ni doble asignación por fecha de inicio.
- **A-02:** hay un único centro y un único responsable de planificación por servicio.
- **A-03:** los usuarios disponen de un navegador moderno.
- **A-04:** la hipótesis de partida es 5 h/semana por miembro durante 6 semanas (120 h nominales). La capacidad efectiva se calcula individualmente en [capacidad del equipo](../../docs/organization/capacity.md); el PO ha confirmado su reparto y los otros roles siguen pendientes. El cálculo homogéneo de H1 no constituye la capacidad definitiva de H2.

## Restricciones
- Prohibido usar datos personales, laborales o sanitarios reales.
- Ejecución de **6 semanas** (del 23/09/2026 al 03/11/2026), en **3 releases de 2 semanas**, con sprints de **1 semana que comienzan en miércoles**.
- Equipo de **4 personas** a 5 h/semana cada una; coste directo de personal de **2.677,50 €** y precio al cliente de **4.935,59 € IVA incluido** (cálculo en `docs/organization/company.md`).
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
