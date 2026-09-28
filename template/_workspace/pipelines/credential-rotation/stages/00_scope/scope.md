# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Sanitized rotation request and metadata |
| Layer 3 reference | `_workspace/workflows/infrastructure/secrets-rotation-review.md` | Rotation scope procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define credential type, reason, environments, owners, expiry/exposure constraints, and success criteria without recording secret values.
2. Identify emergency versus planned rotation and required audit evidence.

## Audit

- No secret value or private material is stored.
- Scope and urgency are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for rotation-scope review.
