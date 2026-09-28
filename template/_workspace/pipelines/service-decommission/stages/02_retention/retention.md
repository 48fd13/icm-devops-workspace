# Stage 02: Retention

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_dependencies.md` | Reviewed dependency/data inventory |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Retention/recovery procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Custody and access checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Resolve data retention/export, backup, compliance, legal/audit, ownership, access, and recovery obligations.
2. Define evidence required before disablement and removal.

## Audit

- Every data class has a disposition or explicit blocker.
- Destruction is not proposed without authority and retention evidence.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_retention.md`.

## Gate

Stop for retention and disposition approval.
