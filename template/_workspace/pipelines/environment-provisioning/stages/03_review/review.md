# Stage 03: Review

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_iac.md` | IaC and plan |
| Layer 3 reference | `_workspace/context/reference/security-and-secrets-rules.md` | Security rules |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | IAM review |
| Layer 3 reference | `_workspace/workflows/infrastructure/dns-tls-review.md` | DNS and TLS review, when the plan touches them |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Cost review |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Review the plan for IAM, network exposure, encryption, secrets, DNS and TLS, and cost.
2. List the approvals each provisioning step needs.

## Audit

- Each risk has a decision or an open question.
- Required approvals are named.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_review.md`.

## Gate

Stop for risk review.
