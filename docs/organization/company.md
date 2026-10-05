# Ficha de la empresa y del equipo

## Empresa
| Campo | Valor |
|---|---|
| Nombre | *MedSwap* |
| Propósito | Desarrollar software a medida para gestión de personas y turnos en organizaciones con horarios rotativos. |
| Servicios | Análisis, desarrollo, pruebas y despliegue de aplicaciones web. |
| Contexto | Empresa ficticia; cliente ficticio: Hospital Comarcal Vega Alta. Producto: TurnoLibre. |

## Equipo
| Miembro (GitHub) | Rol principal | Horas/semana | Coste/hora aprobado el 30/09 |
|---|---|---|---|
| [Lucansado](https://github.com/Lucansado) | Product Owner | 5 | 22,50 € |
| [PaulaJCruz](https://github.com/PaulaJCruz) | Scrum Master | 5 | 21,00 € |
| [MarvelinoGG](https://github.com/MarvelinoGG) | Tech Lead | 5 | 25,50 € |
| [Juliannietoo](https://github.com/Juliannietoo) | DevOps / QA | 5 | 20,25 € |

Todos los miembros participan en el desarrollo con independencia de su rol. La capacidad del equipo se calcula en [capacity.md](capacity.md).

## Justificación de la asignación de roles
| Miembro | Motivo |
|---|---|
| Lucansado (PO) | Asumo el rol de Product Owner para representar las necesidades del hospital ficticio y priorizar con el equipo el valor, alcance y criterios de aceptación de TurnoLibre. |
| PaulaJCruz (SM) | Me encargo de organizar el trabajo del equipo y de que el proceso Scrum funcione: preparo las reuniones, hago el seguimiento de los pendientes y registro las decisiones en la Wiki. |
| MarvelinoGG (TL) | Asumo el rol de Tech Lead para mantener la coherencia técnica del proyecto, identificar dependencias y riesgos y ayudar al equipo a transformar los requisitos definidos en una solución implementable y mantenible.|
| Juliannietoo (DevOps/QA) | Mi objetivo como DevOps/QA es gestionar la calidad, pruebas y entornos del proyecto, asegurando el cumplimiento de los requisitos no funcionales, el despliegue y su correcta operación. |

## Justificación de costes por rol
El presupuesto aprobado el 30/09/2026 utiliza perfiles **júnior** y estimaciones salariales iniciales. El salario del PO fue contrastado el 01/10/2026, el de la SM el 04/10/2026 y los de TL y DevOps/QA el 05/10/2026.

*Por qué júnior:* MedSwap es una empresa de reciente creación formada por titulados sin experiencia profesional previa; un salario de nivel medio no sería creíble para este equipo.

*Método:* coste/hora empresa = salario bruto anual × 1,32 ÷ 1.760 h.
- *Salario bruto anual:* referencia verificada para PO y estimaciones iniciales para los demás roles, según la tabla siguiente.
- *× 1,32:* hipótesis presupuestaria de un 32 % de cargas empresariales; no es un dato de Glassdoor.
- *1.760 h/año:* 40 h/semana × 44 semanas efectivas (descontando vacaciones y festivos).

| Rol | Perfil de referencia | Salario bruto anual | Coste empresa anual (× 1,32) | Coste/hora |
|---|---|---|---|---|
| Product Owner | Junior Product Owner en España; verificado | 26.000 € | 34.320 € | *19,50 €* |
| Scrum Master | Scrum Master en España, 1–3 años de experiencia; verificado | 33.000 € | 43.560 € | *24,75 €* |
| Tech Lead | Junior Software Developer en España; verificado | 21.000 € | 27.720 € | **15,75 €** |
| DevOps / QA | QA / DevOps júnior | 27.000 € | 35.640 € | *20,25 €* |

**Fuente PO:** [Glassdoor: Junior Product Owner en España](https://www.glassdoor.es/Sueldos/junior-product-owner-sueldo-SRCH_KO0,20.htm), consultado el **01/10/2026**. Sueldo base promedio publicado: **26.000 €/año**, con rango de 19.000–30.000 €. La muestra pública es de tres sueldos comunicados en 2021–2022; se utiliza como referencia orientativa.

**Fuente SM:** [Glassdoor: Scrum Master en España](https://www.glassdoor.es/Sueldos/scrum-master-sueldo-SRCH_KO0,12.htm), consultado el **04/10/2026**. Franja de **1–3 años de experiencia: 33.000–40.000 €/año**. Se toma **33.000 €**, el extremo inferior, porque MedSwap es una empresa pequeña y de reciente creación; es el mismo criterio de referencia baja aplicado al PO (26.000 €).

**Fuente TL:** [Glassdoor: Junior Software Developer en España](https://www.glassdoor.es/Sueldos/junior-software-developer-sueldo-SRCH_KO0,25.htm), consultado el **05/10/2026**. Sueldo base promedio publicado: **21.000 €/año**, con un rango de **18.000–25.000 €/año**. Glassdoor indica además una media aproximada de **2.000 €/año** en complementos. Para el presupuesto se utiliza el sueldo base promedio como referencia.

**Fuente DevOps/QA:**[Glassdoor: DevOps en España](https://www.glassdoor.es/Sueldos/espa%C3%B1a-devops-sueldo-SRCH_IL.0,6_IN219_KO7,13.htm), consultado el **05/10/2026**. Sueldo base promedio publicado: 27.000 €/año, con rango de **19.000–30.000** €; Se utiliza como referencia orientativa.

**Revisión pendiente por SM:** el PO pasa de 30.000 a 26.000 €/año (de 22,50 a 19,50 €/h; −90 € por 30 h), la SM de 28.000 a 33.000 €/año (de 21,00 a 24,75 €/h; +112,50 € por 30 h) y el TL de 34.000 a 21.000 €/año (de 25,50 a 15,75 €/h; −292,50 € por 30 h). La referencia de DevOps/QA mantiene los 27.000 €/año utilizados inicialmente. El efecto conjunto sobre el presupuesto queda pendiente de recálculo y aprobación por la SM. Las tablas de presupuesto siguientes conservan la base aprobada del 30/09 hasta que se registre dicha revisión.

## Coste directo de personal — presupuesto aprobado el 30/09
Cada miembro dedica 5 h/semana × 6 semanas = *30 h*. Se pagan las 120 h completas, no solo la capacidad efectiva: las reuniones y la coordinación también son trabajo remunerado.

| Rol | Horas | Coste/hora | Coste |
|---|---|---|---|
| Product Owner | 30 | 22,50 € | 675,00 € |
| Scrum Master | 30 | 21,00 € | 630,00 € |
| Tech Lead | 30 | 25,50 € | 765,00 € |
| DevOps / QA | 30 | 20,25 € | 607,50 € |
| *Total* | *120* | | *2.677,50 €* |

## Coste total y precio al cliente
Presupuesto aprobado el 30/09/2026, pendiente de incorporar la revisión salarial del PO y las verificaciones de los demás roles. Se revisará también en H4 con la planificación final.

| Concepto | Criterio | Importe |
|---|---|---|
| Personal directo | 120 h × coste/hora de cada rol | 2.677,50 € |
| Equipos | 4 portátiles de 1.000 € amortizados en 4 años; parte proporcional de 6 semanas | 115,38 € |
| Software e infraestructura | GitHub y Jira en plan gratuito; servidor de demostración ≈ 20 €/mes durante 1,5 meses | 30,00 € |
| Gastos generales | 15 % del personal directo: oficina, suministros, internet, gestoría | 401,63 € |
| *Coste del proyecto* | | *3.224,51 €* |
| Reserva para imprevistos | 10 % del coste, justificada por los riesgos RT-01 a RT-03 ([`technical-risks.md`](../risks/technical-risks.md)) | 322,45 € |
| *Coste con reserva* | | *3.546,96 €* |
| Margen de beneficio | 15 % | 532,04 € |
| *Precio al cliente (sin IVA)* | | *4.079,00 €* |
| IVA | 21 % | 856,59 € |
| *Precio al cliente (IVA incluido)* | | *4.935,59 €* |
