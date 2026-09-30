# TurnoLibre — Riesgos técnicos

Revisión técnica inicial · Tech Lead (MarvelinoGG) · 29/09/2026

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| RT-01 | Complejidad de las reglas de negocio | [Alta/Media/Baja] | [Alto/Medio/Bajo] | Centralizar las reglas en un módulo de lógica de negocio y probar cada regla y sus casos límite | Abierto |
| RT-02 | Concurrencia y consistencia en los intercambios | [ ] | [ ] | Validar y confirmar dentro de una transacción y volver a comprobar las reglas justo antes de confirmar | Abierto |
| RT-03 | Control de acceso por roles sin definir | [ ] | [ ] | Definir los permisos de cada rol y comprobar siempre la autorización en el servidor | Abierto |

## RT-01 · Complejidad de las reglas de negocio de los turnos
La constitución establece que deben comprobarse reglas como el descanso mínimo, el límite de horas o la cobertura antes de aprobar cualquier intercambio. A medida que aumenten las reglas y sus combinaciones, la lógica de validación puede volverse difícil de mantener y probar.
*Mitigación:* centralizar las reglas en un módulo o capa de lógica de negocio y definir pruebas específicas para cada regla y sus casos límite.

## RT-02 · Concurrencia y consistencia en los intercambios de turnos
Dos solicitudes de intercambio pueden afectar a los mismos turnos a la vez. Aunque ambas sean válidas al comprobarse, la aprobación de una puede invalidar la otra, lo que provocaría estados inconsistentes o problemas de cobertura.
*Mitigación:* validar y confirmar los intercambios de forma consistente, con transacciones y una nueva comprobación de las reglas antes de la confirmación definitiva.

## RT-03 · Definición insuficiente del control de acceso por roles
La constitución distingue entre empleado y responsable, pero no especifica qué acciones puede realizar cada uno. Esto podría permitir operaciones no autorizadas o diferencias entre la interfaz y el servidor.
*Mitigación:* definir los permisos de cada rol y comprobar siempre la autorización en el servidor.