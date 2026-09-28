# Stage 04: Remediation Plan

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_findings.md` | Reviewed findings |
| Layer 3 reference | `_workspace/workflows/operations/rollback-plan-review.md` | Load when remediation has rollout risk |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Prioritize smallest effective fixes, sequencing, validation, rollback, dependencies, residual risk, and owners/dates only when known.
2. Route implementation to the appropriate change pipeline; do not remediate silently.

## Audit

- Every remediation maps to a reviewed finding.
- Unknown ownership and accepted/deferred risk are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_remediation_plan.md`.

## Gate

Stop for remediation-plan review.
