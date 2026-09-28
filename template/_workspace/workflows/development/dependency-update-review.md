# Workflow: Dependency Update Review

Use for package, lockfile, base image, GitHub Action, chart, module, Terraform provider, or other dependency version changes.

## Required context

- changed dependency files and lockfiles
- package manager/build tooling notes when relevant
- changelog, release notes, CVE/advisory, or compatibility notes when available
- validation expectations for affected runtime/build/test paths

## Process

1. Identify each dependency changed, old version, new version, and update type: patch, minor, major, security, replacement, or transitive.
2. Check blast radius: runtime, build-only, test-only, CI/CD, IaC provider, base image, chart, or action.
3. Review lockfile consistency and whether generated files match declared dependency files.
4. Look for breaking changes, changed defaults, removed APIs, permission changes, runtime version requirements, and known vulnerabilities.
5. Define validation: unit/integration tests, build, lint/typecheck, image build, plan-only IaC checks, or package-manager audit when safe.
6. Call out rollback/revert path and any deployment sequencing concerns.

## Stop gates

Ask before installing dependencies, regenerating lockfiles, changing package manager behavior, publishing images/packages, changing provider/plugin versions in shared infrastructure, or accepting auth/permission changes.

## Result

Return:

- dependency changes reviewed
- risk level and rationale
- validation performed or recommended
- compatibility/security notes
- rollback/revert notes
- blocking issues and questions
