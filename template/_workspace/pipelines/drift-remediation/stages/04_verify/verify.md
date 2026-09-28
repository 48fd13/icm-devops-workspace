# Stage 04: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_reconcile.md` | Reconciliation outcome |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-run drift detection for the scope.
2. Confirm reconciled items are clean and list anything that remains.

## Audit

- Remaining drift is explained.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_verify.md`.

## Gate

Stop for verification review.
