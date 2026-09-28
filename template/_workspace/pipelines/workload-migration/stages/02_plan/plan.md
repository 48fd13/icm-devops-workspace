# Stage 02: Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_inventory.md` | Reviewed inventory |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback criteria |
| Layer 3 reference | `_workspace/workflows/infrastructure/dns-tls-review.md` | DNS and TLS criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Plan target preparation, the parallel run, the traffic shift method, data synchronization, cutover criteria, and the rollback window.
2. Route primary data movement to `data-migration`.

## Audit

- Every step has a rollback.
- Cutover criteria are measurable.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_plan.md`.

## Gate

Stop for plan review.
