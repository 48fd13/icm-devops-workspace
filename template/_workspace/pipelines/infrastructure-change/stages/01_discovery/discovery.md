# Stage 01: Discovery

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_request.md` | Reviewed request |
| Layer 3 reference | `_workspace/context/reference/discovery-checklist.md` | Read-only discovery and inventory checklist |
| Layer 3 reference | `_workspace/context/reference/provider-notes/<provider>.md` for the providers involved only | Provider-specific checks |

## Do NOT load

- later stage folders

## Process

1. Identify current state, dependencies, ownership, provider/tool context, and unknowns.
2. Use read-only discovery only.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Read-only discovery | No mutations were performed during this stage |
| Current state covered | Current state, dependencies, ownership, and unknowns are listed |

## Artifacts

Write `01_discovery.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for discovery review.
