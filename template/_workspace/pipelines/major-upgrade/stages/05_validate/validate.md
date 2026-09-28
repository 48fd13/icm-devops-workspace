# Stage 05: Validate

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_implement.md` | Reviewed implementation |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_compatibility.md` | Compatibility criteria |
| Layer 3 reference | `_workspace/workflows/development/pr-review.md` | Diff review procedure |
| Layer 3 reference | Applicable dependency, migration, and technology workflows | Validation criteria |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Review the diff and run approved build, test, render, migration, compatibility, and operational checks.
2. Record exact commands/results and unresolved compatibility risk; do not fix outside scope silently.

## Audit

- Validation maps to compatibility and success criteria.
- Failed, skipped, and unavailable checks are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/05_validate.md`; store detailed results under run `artifacts/`.

## Gate

Stop for upgrade validation review.
