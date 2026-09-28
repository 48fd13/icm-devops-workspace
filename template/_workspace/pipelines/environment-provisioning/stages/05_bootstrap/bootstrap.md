# Stage 05: Platform bootstrap

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_provision.md` | Provisioned environment |
| Layer 3 reference | `_workspace/workflows/ci-cd/argocd-application-create.md` | GitOps registration procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/secret-wiring.md` | Secret wiring procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Install or register the platform components the design names (GitOps controller or registration, ingress, certificate management, secrets operator, observability agents).
2. Request approval for each mutating step, apply it, and verify it before the next.

## Audit

- Each component is verified before the next is added.
- No secret values were written.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_bootstrap.md`.

## Gate

Stop after bootstrap for review.
