# Stage 04: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_deploy.md` | Deployment evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md` | Expected state and checks |
| Layer 3 reference | `_workspace/workflows/ci-cd/release-readiness-review.md` | Post-deploy criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Run approved smoke, health, compatibility, migration, dependency, and user-impact checks.
2. Compare results with expected state and rollback thresholds; do not mutate silently.

## Audit

- Exact checks and pass/fail/not-run status are recorded.
- User impact and migration compatibility are addressed when applicable.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_verify.md`; store detailed results under run `artifacts/`.

## Gate

Stop for verification review.
