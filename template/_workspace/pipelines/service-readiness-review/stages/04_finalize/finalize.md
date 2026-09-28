# Stage 04: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_operations.md` | Operations review |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_risk.md` | Risk review |
| Layer 3 reference | `_workspace/map/naming-conventions.md` | Report naming |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Produce readiness report, prioritized gaps, and recommended next actions.
2. Keep the run active and present the readiness report for review.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Gaps prioritized | Readiness gaps are prioritized with recommended next actions |
| Report standalone | The report is usable without reading prior stage files or chat |

## Artifacts

Write `04_finalize.md` to `_workspace/runs/active/<run-slug>/stages/`.


## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the approved readiness report -> `_workspace/artifacts/reviews/`
- prioritized gaps -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Review gate

Stop for final review.
