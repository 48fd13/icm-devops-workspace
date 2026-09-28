# Workflow: Rollback Plan Review

Use to draft or review rollback, revert, or fix-forward plans for application, config, infrastructure, CI/CD, or operational changes.

## Required context

- change summary and affected components
- deployment/release path
- data/schema/config compatibility notes
- monitoring and incident/on-call expectations

## Process

1. Identify what changed, where it is deployed/applied, and the trigger for rollback.
2. Define rollback option: revert commit, previous artifact/image, config restore, feature flag, IaC rollback, Helm rollback, manual mitigation, or fix-forward.
3. Check data compatibility, migrations, caches, queues, external dependencies, and irreversible operations.
4. Define validation after rollback: health checks, metrics, logs, traces, smoke tests, customer impact checks, and alert status.
5. Identify who approves/executes rollback and what communications are needed.
6. Call out risks where rollback may be unsafe or impossible.

## Stop gates

Ask before executing rollback, running deploy/release commands, mutating infrastructure/clusters/cloud resources, changing data, or altering production/shared environments.

## Result

Return:

- rollback trigger criteria
- rollback/fix-forward steps
- validation and monitoring checks
- owner/approval notes
- irreversible risks
- open questions
