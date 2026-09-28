# Stage 05: Observe

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_verify.md` | Reviewed verification |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Signal review procedure |
| Layer 3 reference | `_workspace/workflows/operations/slo-error-budget-review.md` | Load when SLO/error-budget evidence exists |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback threshold procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Evaluate agreed signals and user impact over the observation window.
2. Recommend continue, extend, rollback, or fix-forward without executing mutation.

## Audit

- Observation window, signals, and uncertainty are stated.
- Recommendation follows thresholds or explains deviation.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_observe.md`.

## Gate

Stop for continue/rollback decision.
