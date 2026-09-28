# Stage 05: Retest

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_remediation_plan.md` | Reviewed remediation and retest plan |
| Layer 4 working | approved fix evidence supplied under `_workspace/runs/active/<run-slug>/input/` | Changed state to assess |
| Layer 3 reference | Workflow procedures originally used for affected controls | Retest criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-evaluate only approved fixes/evidence using read-only or explicitly authorized checks.
2. Classify each finding as resolved, partially resolved, unresolved, not retested, or superseded; do not implement changes.

## Audit

- Retest evidence is comparable to the original finding.
- Intrusive or mutating checks were not run without exact approval.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_retest.md`.

## Gate

Stop for retest review.
