# Methodology

The whole model fits in five ideas. Everything in `template/` is one of them applied to DevOps work.

## 1. Policy is a file the agent reads first

`AGENTS.md` at the workspace root defines how the agent behaves: how it routes, when it opens a run, what the run lifecycle is, and which operations always need confirmation. It is plain Markdown, so it can be read, diffed, and edited like any other file. When a doc or a workflow disagrees with it, `AGENTS.md` wins.

## 2. Routing picks the smallest process that fits

`_workspace/map/routing-table.md` maps a request to one of four outcomes:

| Outcome | Use for | Example |
|---|---|---|
| Direct answer | Questions, status checks, clarification | "Which state backend does this use?" |
| Task | Bounded work with no reusable procedure | "Rename these three variables across the module" |
| Workflow | One-pass work with a known checklist | Terraform review, DNS/TLS review, runbook draft |
| Pipeline | Work that needs human checkpoints between stages | Infrastructure change, release rollout, incident response |

The routing table is short on purpose. Workflow details live in per-domain route files under `_workspace/map/routes/`, and the agent opens only the one that matches. A routine question does not pay the context cost of every route.

## 3. A run holds the work, not the chat

A run is a folder under `_workspace/runs/active/` created before substantive work starts:

```text
_workspace/runs/active/2026-10-02-rds-subnet-move/
├── RUN.md       request, assumptions, plan, current step, open questions
├── input/       material you supplied
├── stages/      pipeline stage handoffs (01_discovery.md, 02_plan.md, ...)
├── artifacts/   working material and deliverables under review
└── final/       approved content, written only on explicit finish
```

Because the state is on disk, a session can end and resume without losing anything, two runs can be in flight at once, and every decision has a record.

## 4. Pipelines stop between stages

A pipeline is `PIPELINE.md` plus one contract per stage. Each contract states:

- **Inputs**: the exact files to load, by layer
- **Do NOT load**: what must stay out of context
- **Process**: the steps
- **Audit**: checks that must pass before the handoff is written
- **Artifacts**: where the handoff and supporting material go
- **Review gate**: where the agent stops

The agent runs one stage, writes `stages/<NN_name>.md`, and stops. You read it, edit it if needed, and tell it to continue. Stages that need a domain procedure reuse a workflow as reference material. For example, the review stage of `infrastructure-change` applies the Terraform review workflow only when the change touches Terraform.

## 5. Finishing is explicit, and learning is kept

Nothing leaves the run until you say the run is finished. Then the approved result goes to the run's `final/`, which remains the record, and only the promotions the process declares are applied. For example, `infrastructure-change` promotes the change packet to `_workspace/artifacts/change-packets/`, `onboarding-map` promotes reviewed facts to `_workspace/context/project/` with a `Last verified` date, and most pipelines send open follow-ups to `_workspace/backlog/items/`. A standalone workflow promotes nothing unless you approve it.

Promoting reviewed facts is how the workspace improves: the next run starts from them instead of rediscovering them. Archiving a finished run is a separate instruction.

## Safety runs through all of it

Every process, including urgent incident work, stops at the gates in `AGENTS.md`: destructive or irreversible operations, infrastructure and cloud mutations, IAM and secrets, DNS/TLS, deployments and production changes, billing, and anything external. Discovery stages are read-only and audit that nothing was changed. Entering an execution stage is never itself approval; approval must name the exact operation and target. See [`../authoring/safety-and-lifecycle.md`](../authoring/safety-and-lifecycle.md).
