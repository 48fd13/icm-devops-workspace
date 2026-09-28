# Workspace Map

| Path | Purpose | Default behavior |
|---|---|---|
| `AGENTS.md` | Local workflow and safety policy | Read first |
| `repos/<name>/` | Repository checkouts: application code, IaC, manifests, charts | Inspect only the repository the selected route needs |
| `_workspace/map/` | Routing, naming, structure | Read first after `AGENTS.md` |
| `_workspace/context/reference/` | Template-provided principles and provider/tool notes | Load only files required by the selected route |
| `_workspace/context/project/` | Reviewed stable project reference | Load when the task depends on reliable repo/service/environment details |
| `_workspace/backlog/` | Unresolved questions, deferred follow-ups, operational risks, and open action items | Add items when work is discovered but not completed |
| `_workspace/runs/` | Standalone task, workflow, and pipeline run state | Use for active, finished, and archived run records |
| `_workspace/workflows/` | One-shot DevOps/cloud task checklists | Use for day-to-day work |
| `_workspace/pipelines/` | Repeatable staged workflows | Execute one stage at a time |
| `_workspace/artifacts/` | Documents others need after a run | Only declared or approved promotions on explicit finish |

Do not read every folder by default. Route first, then load the minimum needed context.
