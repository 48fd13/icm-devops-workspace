# Stage 02: Infrastructure code

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_design.md` | Reviewed design |
| Layer 3 reference | `_workspace/workflows/infrastructure/terraform-module-create.md` | Module procedure |
| Layer 3 reference | `_workspace/workflows/infrastructure/terraform-review.md` | IaC review criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Write the IaC in `repos/<name>/`, reusing existing modules where they fit.
2. Run format, validate, and plan against the new environment's backend.

## Audit

- No apply, import, or state change occurred.
- The plan contains only the new environment's resources.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_iac.md`; store the plan output under run `artifacts/`.

## Gate

Stop for IaC review.
