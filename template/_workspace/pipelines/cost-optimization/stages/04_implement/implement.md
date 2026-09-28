# Stage 04: Implement

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_plan.md` | Reviewed exact optimization plan |
| Layer 3 reference | Applicable development or infrastructure workflow named by the plan | Implementation checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check exact changes, target, expected cost/service effect, rollback, and approval basis.
2. Make approved local changes directly; if any action mutates billing, infrastructure, or an external/shared target, require explicit approval for that exact operation and target.
3. Execute only approved work and stop on unexpected state.

## Audit

- Every change maps to the selected option and approval.
- No unapproved billing or external mutation occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_implement.md`; store changed-file or sanitized action evidence under run `artifacts/`.

## Gate

Stop after implementation for review.
