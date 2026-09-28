# Stage 04: Provision

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_review.md` | Reviewed risks and approvals |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_iac.md` | Reviewed plan |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Evidence rules |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Re-run the plan and confirm it matches the reviewed one.
2. If the exact apply for this step is not approved in the current instruction, stop and request approval.
3. Apply in the designed order, stopping on any unexpected change, and record evidence.

## Audit

- Every apply matches an approval.
- Unexpected plan differences stopped the stage.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_provision.md`; store apply evidence under run `artifacts/`.

## Gate

Stop after provisioning for review.
