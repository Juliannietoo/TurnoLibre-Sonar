# TurnoLibre — Requisitos no funcionales

Versión 1.0 · 02/10/2026 · Responsable: Juliannietoo (DevOps/QA)

Cada requisito debe ser *medible*: tener un umbral o una condición que se pueda comprobar con una prueba o una revisión.
Las historias los referencian por su ID en el apartado "Verificación y restricciones" de su ficha.

## Catálogo

| ID | Categoría | Requisito | Umbral / métrica | Cómo se verifica | Objetivo / principio | Historias afectadas |
|---|---|---|---|---|---|---|
| NFR-001 | Seguridad | Toda operación se autoriza en el servidor según el rol del usuario, aunque la interfaz no la muestre | 100 % de las operaciones del responsable rechazadas con sesión de empleado y viceversa (HTTP 401/403) | Prueba automatizada que llama a cada operación con el rol incorrecto y sin sesión | Principio 5 · RT-03 | US-002, US-009, US-010, US-017, US-018 |
| NFR-002 | Seguridad | Almacenamiento seguro de credenciales mediante hashing criptográfico con sal | 100 % de contraseñas almacenadas mediante algoritmo robusto (bcrypt con coste ≥ 10 o Argon2id); 0 contraseñas en claro en base de datos o trazas | Inspección de código, auditoría estática y prueba unitaria que verifica que el hash en base de datos no contiene el texto en claro | Principio 5 de la constitución | US-002 |
| NFR-003 | Privacidad | Uso exclusivo de datos ficticios o sintéticos y aislamiento de información sensible | 0 datos personales o sanitarios reales en el repositorio, base de datos o logs; empleados solo ven información de su ámbito y servicio | Revisión estática del conjunto de datos de demostración y pruebas de acceso no autorizado entre servicios | Principio 5 de la constitución | US-003, US-006, US-008, US-017 |
| NFR-004 | Accesibilidad | Flujos principales y controles de formulario accesibles según pautas WCAG 2.1 AA básicas | 100 % de elementos interactivos operables mediante teclado, contraste ≥ 4.5:1 en texto normal y controles etiquetados; 0 violaciones críticas | Auditoría automatizada (axe-core / Lighthouse) combinada con revisión manual mediante navegación exclusiva por teclado | Principio 5 de la constitución (usabilidad y accesibilidad) | US-002, US-005, US-007, US-008, US-009, US-010, US-017, US-018, US-024 |
| NFR-005 | Usabilidad | Mensajes de rechazo y error claros, comprensibles y recuperables | 100 % de las validaciones fallidas indican el identificador de la regla (RN-01 a RN-06) y el motivo en lenguaje claro sin tecnicismos | Pruebas automatizadas de validación que asertan la presencia del código de regla y el texto explicativo esperado | G01 · G02 · Experiencia "Recuperable" | US-002, US-009, US-010, US-012, US-013, US-014, US-015, US-018 |
| NFR-006 | Rendimiento | Tiempo de respuesta ágil en la validación y cálculo de reglas de negocio en el servidor | Tiempo de respuesta < 500 ms (percentil 95 < 1 s) para validar el cuadrante completo de dos empleados con los datos de demostración | Prueba automatizada que mide el tiempo de respuesta del motor de validación en el servidor | G02 · G03 (M03) | US-012, US-013, US-014, US-015, US-018 |
| NFR-007 | Fiabilidad | Atomicidad e integridad transaccional en cambios de estado e intercambios | 100 % de operaciones de propuesta, cancelación y resolución ejecutadas como transacción atómica; 0 estados inconsistentes o dobles reservas ante concurrencia | Prueba de integración concurrente automatizada con peticiones simultáneas sobre el mismo turno (RT-02) | RT-02 · Principio 4 de la constitución | US-009, US-010, US-011, US-018 |
| NFR-008 | Instalabilidad | Despliegue e instalación del entorno de demostración desde cero de forma reproducible | Instalación y arranque completados en < 10 minutos en un entorno limpio siguiendo exclusivamente el guion documentado | Prueba de ejecución limpia realizada por una persona ajena a la implementación (métrica M04) | G04 · M04 | US-001, US-023 |
| NFR-009 | Compatibilidad | Funcionamiento correcto en navegadores web de escritorio modernos | 100 % de funcionalidad y estilos visuales correctos en las dos últimas versiones estables de Google Chrome, Mozilla Firefox y Microsoft Edge | Suite de pruebas de interfaz cross-browser automatizada y verificación visual en resolución de escritorio (≥ 1280x720) | Supuesto A-03 | Todas las historias con interfaz (US-002, US-005, US-007, US-008, US-009, US-010, US-017, US-018, US-019, US-020, US-024) |

## Notas
- Los umbrales han sido acordados por DevOps/QA y alineados con los objetivos del producto y los riesgos técnicos (RT-01, RT-02, RT-03).
- Las fichas de historias de usuario en `specs/EP-XXX/spec.md` referencian estos requisitos por su ID (`NFR-001` a `NFR-009`) en su sección de "Verificación y restricciones".
