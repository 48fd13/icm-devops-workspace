# Stage 06: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_retest.md` | Reviewed retest status |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier assessment handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce scope, threat surface, findings, remediation status, retest evidence, residual risk, and follow-ups.
2. Keep sensitive details minimized and the run active for review.

## Audit

- Findings and status are evidence-backed and scoped.
- Sensitive data and secrets are excluded.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_finalize.md`. On explicit finish, write approved sanitized content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- remediation items and residual risks, without exploit or sensitive detail -> `_workspace/backlog/items/`

Findings and evidence stay in the run. Do not copy them to `_workspace/artifacts/`. Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
