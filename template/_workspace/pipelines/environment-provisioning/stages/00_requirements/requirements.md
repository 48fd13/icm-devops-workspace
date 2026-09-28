# Stage 00: Requirements

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Request and constraints |
| Layer 3 reference | `_workspace/context/reference/infrastructure-change-principles.md` | Change principles |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Record purpose, environment name, provider and account or project, regions, network ranges, compute platform, shared services (DNS, registry, secrets, observability, GitOps), access model, budget, owners, and deadline.
2. List unknowns and dependencies on other teams.

## Audit

- Isolation from existing environments is stated.
- Owners and budget are named or flagged.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_requirements.md`.

## Gate

Stop for requirements review.
