# Stage 06: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_measure.md` | Reviewed measured outcome |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier optimization handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce objective, baseline, selected option, changes, measured outcome, confidence, service tradeoffs, residual risks, and follow-ups.
2. Keep the run active for review.

## Audit

- Estimated and realized savings are distinct.
- The record does not hide service degradation or uncertainty.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the selected option and its accepted service tradeoffs -> `_workspace/artifacts/decisions/`
- follow-ups -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
