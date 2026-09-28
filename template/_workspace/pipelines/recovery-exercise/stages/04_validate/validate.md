# Stage 04: Validate

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_execute.md` | Recovery execution evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_objectives.md` | RPO/RTO and success criteria |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Service and signal checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Validate integrity, accessibility, dependencies, service behavior, security, timing, RPO/RTO, and cleanup readiness.
2. Record failed, unavailable, or partial checks without mutation.

## Audit

- Validation maps directly to success criteria.
- Actual RPO/RTO and uncertainty are stated.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_validate.md`; store detailed evidence under run `artifacts/`.

## Gate

Stop for recovery validation review.
