# Workflow: Release Readiness Review

Use before a release or deployment to check whether the change is ready, observable, reversible, and approved.

## Required context

- release/change summary
- diff, changelog, PR, or artifact version
- validation status
- deployment plan and environment gates
- migration, rollback, and observability notes when relevant

## Process

1. Identify release scope, target environment, artifact/version, owner, and expected user/system impact.
2. Check validation status: tests, build, lint/typecheck, security checks, IaC plan/render, smoke checks, and known skipped checks.
3. Review deployment gates: approvals, sequencing, freeze windows, feature flags, migrations, config changes, and dependency readiness.
4. Review observability: dashboards, alerts, logs, metrics, traces, SLOs, and post-deploy smoke checks.
5. Review rollback/fix-forward plan, including data/schema compatibility and irreversible operations.
6. Summarize go/no-go risks and explicit questions.

## Stop gates

Ask before deploying, publishing, pushing tags/images/packages, changing release gates, running migrations, or mutating production/shared environments.

## Result

Return:

- readiness status: ready, ready with risks, not ready, or blocked
- validation summary
- deployment/rollback notes
- observability checks
- blocking issues/questions
- recommended next action
