# CI Pipeline Create Workflow

## Required context

- `_workspace/context/reference/ci-cd-principles.md`
- `_workspace/context/reference/tool-notes/ci-platforms.md`
- `_workspace/context/reference/tool-notes/ci-cd.md`
- `_workspace/context/reference/security-and-secrets-rules.md`

## Process

1. Identify the CI platform, repository, build tool, tests, artifact or image target, and the environments it feeds.
2. Write the pipeline: build, test, lint, and security scan on every change; publish an immutably tagged artifact or image on the main branch.
3. Keep deployment out of this pipeline, or behind a protected environment with approval. With GitOps, the pipeline only updates the image reference through a pull request.
4. Pin actions and images, grant minimal token permissions, use OIDC to reach cloud providers, and read secrets from the platform's store.
5. Validate syntax with the platform's linter or a dry run on a branch. Do not change required checks, runners, or shared templates without approval.

## Result

Produce the pipeline definition, a description of stages and triggers, the required secrets and permissions, validation evidence, and open questions.
