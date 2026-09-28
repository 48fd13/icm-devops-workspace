# Stage 03: Rehearsal

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_upgrade_plan.md` | Reviewed upgrade plan |
| Layer 3 reference | Applicable development and technology workflows named by the plan | Rehearsal procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Rehearse locally or in an isolated/non-production target where possible.
2. If rehearsal mutates an external/shared target, require explicit approval for the exact operation and target.
3. Record timing, failures, compatibility results, and deviations without silently changing scope.

## Audit

- Rehearsal target and representativeness are stated.
- Deviations update the proposed plan, not history.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_rehearsal.md`; store evidence under run `artifacts/`.

## Gate

Stop for rehearsal review.
