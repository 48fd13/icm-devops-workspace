# Stage 01: Threat Surface

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Approved assessment boundary |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/repo-service-review.md` | System discovery procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/environment-config-review.md` | Configuration boundary checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Map identities, trust boundaries, entry points, data classes, dependencies, deployment paths, external exposure, and plausible attacker paths.
2. Separate verified evidence, assumptions, and inaccessible areas.

## Audit

- Threat surface stays inside approved scope.
- Sensitive details are minimized and sanitized.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_threat_surface.md`; put detailed sanitized maps under run `artifacts/`.

## Gate

Stop for threat-surface review.
