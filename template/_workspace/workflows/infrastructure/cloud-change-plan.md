# Cloud Change Plan Workflow

Use for small cloud/devops changes that do not require the full infrastructure-change pipeline.

## Required context

- `_workspace/context/reference/infrastructure-change-principles.md`
- `_workspace/context/reference/security-and-secrets-rules.md`
- relevant provider/tool notes

## Process

1. Define requested change, environment, resources, and non-goals.
2. Identify blast radius, dependencies, security/cost impact, and approvals.
3. Define implementation steps without executing mutations.
4. Define validation and rollback/fix-forward.

## Result

Produce a cloud change plan containing scope, implementation steps, blast radius, approvals, validation, and rollback/fix-forward.
