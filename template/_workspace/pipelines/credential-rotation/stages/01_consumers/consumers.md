# Stage 01: Consumers

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed rotation scope |
| Layer 3 reference | `_workspace/workflows/infrastructure/secrets-rotation-review.md` | Consumer discovery procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Access and audit checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Inventory producers, consumers, stores, injection paths, caches, reload behavior, environments, ownership, and audit trails.
2. Separate verified consumers from assumptions and unknowns.

## Audit

- Consumer coverage and ownership gaps are explicit.
- No credential value was inspected or recorded unnecessarily.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_consumers.md`.

## Gate

Stop for consumer-map review.
