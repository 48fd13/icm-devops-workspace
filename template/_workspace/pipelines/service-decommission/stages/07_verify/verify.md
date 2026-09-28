# Stage 07: Verify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/06_remove.md` | Removal evidence |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Residual access checks |
| Layer 3 reference | `_workspace/workflows/infrastructure/dns-tls-review.md` | Residual routing checks |
| Layer 3 reference | `_workspace/workflows/infrastructure/cost-review.md` | Residual resource/cost checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Verify residual resources, access, DNS, automation, monitoring, data obligations, billing, ownership, and documentation.
2. Record delayed cleanup and unavailable evidence.

## Audit

- Verification covers technical, data, access, and cost residue.
- Remaining obligations are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/07_verify.md`.

## Gate

Stop for decommission verification.
