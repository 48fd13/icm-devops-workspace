# Stage 05: Measure

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_implement.md` | Implementation evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_baseline.md` | Comparison baseline |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Outcome measurement |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Service outcome checks |
| Layer 3 reference | `_workspace/workflows/operations/slo-error-budget-review.md` | Reliability guardrails when available |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Compare cost, usage, performance, reliability, and user/service impact over the agreed window.
2. State realized/estimated savings, confidence, confounders, and recommend keep, extend, adjust, or rollback without mutation.

## Audit

- Savings and service outcomes use comparable evidence.
- Uncertainty and delayed billing data are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_measure.md`; keep calculations under run `artifacts/`.

## Gate

Stop for outcome review.
