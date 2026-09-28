# Architecture

## Repository map

| Path | Owns |
|---|---|
| `template/AGENTS.md` | The enforceable behavior, run lifecycle, and safety policy of an initialized workspace. The only safety authority. |
| `template/_workspace/map/` | Routing table, per-domain route files, workspace map, naming conventions |
| `template/_workspace/workflows/` | One-pass procedures, grouped by `development/`, `infrastructure/`, `ci-cd/`, `operations/`, `knowledge-transfer/` |
| `template/_workspace/pipelines/` | Staged processes: `PIPELINE.md` plus one contract per stage |
| `template/_workspace/context/` | `reference/` (shipped principles, provider and tool notes) and `project/` (facts a workspace learns and a human reviews) |
| `template/_workspace/runs/`, `artifacts/`, `backlog/` | Empty lifecycle folders with their conventions |
| `docs/` | Explanation of the model and authoring guidance. Explains `AGENTS.md`; never overrides it. |
| `examples/` | Illustrative request traces. Not shipped into workspaces. |
| `scripts/init-workspace.py` | Copies `template/` into a target folder |
| `scripts/validate-kit.py` | Checks references and structural contracts in this repository |

## Boundaries

- Everything under `template/` is copied into a user's project; nothing outside it is.
- An initialized workspace is self-contained. It never refers back to this repository.
- The kit is tool-agnostic. It ships no runtime configuration and assumes only an agent that follows `AGENTS.md` and can read and write files.
- Run state lives only under `_workspace/runs/`, never inside `pipelines/` or `workflows/`.
- Docs describe the policy in `template/AGENTS.md`. When they disagree, `AGENTS.md` wins and the doc is a bug.

## Request flow in an initialized workspace

1. The agent reads `AGENTS.md`, then `_workspace/map/routing-table.md`.
2. The routing table selects a direct answer, a standalone task, a one-pass workflow (via a route file), or a pipeline.
3. For anything beyond a quick answer, the agent opens or continues `_workspace/runs/active/<run-slug>/` and writes `RUN.md` first.
4. A workflow runs in one pass inside the run. A pipeline runs one stage, writes `stages/<NN_name>.md`, and stops for review.
5. Safety gates in `AGENTS.md` stop the agent before any mutation that needs approval, in every process.
6. On an explicit finish, the approved result goes to the run's `final/`, and only the promotions the process declares are applied (to `_workspace/artifacts/`, `context/project/`, or `backlog/items/`). Archiving is a separate instruction and keeps the whole run.

## Contracts

- Every pipeline stage contract has `Inputs`, `Do NOT load`, `Process`, `Audit`, `Artifacts`, and `Gate` (or `Review gate`) sections.
- Stage `Inputs` name concrete files. Provider and tool notes are loaded only for the providers and tools involved.
- A stage that reuses a workflow uses only that workflow's procedure and audit criteria; the stage owns inputs, artifact paths, handoff, and gate. No nested runs.
- Stage handoffs are flat files under the run's `stages/`.
- `scripts/validate-kit.py` enforces the checkable parts of these contracts and must pass before a release.
