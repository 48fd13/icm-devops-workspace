# Stage 02: Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_discovery.md` | Reviewed current state |
| Layer 3 reference | `_workspace/context/reference/infrastructure-change-principles.md` | Planning rules |
| Layer 3 reference | `_workspace/context/reference/iac-principles.md` | IaC rules, when the change is code-managed |
| Layer 3 reference | `_workspace/context/reference/tool-notes/<tool>.md` for the tools involved only | Tool-specific planning checks |

## Do NOT load

- later stage folders

## Process

1. Produce implementation plan, blast radius, dependencies, approvals, and rollback/fix-forward path.
2. Do not execute changes.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Blast radius stated | The plan includes blast radius, dependencies, and rollback/fix-forward path |
| No execution | No changes were applied during planning |
| Approvals flagged | Required approvals are called out explicitly |

## Artifacts

Write `02_plan.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for plan review.
