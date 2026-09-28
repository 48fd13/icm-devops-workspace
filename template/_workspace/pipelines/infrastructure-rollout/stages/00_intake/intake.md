# Stage 00: Intake

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Approved infrastructure change packet and supplied evidence |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Confirm target, environment, requested operation, owner, approvals, non-goals, and expected evidence.
2. Verify the packet contains plan, risks, validation, and rollback/fix-forward; do not redesign the change silently.

## Audit

- Target and operation are unambiguous.
- Missing approval or packet evidence is explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_intake.md`.

## Gate

Stop for intake review.
