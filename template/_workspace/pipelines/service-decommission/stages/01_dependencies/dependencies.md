# Stage 01: Dependencies

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed decommission scope |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/repo-service-review.md` | Dependency discovery |
| Layer 3 reference | `_workspace/workflows/infrastructure/dns-tls-review.md` | DNS/edge dependencies |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Identity/access dependencies |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Resource/cost inventory |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Inventory consumers, traffic, data, integrations, jobs, DNS, access, automation, monitoring, owners, resources, and cost.
2. Separate verified dependencies from assumptions and unknowns.

## Audit

- Hidden-consumer discovery paths are documented.
- Unknown ownership or dependency blocks are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_dependencies.md`; put detailed inventory under run `artifacts/`.

## Gate

Stop for dependency review.
