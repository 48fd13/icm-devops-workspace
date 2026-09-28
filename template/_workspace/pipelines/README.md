# Pipelines

This template includes all standard DevOps/cloud pipelines. None is the default; use the routing table to choose based on the task.

Pipelines:

- `onboarding-map/` — discover and map a new team/system/service/project scope
- `implementation-change/` — staged repo change for code, config, scripts, CI/CD, IaC, manifests, or automation
- `infrastructure-change/` — plan/review/validate shared infrastructure changes
- `service-readiness-review/` — assess operational readiness of a service/platform component
- `incident-response/` — coordinate active incident stabilization and recovery
- `data-migration/` — rehearse, execute, and verify primary data mutations
- `credential-rotation/` — introduce, cut over, revoke, and verify credentials safely
- `recovery-exercise/` — tabletop and validate backup/restore or DR capability
- `service-decommission/` — disable, observe, remove, and verify retired services/resources
- `release-rollout/` — deploy and observe an approved application/service candidate
- `infrastructure-rollout/` — execute and observe an approved infrastructure change packet
- `major-upgrade/` — coordinate compatibility, rehearsal, local upgrade, and rollout handoff
- `cost-optimization/` — measure cost reduction against service guardrails
- `security-assessment/` — produce authorized evidence, findings, remediation priorities, and retest status
- `service-onboarding/` — bring a new service onto the platform, from container to first non-production deploy
- `environment-provisioning/` — create and bootstrap a new environment, cluster, or account
- `ci-cd-platform-change/` — change shared delivery infrastructure with a pilot and staged rollout
- `drift-remediation/` — find, classify, and reconcile drift between live state and IaC or Git
- `vulnerability-remediation/` — remediate a known vulnerability from exposure to verified fix
- `workload-migration/` — move a running service to a new cluster, region, account, or provider

Execute one stage at a time and stop for review. Keep run state under `_workspace/runs/active/<run-slug>/` through final review. Finish and archive according to `AGENTS.md` as separate explicit transitions.
