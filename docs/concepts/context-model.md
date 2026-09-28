# Context Model

An agent works best with a small context that contains exactly what the current step needs. The kit gets there by prevention: every route and stage names what to load, and everything else stays out.

## Layers

| Layer | What it is | Where it lives | Changes |
|---|---|---|---|
| 0 | Workspace policy | `AGENTS.md` | Rarely; you own it |
| 1 | Routing | `_workspace/map/routing-table.md`, then one route file or one `PIPELINE.md` | When processes are added |
| 2 | The active contract | One workflow file, or one stage contract | When a process is improved |
| 3 | Reference material | `_workspace/context/` and workflows reused by a stage | Stable across runs |
| 4 | Working material | The active run: `input/`, earlier `stages/` handoffs, `artifacts/` | Every run |

A typical load is the policy, the routing table, one route or pipeline file, one contract, two or three reference files, and the previous handoff.

## Reference context vs project context

`_workspace/context/` has two halves, split by how the knowledge was obtained.

**`reference/`** ships with the kit and is true on day one: DevOps, IaC, Kubernetes, CI/CD, observability, incident, and security principles, plus provider notes (AWS, Azure, GCP, generic cloud) and tool notes (Terraform/OpenTofu, Kubernetes, Helm/Kustomize, CI/CD, observability). Provider and tool notes are loaded only for the providers and tools involved in the task.

**`project/`** starts empty. It holds facts that a run discovered and a human reviewed: environment maps, service inventories, ownership, approval rules. Every file starts with `**Last verified:** YYYY-MM-DD`. These facts are loaded as authoritative, so a stale one produces confident wrong answers. The `context-review` workflow re-checks the oldest entries.

## Where new knowledge goes

| You learned | Put it in |
|---|---|
| A general rule that would be true in any environment | `context/reference/` |
| A reviewed fact about this environment | `context/project/` with a `Last verified` date |
| A procedure for operating your systems | `context/project/`, or keep it in your team's runbook system and link it |
| An unresolved question, risk, or follow-up | `backlog/items/` |
| Material for the current piece of work only | the active run |

## Rules that keep context small

- Route first; do not read folders by default.
- Load provider and tool notes only for what the task touches.
- A stage's `Do NOT load` list is a hard constraint for the agent. You can override it: name extra context during a stage and the agent loads it and records it in the handoff. If the same extra file keeps being useful, add it to the stage's `Inputs`.
- A pipeline stage reads the previous stage's handoff, not the whole run.
- Human edits to handoffs and artifacts replace the agent's version; they are not merged with it.
