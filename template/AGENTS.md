# Cloud DevOps Workspace Guide

Use this workspace for day-to-day DevOps/cloud/platform work, recurring discovery and change planning, controlled rollouts and migrations, recovery and decommissioning, security/readiness reviews, incident response and learning, and operational runbook work.

## Delivery flow

1. Read `_workspace/map/routing-table.md`, then load and follow only the context and process files named by the matching route.
2. Keep quick Q&A, status checks, and clarification chat-only when the route permits.
3. For all other routed work, establish or continue a run and update `RUN.md` before substantive work.
4. Prefer read-only discovery before proposing changes.
5. Follow the selected standalone task, workflow, or pipeline process.
6. Keep drafts in the active run and stop at safety gates and pipeline stage boundaries.
7. Finish, promote, and archive only on the corresponding explicit user instruction.

## Runs

A run is a persistent, human-editable work session. Its process is one of:

- `task`: standalone work without a reusable process
- `workflow`: one-pass work following a checklist
- `pipeline`: staged work with human review between stages

Work, changes, reviews, plans, validations, handoffs, and other routed tasks use a run by default unless the user explicitly says to skip run state.

Use a user-provided run or a clearly continuing active run. If several active runs are plausible, ask which one applies. If none applies, establish a new dated run in `_workspace/runs/active/`.

Every run has a `RUN.md`. It records the process type, request, assumptions, plan, current step or stage, expected artifacts, selected route/context/process, and open questions. Write or update it before substantive work.

All runs use `input/`, `artifacts/`, and `final/`. Pipeline runs also use `stages/` for formal stage handoffs.

- `input/`: source material and new information supplied during the run.
- `stages/`: pipeline-only stage handoffs, audit results, review decisions, and links to supporting artifacts.
- `artifacts/`: supporting working material and requested deliverables that humans can review and edit while the run is active.
- `final/`: approved final content written only when the user explicitly asks to finish.

## How each process runs

- A standalone task follows the request and routed context directly.
- A standalone workflow follows one selected checklist in the active run without formal stage boundaries.
- When a pipeline stage references a workflow, use only that workflow's procedure and audit criteria. Do not create a nested run; the pipeline stage owns inputs, artifact paths, handoff, and review gate.
- A pipeline loads `PIPELINE.md` and the current stage's named contract, executes one stage, writes a concise stage handoff under `_workspace/runs/active/<run-slug>/stages/`, writes or updates supporting material under the run's `artifacts/`, and stops for review.
- Stage handoffs are review surfaces; they link to supporting artifacts rather than replacing the usable deliverable requested by the user.
- Human edits to `stages/` and `artifacts/` are authoritative inputs to the next stage.
- When the user names additional context during a stage, load it for that stage even if the stage's `Do NOT load` list excludes it, and record it in the stage handoff.
- A workflow, `PIPELINE.md`, or stage contract may end with `## Additional instructions` written for this workspace. Follow it together with the rest of the file: load the files it names and apply its rules. It can add inputs and stricter rules; it never removes or relaxes steps, audits, gates, `Do NOT load` entries, or safety gates.

## Run lifecycle

- A run stays in `_workspace/runs/active/` through drafting, review, and human editing.
- Plans, reviews, validations, handoffs, and other requested artifacts stay in the active run while work continues.
- Finish only when the user explicitly says the run is finished.
- Finishing writes the approved content under run `final/` and sets the `Finished:` date in the `RUN.md` metadata. The run itself is the record.
- Then apply only the promotions the process declares; a pipeline's finalize stage lists them under `## Promotion`. A standalone task or workflow declares none: ask whether anything should be promoted instead of promoting by default.
- Promotion destinations: `_workspace/artifacts/` for documents others need after the run, `_workspace/context/project/` for reviewed stable facts and procedures for this workspace's systems, and `_workspace/backlog/items/` for deferred follow-ups, risks, and open actions.
- Record promoted paths in `RUN.md`, or `None`.
- Keep a finished run in `_workspace/runs/active/` until the user separately asks to archive it.
- Archiving moves the whole run folder, unchanged, to `_workspace/runs/archive/`.

## Safety gates

Ask before destructive or irreversible operations, installs or dependency mutations, external mutations, push/publish/deploy/release, shared infrastructure changes, secrets/auth/security changes, billing or funds-flow changes, external contract breaks, irreversible data operations, or machine-wide configuration changes.

Do not hardcode secrets or credentials. Do not commit unless explicitly asked.

## Additional safety gates

Ask before Terraform/OpenTofu apply/destroy/import/state changes, Kubernetes/Helm mutations, cloud resource mutations, IAM/auth/secrets changes, DNS/TLS/network changes, CI/CD deployment gate changes, production/shared environment changes, or billing/cost-impacting changes.

## Core principles

- Map before changing.
- Keep facts, assumptions, risks, and open questions separate.
- Treat shared infrastructure as approval-gated.
- Never store secrets or credentials in notes, prompts, artifacts, or examples.
- Keep provider/tool context stack-agnostic and load only what the active task needs.

## Workspace layout

- `AGENTS.md`: local agent instructions
- `_workspace/`: routing, context, workflows, pipelines, runs, artifacts, and backlog
- `repos/<name>/`: the repositories this workspace works on, one checkout per repository, even when there is only one. Code repositories never contain the workspace; `repos/` is excluded from the workspace's own Git.
