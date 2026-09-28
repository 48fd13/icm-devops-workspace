# Stage 07: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/06_verify.md` | Reviewed rotation outcome |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier sanitized handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce a sanitized record of scope, consumer changes, revocation, verification, residual risks, and follow-ups.
2. Keep the run active for review.

## Audit

- No secret values or private material are present.
- Introduced, cut over, revoked, verified, and unresolved states are distinct.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/07_finalize.md`. On explicit finish, write approved sanitized content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- residual risks and follow-ups, without secret values -> `_workspace/backlog/items/`

The rotation record stays in the run. Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
