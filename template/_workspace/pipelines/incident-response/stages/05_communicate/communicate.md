# Stage 05: Communicate

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_verify.md` | Reviewed recovery status |
| Layer 4 working | `_workspace/runs/active/<run-slug>/artifacts/` | Sanitized timeline and evidence |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Communication summary procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce audience-appropriate current state, impact, actions, verification, risks, unknowns, and next-update expectations.
2. Exclude secrets, sensitive internals, speculation, and unsupported cause claims.

## Audit

- Communication is factual, current, and audience-safe.
- Cause is not claimed before evidence supports it.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_communicate.md`; put requested communication drafts under run `artifacts/`.

## Gate

Stop for communication review.
