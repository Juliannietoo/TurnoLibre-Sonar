# Cuadrante ficticio de demostración

Diseño de TK-005 ([GC02-184](https://gc02-gps26.atlassian.net/browse/GC02-184)), dentro de US-003 ([GC02-173](https://gc02-gps26.atlassian.net/browse/GC02-173)). Preparado el 28/10/2026 para que Paula implemente la carga y el restablecimiento en TK-006 ([GC02-185](https://gc02-gps26.atlassian.net/browse/GC02-185)). La comprobación del diseño aporta evidencia a TK-007 ([GC02-186](https://gc02-gps26.atlassian.net/browse/GC02-186)); queda por repetir la comprobación sobre los datos cargados y restablecidos por Django.

Todos los nombres y datos son inventados. No se incluyen datos sanitarios ni cuentas o contraseñas reales.

## Archivos y alcance

- `cuadrante.json`: fuente de datos estructurada, UTF-8, versión de esquema 1.
- `cuadrante.csv`: vista equivalente por empleado y fecha, UTF-8; `L` significa libre.
- Este documento: relación de personas, tablas semanales y contrato de integración.

El periodo de demostración comprende cuatro semanas naturales completas, del **02/11/2026 al 29/11/2026**. Se incluyen también las asignaciones del **01/11 y del 30/11** como guardas para comprobar las noches que cruzan el límite semanal y el descanso en los extremos. En total hay **30 fechas, 16 empleados y 240 asignaciones**. Los libres no son asignaciones en el JSON.

Las fechas se interpretan en **Europe/Madrid**. Ninguna fecha del conjunto coincide con un cambio de hora. La cobertura es exactamente **3 mañanas, 3 tardes y 2 noches por servicio y fecha de inicio**, también en los días de guarda.

## Servicio, categorías y personas

Servicio único: `urgencias` (Urgencias). Categorías: `enfermeria` (Enfermería) y `auxiliar` (Auxiliar de enfermería). La persona responsable es **Rosa Horizonte**, identificador `responsable01`, del servicio `urgencias`; no tiene asignaciones y no cuenta para la cobertura. Existen 10 empleados de Enfermería y 6 auxiliares.

| Identificador | Nombre ficticio | Categoría | Equipo | Franja |
|---|---|---|---|---|
| empleado01 | Ana Vega | Enfermería | A | M |
| empleado02 | Berta Prado | Enfermería | A | M |
| empleado03 | Carla Lago | Auxiliar | A | M |
| empleado04 | Diego Alba | Enfermería | B | M |
| empleado05 | Elena Rios | Enfermería | B | M |
| empleado06 | Fabio Sol | Auxiliar | B | M |
| empleado07 | Gala Roble | Enfermería | A | T |
| empleado08 | Hugo Sierra | Enfermería | A | T |
| empleado09 | Ines Luna | Auxiliar | A | T |
| empleado10 | Jaime Valle | Enfermería | B | T |
| empleado11 | Kira Mar | Enfermería | B | T |
| empleado12 | Leo Pino | Auxiliar | B | T |
| empleado13 | Mara Nube | Enfermería | A | N |
| empleado14 | Nico Campo | Auxiliar | A | N |
| empleado15 | Olga Monte | Enfermería | B | N |
| empleado16 | Pablo Brisa | Auxiliar | B | N |

## Franjas y patrón

| Código | Inicio local | Fin local | Duración |
|---|---|---|---|
| M | 08:00 | 15:00 del mismo día | 7 h |
| T | 15:00 | 22:00 del mismo día | 7 h |
| N | 22:00 | 08:00 del día siguiente | 10 h |
| L | — | — | Libre |

El equipo A trabaja el 01/11 y cada dos días; el B, el 02/11 y cada dos días. Cada empleado conserva su franja en este conjunto inicial. Cada equipo aporta M: 2 de Enfermería y 1 auxiliar; T: 2 de Enfermería y 1 auxiliar; N: 1 de Enfermería y 1 auxiliar. RN-04 define la cobertura total por servicio y franja; este reparto por categoría facilita los intercambios compatibles de RN-03.

El descanso entre asignaciones consecutivas es de 41 h para M y T, y de 38 h para N. En las semanas completas, M/T suman 21 o 28 h; N suma 32 o 38 h, al repartir las noches del domingo entre dos semanas. Ningún empleado tiene dos inicios en una fecha ni turnos solapados.

## Semana 1: 02/11–08/11/2026

| Empleado | Lun 02/11 | Mar 03/11 | Mié 04/11 | Jue 05/11 | Vie 06/11 | Sáb 07/11 | Dom 08/11 |
|---|---|---|---|---|---|---|---|
| empleado01 | L | M | L | M | L | M | L |
| empleado02 | L | M | L | M | L | M | L |
| empleado03 | L | M | L | M | L | M | L |
| empleado04 | M | L | M | L | M | L | M |
| empleado05 | M | L | M | L | M | L | M |
| empleado06 | M | L | M | L | M | L | M |
| empleado07 | L | T | L | T | L | T | L |
| empleado08 | L | T | L | T | L | T | L |
| empleado09 | L | T | L | T | L | T | L |
| empleado10 | T | L | T | L | T | L | T |
| empleado11 | T | L | T | L | T | L | T |
| empleado12 | T | L | T | L | T | L | T |
| empleado13 | L | N | L | N | L | N | L |
| empleado14 | L | N | L | N | L | N | L |
| empleado15 | N | L | N | L | N | L | N |
| empleado16 | N | L | N | L | N | L | N |

Cobertura diaria: **M3 / T3 / N2**.

## Semana 2: 09/11–15/11/2026

| Empleado | Lun 09/11 | Mar 10/11 | Mié 11/11 | Jue 12/11 | Vie 13/11 | Sáb 14/11 | Dom 15/11 |
|---|---|---|---|---|---|---|---|
| empleado01 | M | L | M | L | M | L | M |
| empleado02 | M | L | M | L | M | L | M |
| empleado03 | M | L | M | L | M | L | M |
| empleado04 | L | M | L | M | L | M | L |
| empleado05 | L | M | L | M | L | M | L |
| empleado06 | L | M | L | M | L | M | L |
| empleado07 | T | L | T | L | T | L | T |
| empleado08 | T | L | T | L | T | L | T |
| empleado09 | T | L | T | L | T | L | T |
| empleado10 | L | T | L | T | L | T | L |
| empleado11 | L | T | L | T | L | T | L |
| empleado12 | L | T | L | T | L | T | L |
| empleado13 | N | L | N | L | N | L | N |
| empleado14 | N | L | N | L | N | L | N |
| empleado15 | L | N | L | N | L | N | L |
| empleado16 | L | N | L | N | L | N | L |

Cobertura diaria: **M3 / T3 / N2**.

## Semana 3: 16/11–22/11/2026

| Empleado | Lun 16/11 | Mar 17/11 | Mié 18/11 | Jue 19/11 | Vie 20/11 | Sáb 21/11 | Dom 22/11 |
|---|---|---|---|---|---|---|---|
| empleado01 | L | M | L | M | L | M | L |
| empleado02 | L | M | L | M | L | M | L |
| empleado03 | L | M | L | M | L | M | L |
| empleado04 | M | L | M | L | M | L | M |
| empleado05 | M | L | M | L | M | L | M |
| empleado06 | M | L | M | L | M | L | M |
| empleado07 | L | T | L | T | L | T | L |
| empleado08 | L | T | L | T | L | T | L |
| empleado09 | L | T | L | T | L | T | L |
| empleado10 | T | L | T | L | T | L | T |
| empleado11 | T | L | T | L | T | L | T |
| empleado12 | T | L | T | L | T | L | T |
| empleado13 | L | N | L | N | L | N | L |
| empleado14 | L | N | L | N | L | N | L |
| empleado15 | N | L | N | L | N | L | N |
| empleado16 | N | L | N | L | N | L | N |

Cobertura diaria: **M3 / T3 / N2**.

## Semana 4: 23/11–29/11/2026

| Empleado | Lun 23/11 | Mar 24/11 | Mié 25/11 | Jue 26/11 | Vie 27/11 | Sáb 28/11 | Dom 29/11 |
|---|---|---|---|---|---|---|---|
| empleado01 | M | L | M | L | M | L | M |
| empleado02 | M | L | M | L | M | L | M |
| empleado03 | M | L | M | L | M | L | M |
| empleado04 | L | M | L | M | L | M | L |
| empleado05 | L | M | L | M | L | M | L |
| empleado06 | L | M | L | M | L | M | L |
| empleado07 | T | L | T | L | T | L | T |
| empleado08 | T | L | T | L | T | L | T |
| empleado09 | T | L | T | L | T | L | T |
| empleado10 | L | T | L | T | L | T | L |
| empleado11 | L | T | L | T | L | T | L |
| empleado12 | L | T | L | T | L | T | L |
| empleado13 | N | L | N | L | N | L | N |
| empleado14 | N | L | N | L | N | L | N |
| empleado15 | L | N | L | N | L | N | L |
| empleado16 | L | N | L | N | L | N | L |

Cobertura diaria: **M3 / T3 / N2**.

## Contrato para TK-006 (Django)

El JSON es independiente de los nombres definitivos de las aplicaciones y modelos, que decide el TL en TK-001. No es una fixture `loaddata` ligada a modelos aún inexistentes. El comando de gestión de TK-006 debe leer esta fuente y mapear sus identificadores estables a los modelos de Django, sin reemplazarla por datos aleatorios.

1. Leer `timezone`, `periodo`, `servicio`, `categorias` y `responsable`.
2. Crear los 16 empleados de `empleados` por `id`, enlazando `servicio_id` y `categoria_id`. Cada empleado se corresponde con una cuenta ficticia de rol empleado; `responsable01`, con una de rol responsable. El comando de carga decide las credenciales de demostración y debe usar el hash de contraseñas de Django.
3. Para cada elemento de `asignaciones`, resolver `empleado_id` y `turno`; combinar `fecha` con `turnos[código].inicio` y `.fin` en Europe/Madrid. Si el fin es anterior o igual al inicio, corresponde al día siguiente (N). Persistir instantes conscientes de zona horaria.
4. Cargar también el 01/11 y el 30/11. Las tablas semanales muestran solo el periodo central. RN-02 suma tiempo realmente transcurrido dentro de cada lunes–domingo, incluyendo las horas que llegan de la noche anterior.
5. Restablecer en una transacción los datos ficticios a esta misma fuente y eliminar los cambios/solicitudes de demostración que impidan repetir el escenario. El nombre del comando y el tratamiento de relaciones pendientes se concretan en TK-006.
6. Repetir la comprobación de RN-01, RN-02, RN-04 y RN-06 sobre los datos persistidos tras cargar y después de restablecer. Esta verificación de integración es la parte pendiente de TK-007.

Para probar RN-03, `empleado01` y `empleado04` pertenecen a Enfermería/Urgencias y trabajan mañanas en fechas alternas; `empleado03` permite comprobar el rechazo por categoría distinta. Como ejemplo compatible, se pueden intercambiar las mañanas del 02/11 de `empleado04` y del 03/11 de `empleado01`: se mantienen la cobertura y los descansos mínimos. Los escenarios inválidos se preparan aparte y se restablecen después.

El 28/10/2026 los primeros turnos centrales están a más de 48 h y permiten probar RN-05 si se incorpora US-015. Esta condición depende de la hora del servidor: si se evalúa después, habrá que trasladar coherentemente el periodo y sus guardas a semanas futuras sin cambio de hora, volver a verificar las reglas y actualizar JSON, CSV y tablas juntos.

## Comprobación reproducible del diseño

Desde la raíz del repositorio, con Python 3.12 y los paquetes de pruebas del entorno común (en Windows, la zona horaria requiere `tzdata`):

```bash
python tools/validar_cuadrante.py --report docs/reviews/datos-demo/TK-007-diseno.md
python -m pytest tests/test_cuadrante_demo.py
python -m ruff check tools tests
```

El comprobador devuelve código 0 cuando el diseño cumple las reglas y código 1 si encuentra errores. Las pruebas incluyen datos alterados que deben rechazarse y una noche de domingo repartida entre dos semanas. El [informe del diseño](../../docs/reviews/datos-demo/TK-007-diseno.md) conserva las horas de cada empleado por semana. Repetir esta comprobación sobre el JSON no sustituye la verificación de los datos persistidos tras TK-006.

## Referencias

- [Especificación US-003](../../specs/EP-001-base-del-producto/spec.md).
- [Reglas de negocio](../../specs/product/business-rules.md).
- [Tecnologías acordadas, D-29](../../docs/architecture/technology-stack.md).
