# Stage 08: Finalize

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/07_deploy_dev.md` | Deployment outcome |
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/` | Earlier handoffs |
| Layer 3 reference | `_workspace/workflows/knowledge-transfer/handoff.md` | Handoff procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. Produce the service handover: repository, image, chart or overlays, pipeline, applications per environment, secrets and owners, alerts, and how to release to production.
2. List open questions and follow-ups.
3. Keep the run active for review.

## Audit

- The handover is usable without chat context.
- Created, deployed, and still-missing parts are distinct.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/08_finalize.md`. On explicit finish, write approved content under the run's `final/`. Promotion is declared under `## Promotion`.

## Promotion

On explicit finish, after writing the run's `final/`, promote only:

- the service's platform facts (repository, environments, applications, secrets owners, alerts, owners) -> `_workspace/context/project/`
- open questions and follow-ups -> `_workspace/backlog/items/`

The code and manifests live in the service and platform repositories. Nothing else leaves the run; archiving keeps the whole run.

## Gate

Stop for final review; finish and archive remain separate.
