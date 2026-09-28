# Pipeline: Infrastructure Rollout

Execute an approved infrastructure change packet through gated preflight, rollout, verification, and observation.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Intake | `stages/00_intake/intake.md` | Accepted change packet and target |
| 01 Preflight | `stages/01_preflight/preflight.md` | Current-state and readiness evidence |
| 02 Rollout plan | `stages/02_rollout_plan/rollout_plan.md` | Exact execution and rollback plan |
| 03 Execute | `stages/03_execute/execute.md` | Approved mutation evidence |
| 04 Verify | `stages/04_verify/verify.md` | Post-change verification |
| 05 Observe | `stages/05_observe/observe.md` | Continue or rollback recommendation |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed rollout record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Applicable workflow procedures | `_workspace/workflows/` paths named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use only when an infrastructure change packet is already reviewed. Use `infrastructure-change` for discovery and planning; use a specific one-pass workflow when execution is not requested.

## Operating rules

- Execute one stage at a time and write its handoff under the active run's `stages/`.
- Load only applicable workflow procedures named by the current stage; never create a nested run.
- Entry into Stage 03 does not authorize infrastructure mutation. Require approval for the exact operation and target.
- Keep supporting evidence under run `artifacts/`; use `final/` only on explicit finish.
