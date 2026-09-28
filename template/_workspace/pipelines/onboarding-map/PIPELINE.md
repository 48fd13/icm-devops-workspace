# Pipeline: Onboarding Map

Use to map a new team, service, platform area, or project scope without making changes.

## Routing

| Task | Go to |
|---|---|
| Clarify scope | `stages/00_intake/intake.md` |
| Inventory facts | `stages/01_inventory/inventory.md` |
| Map relationships | `stages/02_relationships/relationships.md` |
| Prepare questions | `stages/03_questions/questions.md` |
| Finalize map | `stages/04_finalize/finalize.md` |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Reference material | `_workspace/context/` and `_workspace/workflows/` files named by each stage |
| Layer 4 | Working artifacts | active run `input/`, `_workspace/runs/active/<run-slug>/stages/`, and `artifacts/` |
| Run archive | Explicitly archived finished runs | `_workspace/runs/archive/` |


## Route boundary

Use when the scope is new or has changed: a team, service, platform area, environment, or project. The result is a reviewed map and a list of targeted questions. Use the repo/service review workflow for a quick first look at a single repository.

## Operating rules

- Read-only discovery only.
- Execute one stage at a time and stop for review.
- Keep stage-local working files in `_workspace/runs/active/<run-slug>/stages/`; keep other run artifacts in `_workspace/runs/active/<run-slug>/artifacts/`.
- Promote deferred follow-ups, unresolved questions, risks, and next actions that should survive the pipeline into `_workspace/backlog/items/` during the final stage.
- Do not store unresolved risks/questions/TODOs in `_workspace/context/project/`; use project context only for durable facts and reviewed project-specific reference.
- Follow `AGENTS.md` for finish and archive; the finalize stage declares what is promoted.
