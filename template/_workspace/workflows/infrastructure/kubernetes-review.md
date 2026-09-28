# Kubernetes Review Workflow

## Required context

- `_workspace/context/reference/kubernetes-principles.md`
- `_workspace/context/reference/tool-notes/kubernetes.md`
- `_workspace/context/reference/tool-notes/helm-kustomize.md` when Helm/Kustomize is involved

## Process

1. Identify cluster, namespace, workload, environment, and ownership.
2. Review manifests/rendered output for rollout, probes, resources, config, secrets, RBAC, exposure, and observability.
3. Identify mutation risk and validation.

## Result

Produce a Kubernetes review containing findings, mutation risks, validation gaps, and open questions.
