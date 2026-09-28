# Example: a stage-owned pipeline

A trace through `onboarding-map`, a pipeline whose stages carry their own procedure and reuse no workflows. It is read-only from start to finish. Names and details are illustrative.

## Request

> I just joined the payments platform team. Help me map what we run.

## Routing

The scope is new and the result should be reviewed piece by piece, so the routing table selects `_workspace/pipelines/onboarding-map/PIPELINE.md`. Its operating rules allow read-only discovery only.

## Stages

| Stage | Loads (besides the previous handoff) | Produces |
|---|---|---|
| 00 Intake | `onboarding-principles.md` | Scope, sources you can give access to, what "done" means |
| 01 Inventory | `discovery-checklist.md` | Services, environments, repos, accounts, IaC, CI/CD, observability, owners; facts kept separate from assumptions |
| 02 Relationships | `onboarding-principles.md` | Dependencies, data flows, deployment paths, ownership |
| 03 Questions | `onboarding-principles.md` | Targeted questions, grouped by who can answer them |
| 04 Finalize | `map/naming-conventions.md` | Final map, open questions, risks, proposed backlog items |

Each stage writes a flat handoff, from `stages/00_intake.md` to `stages/04_finalize.md`, and stops.

## Why review between stages matters here

The inventory will contain guesses: an environment that looks unused, an owner inferred from commit history. Stage 01 marks them as assumptions. You correct them in `stages/01_inventory.md` before stage 02 builds relationships on top of them. A wrong guess costs one edit instead of a wrong map.

## Finish

On "finish the run", the approved map goes to the run's `final/`, and the finalize stage's `## Promotion` list applies:

- the reviewed map and confirmed facts, such as the environment list, account IDs by environment, and owners, go to `_workspace/context/project/` with `**Last verified:** 2026-10-02`;
- unanswered questions and risks go to `_workspace/backlog/items/`.

The next time someone asks for a change in the payments platform, the infrastructure-change pipeline starts from those reviewed facts instead of rediscovering them.
