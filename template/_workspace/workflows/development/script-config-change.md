# Workflow: Script or Config Change

Use for shell/Python/automation scripts, config files, CI/CD YAML, manifests, Helm values, or repo glue changes that are small enough for one pass.

## Checklist

1. Identify what consumes the script/config and when it runs.
2. Check for secrets, environment-specific values, destructive flags, and production/shared-environment coupling.
3. Make the smallest local edit.
4. Validate with syntax checks, dry-runs, tests, or config-specific validators when safe.
5. Document behavior changes and rollback/revert notes.

## Stop gates

Ask before running commands that mutate cloud/cluster/infra resources, change deployment gates, install dependencies, publish artifacts, or alter secrets/auth.

## Result

Return changed files, behavior impact, validation, and any manual follow-up.
