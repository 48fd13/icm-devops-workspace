# Stage 01: Design

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_requirements.md` | Reviewed requirements |
| Layer 3 reference | `_workspace/context/reference/iac-principles.md` | IaC principles |
| Layer 3 reference | `_workspace/context/reference/provider-notes/<provider>.md` | Provider checks, for the chosen provider only |
| Layer 3 reference | `_workspace/context/reference/tool-notes/terraform-opentofu.md` | Terraform/OpenTofu conventions |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Design the architecture, network layout, IAM model, naming and tagging, and bootstrap order.
2. Design the IaC layout: modules, state backend and isolation, and pipeline for plan and apply.
3. Estimate cost.

## Audit

- State and blast radius are isolated from other environments.
- Every shared dependency has an owner.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_design.md`.

## Gate

Stop for design review.
