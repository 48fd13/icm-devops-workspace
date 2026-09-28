# Workflow: PR / Diff Review

Use to review a proposed implementation change for correctness, operational risk, and validation gaps.

## Checklist

1. Read the diff and changed-file context only as needed.
2. Identify behavior changes, operational impact, and rollback implications.
3. Check tests/validation coverage and likely missing checks.
4. Look for secrets, auth/permission changes, deploy/release changes, infra/cloud/cluster mutations, and data-loss risks.
5. Separate blocking issues from suggestions.

## Stop gates

Do not rewrite the PR unless the user asks. Ask before changing files, committing, pushing, or running risky commands.

## Result

Return findings grouped as: blocking, non-blocking, validation gaps, and questions.
