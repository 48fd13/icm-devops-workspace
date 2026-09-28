# Development Routes

Reached from `_workspace/map/routing-table.md`. Pick one workflow and follow it.

### Small implementation

Use when: making a small code, config, script, automation, or documentation change.

Go to: `_workspace/workflows/development/small-implementation.md`

Context: local repo context and `_workspace/context/reference/validation-evidence.md`.

Avoid when: the change needs staged review; use the implementation-change pipeline instead.

### Bug fix

Use when: debugging or fixing a bug/regression.

Go to: `_workspace/workflows/development/bug-fix.md`

Context: local repo context, logs, test output, and failing behavior if supplied.

### Script or config change

Use when: changing scripts, config, CI/CD glue, manifests, values files, or automation glue.

Go to: `_workspace/workflows/development/script-config-change.md`

Context: local repo context and relevant tool notes.

### CI failure triage

Use when: triaging CI, test, build, lint, or typecheck failures.

Go to: `_workspace/workflows/development/ci-failure-triage.md`

Context: CI logs, test output, and build config.

### PR / diff review

Use when: reviewing a PR or diff for implementation risk.

Go to: `_workspace/workflows/development/pr-review.md`

Context: diff, changed files, validation expectations, and operational risk surface.

### Dependency update review

Use when: reviewing package, lockfile, base image, action, chart, module, or provider version changes.

Go to: `_workspace/workflows/development/dependency-update-review.md`

Context: changed dependency files, changelog/security notes when available, and validation expectations.

### Database migration review

Use when: reviewing schema changes, data migrations, backfills, migration ordering, or database compatibility risks.

Go to: `_workspace/workflows/development/database-migration-review.md`

Context: migration files, application compatibility, deployment order, rollback/fix-forward expectations, and data-safety gates.

### Dockerfile creation

Use when: containerizing a service or rewriting its Dockerfile.

Go to: `_workspace/workflows/development/dockerfile-create.md`

Context: `_workspace/context/reference/tool-notes/containers.md` and secrets rules.
