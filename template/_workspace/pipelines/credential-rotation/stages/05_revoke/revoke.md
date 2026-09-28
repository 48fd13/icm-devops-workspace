# Stage 05: Revoke

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_cutover.md` | Passing cutover evidence |
| Layer 3 reference | `_workspace/workflows/infrastructure/secrets-rotation-review.md` | Revocation checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Confirm all required consumers pass, rollback criteria are clear, and revocation target is the old credential.
2. If the exact revocation operation is not separately and explicitly approved, stop and request approval.
3. Revoke only the approved old credential and capture sanitized evidence.

## Audit

- Passing cutover evidence precedes revocation.
- Approval identifies the exact old credential without exposing it.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_revoke.md`.

## Gate

Stop after revocation for review.
