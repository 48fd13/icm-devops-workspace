# Alert Rule Create Workflow

## Required context

- `_workspace/context/reference/observability-principles.md`
- `_workspace/context/reference/tool-notes/observability.md`

## Process

1. Identify the service, its SLIs (availability, latency, errors, saturation), the SLO if one exists, the owning team, and the escalation path.
2. Write alert rules that fire on user impact or error-budget burn, not on every symptom. Include severity, owner, a clear summary, and a link to the procedure responders should follow.
3. Add or update a dashboard that shows the SLIs and the signals a responder needs first.
4. Validate rule syntax and, where possible, test against historical data. Do not change paging routes or silence existing alerts without approval.

## Result

Produce alert rules and a dashboard definition, the SLI rationale, validation evidence, and open questions.
