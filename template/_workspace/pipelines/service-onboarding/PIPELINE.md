# Pipeline: Service Onboarding

Bring a new service onto the platform: container, Kubernetes packaging, configuration and secrets, CI, GitOps application, observability, and a first approved deployment to a non-production environment.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Intake | `stages/00_intake/intake.md` | Reviewed service profile |
| 01 Container | `stages/01_container/container.md` | Dockerfile and build evidence |
| 02 Kubernetes packaging | `stages/02_packaging/packaging.md` | Chart or overlays with rendered output |
| 03 Configuration and secrets | `stages/03_config_secrets/config_secrets.md` | Per-environment config and secret references |
| 04 Delivery pipeline | `stages/04_delivery/delivery.md` | CI pipeline definition |
| 05 GitOps application | `stages/05_gitops/gitops.md` | Application definitions and registration |
| 06 Observability | `stages/06_observability/observability.md` | Alerts, dashboard, and SLIs |
| 07 Deploy to non-production | `stages/07_deploy_dev/deploy_dev.md` | Verified non-production deployment |
| 08 Finalize | `stages/08_finalize/finalize.md` | Service handover |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Workflow procedures and reference context | `_workspace/workflows/` and `_workspace/context/` files named by the stage |
| Layer 4 | Run inputs, handoffs, and working artifacts | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use to take a new service from source code to a verified deployment in a non-production environment. Use `release-rollout` for production releases, and the individual create workflows (Dockerfile, Helm chart, CI pipeline, GitOps application) for a single piece of this work.

## Operating rules

- Execute one stage at a time and preserve every handoff.
- Referenced workflows supply procedure and audit criteria only; the stage owns inputs, artifact paths, and the gate.
- Stages before the deploy stage write files only in `repos/<name>/` and the run; they do not push, merge, apply, or sync.
- Stage 07 deploys to a non-production environment only, and only after approval for the exact merge, sync, or deployment. Production goes through `release-rollout`.
