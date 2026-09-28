# Stage 03: Pilot

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_implement.md` | Reviewed change |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Evidence rules |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. If enabling for the named pilot consumers is not approved in the current instruction, stop and request approval.
2. Enable it for the pilot, compare build times, success rates, and outputs with the previous version, and record problems.

## Audit

- Only approved pilot consumers were changed.
- Comparison evidence is recorded.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_pilot.md`.

## Gate

Stop after the pilot for review.
