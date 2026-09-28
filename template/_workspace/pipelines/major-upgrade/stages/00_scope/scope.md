# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Upgrade request, current versions, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/development/dependency-update-review.md` | Upgrade scope procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define components, source/target versions, environments, drivers, support windows, exclusions, and success criteria.
2. Distinguish local upgrade work from later external rollout.

## Audit

- Version and component boundaries are exact.
- Small routine updates are redirected to a workflow or implementation-change.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for upgrade-scope review.
