# CI Platform Notes

Applies to GitHub Actions, GitLab CI, and similar platforms.

- Separate stages: build, test, scan, and publish run on every change; deploy or apply runs only from protected branches or tags, behind an environment approval.
- Pin third-party actions, images, and includes to a commit SHA or exact version.
- Grant the minimum token permissions per job, and prefer short-lived OIDC federation to cloud providers over long-lived stored keys.
- Keep secrets in the platform's secret store or an external manager; never echo them, and mask them in logs.
- Cache dependencies by lockfile hash; do not cache anything that contains secrets.
- Publish artifacts and images with immutable identifiers, and pass the same identifier from build to deploy.
- For infrastructure pipelines, run plan on pull requests and apply only on protected branches after approval.
- Changes to shared templates, runners, or required checks affect every repository that uses them and are approval-gated.
