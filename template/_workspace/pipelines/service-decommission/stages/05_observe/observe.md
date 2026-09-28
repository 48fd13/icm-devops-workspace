# Stage 05: Observe

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_disable.md` | Disablement evidence |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Unexpected-use checks |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback threshold procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Observe traffic, errors, jobs, consumers, alerts, support signals, and owner feedback over the agreed window.
2. Recommend rollback, extend, or proceed to removal without mutating.

## Audit

- Window and evidence are stated.
- Unexpected use or uncertainty blocks removal unless explicitly resolved.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_observe.md`.

## Gate

Stop for proceed/rollback decision.
