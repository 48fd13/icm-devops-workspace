# Stage 04: Disable

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_decommission_plan.md` | Reviewed disablement plan |
| Layer 3 reference | Applicable infrastructure workflow named by the plan | Disablement checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check exact target, reversible action, expected effect, rollback, observation, and approval basis.
2. If the exact disablement operation and target are not explicitly approved, stop and request approval.
3. Perform only approved reversible disablement; stop on unexpected state.

## Audit

- Approval matches the exact reversible action and target.
- No destructive removal occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_disable.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop after disablement for review.
