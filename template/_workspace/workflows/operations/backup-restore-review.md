# Workflow: Backup / Restore Review

Use for backup coverage, restore readiness, retention, disaster recovery, recovery testing, snapshots, exports, and RPO/RTO review.

## Required context

- data stores/resources in scope
- backup mechanism and retention policy
- restore/runbook procedure when available
- RPO/RTO expectations and access controls

## Process

1. Identify protected resources, backup frequency, retention, encryption, replication, and owner.
2. Compare backup coverage against RPO/RTO, compliance, and operational expectations.
3. Review restore path: permissions, environment, runbook clarity, dependencies, validation, and estimated duration.
4. Check failure modes: corrupt backups, missing PITR, region/account loss, key access, quota/capacity, and partial restores.
5. Review test history and define safe restore test or tabletop validation.
6. Call out gaps, risk, and follow-up actions.

## Stop gates

Ask before changing backup/retention policies, deleting backups/snapshots, restoring over live data, accessing sensitive data, or mutating production/shared resources.

## Result

Return:

- backup coverage summary
- RPO/RTO fit
- restore readiness assessment
- test/validation recommendations
- gaps and risks
- owner/follow-up actions
