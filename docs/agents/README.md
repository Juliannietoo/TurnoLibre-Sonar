# Agentes de IA de TurnoLibre

Decisión D-20 (07/10/2026); el agente auditor del H4 se añade con D-26 (15/10/2026). El profesorado proporcionó dos plantillas para GitHub Copilot. El equipo no usa Copilot, así que las plantillas se han adaptado a TurnoLibre y se ejecutan con las herramientas de cada miembro. Las instrucciones son las mismas para todos; solo cambia cómo se cargan.

| ID | Agente | Instrucciones de referencia | Informes |
|---|---|---|---|
| AG-01 | Requirements Agent | [`.github/agents/requirements-reviewer.agent.md`](../../.github/agents/requirements-reviewer.agent.md) | `docs/reviews/requirements/requirements-report-vNN.md` |
| AG-03 | Planning Agent | [`.github/agents/initial-planning-reviewer.agent.md`](../../.github/agents/initial-planning-reviewer.agent.md) | `docs/reviews/initial-planning/initial-planning-review-vNN.md` |
| AG-02 | Agente auditor (H4, opcional) | [`.github/agents/project-auditor.agent.md`](../../.github/agents/project-auditor.agent.md) | `docs/reviews/audit/audit-report-vNN.md` |

Los agentes **revisan y proponen**. No cambian requisitos, estimaciones, capacidad ni planes, y no aprueban nada. Cada propuesta se registra y la decide el equipo en la página *Uso de agentes* de la Wiki.

## Herramienta de cada miembro

| Miembro | Rol | Herramienta | Cómo carga el agente |
|---|---|---|---|
| PaulaJCruz | SM | Claude Code | Subagentes de `.claude/agents/` |
| Lucansado | PO | Claude y ChatGPT | Claude Code, como la SM, o ChatGPT, como el TL |
| MarvelinoGG | TL | ChatGPT | Instrucciones pegadas en un proyecto de ChatGPT |
| Juliannietoo | DevOps/QA | Antigravity | Instrucción en el chat del agente con el repositorio abierto |

El modelo concreto (por ejemplo, el que aparece en el selector de ChatGPT o de Claude) se anota en cada ejecución, en los metadatos del informe y en el registro de la Wiki.

## Claude Code

1. Abrir el repositorio actualizado (`git pull`).
2. Pedir, por ejemplo:
   - `Usa el agente requirements-reviewer en modo INITIAL sobre specs/EP-001…EP-007 y specs/product/catalogo.md. Commit revisado: <hash>.`
   - `Usa el agente initial-planning-reviewer en modo READINESS con el extracto docs/planning/extracts/<fichero>.md.`
3. El agente crea un solo informe nuevo. Revisar con `git status` que no se ha modificado ningún otro fichero.

Los ficheros de `.claude/agents/` solo adaptan las herramientas. Las instrucciones completas son las de `.github/agents/`.

## ChatGPT

1. Crear un proyecto (o un GPT personalizado) llamado `TurnoLibre · Requirements Agent` o `TurnoLibre · Planning Agent`.
2. Pegar como instrucciones el contenido completo del `.agent.md` correspondiente, sin la cabecera entre `---`.
3. Adjuntar los ficheros de entrada que indica el apartado *Project configuration* del agente.
4. Indicar el modo y el commit: `Modo INITIAL. Commit revisado: <hash>. Revisa US-002, US-009, US-012, US-013, US-014 y US-018 en detalle.`
5. ChatGPT no puede escribir en el repositorio: devuelve el informe en el chat. Guardarlo **sin modificarlo** con el siguiente número libre (`…-vNN.md`) y hacer commit.

## Antigravity

1. Abrir el repositorio actualizado en Antigravity.
2. Escribir en el chat del agente: `Lee .github/agents/requirements-reviewer.agent.md y sigue sus instrucciones. Modo INITIAL. Commit revisado: <hash>.`
3. No permitir la ejecución de comandos. Antes de aceptar los cambios, comprobar que solo se crea el informe en `docs/reviews/…`; cualquier otro cambio se rechaza.

## Después de cada ejecución

1. Registrar cada propuesta en *Uso de agentes* (Wiki) con: **Agente e ID**, **Entrada**, **Propuesta**, **Justificación** y **Decisión** (aceptada, aceptada con cambios, rechazada o pendiente). Indicar la herramienta y el modelo.
2. Si la decisión cambia un requisito, una estimación o el plan, la persona responsable hace el cambio y lo enlaza (commit o D-NN).
3. Para comprobar las correcciones se lanza el agente en modo RECHECK, que genera un informe nuevo; nunca se edita un informe anterior.
