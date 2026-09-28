# Stage 01: Readiness

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_release_scope.md` | Reviewed release scope |
| Layer 3 reference | `_workspace/workflows/ci-cd/release-readiness-review.md` | Readiness procedure |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Load only when data migration is involved |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Check validation, provenance, approvals, configuration, dependencies, migrations, observability, and rollback readiness.
2. Return ready, ready-with-risks, blocked, or not-ready without deploying.

## Audit

- Skipped evidence and blocking issues are explicit.
- Applicable migration risk is addressed.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_readiness.md`.

## Gate

Stop for readiness review.
