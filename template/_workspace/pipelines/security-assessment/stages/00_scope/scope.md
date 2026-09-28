# Stage 00: Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Assessment request, authorization, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/infrastructure/access-change-review.md` | Access-boundary checks |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Define assets, environments, assessment questions, exclusions, evidence access, authorization, sensitivity, and success criteria.
2. Distinguish read-only assessment from intrusive testing or remediation.

## Audit

- Authorization and evidence boundaries are explicit.
- No penetration testing or secret access is implied.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_scope.md`.

## Gate

Stop for scope and authorization review.
