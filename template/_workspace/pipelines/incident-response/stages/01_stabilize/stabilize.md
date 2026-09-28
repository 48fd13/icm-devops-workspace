# Stage 01: Stabilize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_triage.md` | Current impact and facts |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Mitigation/reversal procedure |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Immediate validation signals |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Compare smallest stabilizing options, expected impact, risks, rollback, and validation.
2. If an exact mitigation and target are not explicitly approved, stop and request approval.
3. Perform only the approved mitigation, validate immediate effect, and update the factual timeline.

## Audit

- Approval matches exact mitigation and target.
- Incident urgency did not bypass safety gates.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_stabilize.md`; update timeline/evidence under run `artifacts/`.

## Gate

Stop after stabilization for human direction.
