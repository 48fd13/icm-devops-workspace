# Stage 04: Validate

## Goal

Review the implementation, run approved local validation checks, and record results clearly.

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_implement.md` | Previous-stage implementation handoff |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Approved scope and validation plan |
| Layer 4 working | changed files and available test/build/lint/check commands | Implementation and executable validation surface |
| Layer 3 reference | Applicable files under `_workspace/workflows/` selected below | Review procedure and audit criteria |

## Workflow selection

Load only workflows that match the implementation:

| Change surface | Workflow |
|---|---|
| Any code/config/documentation diff | `_workspace/workflows/development/pr-review.md` |
| Dependency files | `_workspace/workflows/development/dependency-update-review.md` |
| Database migration | `_workspace/workflows/development/database-migration-review.md` |
| Terraform/OpenTofu | `_workspace/workflows/infrastructure/terraform-review.md` |
| Kubernetes/Helm/Kustomize | `_workspace/workflows/infrastructure/kubernetes-review.md` |
| Container image | `_workspace/workflows/infrastructure/container-image-review.md` |
| CI/CD | `_workspace/workflows/ci-cd/ci-cd-review.md` |
| Environment configuration | `_workspace/workflows/infrastructure/environment-config-review.md` |
| Deployment or rollback risk | `_workspace/workflows/operations/rollback-plan-review.md` |

## Do NOT load

- workflows unrelated to the actual implementation
- later stage folders

## Process

1. Select only the applicable workflows from the table above.
2. Apply their procedures and audit criteria without starting another run or using standalone output behavior.
3. Run only approved/local validation commands.
4. Record review findings plus exact commands and results.
5. If validation fails, summarize failure and likely next step; do not expand scope silently.
6. If validation cannot run, explain why and list manual checks.
7. Do not deploy, publish, push, or mutate external systems.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Commands recorded | Exact commands and pass/fail/not-run status are recorded |
| Procedures scoped | Only workflows matching the actual implementation were loaded and applied |
| No silent scope growth | Failures are summarized with next steps, not fixed outside the approved plan |
| Local only | No deploy, publish, push, or external mutation was performed |

## Artifacts

Write `04_validate.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- validation commands run
- pass/fail/not-run status
- applicable workflow review findings
- key command artifact or error summary
- remaining risk
- recommended next action

## Review gate

Stop after writing the active run stage file. Ask before fixing failed validation if the fix is outside the approved plan.
