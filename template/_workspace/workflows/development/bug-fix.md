# Workflow: Bug Fix

Use for debugging and fixing a local bug or regression in code, scripts, config, CI, or automation.

## Checklist

1. Reproduce or characterize the failure from logs, tests, user report, or code path.
2. Identify the likely cause and affected files.
3. Check whether the fix has deployment, data, compatibility, or operational risk.
4. Apply the smallest local fix.
5. Run focused validation for the failing path.
6. Record what failed before, what changed, and what now passes.

## Stop gates

Stop if the likely fix requires dependency installs, external mutations, production changes, secret/auth changes, schema/data migrations, or large refactors.

## Result

Return root cause, fix summary, changed files, validation, and remaining risk.
