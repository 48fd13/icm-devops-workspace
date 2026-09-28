# Stage 07: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/06_rollout_packet.md` | Reviewed rollout packet |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier upgrade handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce upgrade scope, compatibility, implementation, validation, rollout packet, residual risks, and follow-ups.
2. Keep the run active and do not represent the upgrade as deployed.

## Audit

- Local completion and downstream deployment status are distinct.
- The record is usable without chat context.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/07_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- updated version and platform facts, once deployed -> `_workspace/context/project/`
- residual risks and follow-ups -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
