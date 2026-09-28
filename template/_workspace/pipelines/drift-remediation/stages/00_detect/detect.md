# Stage 00: Detect

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Scope and any drift reports |
| Layer 3 reference | `_workspace/context/reference/iac-principles.md` | IaC principles |
| Layer 3 reference | `_workspace/context/reference/tool-notes/terraform-opentofu.md` | Terraform/OpenTofu drift checks, when involved |
| Layer 3 reference | `_workspace/context/reference/tool-notes/gitops.md` | GitOps drift checks, when involved |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Run read-only comparisons for the scope: `plan` with refresh, GitOps diff, or `kubectl diff`.
2. List each difference with resource, attribute, declared value, and live value.

## Audit

- Only read-only commands were run.
- Every difference is listed with evidence.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_detect.md`; store raw diff output under run `artifacts/`.

## Gate

Stop for drift review.
