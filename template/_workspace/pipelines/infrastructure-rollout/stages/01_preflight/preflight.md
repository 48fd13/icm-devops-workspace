# Stage 01: Preflight

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Reviewed rollout scope |
| Layer 3 reference | Applicable infrastructure workflows named by the packet | Preflight procedure and audit criteria |

## Do NOT load

- unrelated provider or technology workflows

## Process

1. Check current state/drift, access, credentials without exposing them, locks, quotas, dependencies, maintenance window, and rollback readiness.
2. Record blockers and differences from the approved packet; perform no mutation.

## Audit

- Preconditions are evidence-backed.
- Drift and blockers are not hidden.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_preflight.md`; put detailed evidence under run `artifacts/`.

## Gate

Stop for preflight review.
