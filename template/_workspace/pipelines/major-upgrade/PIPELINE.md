# Pipeline: Major Upgrade

Coordinate a substantial dependency, platform, runtime, or service-version upgrade through compatibility analysis, rehearsal, implementation, validation, and rollout handoff.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Upgrade boundary and versions |
| 01 Compatibility | `stages/01_compatibility/compatibility.md` | Compatibility assessment |
| 02 Upgrade plan | `stages/02_upgrade_plan/upgrade_plan.md` | Sequenced upgrade and rollback plan |
| 03 Rehearsal | `stages/03_rehearsal/rehearsal.md` | Rehearsal evidence and deviations |
| 04 Implement | `stages/04_implement/implement.md` | Approved local changes |
| 05 Validate | `stages/05_validate/validate.md` | Upgrade validation |
| 06 Rollout packet | `stages/06_rollout_packet/rollout_packet.md` | Approved rollout input |
| 07 Finalize | `stages/07_finalize/finalize.md` | Reviewed upgrade record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Dependency, migration, rollback, release, and technology procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use for coordinated upgrades with breaking-change, compatibility, or rehearsal work. Use a dependency workflow or implementation-change for small updates. Deployment belongs to release-rollout or infrastructure-rollout.

## Operating rules

- Local implementation is allowed only within approved scope; external rehearsal requires exact approval.
- Do not deploy from this pipeline.
- Keep compatibility evidence and supporting work under run `artifacts/`.
- Use `final/` only on explicit finish.
