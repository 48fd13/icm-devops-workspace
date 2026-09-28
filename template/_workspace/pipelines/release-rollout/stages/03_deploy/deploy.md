# Stage 03: Deploy

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_rollout_plan.md` | Reviewed deployment plan |
| Layer 3 reference | `_workspace/workflows/ci-cd/ci-cd-review.md` | Deployment gate checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check candidate, environment, operation, current state, expected effect, rollback, and approval basis.
2. If the exact deployment is not explicitly approved in the current instruction, stop and request approval.
3. Perform only the approved deployment; stop on unexpected state and capture sanitized evidence.

## Audit

- Approval matches candidate, environment, and operation.
- No unapproved promotion or follow-up mutation occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_deploy.md`; store deployment evidence under run `artifacts/`.

## Gate

Stop after deployment for review.
