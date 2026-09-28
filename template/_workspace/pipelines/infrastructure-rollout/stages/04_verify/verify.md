# Stage 04: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_execute.md` | Execution evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md` | Expected post-change state |
| Layer 3 reference | Applicable infrastructure workflow named in the plan | Verification criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Run approved post-change health, state, drift, connectivity, policy, and dependency checks.
2. Compare actual state with expected state and flag rollback thresholds without triggering mutation silently.

## Audit

- Exact checks and results are recorded.
- Failed or unavailable checks remain explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_verify.md`; store detailed results under run `artifacts/`.

## Gate

Stop for verification review.
