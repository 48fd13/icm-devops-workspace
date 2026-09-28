# Pipeline: Security Assessment

Produce an authorized, evidence-based security assessment with bounded scope, findings, remediation priorities, and retest results.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Authorized assessment boundary |
| 01 Threat surface | `stages/01_threat_surface/threat_surface.md` | Trust-boundary and attack-surface map |
| 02 Controls | `stages/02_controls/controls.md` | Control evidence and gaps |
| 03 Findings | `stages/03_findings/findings.md` | Evidence-backed findings |
| 04 Remediation plan | `stages/04_remediation_plan/remediation_plan.md` | Prioritized remediation plan |
| 05 Retest | `stages/05_retest/retest.md` | Retest evidence |
| 06 Finalize | `stages/06_finalize/finalize.md` | Reviewed assessment report |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace, access, and secret-safety policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Applicable security-domain review procedures | selected `_workspace/workflows/` files |
| Layer 4 | Authorized inputs, handoffs, and sanitized evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use for dedicated security evidence and findings. Use service-readiness review for general operational readiness. This pipeline does not authorize penetration testing, secret access, or remediation changes.

## Operating rules

- Keep evidence access inside the approved scope and stop before intrusive or mutating tests.
- Never record secrets or unnecessary sensitive data.
- Referenced workflows supply review procedure only; remediation uses a separate approved change process.
- Keep sanitized evidence under run `artifacts/`; use `final/` only on explicit finish.
