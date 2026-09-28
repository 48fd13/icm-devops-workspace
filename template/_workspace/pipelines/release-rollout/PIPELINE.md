# Pipeline: Release Rollout

Deploy an approved release candidate through readiness, gated rollout, verification, and observation.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Release scope | `stages/00_release_scope/release_scope.md` | Fixed candidate and target scope |
| 01 Readiness | `stages/01_readiness/readiness.md` | Readiness decision |
| 02 Rollout plan | `stages/02_rollout_plan/rollout_plan.md` | Deployment and rollback plan |
| 03 Deploy | `stages/03_deploy/deploy.md` | Approved deployment evidence |
| 04 Verify | `stages/04_verify/verify.md` | Post-deploy verification |
| 05 Observe | `stages/05_observe/observe.md` | Continue or rollback recommendation |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed release record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Applicable workflow procedures | `_workspace/workflows/` paths named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use for deploying an approved application or service candidate. Use `implementation-change` to build/fix it; use the release-readiness workflow for a one-pass readiness check with no rollout.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Referenced workflows supply procedure and audit criteria only.
- Entry into Stage 03 does not authorize deployment. Require approval for the exact candidate, environment, and operation.
- Keep supporting evidence under run `artifacts/`; use `final/` only on explicit finish.
