# Pipeline: Cost Optimization

Manage measured cost reduction from verified baseline through option selection, controlled implementation, and outcome measurement.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Objective | `stages/00_objective/objective.md` | Scope, constraints, and target |
| 01 Baseline | `stages/01_baseline/baseline.md` | Verified cost and service baseline |
| 02 Options | `stages/02_options/options.md` | Compared optimization options |
| 03 Plan | `stages/03_plan/plan.md` | Implementation and measurement plan |
| 04 Implement | `stages/04_implement/implement.md` | Approved optimization evidence |
| 05 Measure | `stages/05_measure/measure.md` | Measured cost/service outcome |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed optimization record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace and billing policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Cost, observability, SLO, rollback, and technology procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Run inputs, handoffs, and measured evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when optimization requires baseline, change, observation, and measured outcome. Use cost-review for a one-pass assessment; use infrastructure-change when cost is only one risk dimension.

## Operating rules

- Billing-impacting or external/shared changes require exact approval.
- Do not claim savings without a comparable observation window and stated uncertainty.
- Preserve service objectives and rollback thresholds.
- Keep evidence under run `artifacts/`; use `final/` only on explicit finish.
