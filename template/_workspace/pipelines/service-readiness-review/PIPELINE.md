# Pipeline: Service Readiness Review

Use to assess operational readiness of a service, platform component, or environment.

## Routing

| Task | Go to |
|---|---|
| Scope review | `stages/00_scope/scope.md` |
| Map architecture | `stages/01_architecture/architecture.md` |
| Review operations | `stages/02_operations/operations.md` |
| Review risk | `stages/03_risk/risk.md` |
| Finalize readiness | `stages/04_finalize/finalize.md` |

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

Use to assess whether a service, platform component, or environment is ready to operate. The result is a readiness report with prioritized gaps. Use `security-assessment` for dedicated security evidence and findings.

## Operating rules

- Assess readiness; do not mutate systems.
- Execute one stage at a time and stop for review.
