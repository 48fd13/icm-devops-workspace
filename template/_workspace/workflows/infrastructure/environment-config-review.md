# Workflow: Environment Config Review

Use for environment variables, config files, ConfigMaps, Secrets references, Helm values, deployment overlays, feature flags, and per-environment overrides.

## Required context

- changed config files or values
- target environments
- deployment/rendering mechanism
- known defaults and rollback expectations

## Process

1. Identify the affected environments and whether the change is global, environment-specific, or default-only.
2. Separate plain config from secret material. Do not expose secret values in artifacts or chat.
3. Check naming consistency, default behavior, required/optional status, type/format expectations, and startup/runtime impact.
4. Review drift risk between dev/staging/prod and whether overlays/values inherit as expected.
5. Check rollout/rollback behavior: restart required, config reload supported, compatibility with current app version, and failure mode.
6. Define validation: render/diff, schema check, dry run, unit/config tests, or startup/smoke checks when safe.

## Stop gates

Ask before changing secret values, production/shared environment config, deployment gates, DNS/TLS/network config, or any config that can cause data loss or outage.

## Result

Return:

- affected config and environments
- behavior impact
- secret-handling notes without secret values
- validation plan/results
- rollback notes
- blocking issues/questions
