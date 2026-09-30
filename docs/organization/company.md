# Ficha de la empresa y del equipo

## Empresa
| Campo | Valor |
|---|---|
| Nombre | *MedSwap* |
| Propósito | Desarrollar software a medida para gestión de personas y turnos en organizaciones con horarios rotativos. |
| Servicios | Análisis, desarrollo, pruebas y despliegue de aplicaciones web. |
| Contexto | Empresa ficticia; cliente ficticio: Hospital Comarcal Vega Alta. Producto: TurnoLibre. |

## Equipo
| Miembro (GitHub) | Rol principal | Horas/semana | Coste/hora empresa |
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
Aprobado por el equipo el 30/09/2026: perfil *júnior*, salarios de referencia de *Glassdoor*.

*Por qué júnior:* MedSwap es una empresa de reciente creación formada por titulados sin experiencia profesional previa; un salario de nivel medio no sería creíble para este equipo.

*Método:* coste/hora empresa = salario bruto anual × 1,32 ÷ 1.760 h.
- *Salario bruto anual:* salario medio de un perfil júnior en España según Glassdoor. *[COMPLETAR: enlace a cada consulta de Glassdoor y fecha de consulta; si el valor publicado difiere, sustituir la cifra de la tabla y recalcular]*.
- *× 1,32:* cotizaciones a la Seguridad Social a cargo de la empresa (≈ 32 %: contingencias comunes, desempleo, FOGASA, formación profesional, MEI y accidentes de trabajo).
- *1.760 h/año:* 40 h/semana × 44 semanas efectivas (descontando vacaciones y festivos).

| Rol | Puesto consultado en Glassdoor | Salario bruto anual | Coste empresa anual (× 1,32) | Coste/hora |
|---|---|---|---|---|
| Product Owner | Product Owner júnior | 30.000 € | 39.600 € | *22,50 €* |
| Scrum Master | Scrum Master júnior | 28.000 € | 36.960 € | *21,00 €* |
| Tech Lead | Desarrollador/a de software (perfil técnico con mayor responsabilidad) | 34.000 € | 44.880 € | *25,50 €* |
| DevOps / QA | QA / DevOps júnior | 27.000 € | 35.640 € | *20,25 €* |

*Por qué este orden:* el Tech Lead asume la responsabilidad técnica y de arquitectura, por lo que tiene la tarifa más alta; Product Owner y Scrum Master tienen tarifas similares por su papel de gestión; DevOps/QA se sitúa en la media entre DevOps (más alto) y QA (más bajo).

## Coste directo de personal
Cada miembro dedica 5 h/semana × 6 semanas = *30 h*. Se pagan las 120 h completas, no solo la capacidad efectiva: las reuniones y la coordinación también son trabajo remunerado.

| Rol | Horas | Coste/hora | Coste |
|---|---|---|---|
| Product Owner | 30 | 22,50 € | 675,00 € |
| Scrum Master | 30 | 21,00 € | 630,00 € |
| Tech Lead | 30 | 25,50 € | 765,00 € |
| DevOps / QA | 30 | 20,25 € | 607,50 € |
| *Total* | *120* | | *2.677,50 €* |

## Coste total y precio al cliente
Estructura aprobada el 30/09/2026. Se revisará en H4 con la planificación final.

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
