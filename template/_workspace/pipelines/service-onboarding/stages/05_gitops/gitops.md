# Stage 05: GitOps application

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_delivery.md` | Reviewed delivery pipeline |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_packaging.md` | Packaging and environments |
| Layer 3 reference | `_workspace/workflows/ci-cd/argocd-application-create.md` | GitOps application procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Write the application definition for each environment and register it with the root application or generator.
2. Set the sync policy per environment and declare ordering for dependencies.

## Audit

- Nothing was merged to a tracked branch or synced.
- Production sync policy is not fully automated unless the platform explicitly allows it.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_gitops.md`.

## Gate

Stop for GitOps review.
