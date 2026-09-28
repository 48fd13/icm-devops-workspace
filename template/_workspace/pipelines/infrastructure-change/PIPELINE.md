# Pipeline: Infrastructure Change

Use to plan, review, and validate shared cloud, platform, or infrastructure-as-code changes. This pipeline does not execute mutations.

## Routing

| Task | Go to |
|---|---|
| Clarify request | `stages/00_request/request.md` |
| Discover current state | `stages/01_discovery/discovery.md` |
| Plan change | `stages/02_plan/plan.md` |
| Review risk | `stages/03_review/review.md` |
| Define validation | `stages/04_validation/validation.md` |
| Finalize packet | `stages/05_finalize/finalize.md` |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Reference material | `_workspace/context/` and `_workspace/workflows/` files named by each stage |
| Layer 4 | Working artifacts | active run `input/`, `_workspace/runs/active/<run-slug>/stages/`, and `artifacts/` |
| Run archive | Explicitly archived finished runs | `_workspace/runs/archive/` |


## Route boundary

Use for planning, reviewing, and validating a cloud, infrastructure, platform, or shared-environment change. The result is a reviewed change packet; this pipeline never applies it. Use `infrastructure-rollout` to execute an approved packet, and a one-pass workflow such as the cloud change plan or Terraform review when the change is small, local, and reversible.

## Operating rules

- No applies, deploys, cluster mutations, cloud mutations, or secret/auth changes.
- Execute one stage at a time and stop for review.
- Follow `AGENTS.md` for finish and archive; the finalize stage declares what is promoted.
