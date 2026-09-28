# Stage 03: Rehearsal

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_migration_plan.md` | Reviewed migration plan |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Restore and rehearsal checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Prefer a local, isolated, or non-production rehearsal with representative sanitized data.
2. If rehearsal mutates an external/shared target, require explicit approval for the exact operation and target.
3. Record timing, load, integrity, failure behavior, and deviations; do not repair the plan silently.

## Audit

- Rehearsal target and data representativeness are stated.
- Deviations and untested assumptions are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_rehearsal.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop for rehearsal review.
