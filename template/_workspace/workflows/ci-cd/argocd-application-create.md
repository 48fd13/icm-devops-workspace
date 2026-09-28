# GitOps Application Create Workflow

## Required context

- `_workspace/context/reference/tool-notes/gitops.md`
- `_workspace/context/reference/ci-cd-principles.md`

## Process

1. Identify the GitOps controller (Argo CD, Flux), the root or app-of-apps object, the project or tenant, the target cluster and namespace, and the source path and revision per environment.
2. Write the application definition: an Argo CD `Application` or `ApplicationSet`, or a Flux `Kustomization` or `HelmRelease`, with destination, source, and sync options.
3. Choose the sync policy per environment: automated with prune and self-heal for development, manual or gated for production. Add sync waves for dependencies.
4. Register it in the root application or generator so it is discovered.
5. Validate the manifest schema and render the source. Do not merge to a tracked branch or sync; with auto-sync on, merging is a deployment and needs approval.

## Result

Produce the application definitions per environment, the registration change, the sync policy rationale, validation evidence, and open questions.
