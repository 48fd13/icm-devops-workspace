# Stage 03: Risk

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_operations.md` | Reviewed operations |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_architecture.md` | Architecture context |
| Layer 3 reference | `_workspace/context/reference/security-and-secrets-rules.md` | Security risk rules |
| Layer 3 reference | Applicable files under `_workspace/workflows/` selected below | Domain-specific risk procedure and audit criteria |

## Workflow selection

Load only workflows that match the service's risk surface:

| Risk surface | Workflow |
|---|---|
| IAM or access | `_workspace/workflows/infrastructure/access-change-review.md` |
| Secrets or rotation | `_workspace/workflows/infrastructure/secrets-rotation-review.md` |
| Environment configuration | `_workspace/workflows/infrastructure/environment-config-review.md` |
| Material cost exposure | `_workspace/workflows/infrastructure/cost-review.md` |
| DNS or TLS | `_workspace/workflows/infrastructure/dns-tls-review.md` |

## Do NOT load

- later stage folders
- workflows unrelated to the service's risk surface

## Process

1. Select only applicable workflows from the table above.
2. Apply their procedures and audit criteria without starting another run or using standalone output behavior.
3. Review security, secrets, reliability, cost, data, dependency, ownership, and failure-mode risks not already covered.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Risk categories covered | Security, secrets, reliability, cost, data, dependency, ownership, and failure modes are each addressed |
| Procedures scoped | Only workflows matching the actual risk surface were loaded and applied |
| Evidence-based | Each risk ties to evidence from prior stages, without overclaiming |

## Artifacts

Write `03_risk.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for risk review.
