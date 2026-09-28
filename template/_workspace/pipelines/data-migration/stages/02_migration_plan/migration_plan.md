# Stage 02: Migration Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_compatibility.md` | Reviewed compatibility assessment |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Migration procedure |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Recovery readiness |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback/fix-forward procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define exact sequence, batching, backups, access, monitoring, validation, abort thresholds, rollback/fix-forward, and cleanup.
2. Identify exact approval separately for rehearsal and production/shared execution.

## Audit

- Backup/restore evidence and data-integrity checks are named.
- The plan addresses partial completion and restart safety.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_migration_plan.md`.

## Gate

Stop for migration-plan review.
