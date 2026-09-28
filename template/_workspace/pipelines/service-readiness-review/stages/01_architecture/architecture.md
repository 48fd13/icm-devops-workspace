# Stage 01: Architecture

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed scope |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/repo-service-review.md` | Service architecture review procedure and audit criteria |

## Do NOT load

- later stage folders

## Process

1. Apply the repo/service review procedure without starting another run or using standalone output behavior.
2. Map runtime, dependencies, data flow, deployment path, environments, ownership, configuration, CI/CD, IaC, observability, and runbooks.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Map complete | Runtime, dependencies, data flow, deployment path, and ownership are mapped |
| Unknowns flagged | Unclear areas are marked as unknown, not assumed |

## Artifacts

Write `01_architecture.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for architecture review.
