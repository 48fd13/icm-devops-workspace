# Pipeline: Environment Provisioning

Create a new environment, cluster, or cloud account from requirements through IaC, approved provisioning, platform bootstrap, and validated handover.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Requirements | `stages/00_requirements/requirements.md` | Reviewed requirements |
| 01 Design | `stages/01_design/design.md` | Architecture and IaC design |
| 02 Infrastructure code | `stages/02_iac/iac.md` | IaC and plan |
| 03 Review | `stages/03_review/review.md` | Risk review and approvals needed |
| 04 Provision | `stages/04_provision/provision.md` | Provisioned resources and evidence |
| 05 Platform bootstrap | `stages/05_bootstrap/bootstrap.md` | Bootstrapped platform components |
| 06 Validate and hand over | `stages/06_handover/handover.md` | Validated environment and handover |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Workflow procedures and reference context | `_workspace/workflows/` and `_workspace/context/` files named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use to create an environment, cluster, or account that does not exist yet. Use `infrastructure-change` and `infrastructure-rollout` to change an existing one.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Referenced workflows supply procedure and audit criteria only.
- Stages 00 to 03 do not create or modify cloud resources.
- Stages 04 and 05 require approval for each exact apply or bootstrap step; entering the stage is not approval.
