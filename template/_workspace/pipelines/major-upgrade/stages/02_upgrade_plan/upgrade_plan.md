# Stage 02: Upgrade Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_compatibility.md` | Reviewed compatibility assessment |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Rollback/fix-forward procedure |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Load when data changes are involved |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define sequencing, intermediate versions, code/config/data changes, rehearsal, validation, rollback, and rollout handoff.
2. Separate local changes from external/shared mutations and their approvals.

## Audit

- Plan covers partial completion and compatibility windows.
- Rollback or explicit fix-forward rationale is actionable.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_upgrade_plan.md`.

## Gate

Stop for upgrade-plan review.
