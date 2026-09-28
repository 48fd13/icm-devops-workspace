# Stage 01: Impact analysis

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed scope |
| Layer 3 reference | `_workspace/workflows/ci-cd/ci-cd-review.md` | Delivery review criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. List consuming repositories and teams, using read-only searches.
2. Assess compatibility, permission and secret changes, failure modes, and the cost of rolling back.

## Audit

- Consumers are listed with evidence.
- Breaking changes are called out.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_impact.md`.

## Gate

Stop for impact review.
