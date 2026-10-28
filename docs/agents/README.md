# Agentes de IA de TurnoLibre

Decisión D-20 (07/10/2026); el agente auditor del H4 se añade con D-26 (14/10/2026) y el generador de smart commits de la Práctica 3 con D-29 (28/10/2026). El profesorado proporcionó dos plantillas para GitHub Copilot. El equipo no usa Copilot, así que las plantillas se han adaptado a TurnoLibre y se ejecutan con las herramientas de cada miembro. Las instrucciones son las mismas para todos; solo cambia cómo se cargan.

| ID | Agente | Instrucciones de referencia | Informes |
|---|---|---|---|
| AG-01 | Requirements Agent | [`.github/agents/requirements-reviewer.agent.md`](../../.github/agents/requirements-reviewer.agent.md) | `docs/reviews/requirements/requirements-report-vNN.md` |
| AG-03 | Planning Agent | [`.github/agents/initial-planning-reviewer.agent.md`](../../.github/agents/initial-planning-reviewer.agent.md) | `docs/reviews/initial-planning/initial-planning-review-vNN.md` |
| AG-02 | Agente auditor (H4, opcional) | [`.github/agents/project-auditor.agent.md`](../../.github/agents/project-auditor.agent.md) | `docs/reviews/audit/audit-report-vNN.md` |
| AG-04 | Generador de smart commits (Práctica 3, D-29) | [`.github/agents/jira-smartcommit-generator.agent.md`](../../.github/agents/jira-smartcommit-generator.agent.md) | No guarda informe: devuelve el mensaje de commit |

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

## Generador de smart commits (AG-04)

No revisa documentos ni guarda informes: a partir de la clave de Jira, el tiempo y lo que se ha hecho devuelve el mensaje del commit, que cada uno copia en `git commit -m "…"` o en GitHub Desktop. Formato y reglas en [docs/git/README.md](../git/README.md#3-smart-commits).

- **Claude Code:** `Usa el agente jira-smartcommit-generator: GC02-61, 1h 30m, he creado el proyecto Django con la app de cuentas, terminada.`
- **ChatGPT o Antigravity:** pegar o cargar `.github/agents/jira-smartcommit-generator.agent.md` como en los otros agentes y escribir la misma petición.

Revisa siempre la clave y el tiempo antes de hacer el commit. Su uso no se registra en *Uso de agentes*, porque no hace propuestas que decida el equipo.

## Después de cada ejecución

1. Registrar cada propuesta en *Uso de agentes* (Wiki) con: **Agente e ID**, **Entrada**, **Propuesta**, **Justificación** y **Decisión** (aceptada, aceptada con cambios, rechazada o pendiente). Indicar la herramienta y el modelo.
2. Si la decisión cambia un requisito, una estimación o el plan, la persona responsable hace el cambio y lo enlaza (commit o D-NN).
3. Para comprobar las correcciones se lanza el agente en modo RECHECK, que genera un informe nuevo; nunca se edita un informe anterior.
