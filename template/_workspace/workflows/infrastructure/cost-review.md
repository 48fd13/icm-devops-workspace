# Workflow: Cost Review

Use for cloud/platform cost, billing-impacting changes, resource sizing, quotas, capacity, retention, scaling, and managed-service pricing review.

## Required context

- changed resources or planned resource usage
- environment and expected traffic/data volume
- current cost signals, budgets, or tags when available
- scaling/retention/capacity assumptions

## Process

1. Identify cost-driving resources: compute, storage, network egress, databases, logs/metrics/traces, queues, load balancers, snapshots, or managed services.
2. Check environment scope, autoscaling/min/max, retention, replication, backup, HA, and data-transfer assumptions.
3. Review whether sizing is justified and whether defaults create hidden recurring cost.
4. Check tags/labels/ownership, budget/alert coverage, quotas, and cleanup/lifecycle policies.
5. Define validation: cost estimate, pricing calculator, plan/diff review, usage dashboard, or before/after monitoring.
6. Call out trade-offs between cost, reliability, performance, and security.

## Stop gates

Ask before creating cost-impacting resources, changing retention/replication/HA, increasing quotas/capacity, or making billing-impacting changes.

## Result

Return:

- cost drivers and assumptions
- risk level and likely cost direction
- monitoring/budget/tagging gaps
- optimization options
- approval questions
