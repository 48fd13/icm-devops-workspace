# Example: a one-pass workflow

A trace of a small request through the Terraform/OpenTofu review workflow. Names, paths, and findings are illustrative.

## Request

> Review the Terraform change in `repos/network-infra/` before I open the PR.

## Routing

1. The agent reads `AGENTS.md`, then `_workspace/map/routing-table.md`.
2. One pass is enough and no staged review is needed, so it picks a workflow. The table sends Terraform work to `_workspace/map/routes/infrastructure.md`.
3. That route file points to `_workspace/workflows/infrastructure/terraform-review.md`.

It loaded no pipeline, no Kubernetes notes, and no provider notes except the one the diff touches.

## Run

```text
_workspace/runs/active/2026-10-02-network-tf-review/
├── RUN.md
├── input/
│   └── plan-output.txt          the `terraform plan` output you pasted
└── artifacts/
    └── terraform-review.md      the review
```

`RUN.md` is written first:

```markdown
## Run metadata

- Process: workflow
- Started: 2026-10-02
- Finished:
- Route: routing-table → routes/infrastructure.md → workflows/infrastructure/terraform-review.md

## Request

Review Terraform change in repos/network-infra/ before PR.

## Plan

1. Identify backend, state, and environment.
2. Review providers, modules, variables, and resource lifecycle.
3. Review the plan for create/update/delete/replace and blast radius.
4. Flag gated operations.
```

## Context loaded

- `_workspace/context/reference/iac-principles.md`
- `_workspace/context/reference/tool-notes/terraform-opentofu.md`
- `_workspace/context/reference/provider-notes/aws.md`, because the diff uses the AWS provider

## Result

`artifacts/terraform-review.md` lists the findings, for example:

- `aws_route_table.private` will be **replaced**, not updated. Private subnets lose their default route between destroy and create. Suggest `create_before_destroy`.
- The NAT gateway EIP is not tagged with the cost-center tag required by the module's variables.
- Validation gap: no `terraform plan` output for the `prod` workspace was supplied.
- Safety gate: applying this change is a Terraform apply on shared networking and needs explicit approval.

The agent does not run `terraform apply`, and it does not open the PR.

## Finish

You fix the route table, re-run the review, and say "finish the run". The approved review goes to the run's `final/`, which is its record. A standalone workflow declares no promotion, so the agent asks whether anything should be kept outside the run. You choose to put the missing prod plan in the backlog, and nothing else leaves the run.
