# Stage 02: Rollout Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_preflight.md` | Reviewed preflight state |
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Approved change packet |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Observation procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define exact commands/actions, target, sequence, checkpoints, abort thresholds, validation, observation, and rollback/fix-forward.
2. Separate read-only prechecks from mutation and identify the approval required for Stage 03.

## Audit

- The execution unit and rollback trigger are exact.
- No command is executed in this stage.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md`.

## Gate

Stop for rollout-plan review.
