# Stage 06: Rollout Packet

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_validate.md` | Reviewed upgrade validation |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_upgrade_plan.md` | Rollout and rollback design |
| Layer 3 reference | `_workspace/workflows/ci-cd/release-readiness-review.md` | Release readiness procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Observation criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce exact candidate/version, target, prerequisites, sequencing, verification, observation, abort, and rollback criteria.
2. Select release-rollout or infrastructure-rollout as the downstream execution process; do not deploy here.

## Audit

- Packet is executable without hidden chat context.
- Downstream rollout type and unresolved risks are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_rollout_packet.md`; put detailed packet under run `artifacts/`.

## Gate

Stop for rollout-packet review.
