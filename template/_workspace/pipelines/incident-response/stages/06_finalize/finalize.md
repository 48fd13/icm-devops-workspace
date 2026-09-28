# Stage 06: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_communicate.md` | Reviewed response status |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier response handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Handoff procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce response outcome, sanitized timeline link, actions, residual impact, risks, next ownership, and explicit input for a follow-up incident review.
2. Keep cause hypotheses separate and the run active for review.

## Audit

- Response and post-incident learning boundaries are clear.
- Sensitive data and unsupported cause claims are excluded.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the sanitized response record -> `_workspace/artifacts/incident-notes/`
- open actions, residual risks, and the follow-up incident review -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final response review; finish and archive remain separate.
