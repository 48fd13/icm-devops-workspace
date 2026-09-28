# Stage 03: Decommission Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_retention.md` | Approved retention disposition |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_dependencies.md` | Reviewed dependency map |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Reversal procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Observation procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define communications, traffic drain, reversible disablement, observation window, rollback, destructive removal, verification, and residual cleanup.
2. Define separate exact approvals for disablement and removal.

## Audit

- Disable-observe-remove boundaries are explicit.
- Rollback and unexpected-consumer handling are actionable.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_decommission_plan.md`.

## Gate

Stop for decommission-plan review.
