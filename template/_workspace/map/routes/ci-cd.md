# CI/CD Routes

Reached from `_workspace/map/routing-table.md`. Pick one workflow and follow it.

### CI/CD review

Use when: reviewing CI/CD pipelines, build automation, release automation, or deployment workflow config.

Go to: `_workspace/workflows/ci-cd/ci-cd-review.md`

Context: `_workspace/context/reference/tool-notes/ci-cd.md` and secrets rules.

### Release readiness review

Use when: checking whether a release/deployment is ready to proceed.

Go to: `_workspace/workflows/ci-cd/release-readiness-review.md`

Context: changelog, validation status, migration/rollback notes, observability, and deployment gates.

### CI pipeline creation

Use when: creating or extending a build, test, scan, and publish pipeline for a repository.

Go to: `_workspace/workflows/ci-cd/ci-pipeline-create.md`

Context: `_workspace/context/reference/tool-notes/ci-platforms.md`, CI/CD principles, and secrets rules.

### GitOps application creation

Use when: adding a service or environment to Argo CD, Flux, or another GitOps controller.

Go to: `_workspace/workflows/ci-cd/argocd-application-create.md`

Context: `_workspace/context/reference/tool-notes/gitops.md` and the target cluster and environment.
