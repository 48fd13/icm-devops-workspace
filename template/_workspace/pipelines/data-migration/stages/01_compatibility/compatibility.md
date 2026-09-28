# Stage 01: Compatibility

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed migration scope |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Compatibility procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Assess application/version compatibility, ordering, locks, load, replication, downtime, dual-read/write, and irreversible transitions.
2. Identify required intermediate states and unsupported assumptions.

## Audit

- Forward and backward compatibility are addressed.
- Irreversible or unknown transitions are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_compatibility.md`.

## Gate

Stop for compatibility review.
