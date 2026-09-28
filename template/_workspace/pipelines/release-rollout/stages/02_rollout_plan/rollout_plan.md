# Stage 02: Rollout Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_readiness.md` | Reviewed readiness decision |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Observation procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define exact deployment operation, target, strategy/waves, checkpoints, communications, abort thresholds, verification, observation, and rollback.
2. State the exact approval required for Stage 03.

## Audit

- Candidate, target, deployment unit, and rollback trigger are exact.
- No deployment occurs in this stage.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md`.

## Gate

Stop for rollout-plan review.
