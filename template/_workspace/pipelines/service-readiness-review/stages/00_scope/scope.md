# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Service/readiness source material |
| Layer 3 reference | `_workspace/context/reference/devops-principles.md` | Readiness principles |

## Do NOT load

- later stage folders

## Process

1. Identify service/component, environment, criticality, owner, scope, and non-goals.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Scope complete | Service, environment, criticality, owner, scope, and non-goals are stated |
| Unknowns explicit | Missing scope information is listed as questions |

## Artifacts

Write `00_scope.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for scope review.
