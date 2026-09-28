# Stage 03: Implement

## Goal

Apply the approved scoped change without performing external mutations or hidden broad refactors.

## Inputs

- Approved `_workspace/runs/active/<run-slug>/stages/02_plan.md`
- Relevant source/config/script/docs files
- User approval notes, if any

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-check safety gates before editing.
2. Make only the planned local file changes.
3. Keep changes small and reviewable.
4. Update nearby docs/runbooks when behavior or operation changes.
5. Do not install dependencies, deploy, push, apply infrastructure, mutate clusters/cloud resources, or alter secrets/auth unless explicitly approved.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Plan adherence | Only planned files changed, or deviations are listed explicitly |
| No gated mutations | No installs, deploys, pushes, infra, cluster, or secret changes without approval |
| Docs updated | Nearby docs/runbooks are updated when behavior or operation changed |

## Artifacts

Write `03_implement.md` under `_workspace/runs/active/<run-slug>/stages/` containing:

- files changed
- implementation summary
- deviations from plan
- risks introduced or reduced
- validation still needed

## Review gate

Stop after writing the active run stage file. Ask for review before validation if implementation deviated from the plan.
