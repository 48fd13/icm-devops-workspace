# Stage 01: Recovery Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_objectives.md` | Reviewed objectives |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Recovery procedure |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/runbook-draft.md` | Runbook structure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define recovery sources, target, access, dependencies, sequence, timing, validation, rollback, cleanup, and communications.
2. Mark every mutation and the exact approval it requires.

## Audit

- Restore source and target are unambiguous.
- Cleanup and live-system isolation are addressed.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_recovery_plan.md`.

## Gate

Stop for recovery-plan review.
