# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Requested change |
| Layer 3 reference | `_workspace/context/reference/ci-cd-principles.md` | CI/CD principles |
| Layer 3 reference | `_workspace/context/reference/tool-notes/ci-platforms.md` | CI platform conventions |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Describe the current behavior, the desired behavior, and why.
2. Identify the shared components involved: templates, runners, required checks, registries, promotion flow.

## Audit

- Scope and non-goals are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for scope review.
