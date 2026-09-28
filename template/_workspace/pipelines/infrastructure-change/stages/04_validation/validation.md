# Stage 04: Validation

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_review.md` | Reviewed risks |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_plan.md` | Plan to validate |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Validation evidence rules |

## Do NOT load

- later stage folders

## Process

1. Define pre-change, change-time, and post-change validation evidence.
2. Mark mutation-gated checks clearly.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Evidence phases defined | Pre-change, change-time, and post-change validation evidence is defined |
| Mutation gates marked | Checks that require mutations are clearly marked as gated |

## Artifacts

Write `04_validation.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for validation review.
