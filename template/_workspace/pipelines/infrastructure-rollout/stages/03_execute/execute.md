# Stage 03: Execute

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md` | Reviewed exact rollout plan |
| Layer 3 reference | Applicable infrastructure workflow named in the plan | Execution checks only |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check target, current state, operation, expected effect, rollback path, and approval basis.
2. If the exact operation and target are not explicitly approved in the current instruction, stop and request approval.
3. Execute only the approved infrastructure mutation; stop on unexpected state and capture sanitized evidence.

## Audit

- Approval matches the exact operation and target.
- No unapproved follow-up mutation occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_execute.md`; store sanitized command/action evidence under run `artifacts/`.

## Gate

Stop after execution for human review.
