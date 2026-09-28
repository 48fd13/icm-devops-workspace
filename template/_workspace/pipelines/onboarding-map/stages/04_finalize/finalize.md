# Stage 04: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_relationships.md` | Reviewed relationship map |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_questions.md` | Reviewed questions |
| Layer 3 reference | `_workspace/map/naming-conventions.md` | Map naming |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Create final onboarding map, open questions, risks, and next actions.
2. Identify deferred follow-ups, unresolved questions, risks, and next actions that should become backlog items on finish.
3. Identify durable facts/maps that may enter `_workspace/context/project/` after review.
4. Keep the run active and present the final map for review.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Consistent with map | The final map matches the reviewed relationships and questions, or deviations are flagged |
| Backlog candidates linked | Each proposed backlog item links back to its pipeline/stage source |
| Clean project context | No unresolved questions, risks, or TODOs are written to `_workspace/context/project/` |

## Artifacts

Write `04_finalize.md` to `_workspace/runs/active/<run-slug>/stages/` containing the final onboarding map, open questions, risks, and next actions.

Include proposed backlog items and their source links in the stage handoff for promotion on finish.


## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the reviewed map and confirmed facts (services, environments, ownership, dependencies) -> `_workspace/context/project/`
- open questions, risks, and next actions -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Review gate

Stop for final review.
