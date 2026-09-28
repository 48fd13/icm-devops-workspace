# Stage 04: Delivery pipeline

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_config_secrets.md` | Reviewed configuration |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Service profile |
| Layer 3 reference | `_workspace/workflows/ci-cd/ci-pipeline-create.md` | CI procedure and audit criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Create the build, test, scan, and publish pipeline with immutable image tags.
2. Connect it to deployment the way the platform does, usually by proposing image updates to the GitOps repository through a pull request.

## Audit

- Actions and images are pinned; permissions are minimal.
- The pipeline cannot deploy to production by itself.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_delivery.md`.

## Gate

Stop for delivery review.
