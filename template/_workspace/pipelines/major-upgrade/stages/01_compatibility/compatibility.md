# Stage 01: Compatibility

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_scope.md` | Reviewed upgrade scope |
| Layer 3 reference | `_workspace/workflows/development/dependency-update-review.md` | Dependency compatibility procedure |
| Layer 3 reference | Applicable database, container, Kubernetes, Terraform, CI/CD, or config workflow | Domain compatibility checks |

## Do NOT load

- workflow procedures unrelated to the upgrade surface

## Process

1. Assess breaking changes, APIs, data formats, plugins, clients, infrastructure, observability, and support constraints.
2. Identify intermediate versions, migration needs, and unsupported assumptions.

## Audit

- Compatibility claims cite evidence or state uncertainty.
- Cross-component ordering and irreversible transitions are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_compatibility.md`; store detailed matrix under run `artifacts/`.

## Gate

Stop for compatibility review.
