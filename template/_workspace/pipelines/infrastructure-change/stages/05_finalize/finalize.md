# Stage 05: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Approved plan |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_review.md` | Risk review |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_validation.md` | Validation plan |
| Layer 3 reference | `_workspace/map/naming-conventions.md` | Change packet naming |

## Do NOT load

- unrelated raw input unless needed for unresolved gaps

## Process

1. Produce final change packet for human/team approval.
2. Keep the run active and present the final packet for review.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Packet standalone | The change packet is reviewable without reading chat history |
| Consistent with prior stages | The packet matches the approved plan, risk review, and validation plan, or deviations are flagged |

## Artifacts

Write `05_finalize.md` to `_workspace/runs/active/<run-slug>/stages/`.


## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the approved change packet -> `_workspace/artifacts/change-packets/`
- reviewed facts about the affected environment confirmed during discovery -> `_workspace/context/project/`
- deferred actions and unresolved risks -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Review gate

Stop for final approval.
