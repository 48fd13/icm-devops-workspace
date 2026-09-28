# Stage 04: Cutover

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_introduce.md` | Reviewed introduction evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rotation_plan.md` | Approved cutover waves |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Authentication monitoring checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check consumer wave, target, reload behavior, validation, rollback, and exact approval.
2. If the exact consumer mutation is not explicitly approved, stop and request approval.
3. Cut over only approved consumers; validate each wave and stop on unexpected authentication failure.

## Audit

- Each changed consumer and result is recorded without secrets.
- Unchanged, failed, or unknown consumers remain explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_cutover.md`; store sanitized wave evidence under run `artifacts/`.

## Gate

Stop for cutover review.
