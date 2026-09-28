# Stage 03: Prepare target

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Reviewed plan |
| Layer 3 reference | `_workspace/workflows/ci-cd/argocd-application-create.md` | GitOps application procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/secret-wiring.md` | Secret wiring procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Prepare manifests, applications, configuration, and secret references for the target in `repos/<name>/`.
2. Request approval for any target resource that must be created, and create only what is approved.

## Audit

- Only approved target resources were created.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_prepare_target.md`.

## Gate

Stop for target review.
