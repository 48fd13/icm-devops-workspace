# Stage 04: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_recover.md` | Recovery action evidence |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Service-health checks |
| Layer 3 reference | `_workspace/workflows/operations/slo-error-budget-review.md` | Reliability-impact checks when available |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Verify user impact, service health, dependencies, data integrity, alerts, and recurrence indicators over an appropriate window.
2. Recommend recovered, partially recovered, unstable, or further approved action.

## Audit

- Recovery status is evidence-backed and time-bounded.
- Residual impact and uncertainty are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_verify.md`; update timeline/evidence under run `artifacts/`.

## Gate

Stop for recovery verification.
