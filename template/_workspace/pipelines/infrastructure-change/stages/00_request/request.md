# Stage 00: Request

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Change request/source material |
| Layer 3 reference | `_workspace/context/reference/infrastructure-change-principles.md` | Change principles |
| Layer 3 reference | `_workspace/context/project/` files for the affected environment, if present | Reviewed environment facts and approval rules |

## Do NOT load

- later stage folders

## Process

1. Clarify requested change, scope, non-goals, environments, and approval needs.
2. Identify missing information.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Scope captured | Change, non-goals, environments, and approval needs are stated |
| Missing info explicit | Unknowns are listed as questions, not guessed |

## Artifacts

Write `00_request.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for request review.
