# Pipeline: CI/CD Platform Change

Change shared delivery infrastructure, such as reusable pipeline templates, runners, required checks, or the promotion flow, with impact analysis, a pilot, and a staged rollout.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Change scope |
| 01 Impact analysis | `stages/01_impact/impact.md` | Consumers and risks |
| 02 Implement | `stages/02_implement/implement.md` | Versioned change and test evidence |
| 03 Pilot | `stages/03_pilot/pilot.md` | Pilot results |
| 04 Rollout | `stages/04_rollout/rollout.md` | Rolled-out change |
| 05 Finalize | `stages/05_finalize/finalize.md` | Change record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Workflow procedures and reference context | `_workspace/workflows/` and `_workspace/context/` files named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when a change to delivery infrastructure affects many repositories or teams. Use the CI pipeline creation workflow for one repository's pipeline, and `release-rollout` to deploy an application.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Ship shared changes as a new version or opt-in first; do not change defaults or required checks before the pilot.
- Enabling the change for pilot or all consumers requires approval for the exact scope.
