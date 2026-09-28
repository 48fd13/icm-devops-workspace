# Stage 02: Controls

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/01_threat_surface.md` | Reviewed threat surface |
| Layer 3 reference | Applicable infrastructure, CI/CD, container, Kubernetes, access, secrets, and observability workflows | Control procedures |

## Do NOT load

- workflow procedures unrelated to the scoped control surface

## Process

1. Select only applicable workflow procedures and evaluate identity, secrets, network, CI/CD, IaC, image, runtime, logging, backup, and recovery controls.
2. Record evidence, gaps, compensating controls, and inaccessible areas; do not run intrusive tests.

## Audit

- Every control conclusion cites evidence or states uncertainty.
- No workflow creates a nested run or controls output paths.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/02_controls.md`; store sanitized evidence under run `artifacts/`.

## Gate

Stop for control-evidence review.
