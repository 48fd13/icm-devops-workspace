# Stage 03: Recover

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_investigate.md` | Reviewed evidence and recovery recommendation |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Recovery/rollback procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define exact recovery, rollback, failover, or fix-forward action, target, expected effect, validation, and reversal.
2. If the exact recovery mutation is not explicitly approved, stop and request approval.
3. Execute only the approved action; stop on unexpected state and update the timeline.

## Audit

- Approval matches exact action and target.
- No unrelated remediation or cleanup occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_recover.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop after recovery action for review.
