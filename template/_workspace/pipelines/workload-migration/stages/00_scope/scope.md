# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Migration request |
| Layer 3 reference | `_workspace/context/reference/devops-principles.md` | Platform principles |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Record the workloads, source and target, reason, deadline, downtime tolerance, and data involved.

## Audit

- Source, target, and constraints are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for scope review.
