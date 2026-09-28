# Stage 05: Findings

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_validate.md` | Reviewed validation results |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_tabletop.md` | Tabletop assumptions and blockers |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/runbook-draft.md` | Runbook improvement procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Identify recovery gaps, runbook changes, access/dependency issues, remediation priorities, and owners/dates only when known.
2. Separate observed failures from hypotheses and future experiments.

## Audit

- Every finding ties to tabletop or execution evidence.
- No owner or deadline is invented.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_findings.md`.

## Gate

Stop for findings review.
