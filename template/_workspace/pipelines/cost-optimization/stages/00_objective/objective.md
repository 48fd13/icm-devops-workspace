# Stage 00: Objective

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Optimization request, billing data, and supplied constraints |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Cost scope procedure |
| Layer 3 reference | `_workspace/workflows/operations/slo-error-budget-review.md` | Service-objective constraints when available |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define resources/services, environments, baseline period, target, owners, reliability/performance constraints, exclusions, and measurement horizon.
2. Separate cost reduction from capacity or reliability degradation.

## Audit

- Scope and target are measurable.
- Billing data sensitivity and uncertainty are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_objective.md`.

## Gate

Stop for objective review.
