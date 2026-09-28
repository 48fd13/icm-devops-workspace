# Stage 04: Rollout

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_pilot.md` | Pilot results |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Plan waves, communication to consumers, and the rollback path.
2. Request approval for each wave, including changing defaults or required checks, and roll out one wave at a time.

## Audit

- Each wave matches an approval.
- Consumers were told before defaults changed.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_rollout.md`.

## Gate

Stop after rollout for review.
