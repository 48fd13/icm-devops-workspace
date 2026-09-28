# Stage 05: Handoff

## Goal

Produce the final implementation handoff for human review, follow-up, or PR preparation.

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_validate.md` | Approved validation results from the previous stage |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier handoffs needed to summarize the change, risks, or decisions |
| Layer 4 working | `_workspace/runs/active/<run-slug>/artifacts/` | Supporting changed-file details and validation material |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Summarize what changed and why.
2. List validation status and any skipped checks.
3. Capture risks, follow-ups, and rollback notes.
4. Recommend next human action: review, commit, PR, rerun validation, or revise plan.
5. Keep the run active and present the handoff for review.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Standalone summary | The handoff explains what changed and why without needing chat context |
| Risks and follow-ups | Known risks, skipped checks, and follow-ups are captured |
| Next action clear | A concrete recommended next human action is stated |

## Artifacts

Write `05_handoff.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- change summary
- files changed
- validation summary
- known risks/follow-ups
- rollback/revert notes
- next action


## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- follow-ups and skipped validation -> `_workspace/backlog/items/`

The change itself lives in the repository and its review. Nothing else leaves the run; archiving keeps the whole run.

## Review gate

Stop after writing the active run stage file. Do not commit, push, deploy, archive, or clear active artifacts without explicit approval.
