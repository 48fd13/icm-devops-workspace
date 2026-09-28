# Stage 05: Cutover

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_parallel_run.md` | Parallel-run evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Cutover criteria and rollback |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. If the exact traffic shift is not approved in the current instruction, stop and request approval.
2. Shift traffic in the approved steps, watch the cutover criteria, and roll back if they fail.

## Audit

- Every shift matches an approval.
- Rollback triggers were watched.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_cutover.md`.

## Gate

Stop after cutover for review.
