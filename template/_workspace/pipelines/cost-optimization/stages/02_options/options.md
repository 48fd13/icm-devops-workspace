# Stage 02: Options

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_baseline.md` | Reviewed cost/service baseline |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Option analysis procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Compare options by estimated savings, assumptions, implementation effort, reliability/performance impact, reversibility, lock-in, and evidence quality.
2. Recommend one bounded option or no change.

## Audit

- Savings are estimates with assumptions, not guarantees.
- Tradeoffs and rejected options are visible.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_options.md`.

## Gate

Stop for option selection.
