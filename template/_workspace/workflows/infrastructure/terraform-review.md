# Terraform / OpenTofu Review Workflow

## Required context

- `_workspace/context/reference/iac-principles.md`
- `_workspace/context/reference/tool-notes/terraform-opentofu.md`

## Process

1. Identify backend/state/workspace/environment.
2. Review providers, modules, variables, secrets, outputs, and resource lifecycle.
3. Review plan or diff for create/update/delete/replace and blast radius.
4. Flag apply/destroy/import/state operations as approval-gated.

## Result

Produce a Terraform/OpenTofu review containing findings, blast radius, safety gates, validation gaps, and open questions.
