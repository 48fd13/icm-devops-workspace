# Stage 06: Validate and hand over

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_bootstrap.md` | Bootstrapped environment |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/04_provision.md` | Provisioning evidence |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Evidence rules |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Handoff procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Validate access, network connectivity, DNS, TLS, GitOps sync, and observability end to end.
2. Produce the handover: what exists, where it is defined, who owns it, and how to change it.
3. Keep the run active for review.

## Audit

- Validation evidence covers every requirement.
- The handover is usable without chat context.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_handover.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- environment facts (account or project, regions, network ranges, endpoints, access model, owners) -> `_workspace/context/project/`
- the design and its key decisions -> `_workspace/artifacts/decisions/`
- follow-ups -> `_workspace/backlog/items/`

Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
