# Stage 03: Review

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Reviewed plan |
| Layer 3 reference | Applicable files under `_workspace/workflows/` selected below | Domain-specific review procedure and audit criteria |
| Layer 3 reference | `_workspace/context/reference/security-and-secrets-rules.md` | Security and secrets risk rules |

## Workflow selection

Load only workflows that match the planned change:

| Change surface | Workflow |
|---|---|
| Terraform/OpenTofu | `_workspace/workflows/infrastructure/terraform-review.md` |
| Kubernetes/Helm/Kustomize | `_workspace/workflows/infrastructure/kubernetes-review.md` |
| Container image | `_workspace/workflows/infrastructure/container-image-review.md` |
| CI/CD | `_workspace/workflows/ci-cd/ci-cd-review.md` |
| IAM or access | `_workspace/workflows/infrastructure/access-change-review.md` |
| DNS or TLS | `_workspace/workflows/infrastructure/dns-tls-review.md` |
| Environment configuration | `_workspace/workflows/infrastructure/environment-config-review.md` |
| Secrets or rotation | `_workspace/workflows/infrastructure/secrets-rotation-review.md` |
| Material cost impact | `_workspace/workflows/infrastructure/cost-review.md` |
| Deployment or rollback risk | `_workspace/workflows/operations/rollback-plan-review.md` |

## Do NOT load

- later stage folders
- workflows unrelated to the planned change

## Process

1. Select only the applicable workflows from the table above.
2. Apply their procedures and audit criteria without starting another run or using standalone output behavior.
3. Review security, reliability, cost, operational, dependency, and rollback risks not already covered.
4. Flag unresolved approvals or missing evidence.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Risk categories covered | Security, reliability, cost, operational, dependency, and rollback risks are each addressed |
| Procedures scoped | Only workflows matching the actual change surface were loaded and applied |
| Gaps flagged | Unresolved approvals or missing evidence are flagged, not skipped |

## Artifacts

Write `03_review.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for risk review.
