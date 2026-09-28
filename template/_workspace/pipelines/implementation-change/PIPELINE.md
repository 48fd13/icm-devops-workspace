# Pipeline: Implementation Change

Use for staged repo, automation, configuration, CI/CD, documentation, or non-mutating infrastructure-file changes that need human checkpoints.

## Routing

| Task | Go to |
|---|---|
| Clarify request and constraints | `stages/00_intake/intake.md` |
| Understand current behavior | `stages/01_understand/understand.md` |
| Plan implementation | `stages/02_plan/plan.md` |
| Implement scoped change | `stages/03_implement/implement.md` |
| Validate result | `stages/04_validate/validate.md` |
| Finalize handoff | `stages/05_handoff/handoff.md` |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Identity and safety rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Reference material | `_workspace/context/` and `_workspace/workflows/` files named by each stage |
| Layer 4 | Working artifacts | active run `input/`, `_workspace/runs/active/<run-slug>/stages/`, and `artifacts/` |
| Run archive | Explicitly archived finished runs | `_workspace/runs/archive/` |


## Route boundary

Use for staged changes to repository files: code, automation, configuration, CI/CD, documentation, or infrastructure code that is not applied. Use `infrastructure-change` to plan a change to live infrastructure, and `release-rollout` to deploy the result.

## Operating rules

- Execute exactly one stage, write the stage handoff artifact, and write any supporting artifacts under the active run's `artifacts/` directory; then stop for review.
- Prefer read-only discovery before editing.
- Keep scope tight; do not expand a small change into a redesign without approval.
- Do not install dependencies, push, publish, deploy, mutate infrastructure, or change secrets/auth/billing without explicit approval.
- Treat Terraform/OpenTofu apply/import/state changes, Kubernetes/Helm mutations, cloud mutations, and production/shared environment changes as out of scope unless the user explicitly approves a separate gated operation.
- Follow `AGENTS.md` for finish and archive; the finalize stage declares what is promoted.
