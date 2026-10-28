# Git, GitFlow y Jira · Práctica 3

Cómo trabajamos con el repositorio a partir de IT-002 (D-29). Tecnologías en [docs/architecture/technology-stack.md](../architecture/technology-stack.md). Proyecto Jira: clave `GC02`, <https://gc02-gps26.atlassian.net/jira/software/projects/GC02/boards/1>.

## 1. Ramas

| Rama | Para qué | Quién integra |
|---|---|---|
| `main` | Versión entregable. Solo recibe `develop` al cerrar un sprint. | SM o DevOps |
| `develop` | Integración de las historias terminadas. Se crea una vez desde `main`. | Responsables de cada historia |
| `feature/GC02-XX-nombre` | Una rama por historia (`GC02-XX` es la clave de la historia en Jira). Se crea desde `develop`. | Quienes tienen subtareas en la historia |

Nunca se programa directamente en `main` ni en `develop`. Todas las integraciones son **merge sin fast-forward** (`--no-ff`). No se usa *squash* ni *rebase*.

## 2. Preparación (una vez por persona)

```bash
git clone https://github.com/UniExtremadura/TurnoLibre_GC02.git
cd TurnoLibre_GC02
git config user.name "Nombre Apellido"
git config user.email "correo-de-tu-cuenta-de-Jira"
git config merge.ff false
```

- **El correo de Git tiene que ser el de tu usuario de Jira.** Si no coincide, Jira no asocia el commit a nadie y no registra ni el tiempo ni el cambio de estado.
- En GitHub Desktop el correo está en *File → Options → Git*; `merge.ff` hay que fijarlo en la terminal de todas formas.
- Instalación del entorno de Python: [technology-stack.md](../architecture/technology-stack.md#puesta-en-marcha-en-local).

**Una sola vez para todo el equipo:**

- DevOps crea `develop` desde `main` y la sube: `git checkout -b develop main` y `git push -u origin develop`.
- La SM conecta Jira con GitHub en *Aplicaciones → Explorar más aplicaciones → GitHub for Jira*. El acceso a la organización UniExtremadura lo aprueba el profesor.

## 3. Smart commits

Cada commit lleva en **una sola línea** la clave de Jira y los comandos:

```text
<CLAVE> #time <tiempo> #comment <qué se ha hecho> #done
```

| Parte | Regla |
|---|---|
| `<CLAVE>` | La de la **subtarea** en Jira (`GC02-NN`), no la de la historia. |
| `#time` | Tiempo real dedicado: `1h 30m`, `45m`, `2h`. Solo en commits de trabajo, **nunca en merges**. |
| `#comment` | Qué se ha hecho, en español y en una frase. |
| `#done` | Solo si la subtarea está terminada. Mueve la incidencia a *Done*. |

Ejemplos:

```text
GC02-61 #time 1h 30m #comment Proyecto Django con la aplicación de cuentas y configuración de pytest #done
GC02-62 #time 45m #comment Primera versión del flujo de GitHub Actions
GC02-62 #time 45m #comment Flujo de CI con Ruff, migraciones y pytest; bloquea si falla #done
```

El agente [`jira-smartcommit-generator`](../../.github/agents/jira-smartcommit-generator.agent.md) genera el mensaje a partir de una descripción (ver [docs/agents/README.md](../agents/README.md)).

## 4. Al empezar cada sprint (planning del miércoles)

1. El equipo revisa las historias del sprint y sus subtareas en Jira (responsable, estimación y descripción).
2. Para cada historia, uno de sus responsables abre la historia en Jira → **Desarrollo → Crear rama**.
   - Repositorio: `TurnoLibre_GC02`.
   - Rama de origen: **`develop`**.
   - Tipo: `feature`.
   - Nombre: `feature/GC02-XX-nombre-corto`.

   Si la conexión con Jira todavía no funciona, se crea a mano: `git checkout develop`, `git pull`, `git checkout -b feature/GC02-XX-nombre-corto` y `git push -u origin feature/GC02-XX-nombre-corto`.

## 5. Por cada subtarea (cada desarrollador)

1. En Jira, pasar la subtarea a **In Progress**.
2. Ponerse en la rama de la historia y traer lo último:

   ```bash
   git fetch
   git checkout feature/GC02-XX-nombre-corto
   git pull
   ```

3. Programar y comprobar en local: `ruff check .` y `pytest`.
4. **Un commit y un push por subtarea:**

   ```bash
   git add .
   git commit -m "GC02-NN #time 1h 15m #comment Lo que se ha hecho #done"
   git push
   ```

5. Comprobar en Jira que la subtarea tiene el tiempo, el comentario y el estado *Done*, y en GitHub que la integración continua está en verde.

**Si una historia tiene subtareas de varias personas, se trabaja por turnos.** Cada uno hace `git pull` antes de empezar y avisa por Discord cuando ha subido lo suyo, para no pisarse.

## 6. Integrar una historia en `develop`

Cuando todas las subtareas de la historia están en *Done*, uno de sus responsables:

```bash
# 1. Traer develop a la rama de la historia y probar
git checkout feature/GC02-XX-nombre-corto
git pull
git merge --no-ff develop -m "GC02-XX #comment Integrados los cambios de develop en la rama"
ruff check .
pytest
git push

# 2. Integrar la historia en develop
git checkout develop
git pull
git merge --no-ff feature/GC02-XX-nombre-corto -m "GC02-XX #comment Requisito integrado en develop #done"
git push
```

- Aquí `GC02-XX` es la clave de la **historia**. El `#done` del segundo merge cierra la historia en Jira.
- **Si hay conflictos:** se resuelven en la rama de la historia, en el paso 1, nunca en `develop`.
- **Con ramas protegidas (opcional, +1 punto):** el paso 2 se hace con una *pull request* de la rama a `develop`. La revisa otro miembro y se integra con **«Create a merge commit»**, con el mensaje anterior.

## 7. Cerrar el sprint: `develop` → `main`

Tras la review, con todas las historias del sprint integradas y la integración continua en verde, la SM o DevOps:

```bash
git checkout main
git pull
git merge --no-ff develop -m "Cierre de IT-X: historias GC02-XX y GC02-YY"
git push
```

La integración continua construye `main` y se comprueba el despliegue de demostración (US-001-AC-03).

## 8. Errores frecuentes

| Problema | Solución |
|---|---|
| El commit no aparece en Jira | El correo de `git config user.email` no es el de Jira, o la clave está mal escrita (`GC02-NN`, en mayúsculas). |
| La subtarea no cambia de estado | Falta `#done`, o el estado final del flujo no se llama *Done*. Hay que usar el nombre de la transición. |
| `git push` rechazado | Otra persona subió antes: `git pull`, resolver los conflictos si los hay y repetir `git push`. |
| Me he equivocado en el mensaje y aún no he hecho push | `git commit --amend -m "mensaje correcto"`. Si ya está subido, no se reescribe: se registra el tiempo a mano en Jira. |
| Commit en la rama equivocada sin push | `git reset --soft HEAD~1`, cambiar de rama y repetir el commit. |

Las tareas MGT no tienen código: su tiempo se registra a mano en Jira, en *Registrar trabajo*.
