# Workflow: SLO / Error Budget Review

Use for SLOs, SLIs, error budgets, reliability targets, burn-rate alerts, service health signals, and release risk against reliability goals.

## Required context

- service objectives and owner
- current SLIs/SLOs/error budget policy when available
- dashboards, alerts, incidents, and recent release history when relevant
- user journey or dependency map when available

## Process

1. Identify the user-facing promise, critical journey, owner, and measurement window.
2. Review SLIs: signal quality, source, aggregation, latency/error/availability definitions, and missing dimensions.
3. Review SLO target and error budget policy: realistic target, alerting thresholds, burn-rate alerts, and release gates.
4. Compare recent incidents, alert noise, and reliability trends against the stated objective.
5. Identify gaps in monitoring, ownership, escalation, or actionability.
6. Recommend changes to SLOs, alerts, dashboards, release risk, or operational follow-up.

## Stop gates

Ask before changing alert paging behavior, release gates, incident policy, production dashboards used for on-call decisions, or customer-facing reliability commitments.

## Result

Return:

- SLI/SLO/error budget summary
- signal quality assessment
- reliability/release risk
- alerting and dashboard gaps
- recommendations and open questions
