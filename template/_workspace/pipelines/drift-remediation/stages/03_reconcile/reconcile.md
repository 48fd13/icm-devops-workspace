# Stage 03: Reconcile

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Reviewed plan |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Evidence rules |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-run the plan and confirm it matches the reviewed one.
2. If the exact apply or sync is not approved in the current instruction, stop and request approval.
3. Apply only the approved items and record evidence.

## Audit

- Every change matches an approval.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_reconcile.md`.

## Gate

Stop after reconciliation for review.
