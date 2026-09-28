# Workflow: CI Failure Triage

Use to inspect failing CI/test/build/lint output and propose or apply a safe local fix.

## Checklist

1. Capture the failing job, command, and key error.
2. Classify the failure: test, lint, typecheck, build, dependency, environment, credentials, flaky, or external service.
3. Inspect only relevant files/config.
4. If a safe local fix is clear, apply it; otherwise produce a triage note.
5. Run the closest local validation command when available and safe.
6. Summarize whether this is fixed, likely flaky, blocked, or needs human/environment access.

## Stop gates

Ask before changing secrets, CI deployment permissions, package lock/dependencies, external service settings, or protected branch/release behavior.

## Result

Return failure summary, suspected cause, action taken, validation, and next step.
