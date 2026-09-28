# Stage 03: Questions

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_relationships.md` | Reviewed relationships |
| Layer 3 reference | `_workspace/context/reference/onboarding-principles.md` | Unknowns to turn into questions |

## Do NOT load

- later stage folders

## Process

1. Produce targeted questions grouped by owner/team/system/environment/risk.
2. Prioritize questions that unblock safe operations.
3. Mark which questions are backlog candidates if they remain unresolved after finalization.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Questions grouped | Questions are grouped by owner/team/system/environment/risk |
| Prioritized | Questions that unblock safe operations come first |
| Backlog candidates marked | Questions that should survive the pipeline are marked for Stage 04 promotion |

## Artifacts

Write `03_questions.md` to `_workspace/runs/active/<run-slug>/stages/`.

Do not write questions to `_workspace/context/project/`. Final-stage unresolved questions or deferred follow-ups must be promoted to `_workspace/backlog/items/` by Stage 04.

## Review gate

Stop for review before final map.
