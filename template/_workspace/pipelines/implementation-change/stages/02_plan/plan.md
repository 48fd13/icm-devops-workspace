# Stage 02: Plan

## Goal

Create a small, reviewable implementation plan with validation and rollback expectations.

## Inputs

- `_workspace/runs/active/<run-slug>/stages/00_intake.md`
- `_workspace/runs/active/<run-slug>/stages/01_understand.md`
- Relevant runbooks, tests, and tool notes

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define the smallest useful change.
2. List files expected to change.
3. Define validation commands/checks and expected outcomes.
4. Identify rollback/revert approach.
5. Call out approvals required before implementation or validation.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Smallest useful change | The plan lists only the files needed for the approved scope |
| Validation defined | Each planned change has a validation command/check with expected outcome |
| Rollback and approvals | A revert approach is stated and required approvals are flagged |

## Artifacts

Write `02_plan.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- scope
- non-goals
- planned file changes
- implementation steps
- validation plan
- rollback/revert notes
- approval questions

## Review gate

Stop after writing the active run stage file. Wait for approval before implementation.
