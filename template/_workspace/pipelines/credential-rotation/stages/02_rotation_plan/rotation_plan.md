# Stage 02: Rotation Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_consumers.md` | Reviewed consumer map |
| Layer 3 reference | `_workspace/workflows/infrastructure/secrets-rotation-review.md` | Rotation procedure |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Recovery procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define overlap/dual-secret strategy, creation, consumer waves, validation, monitoring, rollback, revocation criteria, and cleanup.
2. Define separate approvals for introduction, cutover, and revocation.

## Audit

- Lockout, reload, cache, and partial-cutover risks are addressed.
- Revocation depends on explicit passing evidence.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_rotation_plan.md`.

## Gate

Stop for rotation-plan review.
