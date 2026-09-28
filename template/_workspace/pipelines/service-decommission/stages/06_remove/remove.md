# Stage 06: Remove

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_observe.md` | Passing observation decision |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_retention.md` | Approved data disposition |
| Layer 3 reference | Applicable infrastructure workflow named by the plan | Removal checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check target, passing observation, retention evidence, destructive operation, residual effects, and approval basis.
2. If the exact removal/deletion operation is not separately and explicitly approved, stop and request approval.
3. Remove only approved resources; stop on unexpected state and capture sanitized evidence.

## Audit

- Removal has independent exact approval.
- Data and dependency obligations passed before deletion.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_remove.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop after removal for review.
