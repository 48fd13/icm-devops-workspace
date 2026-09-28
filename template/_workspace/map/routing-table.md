# Routing Table

Use this file after reading `AGENTS.md`.

## First decision

- If the work needs human checkpoints between stages, use a pipeline.
- If the work can be completed in one pass, use a workflow.
- If no reusable workflow or pipeline matches, use a standalone task run.
- Quick Q&A, status checks, and clarification questions may use the direct route.
- If the task is unclear, ask one short clarifying question before loading more context.
- Load provider/tool notes only for providers or tools involved in the active task. Do not load AWS/GCP/Azure/tool notes all at once.

## Pipelines

Staged work with review between stages.

| Use when | Go to |
|---|---|
| Active incident impact needs triage, stabilization, recovery, verification, and communication | `_workspace/pipelines/incident-response/PIPELINE.md` |
| Schema/data mutation, backfill, transformation, or datastore movement is the primary operation | `_workspace/pipelines/data-migration/PIPELINE.md` |
| A secret, token, key, certificate, or credential needs staged rotation and revocation | `_workspace/pipelines/credential-rotation/PIPELINE.md` |
| Recovery capability needs a tabletop, isolated restore, or approved DR exercise | `_workspace/pipelines/recovery-exercise/PIPELINE.md` |
| A service or resource needs dependency-aware disablement, observation, and removal | `_workspace/pipelines/service-decommission/PIPELINE.md` |
| An approved application/service candidate needs gated deployment and observation | `_workspace/pipelines/release-rollout/PIPELINE.md` |
| An approved infrastructure change packet needs gated execution and observation | `_workspace/pipelines/infrastructure-rollout/PIPELINE.md` |
| A substantial version/platform upgrade needs compatibility analysis and rehearsal | `_workspace/pipelines/major-upgrade/PIPELINE.md` |
| Cost reduction needs a verified baseline, controlled change, and measured outcome | `_workspace/pipelines/cost-optimization/PIPELINE.md` |
| Dedicated authorized security evidence, findings, remediation planning, and retest are required | `_workspace/pipelines/security-assessment/PIPELINE.md` |
| Understanding a new team, system, service, or project scope | `_workspace/pipelines/onboarding-map/PIPELINE.md` |
| A repo change needs checkpoints between understanding, planning, implementation, validation, and handoff | `_workspace/pipelines/implementation-change/PIPELINE.md` |
| Planning, reviewing, or validating a cloud, infrastructure, platform, or shared-environment change | `_workspace/pipelines/infrastructure-change/PIPELINE.md` |
| Reviewing service, platform component, or environment operational readiness | `_workspace/pipelines/service-readiness-review/PIPELINE.md` |
| A new service needs a container, Kubernetes packaging, CI, a GitOps application, observability, and a first non-production deploy | `_workspace/pipelines/service-onboarding/PIPELINE.md` |
| A new environment, cluster, or cloud account needs to be created and bootstrapped | `_workspace/pipelines/environment-provisioning/PIPELINE.md` |
| Shared CI/CD templates, runners, required checks, or the promotion flow need a change that affects many repositories | `_workspace/pipelines/ci-cd-platform-change/PIPELINE.md` |
| Live infrastructure or cluster state differs from IaC or Git | `_workspace/pipelines/drift-remediation/PIPELINE.md` |
| A known vulnerability or advisory needs remediation across running systems | `_workspace/pipelines/vulnerability-remediation/PIPELINE.md` |
| A running service needs to move to another cluster, region, account, or provider | `_workspace/pipelines/workload-migration/PIPELINE.md` |

Prefer a one-pass workflow when the change is small, local, reversible, and needs no staged review.

When routes overlap, choose the most specific primary lifecycle: active response; vulnerability remediation; data mutation; credential rotation; drift remediation; recovery; decommission; release or infrastructure rollout; workload migration; service onboarding; environment provisioning; CI/CD platform change; major upgrade; measured cost optimization; dedicated security assessment; then the existing general pipelines.

## Workflows

One-pass checklists. Open the route file for the matching group, then follow the workflow it names.

| Work is about | Route file |
|---|---|
| Code, bug fixes, scripts, CI failures, PRs, dependencies, database migrations | `_workspace/map/routes/development.md` |
| Cloud, Terraform/OpenTofu, Kubernetes/Helm, containers, environment config, access, DNS/TLS, secrets, cost | `_workspace/map/routes/infrastructure.md` |
| CI/CD pipelines, build/release automation, release readiness | `_workspace/map/routes/ci-cd.md` |
| Observability, incidents, rollback, backup/restore, SLOs | `_workspace/map/routes/operations.md` |
| Repo/service review, runbooks, session handoff | `_workspace/map/routes/knowledge-transfer.md` |

Read only the route file that matches the active request.

## Fallback

- For other in-scope work, use a standalone task run with the relevant target and workspace context.
- For general Q&A, no workflow is required; read only the files needed to answer.
