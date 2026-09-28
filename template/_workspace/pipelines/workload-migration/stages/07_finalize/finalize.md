# Stage 07: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/06_source_cleanup.md` | Cleanup outcome |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Handoff procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Summarize the new location, what changed for consumers, deviations, and follow-ups.
2. Keep the run active for review.

## Audit

- Old and new locations are unambiguous.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/07_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- updated location facts (cluster, region, account, endpoints, DNS) -> `_workspace/context/project/`
- follow-ups -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
