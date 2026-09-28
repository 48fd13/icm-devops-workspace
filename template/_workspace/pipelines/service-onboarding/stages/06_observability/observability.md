# Stage 06: Observability

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Service profile and reliability expectations |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_gitops.md` | Deployment layout |
| Layer 3 reference | `_workspace/workflows/operations/alert-rule-create.md` | Alert and dashboard procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define SLIs, alert rules with owners, and a dashboard for the service.
2. Confirm logs and metrics reach the platform's observability stack.

## Audit

- Every alert has an owner and an expected response.
- No paging routes were changed.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_observability.md`.

## Gate

Stop for observability review.
