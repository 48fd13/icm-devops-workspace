# Relationship to ICM

This kit is inspired by and adapted from **Interpretable Context Methodology (ICM)**:

- Jake Van Clief and David McDermott, *Interpretable Context Methodology: Folder Structure as Agentic Architecture*, arXiv:2603.16021, 2026. <https://arxiv.org/abs/2603.16021>
- Reference implementation: <https://github.com/RinDig/Interpretable-Context-Methodology>

Earlier versions of the paper called the approach the Model Workspace Protocol (MWP).

It is not an official or conforming ICM implementation. It keeps ICM's core ideas and extends them where operations work needs more than a single linear pipeline.

## What ICM proposes

For sequential work with human review between steps, ICM replaces multi-agent orchestration with one agent reading the right files at the right moment. Numbered stage folders encode order, Markdown files carry the prompts and context, and a five-layer hierarchy keeps each step's context small: global identity, workspace routing, a stage contract with inputs, process, and outputs, stable reference material, and the working artifacts of the current run. Its principles are one stage, one job; plain text as the interface; layered context loading; every output is an edit surface; and configure the factory, not the product.

The paper grounds these ideas in older software practice: Unix pipelines (small stages that each do one job and pass text to the next), modular decomposition, multi-pass compilers, and literate programming. Unlike a Unix pipe, which streams data straight through, each ICM handoff is a file that a person can inspect and edit before the next stage reads it.

## What this kit keeps

| ICM idea | Here |
|---|---|
| One agent, filesystem as the architecture | No orchestration code; `AGENTS.md`, routing, and contracts are Markdown |
| Five context layers | Same layering; see [`context-model.md`](context-model.md) |
| Stage contract: inputs, process, outputs | `Inputs`, `Process`, `Artifacts`, plus `Do NOT load`, `Audit`, and `Review gate` |
| Selective loading, "prevention rather than compression" | Every route and stage names concrete files; provider and tool notes load only when involved |
| Every output is an edit surface | Human edits to `stages/` and `artifacts/` are authoritative input to the next stage |
| Human review at every stage boundary | Every stage ends in a review gate |
| Plain text, Git-friendly | Everything is Markdown |

Sizes stay close to ICM's budgets. Measured roughly as words × 1.33: the workspace `AGENTS.md` is about 1,000 tokens (ICM budgets about 800 for Layer 0), the top-level routing table about 470 (about 300), and stage contracts 150 to 380 (200 to 500).

## What this kit adds for DevOps

1. **Workspace-level runs.** ICM writes each stage's output into that stage's own output folder, so a workspace holds one execution at a time and history lives in version control. Here, work lives in `_workspace/runs/active/<run-slug>/`, so runs can overlap, resume after a session ends, and be finished and archived explicitly.
2. **One workspace, many processes.** An ICM workspace is usually one pipeline. Operations work is not one pipeline, so a routing table sends each request to a direct answer, a standalone task, a one-pass workflow, or a staged pipeline. This matches ICM's own guidance that small work should not go through a staged pipeline.
3. **Safety gates.** ICM does not address permissions or destructive actions. Here, `AGENTS.md` is the single safety authority, and infrastructure, IAM, secrets, DNS/TLS, deployment, production, and billing changes always stop for confirmation. Discovery stages audit that nothing was changed, and entering an execution stage is never itself approval.
4. **Workflow reuse inside stages.** A stage can apply an existing workflow's procedure and audit criteria as Layer 3 material without starting a nested run. For example, the infrastructure-change review stage applies the Terraform review only when the change touches Terraform.
5. **A lifecycle after the run.** Finishing applies the promotions each pipeline declares: documents others need go to `_workspace/artifacts/`, follow-ups to the backlog, and reviewed facts to `context/project/` with a `Last verified` date. It is a partial answer to ICM's proposed edit-source principle: what a run learns flows back into stable context instead of being rediscovered.
6. **Tool-agnostic policy file.** The ICM reference implementation uses a `CLAUDE.md` as Layer 0. This kit uses `AGENTS.md` and ships no runtime-specific files.

## Terminology differences

| ICM | This kit |
|---|---|
| `CLAUDE.md` (Layer 0) | `AGENTS.md` |
| Root `CONTEXT.md` (Layer 1) | `_workspace/map/routing-table.md` and route files; `PIPELINE.md` inside a pipeline |
| Stage `CONTEXT.md` (Layer 2) | `stages/<NN_name>/<name>.md` |
| `references/`, `_config/`, `shared/`, `skills/` (Layer 3) | Workspace-wide `_workspace/context/` and reused workflows, named per stage |
| Each stage's output folder (Layer 4, "working artifacts") | The run's `stages/` handoffs and `artifacts/` working material |
| (none) | `_workspace/artifacts/`: durable results promoted on explicit finish |

Readers coming from the paper should note the last row: ICM uses "working artifacts" for per-run output, while `_workspace/artifacts/` here means promoted, durable results.

## Not adopted yet

- **A setup questionnaire.** ICM configures the factory once through `setup/questionnaire.md`. Here, local rules go into `context/reference/` by hand, and environment facts accumulate in `context/project/`, usually from the `onboarding-map` pipeline.
- **Scripts for mechanical steps.** ICM uses local scripts for work that needs no model. Runbooks here describe commands; they do not ship scripts that run them.

## Where ICM says not to use it, and so does this kit

ICM's sequential, file-based handoffs are the wrong tool for tight real-time multi-agent loops, high-concurrency pipelines, and branching decided by the model mid-pipeline. This kit inherits those limits. Its incident pipeline, for example, still stops for human direction after stabilization.
