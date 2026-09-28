# Stage 01: Inventory

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed scope |
| Layer 3 reference | `_workspace/context/reference/discovery-checklist.md` | Read-only discovery |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Inventory dependencies, configuration, secrets, data stores, DNS, certificates, identities, network paths, and observability for each workload.

## Audit

- The inventory is read-only and evidence-based.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_inventory.md`.

## Gate

Stop for inventory review.
