# Stage 04: Execute

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_rehearsal.md` | Reviewed rehearsal evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_migration_plan.md` | Approved exact migration plan |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Execution checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check dataset, environment, operation, backup/recovery, abort threshold, current state, and approval basis.
2. If the exact data mutation and target are not explicitly approved in the current instruction, stop and request approval.
3. Execute only the approved migration; stop on unexpected state and capture sanitized progress/evidence.

## Audit

- Approval matches the exact operation, data scope, and environment.
- Partial completion and errors are recorded without concealment.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_execute.md`; store sanitized execution evidence under run `artifacts/`.

## Gate

Stop after execution for review.
