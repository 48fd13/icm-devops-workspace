# Workflow: Access Change Review

Use for IAM, RBAC, service accounts, roles, policies, security groups, firewall rules, credentials, tokens, and access-control changes.

## Required context

- changed access/IAM/RBAC/security policy files
- affected identities, resources, environments, and actions
- security/secrets rules
- audit and rollback expectations

## Process

1. Identify principal, resource, action, environment, and reason for each access change.
2. Check least privilege: scope, wildcards, broad admin permissions, cross-account/namespace access, and time-bound needs.
3. Review blast radius, privilege escalation paths, public exposure, network reachability, and data sensitivity.
4. Check auditability: ownership, ticket/change reference, logging, expiration, and break-glass considerations.
5. Define validation without mutation when possible: policy lint, plan/diff, dry run, access simulation, or peer review.
6. Define rollback/revoke path and monitoring after change.

## Stop gates

Ask before applying IAM/RBAC/security group changes, creating credentials, rotating secrets, changing auth flows, or widening production/shared access.

## Result

Return:

- access changes summarized by principal/resource/action
- least-privilege assessment
- blast radius and audit notes
- validation plan/results
- rollback/revoke notes
- blocking issues/questions
