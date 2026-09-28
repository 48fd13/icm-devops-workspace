# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Migration request, data model, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/development/database-migration-review.md` | Scope procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define datasets, environments, owners, volume, sensitivity, migration type, downtime tolerance, and success criteria.
2. Separate schema, data, application, and infrastructure concerns.

## Audit

- Data and environment boundaries are exact.
- Sensitive data is not copied into the run unnecessarily.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for scope review.
