# Stage 05: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_execute.md` | Migration evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_migration_plan.md` | Success and abort criteria |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Service-impact checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Verify integrity, counts, constraints, application compatibility, performance, lag, errors, dependencies, and service health.
2. Recommend accept, observe, rollback, or fix-forward; any mutation requires separate approval.

## Audit

- Data and application checks are evidence-backed.
- Residual inconsistency and unavailable checks are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_verify.md`; store detailed checks under run `artifacts/`.

## Gate

Stop for migration outcome decision.
