# Example: a pipeline that reuses workflows

A trace of a change that needs staged review, through `infrastructure-change`. The review stage applies existing workflows as reference material. Names and details are illustrative.

## Request

> We need to move the orders database to the new private subnet group and tighten its security group. Plan it.

## Routing

The change touches shared infrastructure and should be reviewed before anyone acts on it, so the routing table selects `_workspace/pipelines/infrastructure-change/PIPELINE.md`. The pipeline's route boundary confirms the fit: the result is a reviewed change packet, and the pipeline never applies it.

## Stages

| Stage | Loads (besides the previous handoff) | Writes | Human reviews |
|---|---|---|---|
| 00 Request | `infrastructure-change-principles.md`; environment facts in `context/project/` if present | `stages/00_request.md` | Scope, environments, constraints |
| 01 Discovery | `discovery-checklist.md`, `provider-notes/aws.md` | `stages/01_discovery.md` | Current state, dependencies, unknowns. The audit confirms no mutations. |
| 02 Plan | `infrastructure-change-principles.md`, `iac-principles.md`, `tool-notes/terraform-opentofu.md` | `stages/02_plan.md` | Steps, blast radius, approvals, rollback |
| 03 Review | `security-and-secrets-rules.md` plus the workflows selected below | `stages/03_review.md` | Risks and missing evidence |
| 04 Validation | `validation-evidence.md` | `stages/04_validation.md` | Checks, expected results, evidence |
| 05 Finalize | `map/naming-conventions.md` | `stages/05_finalize.md` | The change packet |

After each stage the agent stops. You might edit `02_plan.md` to add a maintenance window before continuing. Stage 03 reads your edited version.

## Workflow reuse in stage 03

`stages/03_review/review.md` has a workflow selection table. This change touches Terraform, access rules, and a database cutover, so the agent loads only:

- `_workspace/workflows/infrastructure/terraform-review.md`
- `_workspace/workflows/infrastructure/access-change-review.md`
- `_workspace/workflows/operations/rollback-plan-review.md`

It applies their procedures and audit criteria inside stage 03. It does not start a separate run, and it writes to `stages/03_review.md`, not to wherever a standalone workflow would save its result. It does not load the DNS/TLS, Kubernetes, or cost workflows, because the change does not touch them.

## Finish

The final packet is ready for the team's change process. On "finish the run" it is promoted to `_workspace/artifacts/change-packets/2026-10-02-orders-db-subnet-change-packet-v01.md`. The unknown replication lag found in discovery becomes a backlog item. The confirmed subnet layout goes to `context/project/` with a `Last verified` date.

Applying the change is a separate piece of work, and every Terraform apply in it stops at the safety gate.
