# Stage 02: Relationships

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_inventory.md` | Reviewed inventory |
| Layer 3 reference | `_workspace/context/reference/onboarding-principles.md` | Relationships to map |

## Do NOT load

- later stage folders

## Process

1. Map service, environment, ownership, dependency, deploy, network, and observability relationships.
2. Flag unclear or risky relationships.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Traceable to inventory | Every relationship references items from the reviewed inventory |
| Risky links flagged | Unclear or risky relationships are flagged explicitly |

## Artifacts

Write `02_relationships.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for review before question generation.
