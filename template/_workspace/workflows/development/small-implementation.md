# Workflow: Small Implementation

Use for small, local, reversible code/config/script/docs changes that do not need staged review.

## Checklist

1. Read the request and nearest relevant files.
2. Identify safety gates: dependency install, deploy, push, infra/cloud/cluster mutation, secrets/auth, billing, data loss.
3. State the smallest intended change if scope is not obvious.
4. Make the local change.
5. Run the smallest relevant validation, or explain why validation was not run.
6. Summarize changed files, validation, and follow-ups.

## Stop gates

Stop and ask before expanding scope, changing external contracts, installing dependencies, mutating infrastructure, deploying, pushing, or touching secrets/auth.

## Result

Produce the requested change plus a concise summary of changed files, validation, and follow-ups.
