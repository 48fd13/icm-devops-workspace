# Stage 06: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_revoke.md` | Revocation evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_cutover.md` | Consumer cutover evidence |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Scope/audit verification |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Authentication signal verification |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Verify consumers, audit trail, access scope, expiry, monitoring, and expected old-credential failure without exposing values.
2. Record residual consumers, references, failures, and cleanup needs.

## Audit

- New credential use and old credential rejection are evidence-backed.
- Remaining exposure or cleanup is explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_verify.md`.

## Gate

Stop for rotation verification.
