# Changelog

## 0.1.0 — unreleased

First release.

- One tool-agnostic workspace template under `template/`, with `AGENTS.md` as the single behavior and safety authority.
- 20 pipelines covering service onboarding, environment provisioning, onboarding maps, implementation and infrastructure change, infrastructure and release rollout, CI/CD platform changes, workload and data migration, drift and vulnerability remediation, incident response, credential rotation, major upgrades, recovery exercises, service decommission, service readiness, cost optimization, and security assessment.
- 37 one-pass workflows across development, infrastructure, CI/CD, operations, and knowledge transfer, including create workflows for Dockerfiles, Helm charts, Kustomize overlays, CI pipelines, GitOps applications, secret wiring, Terraform modules, and alert rules.
- Reference context: principles, discovery and validation checklists, provider notes, and tool notes. Every pipeline stage names the concrete context files it loads.
- Persistent runs with explicit finish, promotion, and archive.
- `scripts/init-workspace.py` (non-destructive by default) and `scripts/validate-kit.py`, standard library only.
- Docs for the model, ICM alignment, authoring, and safety; three example request traces.
- CC0-1.0 license.
