# Stage 02: Investigate

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_stabilize.md` | Stabilized state and evidence |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Evidence-quality procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Gather bounded evidence, test hypotheses safely, compare expected/current behavior, and update facts, timeline, and unknowns.
2. Do not make broad fixes or mutate external systems without exact approval.

## Audit

- Conclusions distinguish correlation, hypothesis, and confirmed evidence.
- Investigation remains bounded to current recovery decisions.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_investigate.md`; update supporting evidence under run `artifacts/`.

## Gate

Stop for investigation checkpoint unless continuous non-mutating stages were explicitly authorized.
