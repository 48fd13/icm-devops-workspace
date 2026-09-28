# Stage 03: Introduce

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rotation_plan.md` | Reviewed introduction plan |
| Layer 3 reference | `_workspace/workflows/infrastructure/secrets-rotation-review.md` | Introduction checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check credential metadata, target, operation, overlap, rollback, and approval without reading or recording the value.
2. If the exact create/introduction operation and target are not explicitly approved, stop and request approval.
3. Perform only the approved introduction and capture sanitized identifiers/evidence.

## Audit

- Approval matches exact credential type, target, and operation.
- No secret material appears in artifacts or chat.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_introduce.md` with sanitized evidence.

## Gate

Stop after introduction for review.
