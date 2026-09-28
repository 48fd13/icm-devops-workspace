# Stage 03: Findings

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/02_controls.md` | Reviewed control evidence |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_threat_surface.md` | Threat context |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Form evidence-backed findings with condition, affected asset, exploitability, impact, severity rationale, uncertainty, and smallest useful recommendation.
2. Separate findings from observations and unverified hypotheses.

## Audit

- Each finding is traceable to evidence and scoped assets.
- Severity is justified without overclaiming.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/03_findings.md`; put detailed finding records under run `artifacts/`.

## Gate

Stop for findings review.
