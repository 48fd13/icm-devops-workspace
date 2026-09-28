# Container Notes

- Use multi-stage builds: compile and test in a build stage, copy only runtime artifacts into a minimal final image.
- Pin base images by digest or exact tag, and prefer maintained minimal bases (distroless, slim, alpine where compatible).
- Run as a non-root user with a fixed UID, and keep the root filesystem read-only where the application allows it.
- Declare the listening port, a healthcheck or probe endpoint, and graceful shutdown on SIGTERM.
- Order layers so dependency installation is cached separately from source changes. Keep `.dockerignore` current.
- Never bake secrets, credentials, or environment-specific configuration into an image; inject them at runtime.
- Tag images immutably (commit SHA or version) and record the digest that was deployed. Scan images in CI before they are promoted.
