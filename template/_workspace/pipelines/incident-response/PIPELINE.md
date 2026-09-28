# Pipeline: Incident Response

Coordinate active incident triage, stabilization, investigation, recovery, verification, communication, and handoff.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Triage | `stages/00_triage/triage.md` | Current impact and response frame |
| 01 Stabilize | `stages/01_stabilize/stabilize.md` | Approved mitigation evidence |
| 02 Investigate | `stages/02_investigate/investigate.md` | Evidence and ranked hypotheses |
| 03 Recover | `stages/03_recover/recover.md` | Approved recovery evidence |
| 04 Verify | `stages/04_verify/verify.md` | Recovery verification |
| 05 Communicate | `stages/05_communicate/communicate.md` | Current-state communication |
| 06 Finalize | `stages/06_finalize/finalize.md` | Response handoff and learning input |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace and incident safety policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Observability, rollback, SLO, and handoff procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Timeline, handoffs, and sanitized response evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use during active impact. After recovery, use the incident-review workflow for cause analysis and a retrospective note.

## Operating rules

- Urgency may shorten review cadence only when the user explicitly authorizes continuous non-mutating stages.
- Every mitigation, rollback, failover, recovery, or external mutation still requires exact approval.
- Preserve factual timestamps and separate facts, hypotheses, actions, and unknowns.
- Never expose secrets or sensitive incident data in artifacts.
