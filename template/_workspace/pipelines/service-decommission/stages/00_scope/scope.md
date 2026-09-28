# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Decommission request and supplied evidence |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/repo-service-review.md` | Service scope procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define service/resources, environments, owner, reason, requested end state, exclusions, and timeline constraints.
2. Distinguish reversible disablement from destructive removal.

## Audit

- Scope identifies exact resources and environments.
- Ownership and unknowns are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for decommission-scope review.
