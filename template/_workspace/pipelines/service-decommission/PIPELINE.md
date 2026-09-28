# Pipeline: Service Decommission

Retire a service or resource through dependency discovery, retention approval, reversible disablement, observation, removal, and verification.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Decommission boundary |
| 01 Dependencies | `stages/01_dependencies/dependencies.md` | Consumer/resource map |
| 02 Retention | `stages/02_retention/retention.md` | Approved data and compliance disposition |
| 03 Plan | `stages/03_decommission_plan/decommission_plan.md` | Disable-observe-remove plan |
| 04 Disable | `stages/04_disable/disable.md` | Reversible disablement evidence |
| 05 Observe | `stages/05_observe/observe.md` | Continue or rollback decision |
| 06 Remove | `stages/06_remove/remove.md` | Approved removal evidence |
| 07 Verify | `stages/07_verify/verify.md` | Residual-resource verification |
| 08 Finalize | `stages/08_finalize/finalize.md` | Reviewed decommission record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace and destructive-action policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Service, retention, access, DNS, cost, rollback, and observability procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Run inputs, handoffs, and evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when retirement/removal is the primary lifecycle. Use infrastructure rollout for ordinary resource deletion inside a broader approved change.

## Operating rules

- Disablement and removal are separate safety gates; removal is never implied by disablement approval.
- Resolve retention, export, ownership, and compliance obligations before destructive action.
- Stop on unexpected consumers, traffic, dependencies, or data obligations.
- Keep evidence under run `artifacts/`; use `final/` only on explicit finish.
