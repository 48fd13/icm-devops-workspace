# Stage 07: Deploy to non-production

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_gitops.md` | Application definitions |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/06_observability.md` | Signals to verify |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Validation evidence rules |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Confirm the target is a non-production environment. If it is not, stop and route to `release-rollout`.
2. If the exact merge, sync, or deployment is not approved in the current instruction, stop and request approval.
3. Perform only the approved operation, then verify rollout status, probes, logs, metrics, and that alerts stay quiet.

## Audit

- Approval matches the environment and operation.
- Verification evidence is recorded, including anything that failed.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/07_deploy_dev.md`; store verification evidence under run `artifacts/`.

## Gate

Stop after deployment for review.
