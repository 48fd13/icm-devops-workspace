# Stage 02: Kubernetes packaging

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_container.md` | Reviewed container |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Service profile |
| Layer 3 reference | `_workspace/workflows/infrastructure/helm-chart-create.md` | Helm procedure, when the platform uses Helm |
| Layer 3 reference | `_workspace/workflows/infrastructure/kustomize-overlay-create.md` | Kustomize procedure, when the platform uses Kustomize |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Package the service the way the platform already does (Helm chart or Kustomize base and overlays); do not introduce a second convention.
2. Include probes, resources, security context, disruption budget, and autoscaling where the profile calls for it.
3. Lint and render every environment.

## Audit

- Only the procedure matching the platform convention was used.
- Rendered manifests exist for every target environment.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_packaging.md`; store rendered manifests under run `artifacts/`.

## Gate

Stop for packaging review.
