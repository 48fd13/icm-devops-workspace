# Stage 02: Operations

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_architecture.md` | Reviewed architecture |
| Layer 3 reference | `_workspace/context/reference/observability-principles.md` | Operational signals |
| Layer 3 reference | Applicable files under `_workspace/workflows/` selected below | Operational review procedure and audit criteria |

## Workflow selection

Load only workflows that match the service's operational surface:

| Operational surface | Workflow |
|---|---|
| Logs, metrics, traces, dashboards, or alerts | `_workspace/workflows/operations/observability-review.md` |
| Backups, restore, RPO, or RTO | `_workspace/workflows/operations/backup-restore-review.md` |
| SLOs or error budgets | `_workspace/workflows/operations/slo-error-budget-review.md` |
| Rollback or fix-forward | `_workspace/workflows/operations/rollback-plan-review.md` |
| Release or deployment readiness | `_workspace/workflows/ci-cd/release-readiness-review.md` |

## Do NOT load

- later stage folders
- workflows unrelated to the service's operational surface

## Process

1. Select only applicable workflows from the table above.
2. Apply their procedures and audit criteria without starting another run or using standalone output behavior.
3. Review deploy, rollback/fix-forward, scaling, observability, alerts, runbooks, and on-call paths not already covered.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Operations areas covered | Deploy, rollback, scaling, observability, alerts, runbooks, and on-call are each addressed |
| Procedures scoped | Only workflows matching the actual operational surface were loaded and applied |
| Gaps explicit | Missing operational capabilities are listed as gaps, not omitted |

## Artifacts

Write `02_operations.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for operations review.
