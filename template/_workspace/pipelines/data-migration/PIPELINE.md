# Pipeline: Data Migration

Plan, rehearse, execute, and verify a schema change, backfill, transformation, or datastore movement where data mutation is primary.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Migration boundary and success criteria |
| 01 Compatibility | `stages/01_compatibility/compatibility.md` | Compatibility assessment |
| 02 Migration plan | `stages/02_migration_plan/migration_plan.md` | Executable migration and recovery plan |
| 03 Rehearsal | `stages/03_rehearsal/rehearsal.md` | Rehearsal evidence and deviations |
| 04 Execute | `stages/04_execute/execute.md` | Approved migration evidence |
| 05 Verify | `stages/05_verify/verify.md` | Integrity and service verification |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed migration record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Migration, recovery, rollback, and observability procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when data mutation is the primary lifecycle. Use the database-migration workflow for a one-pass review; use release rollout only when migration is incidental to a broader release.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Rehearsal and execution mutations require exact target-and-operation approval.
- Production/shared data execution is never implied by plan approval.
- Keep supporting evidence under run `artifacts/`; use `final/` only on explicit finish.
