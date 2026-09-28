# Stage 02: Implement

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_impact.md` | Reviewed impact |
| Layer 3 reference | `_workspace/workflows/ci-cd/ci-pipeline-create.md` | Pipeline procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Implement the change in `repos/<name>/` as a new version or behind an opt-in.
2. Validate it on a branch or test repository.

## Audit

- Defaults and required checks are unchanged.
- Validation evidence exists.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_implement.md`.

## Gate

Stop for implementation review.
