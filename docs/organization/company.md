# Ficha de la empresa y del equipo

## Empresa
| Campo | Valor |
|---|---|
| Nombre | *MedSwap* |
| Propósito | Desarrollar software a medida para gestión de personas y turnos en organizaciones con horarios rotativos. |
| Servicios | Análisis, desarrollo, pruebas y despliegue de aplicaciones web. |
| Contexto | Empresa ficticia; cliente ficticio: Hospital Comarcal Vega Alta. Producto: TurnoLibre. |

## Equipo
| Miembro (GitHub) | Rol principal | Horas/semana | Coste/hora (salario verificado) |
|---|---|---|---|
| [Lucansado](https://github.com/Lucansado) | Product Owner | 6 | 19,50 € |
| [PaulaJCruz](https://github.com/PaulaJCruz) | Scrum Master | 6 | 24,75 € |
| [MarvelinoGG](https://github.com/MarvelinoGG) | Tech Lead | 6 | 15,75 € |
| [Juliannietoo](https://github.com/Juliannietoo) | DevOps / QA | 6 | 20,25 € |

Todos los miembros participan en el desarrollo con independencia de su rol. La capacidad del equipo se calcula en [capacity.md](capacity.md).

## Justificación de la asignación de roles
| Miembro | Motivo |
|---|---|
| Lucansado (PO) | Asumo el rol de Product Owner para representar las necesidades del hospital ficticio y priorizar con el equipo el valor, alcance y criterios de aceptación de TurnoLibre. |
| PaulaJCruz (SM) | Me encargo de organizar el trabajo del equipo y de que el proceso Scrum funcione: preparo las reuniones, hago el seguimiento de los pendientes y registro las decisiones en la Wiki. |
| MarvelinoGG (TL) | Asumo el rol de Tech Lead para mantener la coherencia técnica del proyecto, identificar dependencias y riesgos y ayudar al equipo a transformar los requisitos definidos en una solución implementable y mantenible.|
| Juliannietoo (DevOps/QA) | Mi objetivo como DevOps/QA es gestionar la calidad, pruebas y entornos del proyecto, asegurando el cumplimiento de los requisitos no funcionales, el despliegue y su correcta operación. |

## Justificación de costes por rol
El presupuesto utiliza perfiles **júnior**. Los cuatro salarios se han contrastado en Glassdoor entre el 01/10 y el 05/10/2026; el presupuesto se recalculó el 07/10/2026 por D-21 y el 15/10/2026 por D-26 (fórmula del enunciado: horas asignadas × tarifa).

*Por qué júnior:* MedSwap es una empresa de reciente creación formada por titulados sin experiencia profesional previa; un salario de nivel medio no sería creíble para este equipo.

*Método:* coste/hora empresa = salario bruto anual × 1,32 ÷ 1.760 h.
- *Salario bruto anual:* referencia de Glassdoor verificada para los cuatro roles (enlace y fecha de consulta en las fuentes de abajo).
- *× 1,32:* hipótesis presupuestaria de un 32 % de cargas empresariales; no es un dato de Glassdoor.
- *1.760 h/año:* 40 h/semana × 44 semanas efectivas (descontando vacaciones y festivos).

| Rol | Perfil de referencia | Salario bruto anual | Coste empresa anual (× 1,32) | Coste/hora |
|---|---|---|---|---|
| Product Owner | Junior Product Owner en España; verificado | 26.000 € | 34.320 € | *19,50 €* |
| Scrum Master | Scrum Master en España, 1–3 años de experiencia; verificado | 33.000 € | 43.560 € | *24,75 €* |
| Tech Lead | Junior Software Developer en España; verificado | 21.000 € | 27.720 € | *15,75 €* |
| DevOps / QA | QA / DevOps júnior en España; verificado | 27.000 € | 35.640 € | *20,25 €* |

**Fuente PO:** [Glassdoor: Junior Product Owner en España](https://www.glassdoor.es/Sueldos/junior-product-owner-sueldo-SRCH_KO0,20.htm), consultado el **01/10/2026**. Sueldo base promedio publicado: **26.000 €/año**, con rango de 19.000–30.000 €. La muestra pública es de tres sueldos comunicados en 2021–2022; se utiliza como referencia orientativa.

**Fuente SM:** [Glassdoor: Scrum Master en España](https://www.glassdoor.es/Sueldos/scrum-master-sueldo-SRCH_KO0,12.htm), consultado el **04/10/2026**. Franja de **1–3 años de experiencia: 33.000–40.000 €/año**. Se toma **33.000 €**, el extremo inferior, porque MedSwap es una empresa pequeña y de reciente creación; es el mismo criterio de referencia baja aplicado al PO (26.000 €).

**Fuente TL:** [Glassdoor: Junior Software Developer en España](https://www.glassdoor.es/Sueldos/junior-software-developer-sueldo-SRCH_KO0,25.htm), consultado el **05/10/2026**. Sueldo base promedio publicado: **21.000 €/año**, con un rango de **18.000–25.000 €/año**. Glassdoor indica además una media aproximada de **2.000 €/año** en complementos. Para el presupuesto se utiliza el sueldo base promedio como referencia.

**Fuente DevOps/QA:**[Glassdoor: DevOps en España](https://www.glassdoor.es/Sueldos/espa%C3%B1a-devops-sueldo-SRCH_IL.0,6_IN219_KO7,13.htm), consultado el **05/10/2026**. Sueldo base promedio publicado: 27.000 €/año, con rango de **19.000–30.000** €; Se utiliza como referencia orientativa.

**Revisión D-21 (07/10/2026):** la decisión del PO de planificar 6 h semanales por persona eleva el personal directo de 2.407,50 € a 2.889,00 € y el precio con IVA de 4.460,33 € a 5.307,88 €. Las tarifas y porcentajes se mantienen.

*Nota sobre el TL:* resulta el perfil con menor coste/hora porque la referencia verificada es *Junior Software Developer*; se mantiene por coherencia con el criterio júnior, aunque el rol tenga mayor responsabilidad técnica. Confirmado por todo el equipo en la sesión del 07/10/2026.

## Coste directo de personal
**D-26 (15/10/2026):** se aplica la fórmula del enunciado de la Semana 4: **coste de personal = Σ (horas asignadas × tarifa justificada)**. Las horas asignadas son las del plan del H3–H4 ([`TurnoLibre_H3_planificacion.xlsx`](../planning/TurnoLibre_H3_planificacion.xlsx), versión 4, y planes de ProjectLibre en [`docs/planning/projectlibre/`](../planning/projectlibre/)):
- **Historias de usuario:** 46 h (las Must del catálogo V1).
- **Tareas de gestión (MGT):** 54 h, 9 h por iteración: sprint planning (0,5 h por persona), dailies (0,5 h), review (0,25 h), retrospectiva (0,25 h) y coordinación del rol (PO 0,5 · SM 1 · TL 1 · QA 0,5).

Las horas nominales que no se asignan a ninguna tarea (ausencias por exámenes, márgenes individuales y margen del equipo) no se imputan. Sustituye al cálculo sobre 144 h nominales de D-21 (2.889,00 € de personal y 5.307,88 € de precio).

| Rol | Horas de historias | Horas de gestión | Horas asignadas | Coste/hora | Coste |
|---|---|---|---|---|---|
| Product Owner | 10,5 | 12 | 22,5 | 19,50 € | 438,75 € |
| Scrum Master | 10 | 15 | 25 | 24,75 € | 618,75 € |
| Tech Lead | 12,5 | 15 | 27,5 | 15,75 € | 433,13 € |
| DevOps / QA | 13 | 12 | 25 | 20,25 € | 506,25 € |
| *Total* | *46* | *54* | *100* | | *1.996,88 €* |

## Coste total y precio al cliente
Presupuesto revisado el 15/10/2026 por D-26, con las tarifas verificadas de D-17 y los porcentajes de D-13.

| Concepto | Criterio | Importe |
|---|---|---|
| Personal directo | Σ horas asignadas × coste/hora de cada rol (100 h) | 1.996,88 € |
| Equipos | 4 portátiles de 1.000 € amortizados en 4 años; parte proporcional de 6 semanas | 115,38 € |
| Software e infraestructura | GitHub y Jira en plan gratuito; servidor de demostración ≈ 20 €/mes durante 1,5 meses | 30,00 € |
| Gastos generales | 15 % del personal directo: oficina, suministros, internet, gestoría | 299,53 € |
| *Coste del proyecto* | | *2.441,79 €* |
| Reserva para imprevistos | 10 % del coste, justificada por los riesgos RT-01 a RT-04 ([`technical-risks.md`](../risks/technical-risks.md)) | 244,18 € |
| *Coste con reserva* | | *2.685,97 €* |
| Margen de beneficio | 15 % | 402,90 € |
| *Precio al cliente (sin IVA)* | | *3.088,87 €* |
| IVA | 21 % | 648,66 € |
| *Precio al cliente (IVA incluido)* | | *3.737,53 €* |

**Historial:** D-13 (30/09) 4.935,59 € → D-17 (06/10, salarios verificados) 4.460,33 € → D-21 (07/10, 6 h/semana sobre horas nominales) 5.307,88 € → **D-26 (15/10, horas asignadas) 3.737,53 €**.
