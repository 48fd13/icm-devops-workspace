# Pipeline: Recovery Exercise

Validate recovery capability through a tabletop, isolated restore, or explicitly approved disaster-recovery exercise.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Objectives | `stages/00_objectives/objectives.md` | Scenario, RPO/RTO, and success criteria |
| 01 Recovery plan | `stages/01_recovery_plan/recovery_plan.md` | Recovery and cleanup plan |
| 02 Tabletop | `stages/02_tabletop/tabletop.md` | Reviewed assumptions and failure modes |
| 03 Execute | `stages/03_execute/execute.md` | Approved exercise evidence |
| 04 Validate | `stages/04_validate/validate.md` | Recovery validation |
| 05 Findings | `stages/05_findings/findings.md` | Gaps and remediation priorities |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed exercise record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace and data-safety policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Backup/restore, runbook, and observability procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Run inputs, handoffs, and sanitized evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use for staged recovery validation. Use backup/restore review for a one-pass posture assessment; do not use this pipeline as implicit permission to restore over live data.

## Operating rules

- Prefer isolated/non-production targets.
- Entry into Stage 03 does not authorize restoration or mutation; require exact operation-and-target approval.
- Restoration over live data and cleanup mutations require separate explicit approval.
- Keep evidence under run `artifacts/`; use `final/` only on explicit finish.
