# Workflow: Container Image Review

Use for Dockerfiles, image build config, container runtime settings, base images, registry behavior, and container security posture.

## Required context

- Dockerfile or image build config
- deployment/runtime manifest when available
- registry/release expectations
- secrets rules and CI/CD build context when relevant

## Process

1. Identify base image, version pinning strategy, build stages, copied files, and runtime command/entrypoint.
2. Check for secrets in build args, environment variables, layers, copied files, logs, or package manager config.
3. Review user/group privileges, writable paths, exposed ports, healthchecks, signal handling, and filesystem assumptions.
4. Check image size/layer hygiene, package cleanup, reproducibility, and dependency pinning.
5. Review supply-chain concerns: unpinned tags, external downloads, checksum verification, package repositories, and build provenance.
6. Define safe validation: image build, lint, vulnerability scan, smoke test, or manifest render without push/deploy.

## Stop gates

Ask before pushing images, changing shared registry tags, changing production image references, installing new tooling, or running deploy/release commands.

## Result

Return:

- image/build summary
- security and runtime findings
- validation recommendations/results
- blocking issues vs suggestions
- rollout/rollback notes
