# Pipeline: Drift Remediation

Find where live infrastructure or cluster state differs from IaC or Git, decide per difference whether to codify or revert it, and reconcile with approval.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Detect | `stages/00_detect/detect.md` | Drift list |
| 01 Classify | `stages/01_classify/classify.md` | Classified drift |
| 02 Plan | `stages/02_plan/plan.md` | Reconciliation plan |
| 03 Reconcile | `stages/03_reconcile/reconcile.md` | Reconciled state |
| 04 Verify | `stages/04_verify/verify.md` | Post-reconciliation drift check |
| 05 Finalize | `stages/05_finalize/finalize.md` | Drift record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Workflow procedures and reference context | `_workspace/workflows/` and `_workspace/context/` files named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when live state has drifted from its declared source. Use `infrastructure-change` for a planned change that is not about drift.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Stages 00 to 02 are read-only against live systems.
- Stage 03 requires approval for each exact apply or sync; drift that someone made on purpose is never reverted without its owner's agreement.
