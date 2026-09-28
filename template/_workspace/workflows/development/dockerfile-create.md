# Dockerfile Create Workflow

## Required context

- `_workspace/context/reference/tool-notes/containers.md`
- `_workspace/context/reference/security-and-secrets-rules.md`

## Process

1. Identify the application runtime, build tool, entrypoint, listening port, health endpoint, and the repository under `repos/<name>/`.
2. Write a multi-stage Dockerfile: a pinned build stage that installs dependencies and builds, and a minimal pinned runtime stage that copies only runtime artifacts.
3. Run as a non-root user, expose the port, add a healthcheck or document the probe endpoint, and handle SIGTERM.
4. Add or update `.dockerignore`. Keep secrets and environment-specific configuration out of the image.
5. Validate locally where possible (build, run, hit the health endpoint). Do not push images or change registries without approval.

## Result

Produce a Dockerfile and `.dockerignore` in the service repository, with build and run commands, image size and user, validation evidence, and open questions.
