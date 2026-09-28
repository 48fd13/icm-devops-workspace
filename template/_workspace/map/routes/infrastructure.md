# Infrastructure Routes

Reached from `_workspace/map/routing-table.md`. Pick one workflow and follow it.

Load provider/tool notes only for the providers or tools involved in the active task.

### Cloud change plan

Use when: preparing a small cloud/DevOps change plan that does not need the full infrastructure-change pipeline.

Go to: `_workspace/workflows/infrastructure/cloud-change-plan.md`

Context: infrastructure change principles.

### Terraform/OpenTofu review

Use when: reviewing Terraform or OpenTofu changes.

Go to: `_workspace/workflows/infrastructure/terraform-review.md`

Context: `_workspace/context/reference/tool-notes/terraform-opentofu.md`

### Kubernetes/Helm/Kustomize review

Use when: reviewing Kubernetes, Helm, or Kustomize changes.

Go to: `_workspace/workflows/infrastructure/kubernetes-review.md`

Context: `_workspace/context/reference/tool-notes/kubernetes.md` and `_workspace/context/reference/tool-notes/helm-kustomize.md` as needed.

### Container image review

Use when: reviewing Dockerfiles, image build config, base images, runtime users, layers, healthchecks, or registry behavior.

Go to: `_workspace/workflows/infrastructure/container-image-review.md`

Context: container/build files, deployment runtime, registry policy, and secrets rules.

### Environment config review

Use when: reviewing environment variables, ConfigMaps, Secrets references, values files, per-environment overrides, or config drift.

Go to: `_workspace/workflows/infrastructure/environment-config-review.md`

Context: affected environments, config source, deployment mechanism, and rollback expectations.

### Access change review

Use when: reviewing IAM, RBAC, security groups, permissions, service accounts, roles, credentials, or access-control changes.

Go to: `_workspace/workflows/infrastructure/access-change-review.md`

Context: security/secrets rules, identity/resource scope, auditability, and rollback path.

### DNS/TLS review

Use when: reviewing DNS records, certificates, TLS settings, ingress/edge routing, load balancer listeners, or domain cutovers.

Go to: `_workspace/workflows/infrastructure/dns-tls-review.md`

Context: affected domains, environments, TTLs, certificate lifecycle, routing path, and rollback expectations.

### Secrets rotation review

Use when: planning or reviewing secret, token, key, certificate, credential, or KMS/key-material rotation.

Go to: `_workspace/workflows/infrastructure/secrets-rotation-review.md`

Context: secret consumers, deployment/reload behavior, access scope, auditability, and rollback/revoke path.

### Cost review

Use when: reviewing cloud/platform cost, resource sizing, usage changes, or billing-impacting infrastructure choices.

Go to: `_workspace/workflows/infrastructure/cost-review.md`

Context: affected resources, usage assumptions, environment scope, monitoring/budgets, and cost-risk gates.

### Helm chart creation

Use when: creating a Helm chart for a service, or adding templates and values to an existing chart.

Go to: `_workspace/workflows/infrastructure/helm-chart-create.md`

Context: Kubernetes principles, Kubernetes and Helm/Kustomize tool notes, and secrets rules.

### Kustomize overlay creation

Use when: adding an environment overlay to an existing Kustomize base.

Go to: `_workspace/workflows/infrastructure/kustomize-overlay-create.md`

Context: Kubernetes principles and Helm/Kustomize tool notes.

### Secret wiring

Use when: connecting a workload to secrets through External Secrets, Sealed Secrets, a CSI driver, or CI secret references.

Go to: `_workspace/workflows/infrastructure/secret-wiring.md`

Context: security and secrets rules.

### Terraform/OpenTofu module creation

Use when: writing a new reusable Terraform or OpenTofu module.

Go to: `_workspace/workflows/infrastructure/terraform-module-create.md`

Context: IaC principles and Terraform/OpenTofu tool notes.
