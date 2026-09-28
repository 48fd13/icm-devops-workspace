# Stage 02: Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_classify.md` | Classified drift |
| Layer 3 reference | `_workspace/workflows/infrastructure/terraform-review.md` | IaC review, when Terraform is involved |
| Layer 3 reference | `_workspace/workflows/infrastructure/kubernetes-review.md` | Kubernetes review, when manifests are involved |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. For items to codify, change the IaC or manifests in `repos/<name>/` to match live state.
2. For items to revert, confirm the declared state is correct and plan the reconciliation.
3. Re-run the plan or diff and state the blast radius and rollback for each item.

## Audit

- The resulting plan changes only the classified items.
- Nothing was applied.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_plan.md`.

## Gate

Stop for plan review.
