# Stage 04: Implement

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_rehearsal.md` | Reviewed rehearsal and adjusted plan |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_upgrade_plan.md` | Approved local implementation scope |
| Layer 3 reference | Applicable development workflow named by the plan | Implementation procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Make only approved local repository/configuration changes.
2. Keep changes reviewable and update nearby docs/runbooks; do not deploy or mutate external systems.

## Audit

- Changed files map to the approved plan.
- No external deployment or infrastructure mutation occurred.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_implement.md`; keep changed-file details under run `artifacts/`.

## Gate

Stop for implementation review.
