# Authoring Pipelines

A pipeline is a staged process where a human reviews each stage's result before the next stage builds on it.

## Layout

```text
_workspace/pipelines/<name>/
├── PIPELINE.md                      routing table of stages, layer table, route boundary, operating rules
└── stages/
    ├── 00_<name>/<name>.md          one contract per stage
    ├── 01_<name>/<name>.md
    └── ...
```

Stage folders are numbered in execution order. Each contract file is named after its stage.

## `PIPELINE.md`

Four sections:

- **Routing**: a table of stage, contract path, and outcome.
- **Layers**: what Layers 0 to 4 are for this pipeline.
- **Route boundary**: when to use this pipeline and what to use instead.
- **Operating rules**: pipeline-wide constraints, for example "entry into the deploy stage does not authorize deployment".

## Stage contracts

Every contract has these sections. `scripts/validate-kit.py` fails if one is missing.

| Section | Contents |
|---|---|
| `Inputs` | A table of layer, exact path, and use. Layer 4 is the previous stage's handoff; Layer 3 names concrete context or workflow files. |
| `Do NOT load` | What must stay out of context: later stages, unrelated workflows, provider notes not involved. |
| `Process` | Numbered steps. Mutating steps say they need explicit approval. |
| `Audit` | Checks that must pass before the handoff is written. |
| `Artifacts` | The flat handoff path, `_workspace/runs/active/<run-slug>/stages/<NN_name>.md`, plus any supporting files under the run's `artifacts/`. |
| `Gate` (or `Review gate`) | Where the agent stops and what the human reviews before the next stage. |

Layer 3 rows name exact files in `_workspace/context/` or `_workspace/workflows/`. To give a stage local rules or checklists, add them to `_workspace/context/reference/` and name them in that stage's `Inputs`.

To reuse a workflow, name it in `Inputs` as Layer 3, or add a `Workflow selection` table when the right one depends on the change surface, as `infrastructure-change/stages/03_review/review.md` does.

## Additional instructions

Shipped pipelines are meant to stay the same in every workspace and improve over time through review, not drift per workspace. For what a workspace genuinely needs on top, such as a file of approvers, a change window, or a team checklist, append one section at the end of `PIPELINE.md` or a stage contract:

```markdown
## Additional instructions

- Also load `_workspace/context/project/prod-approvers.md`.
- Changes to the `payments` namespace need a second approver.
```

The agent follows it together with the rest of the file. It can add inputs, named exactly, and stricter rules. It never removes or relaxes steps, audits, gates, `Do NOT load` entries, or safety gates; if the shipped contract is wrong, fix the contract. Keep everything workspace-specific inside this section, so the rest of the file can be updated from the kit without losing it. When the same additional instruction appears in several workspaces, propose it for the shipped pipeline.

## Adding a pipeline

1. Copy the closest existing pipeline. `infrastructure-change/` is the fullest example of planning and review; `release-rollout/` and `incident-response/` show approval-gated execution.
2. Rewrite `PIPELINE.md` and each stage contract for the new lifecycle. Add, remove, and renumber stages as needed.
3. Add a row to `_workspace/map/routing-table.md` and, if it overlaps an existing pipeline, update the overlap-priority sentence.
4. Run `python3 scripts/validate-kit.py`.

## Design guidance

- One stage, one job. If a stage's handoff is hard to review, split it.
- Put the read-only stages first. Discovery and planning should be done before any stage that can change something.
- Make execution stages ask for approval of the exact operation and target, even when the pipeline is urgent.
- Reviewers tend to edit the first and last stages heavily and the middle ones lightly. Put the decisions that set direction in early stages so they are cheap to change.
