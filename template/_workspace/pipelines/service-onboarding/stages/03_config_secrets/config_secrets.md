# Stage 03: Configuration and secrets

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_packaging.md` | Reviewed packaging |
| Layer 3 reference | `_workspace/workflows/infrastructure/secret-wiring.md` | Secret wiring procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/environment-config-review.md` | Environment configuration checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Write per-environment configuration values.
2. Wire secrets by reference and list each required secret with its owner.
3. Check environment differences are intentional.

## Audit

- No secret values appear anywhere in the repository or the run.
- Every secret reference has an owner.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_config_secrets.md`.

## Gate

Stop for configuration review.
