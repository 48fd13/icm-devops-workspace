# Getting Started

## 1. Initialize a workspace

The workspace is its own folder, and your code lives under it in `repos/`, even for a single project. Code repositories never contain the workspace, so nobody has to add `AGENTS.md` or `_workspace/` to a project's `.gitignore`.

```sh
mkdir -p ~/ops-workspace
python3 scripts/init-workspace.py ~/ops-workspace
git clone <your-infra-repo> ~/ops-workspace/repos/network-infra
```

This copies `template/` into the target:

```text
ops-workspace/
├── AGENTS.md        behavior, run lifecycle, and safety gates
├── repos/           one checkout per repository (excluded from the workspace's Git)
└── _workspace/
    ├── map/         routing table, route files, workspace map, naming
    ├── workflows/   one-pass procedures
    ├── pipelines/   staged processes
    ├── context/     reference/ (shipped) and project/ (learned, reviewed)
    ├── runs/        active/ and archive/ work sessions
    ├── artifacts/   durable results promoted on finish
    └── backlog/     deferred follow-ups and risks
```

Existing files are left untouched unless you pass `--overwrite`. The script does not initialize Git or register the workspace anywhere.

## 2. Adapt it to your environment

Three edits are worth making before the first real request:

1. **`AGENTS.md` → `## Additional safety gates`.** Add anything specific to your organization, such as a change-freeze window or a production account that needs a second approver.
2. **`_workspace/map/workspace-map.md`.** List each repository under `repos/` and what it contains.
3. **`_workspace/context/project/`.** Optional on day one. The `onboarding-map` pipeline produces reviewed facts to put here.

If your agent does not read `AGENTS.md` automatically, tell it to at the start of a session: "Read AGENTS.md and follow it."

## 3. Make a first request

Ask in plain language. You do not need to name a process.

| You say | The agent picks |
|---|---|
| "What does this module's `lifecycle` block do?" | Direct answer; no run |
| "Review the Terraform change in `repos/network-infra/`" | Terraform/OpenTofu review workflow |
| "Plan moving the RDS instance to a new subnet group" | `infrastructure-change` pipeline |
| "Checkout is returning 5xx since 14:10" | `incident-response` pipeline |

For anything beyond a direct answer, the agent creates `_workspace/runs/active/<YYYY-MM-DD>-<slug>/`, writes `RUN.md` with the plan, and then works. In a pipeline it completes one stage, writes the handoff to the run's `stages/`, and stops.

## 4. Review, edit, continue

Open the handoff or artifact, edit it if it is wrong, and tell the agent to continue. Your edits are authoritative input to the next stage.

When the work is done, say so explicitly ("finish the run"). The agent writes the approved result to `final/` and applies only the promotions the process declares, for example a change packet to `_workspace/artifacts/` or follow-ups to the backlog. For a standalone workflow it asks you first. The run stays in `active/` until you ask to archive it.

Working with a team? See [Using the kit as a team](team-use.md) for what to share, what to keep private, and how to evolve the kit together.

## 5. Check your changes to the kit

If you extend the kit itself, run the validator before sharing it:

```sh
python3 scripts/validate-kit.py
```
