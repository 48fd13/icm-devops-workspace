# Stage 03: Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_options.md` | Selected optimization option |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Reversal procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Measurement procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define exact changes, target, sequence, validation, observation window, service guardrails, rollback, and measurement method.
2. Separate local changes from billing-impacting/external mutations and define exact approvals.

## Audit

- Measurement compares like-for-like windows or explains limitations.
- Rollback and service guardrails are actionable.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_plan.md`.

## Gate

Stop for optimization-plan review.
