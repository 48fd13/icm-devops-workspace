# Stage 00: Triage

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Alerts, reports, timestamps, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/operations/observability-review.md` | Signal triage procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Establish impact, severity, affected services/users, incident lead when known, timeline start, current facts, hypotheses, unknowns, and immediate constraints.
2. Identify urgent read-only checks and candidate mitigations without mutating.

## Audit

- Facts, hypotheses, actions, and unknowns are separate.
- Sensitive incident data is sanitized.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_triage.md`; begin a factual timeline under run `artifacts/`.

## Gate

Stop for triage checkpoint unless continuous non-mutating incident stages were explicitly authorized.
