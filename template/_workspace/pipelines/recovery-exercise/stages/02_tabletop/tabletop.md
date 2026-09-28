# Stage 02: Tabletop

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_recovery_plan.md` | Reviewed recovery plan |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Failure-mode checklist |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Walk through prerequisites, decisions, failure modes, access, dependencies, communications, abort conditions, and cleanup.
2. Record assumptions, blockers, and plan corrections without executing recovery.

## Audit

- Critical decision points and owners when known are clear.
- Untested assumptions and blockers are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_tabletop.md`.

## Gate

Stop for tabletop review.
