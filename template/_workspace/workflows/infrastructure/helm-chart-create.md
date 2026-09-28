# Helm Chart Create Workflow

## Required context

- `_workspace/context/reference/kubernetes-principles.md`
- `_workspace/context/reference/tool-notes/kubernetes.md`
- `_workspace/context/reference/tool-notes/helm-kustomize.md`
- `_workspace/context/reference/security-and-secrets-rules.md`

## Process

1. Collect the service profile: image, ports, probes, resources, configuration, secret references, dependencies, exposure, and environments.
2. Scaffold the chart in the service or platform repository under `repos/<name>/`: `Chart.yaml`, `values.yaml`, and templates for Deployment, Service, ServiceAccount, and optional Ingress, HPA, and PodDisruptionBudget behind values toggles.
3. Set safe defaults: non-root security context, liveness and readiness probes, resource requests and limits, rolling update strategy, and standard labels.
4. Add `values.schema.json` or documented values, and one values file per environment. Reference secrets by name only.
5. Validate with `helm lint` and `helm template`, and review the rendered manifests. Do not install or upgrade releases.

## Result

Produce a Helm chart with per-environment values, lint and render evidence, and open questions.
