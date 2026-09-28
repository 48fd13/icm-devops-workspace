# Stage 01: Container

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Reviewed service profile |
| Layer 3 reference | `_workspace/workflows/development/dockerfile-create.md` | Container procedure and audit criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Apply the Dockerfile procedure in the service repository.
2. Build and run locally where possible and check the health endpoint.

## Audit

- Base images pinned, non-root user, no secrets in the image.
- Nothing was pushed to a registry.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_container.md`; record build evidence under run `artifacts/`.

## Gate

Stop for container review.
