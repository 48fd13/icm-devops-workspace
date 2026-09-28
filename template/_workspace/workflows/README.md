# Workflows

Reusable one-pass procedures for day-to-day DevOps work.

Use a workflow when one pass is enough. Use a pipeline when you need review between stages.

Run selection and lifecycle follow `AGENTS.md`. Workflow runs record `Process: workflow`, put supplied material under `input/`, keep working artifacts under `artifacts/`, and write `final/` content only during explicit finish.

Approved content goes under the run's `final/`, and the run is the record. A standalone workflow declares no promotion: at finish, ask whether anything should go to `_workspace/artifacts/`, `_workspace/backlog/items/`, or `_workspace/context/project/`.

A pipeline stage may reference an applicable workflow for its procedure and audit criteria. In that case, do not create a nested run and do not apply standalone lifecycle behavior: the stage contract owns inputs, artifact paths, handoff, and review gate. If instructions conflict, the stage contract wins.

Individual workflow files describe the result they produce but do not choose where to store it. Standalone workflow runs use the active run's `artifacts/`; embedded workflows use the path selected by the calling stage.

Workflow sets:

- `development/` — implementation, bugs, dependencies, migrations, scripts/config, CI failures, PRs
- `infrastructure/` — cloud, IaC, Kubernetes, containers, config, access, DNS/TLS, cost, secrets
- `ci-cd/` — CI/CD, release readiness, build and deployment workflows
- `operations/` — observability, incidents, backups, SLOs, rollback planning
- `knowledge-transfer/` — repo/service review, runbooks, handoffs
