# EP-001 — Base del producto: acceso y datos de demostración

**Objetivos:** G04
**Línea base documental:** requisitos-v1-revisado · revisión 13/10/2026 (D-18/D-21/D-22/D-23; decisiones en Uso de agentes)
**Límites:** incluye el entorno técnico común, el inicio de sesión con rol y los datos ficticios de demostración (S-04, S-05). No incluye registro de usuarios, recuperación de contraseña ni integración con sistemas reales de RR. HH. (EX-02).

La solución inicial utiliza datos ficticios precargados y restablecibles mediante US-003. La pantalla de alta y modificación de turnos (US-004) se mantiene como mejora opcional, sujeta a capacidad disponible. Decisión confirmada por el PO el 01/10/2026.

## Resultado de la épica

Cualquier persona puede instalar el producto, entrar con una cuenta ficticia de empleado o de responsable y encontrar un cuadrante de demostración coherente con las reglas.

**Aplicación común:** cada historia aplica los límites de esta épica y utiliza datos ficticios. Los requisitos no funcionales aplican según los IDs definidos en el [catálogo NFR](../product/non-functional-requirements.md).

## Historias

### US-001 — Preparar el entorno base

> Como equipo de desarrollo, quiero un repositorio con integración continua y un entorno de demostración, para integrar y desplegar cada incremento de forma estable.

- **Necesidad:** sin un entorno común no se puede cumplir la Definition of Done (CI en verde, despliegue en demostración).
- **Objetivo:** G04
- **Prioridad:** Must — *valor:* habilita todas las demás historias; *riesgo:* alto si se retrasa, porque bloquea el resto; *dependencias:* es la raíz del grafo.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 6 · SM 5 · TL 5 · QA 5).
- **Incertidumbre:** Media (tecnologías fijadas el 28/10/2026, D-29)
- **Predecesoras:** — (la dependencia externa de las tecnologías quedó resuelta con D-29)
- **Plan inicial:** IT-001 · R1

**Criterios de aceptación**
- US-001-AC-01: Un push a una rama ejecuta automáticamente la compilación y las pruebas.
- US-001-AC-02: La integración de cambios en `main` requiere que la compilación y las pruebas terminen correctamente.
- US-001-AC-03: La versión de `main` puede desplegarse en el entorno de demostración siguiendo un procedimiento documentado.

**Verificación y restricciones**
- NFR: NFR-008 (instalabilidad y reproducibilidad del entorno en < 10 min).
- Restricción: uso de las tecnologías del proyecto (D-29): Python 3.12 con Django 5, plantillas HTML y CSS, SQLite, pytest con pytest-django, Ruff y GitHub Actions.

- **Reglas y límites:** Sin regla de negocio propia; se aplican los límites de la épica. Se aplican los límites comunes de la épica.

---

### US-002 — Iniciar sesión con rol  *(muestra detallada)*

> **Cambio D-18 (06/10/2026):** sin bloqueo por intentos fallidos; queda como mejora futura.

> Como usuario de TurnoLibre, quiero iniciar sesión con mi cuenta ficticia, para acceder solo a las funciones de mi rol (empleado o responsable).

- **Necesidad:** empleados y responsable realizan acciones distintas; sin identificación no hay trazabilidad de quién pide, acepta y aprueba.
- **Objetivo:** G04 (producto evaluable con cuentas de prueba) y principio 5 de la constitución (control de acceso por rol).
- **Prioridad:** Must — *valor:* todo el flujo depende de saber quién es el usuario; *riesgo:* mitiga RT-03; *dependencias:* predecesora de todas las historias funcionales.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 6 · SM 5 · TL 8 · QA 5); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Media
- **Predecesoras:** US-001 (técnica), US-003 (técnica)
- **Plan inicial:** IT-002 · R1

**Criterios de aceptación**
- US-002-AC-01: Con usuario y contraseña correctos de un empleado, se inicia una sesión identificada con su rol y se muestra su página de inicio, sin opciones exclusivas del responsable.
- US-002-AC-02: Con credenciales del responsable, se inicia una sesión con su rol y servicio. El acceso no depende de que el calendario o la bandeja estén implementados; cada función se incorpora a la navegación al estar disponible.
- US-002-AC-03: Con credenciales incorrectas, se muestra "Usuario o contraseña incorrectos" sin indicar cuál de los dos falla.
- US-002-AC-04: Un usuario sin sesión que abre una página interna es redirigido al inicio de sesión.
- US-002-AC-05: Una petición al servidor a una operación del responsable hecha con sesión de empleado es rechazada.
- US-002-AC-06 (fuera de esta versión por D-18): Cinco intentos consecutivos con contraseña incorrecta bloquean el inicio de sesión de esa cuenta durante 15 minutos desde el quinto fallo. Durante ese periodo tampoco se admite la contraseña correcta.
- US-002-AC-07 (fuera de esta versión por D-18): Al cumplirse los 15 minutos se permite volver a intentar el acceso y se reinicia el contador. Los intentos durante el bloqueo no prolongan su duración; un acceso correcto también reinicia el contador.
- US-002-AC-08 (fuera de esta versión por D-18): El servidor aplica el bloqueo aunque se cambie de navegador. Los fallos de acceso, incluidos los de cuentas bloqueadas o inexistentes, muestran el mismo mensaje genérico.
- US-002-AC-09: Cerrar sesión invalida el acceso a operaciones protegidas en el servidor; una sesión caducada se trata como una sesión no iniciada.

**Reglas:** matriz de permisos por rol:

| Acción | Empleado | Responsable |
|---|---|---|
| Ver su calendario | Sí | Sí |
| Proponer y aceptar intercambios; cancelar si se incorpora US-011 | Sí | No |
| Ver bandeja y resolver solicitudes | No | Sí |
| Ver el detalle de sus propias solicitudes | Sí | No |
| Ver historial de decisiones de su servicio | No | Sí |

**Verificación y restricciones**
- NFR: NFR-001 (autorización en servidor por rol, RT-03), NFR-002 (contraseñas hasheadas con sal), NFR-004 (accesibilidad básica WCAG 2.1 AA en formulario), NFR-005 (mensajes de error genéricos y claros) y NFR-009 (compatibilidad en navegadores). El bloqueo por intentos fallidos queda fuera de esta versión (D-18).
- Restricción: solo cuentas ficticias (NFR-003); no hay alta de usuarios en el MVP.

**Ejemplos**
- `empleado01` / contraseña de demo → sesión de empleado y página de inicio de Ana (Enfermería, Urgencias).
- `responsable01` → sesión del responsable de Urgencias, con acceso solo a las funciones de su rol.

**Casos límite**
- El nombre de usuario admite mayúsculas y espacios exteriores: se normaliza antes de identificar la cuenta. La contraseña se compara sin alterarla.
- Sesión caducada mientras se rellena una propuesta: el servidor rechaza el envío y pide volver a iniciar sesión; no crea ninguna solicitud.
- Intentos con contraseña incorrecta seguidos de una correcta: permite entrar; el MVP no añade bloqueo por intentos fallidos.

**Supuestos**
- Hay un único responsable por servicio (A-02).
- No se incluyen bloqueo temporal, recuperación de contraseña ni desbloqueo manual en esta versión (D-18).

---

### US-003 — Cargar los datos de demostración

> **Cambio D-18 (06/10/2026):** un solo servicio con 2 categorías y sin semanas con cambio de hora; RN-04 (cobertura 3/3/2) se comprueba aquí, al preparar el cuadrante.

> Como evaluador, quiero que la aplicación arranque con empleados, turnos y un cuadrante ficticios, para poder probarla sin preparar datos.

- **Necesidad:** la métrica M04 exige que un tercero evalúe el producto siguiendo solo el guion.
- **Objetivo:** G04 · S-04/S-05
- **Prioridad:** Must — *valor:* sin datos no se puede demostrar nada; *riesgo:* un cuadrante incoherente falsearía las pruebas de reglas; *dependencias:* predecesora del calendario y del flujo de intercambio.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 6 · SM 5 · TL 5 · QA 5); revisada por D-18: **3 h-p**, votada por el equipo.
- **Incertidumbre:** Media (preparar un cuadrante coherente con cobertura y descansos).
- **Predecesoras:** US-001 (técnica)
- **Plan inicial:** IT-001 · R1

**Criterios de aceptación**
- US-003-AC-01: Tras la instalación existe 1 servicio con 2 categorías profesionales, 1 responsable y los empleados necesarios para cubrir el mínimo 3/3/2 (D-18).
- US-003-AC-02: El cuadrante inicial cumple RN-01, RN-02, RN-04 y RN-06. Hay empleados compatibles para probar RN-03 y fechas que permiten solicitudes con RN-05; los escenarios inválidos se preparan de forma controlada para las pruebas.
- US-003-AC-03: Los datos pueden restablecerse a su estado inicial con un único paso documentado.

**Verificación y restricciones**
- Reglas: RN-04 (el cuadrante de partida cumple 3/3/2; mínimo teórico de 11 empleados por servicio, ver [reglas de negocio](../product/business-rules.md)).
- Restricción: datos 100 % ficticios (principio 5).
- NFR: NFR-003 (datos ficticios) y NFR-008 (instalación reproducible). Todos los datos son ficticios y se restablecen con un único procedimiento documentado.

---

### US-004 — Mantener los turnos del cuadrante

> Como responsable, quiero dar de alta y modificar turnos asignados, para mantener el cuadrante de demostración.

- **Necesidad:** permitiría preparar escenarios de prueba sin tocar datos a mano.
- **Objetivo:** G04 · S-05
- **Prioridad:** Could — *valor:* bajo, US-003 ya aporta los datos; *riesgo:* abre casos de edición que chocan con solicitudes en curso; *dependencias:* ninguna historia depende de ella.
- **Estimación:** consenso del 06/10/2026: **5 h-p** (individuales: PO 5 · SM 8 · TL 5 · QA 5).
- **Incertidumbre:** Media
- **Predecesoras:** US-002 (funcional), US-003 (técnica), US-012 (técnica), US-013 (técnica), US-014 (técnica)
- **Plan inicial:** fuera del plan salvo capacidad sobrante

**Criterios de aceptación**
- US-004-AC-01: El responsable puede asignar un turno libre a un empleado de su servicio.
- US-004-AC-02: El sistema impide modificar un turno que forma parte de una solicitud pendiente.
- US-004-AC-03: Solo el responsable del servicio puede modificar sus turnos; la asignación resultante respeta descansos, horas, solapes y cobertura mínima.

**Verificación y restricciones**
- Reglas: la asignación debe cumplir RN-01, RN-02, RN-04 y RN-06.
- NFR: Autorización en servidor y cambios indivisibles: un fallo conserva el cuadrante anterior.
