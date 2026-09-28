# Pipeline: Workload Migration

Move a running service between clusters, regions, accounts, or providers through inventory, target preparation, a parallel run, gated cutover, and source cleanup.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Migration scope |
| 01 Inventory | `stages/01_inventory/inventory.md` | Dependency inventory |
| 02 Plan | `stages/02_plan/plan.md` | Migration plan |
| 03 Prepare target | `stages/03_prepare_target/prepare_target.md` | Prepared target |
| 04 Parallel run | `stages/04_parallel_run/parallel_run.md` | Parallel-run evidence |
| 05 Cutover | `stages/05_cutover/cutover.md` | Completed cutover |
| 06 Source cleanup | `stages/06_source_cleanup/source_cleanup.md` | Source removed or handed off |
| 07 Finalize | `stages/07_finalize/finalize.md` | Migration record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Workflow procedures and reference context | `_workspace/workflows/` and `_workspace/context/` files named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use to move a running workload to a new location. Use `data-migration` when moving primary data is the main operation, and `service-decommission` to retire a service without a replacement.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Referenced workflows supply procedure and audit criteria only.
- Deploying to the target, shifting traffic, and removing the source each require approval for the exact operation.
