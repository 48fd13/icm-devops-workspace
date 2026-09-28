# Terraform Module Create Workflow

## Required context

- `_workspace/context/reference/iac-principles.md`
- `_workspace/context/reference/tool-notes/terraform-opentofu.md`

## Process

1. Define the module's purpose, the resources it manages, and what the caller controls.
2. Write `main.tf`, `variables.tf` with types, descriptions, and validation, `outputs.tf`, and `versions.tf` with provider and Terraform or OpenTofu constraints.
3. Keep secure defaults: encryption, private access, least-privilege IAM, and tags. Do not hardcode account IDs, regions, or secrets.
4. Add an example caller and a README with inputs and outputs.
5. Validate with `fmt`, `validate`, and a plan against a non-shared environment if one is available. Do not apply, import, or change state.

## Result

Produce the module, an example, validation and plan evidence, and open questions.
