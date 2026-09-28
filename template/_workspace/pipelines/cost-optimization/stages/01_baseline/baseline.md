# Stage 01: Baseline

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_objective.md` | Reviewed objective and window |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Cost-driver procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Usage/service evidence |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Verify cost drivers, allocation, usage, sizing, retention, transfer, performance, reliability, seasonality, and data quality.
2. State normalization, missing data, and confidence limits.

## Audit

- Baseline period and comparison method are reproducible.
- Cost and service signals are both represented.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_baseline.md`; keep detailed calculations under run `artifacts/`.

## Gate

Stop for baseline review.
