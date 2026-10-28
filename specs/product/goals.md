# TurnoLibre — Objetivos

Precisiones de G01, G02 y M01–M05 propuestas el 24/09/2026 y validadas por el Product Owner el 28/09/2026 tras la revisión de PaulaJCruz ([PR #1](https://github.com/UniExtremadura/TurnoLibre_GC02/pull/1)). M01 revisada por decisión del PO el 01/10/2026: muestra de tres participantes para reducir el esfuerzo de evaluación; se exige que los tres completen el flujo.

## Objetivos
| ID | Objetivo | Resultado esperado |
|---|---|---|
| G01 | Autonomía del empleado | Los dos empleados completan sin ayuda los pasos que les corresponden hasta dejar la solicitud pendiente de aprobación. |
| G02 | Cumplimiento de reglas | En el MVP, ningún cambio que incumpla RN-01, RN-03 o RN-06 llega a aprobarse, y el cuadrante de partida cumple RN-04. RN-02 y RN-05 quedan como Should (D-18). |
| G03 | Control ágil del responsable | El responsable resuelve solicitudes con la información y validaciones ya disponibles. |
| G04 | Incremento revisable | Un tercero puede instalar, ejecutar y evaluar la versión final de forma estable (D-18). |

> **Decisiones D-22/D-23 (13/10/2026):** la constitución v1.1 y la DoD aplican las reglas vigentes del MVP de G02. R-07 precisa el resultado vacío de US-006; R-09 fija el rechazo por regla y la liberación de reservas al fallar la revalidación; R-08 deja M03 pendiente si no se realiza US-024. Se conserva el alcance y las estimaciones acordadas; la medición opcional no se declara superada sin evidencia.

## Indicadores de éxito
| ID | Objetivo | Meta |
|---|---|---|
| M01 | G01 | Los 3 participantes de prueba proponen y aceptan un intercambio válido sobre un turno de un compañero compatible, con dos cuentas ficticias, hasta el estado «pendiente de aprobación» en menos de 5 minutos cada uno, sin ayuda (3 de 3). El tiempo no incluye la decisión del responsable. La prueba con usuarios (US-024) es Should: si no se realiza, M01 queda pendiente de validación (D-18). |
| M02 | G02 | El 100 % de la suite de casos de las reglas del MVP se resuelve correctamente: RN-01, RN-03 y RN-06 en el servidor (los casos inválidos quedan bloqueados antes de aprobar y los válidos pueden aprobarse) y RN-04 sobre el cuadrante de partida. Incluye casos límite. |
| M03 | G03 | En 3 solicitudes de muestra, el responsable decide cada una en menos de 1 minuto desde que abre el detalle hasta que registra la decisión. Se mide mediante US-024; si esa prueba Should no se realiza, M03 queda pendiente de validación, igual que M01 (D-23, 13/10/2026). |
| M04 | G04 | Una persona ajena a la implementación instala y evalúa la versión final desde un entorno limpio siguiendo solo el guion documentado, sin intervenciones no documentadas (D-18). |
| M05 | Todos | No hay defectos bloqueantes abiertos al cierre de cada release. Es bloqueante un fallo que impide el flujo principal, la instalación o el bloqueo de un intercambio inválido. |

> Metas propuestas: el equipo puede ajustarlas, pero deben seguir siendo medibles.

## Alcance incluido
- **S-01:** flujo esencial de intercambio de un turno entre dos empleados: proponer sobre un turno de un compañero compatible y aceptar. La publicación previa de turnos queda fuera de esta versión (D-18).
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
- **A-04:** D-21 fija 6 h/semana por persona durante 6 semanas (144 h nominales). La capacidad efectiva es 57,65 h según el [cálculo individual](../../docs/organization/capacity.md); se mantienen las ausencias publicadas por la SM en D-19.
- **A-05:** los datos de demostración no incluyen semanas con cambio de hora; el tratamiento del cambio de hora en las reglas queda fuera del MVP (D-18, 06/10/2026).

## Restricciones
- Prohibido usar datos personales, laborales o sanitarios reales.
- Ejecución de **6 semanas** (del 21/10/2026 al 01/12/2026), en **3 releases de 2 semanas**, con sprints de **1 semana que comienzan en miércoles**.
- Equipo de **4 personas** a 6 h/semana cada una; coste de personal de **1.996,88 €** (Σ horas asignadas × tarifa: 46 h de historias y 54 h de gestión, D-26) y precio al cliente de **3.737,53 € IVA incluido** (cálculo en `docs/organization/company.md`).
- Tecnologías del proyecto (D-29, 28/10/2026): Python 3.12 con Django 5, plantillas HTML y CSS, SQLite, pytest con pytest-django, Ruff y GitHub Actions. Ramas con GitFlow y commits con smart commits de Jira.

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
