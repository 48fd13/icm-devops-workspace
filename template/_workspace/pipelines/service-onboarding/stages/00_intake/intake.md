# Stage 00: Intake

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Service description, repository, and requirements |
| Layer 3 reference | `_workspace/context/reference/devops-principles.md` | Platform principles |
| Layer 3 reference | `_workspace/context/project/` files for the target platform, if present | Existing conventions (chart style, GitOps layout, CI platform) |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Build the service profile: purpose, owner, runtime and build tool, ports, health endpoints, dependencies, data stores, configuration, required secrets by name, exposure, environments, and reliability expectations.
2. Record the repository under `repos/<name>/` and the platform conventions to follow.
3. List unknowns as questions instead of assuming.

## Audit

- Every later stage has the inputs it needs, or a named open question.
- Facts and assumptions are separate.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_intake.md`.

## Gate

Stop for service profile review.
