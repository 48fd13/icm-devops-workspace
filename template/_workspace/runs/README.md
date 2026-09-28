# Runs

Persistent, human-editable work state and history for this workspace.

- `active/`: active runs plus finished runs awaiting explicit archive
- `archive/`: explicitly archived run history

A run's process is `task`, `workflow`, or `pipeline`. All runs use `input/`, `artifacts/`, and `final/`; pipeline runs also use `stages/` for formal stage handoffs.

- Put source material and newly supplied information in `input/`.
- Put pipeline stage handoffs, audits, and review decisions in `stages/`; link to supporting `artifacts/` rather than treating the handoff as the deliverable.
- Put supporting working material and requested reviewable deliverables in `artifacts/`.
- Put approved final content in `final/` only on explicit finish.
- Treat human edits in `stages/` and `artifacts/` as authoritative input to later stages.

Use a run for work, changes, reviews, plans, validations, and handoffs unless the user explicitly says to skip run state.

Runs stay in `active/` through drafting and review. Explicit finish writes the approved result under run `final/`; the run itself is the record. Finish then promotes only what the process declares, or what the user approves when the process declares nothing. Archiving is a separate explicit transition that moves the whole run folder, unchanged, to `archive/`.

Promotion destinations, used only when declared or approved:

- documents others need after the run -> `_workspace/artifacts/`
- open follow-ups, unresolved questions, risks, TODOs -> `_workspace/backlog/items/`
- reviewed stable facts -> `_workspace/context/project/`

Do not promote by default. Do not copy run content to `_workspace/artifacts/` only to keep a record; the run is the record.

Do not store run state inside `_workspace/pipelines/`.

## RUN.md

Every run has one. Copy `run-template.md` when starting a run.
