# Stage 06: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_verify.md` | Reviewed migration outcome |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier migration handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce migration scope, execution outcome, integrity evidence, deviations, residual risks, and follow-ups.
2. Keep the run active for review.

## Audit

- The record distinguishes migrated, verified, deferred, and unresolved work.
- Sensitive data is excluded.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- residual risks and follow-ups -> `_workspace/backlog/items/`

Integrity evidence stays in the run. Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
