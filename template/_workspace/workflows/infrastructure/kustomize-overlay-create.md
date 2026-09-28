# Kustomize Overlay Create Workflow

## Required context

- `_workspace/context/reference/kubernetes-principles.md`
- `_workspace/context/reference/tool-notes/helm-kustomize.md`

## Process

1. Identify the base, the new environment, and what must differ: replicas, resources, image tag, configuration, ingress hosts, and secret references.
2. Create `overlays/<environment>/kustomization.yaml` that references the base and applies only the needed patches, name prefixes or suffixes, labels, and image overrides.
3. Keep patches small and explicit; do not copy base manifests into the overlay.
4. Validate with `kustomize build` (or `kubectl kustomize`) and diff the output against another environment. Do not apply.

## Result

Produce the overlay, its rendered diff against an existing environment, and open questions.
