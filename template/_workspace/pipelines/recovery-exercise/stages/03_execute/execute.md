# Stage 03: Execute

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_tabletop.md` | Reviewed tabletop and plan corrections |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_recovery_plan.md` | Exact recovery operation |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Execution checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check source, target, isolation, operation, expected effect, rollback/cleanup, and approval basis.
2. If the exact restore/recovery operation and target are not explicitly approved, stop and request approval.
3. Execute only the approved operation; stop on unexpected state and capture sanitized timing/evidence.

## Audit

- Approval matches exact source, target, and operation.
- No live overwrite or cleanup mutation occurred without separate approval.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_execute.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop after exercise execution for review.
