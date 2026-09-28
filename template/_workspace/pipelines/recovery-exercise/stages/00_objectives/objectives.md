# Stage 00: Objectives

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Exercise request, recovery policy, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/operations/backup-restore-review.md` | Objective procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define scenario, protected resources, isolation, participants, RPO/RTO, success criteria, exclusions, and allowed exercise type.
2. Clarify tabletop, isolated restore, failover, or live recovery boundaries.

## Audit

- Scenario and target isolation are explicit.
- Live-data risk is not hidden.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_objectives.md`.

## Gate

Stop for objective review.
