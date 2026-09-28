# Operations Routes

Reached from `_workspace/map/routing-table.md`. Pick one workflow and follow it.

### Observability review

Use when: reviewing observability, alerts, dashboards, logs, metrics, traces, or SLO/support signals.

Go to: `_workspace/workflows/operations/observability-review.md`

Context: observability principles and relevant tool notes.

### Incident review

Use when: drafting an incident review or postmortem note after impact has ended. For active impact, use the incident-response pipeline.

Go to: `_workspace/workflows/operations/incident-review.md`

Context: incident/on-call principles.

### Rollback plan review

Use when: reviewing or drafting a rollback/revert/fix-forward plan for a change.

Go to: `_workspace/workflows/operations/rollback-plan-review.md`

Context: changed components, data compatibility, deployment path, monitoring, and irreversible-operation risks.

### Backup/restore review

Use when: reviewing backup coverage, restore readiness, retention, recovery testing, or disaster-recovery assumptions.

Go to: `_workspace/workflows/operations/backup-restore-review.md`

Context: data stores, RPO/RTO expectations, restore procedure, retention policy, and access controls.

### SLO / error budget review

Use when: reviewing SLOs, SLIs, error budgets, reliability targets, burn-rate alerts, or release risk against reliability goals.

Go to: `_workspace/workflows/operations/slo-error-budget-review.md`

Context: service objectives, metrics, alerting, recent incidents, deployment/release risk, and ownership.

### Alert and dashboard creation

Use when: creating alert rules or a dashboard for a service, from its SLIs.

Go to: `_workspace/workflows/operations/alert-rule-create.md`

Context: observability principles and tool notes.

### Kubernetes workload triage

Use when: a workload is crash-looping, OOM-killed, pending, failing probes, or restarting, and no active user impact needs incident response.

Go to: `_workspace/workflows/operations/k8s-workload-triage.md`

Context: Kubernetes principles and tool notes, and the affected cluster and namespace.

### On-call handover

Use when: handing over on-call, or summarizing the current operational state for the next shift.

Go to: `_workspace/workflows/operations/oncall-handover.md`

Context: incident/on-call principles and open runs.
