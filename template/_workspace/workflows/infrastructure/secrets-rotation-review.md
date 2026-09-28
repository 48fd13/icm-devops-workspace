# Workflow: Secrets Rotation Review

Use for secret, token, API key, certificate, credential, password, KMS/key-material, or service-account rotation planning/review.

## Required context

- secret name/placeholder and consumers, without secret values
- storage location type: secret manager, Kubernetes Secret, CI/CD secret, env var, config store, certificate store, etc.
- deployment/reload behavior and rollback/revoke expectations
- audit/access ownership notes

## Process

1. Identify producers, consumers, environments, rotation reason, and whether dual-read/dual-write or overlap is needed.
2. Check where the secret is stored, injected, cached, logged, and reloaded.
3. Review access scope, least privilege, audit trail, expiration, revocation, and break-glass concerns.
4. Plan sequencing: create new secret, update consumers, validate, revoke old secret, monitor, and clean up references.
5. Define validation without exposing secret values: connectivity checks, health checks, auth simulation, or smoke tests.
6. Define rollback/revoke behavior and monitoring for auth failures.

## Stop gates

Ask before viewing secret values, creating/rotating/revoking credentials, changing auth flows, changing KMS/key management, or mutating production/shared secret stores.

## Result

Return:

- rotation scope and consumers
- sequencing plan
- validation and monitoring checks
- rollback/revoke notes
- access/audit risks
- open questions
