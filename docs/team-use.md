# Using the Kit as a Team

This is a usage pattern, not built-in tooling. The template works the same for one person or ten; what changes is how a team shares the files around it. Because everything is plain Markdown in a Git repository, the usual engineering practices of pull requests, review, and versioning are enough.

## What is shared and what is private

| Part | Contents | Shared? |
|---|---|---|
| Kit | `AGENTS.md`, `_workspace/map/`, `workflows/`, `pipelines/`, `context/reference/` | Yes. Everyone's agent follows the same rules and processes. |
| Team knowledge | `_workspace/artifacts/`, `context/project/`, `backlog/` | Yes. What finished runs promote for others to use. |
| Runs | `_workspace/runs/active/`, `_workspace/runs/archive/` | No. Each operator's runs stay on their own machine. |

A practical setup is one team repository holding the initialized workspace, with `_workspace/runs/` added to its `.gitignore` next to the `repos/` entry it already has. Code repositories are cloned under `repos/` and keep their own history. Each operator clones it, works with their own agent, and contributes back through pull requests.

## Runs stay private

Runs hold raw working material: pasted logs, command output, draft reasoning, and sometimes sensitive detail. Keeping them out of the shared repository avoids leaking that material and avoids conflicts between operators.

A run is still a self-contained folder, and that makes sharing one simple when it is useful. To show a teammate how a difficult task went, or to hand work over, copy the run folder and pass it on. Its `RUN.md` states the request, assumptions, and plan, and its `stages/` handoffs show each step and each review decision in order. That is usually more useful than a chat transcript. Remove secrets and sensitive output before sharing.

## Contributing knowledge day to day

When a run finishes, its pipeline declares what gets promoted: a change packet, an incident note, a corrected procedure, verified environment facts, backlog items. Those promotions become small pull requests to the team repository.

- Review them like any documentation change.
- Give each file in `context/project/` an owner as well as its `Last verified` date. With several authors, stale facts are the main risk, and the `context-review` workflow is how they get re-checked.

Because promotion is declared rather than automatic, the shared space holds what others need instead of a copy of every run.

## A shared knowledge base for the team

Over time, `context/project/` and `_workspace/artifacts/` become a Markdown knowledge base about your systems that every agent reads, similar in spirit to the LLM-maintained wikis popularized by Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) note. The difference matters once several people work on it. When an agent continuously rewrites shared pages, every contributor produces broad, overlapping diffs that are hard to review and merge. Here the churn stays in each operator's private runs, and the shared repository only receives what a finished run declares: a few dated files or a corrected fact, as a small pull request that one person can review. Two operators rarely touch the same file, and every change to shared knowledge has a run behind it that explains where it came from.

## Evolving the kit on a cadence

New workflows, new pipelines, and changed rules affect how every operator's agent behaves, so they deserve more review than knowledge updates.

1. An operator adds or changes a workflow or pipeline in their own copy and uses it.
2. When it has proved itself, they open a pull request against the team kit.
3. The team reviews kit changes together on a regular cadence, for example monthly, and accepts, revises, or rejects them.
4. Accepted changes are released with a version bump and a `CHANGELOG.md` entry, and operators pull the new version.

Changes to safety gates in `AGENTS.md` should need an explicit approver, for example through `CODEOWNERS`. Keep organization-specific gates in `## Additional safety gates` so the general gates stay stable.

The same pattern applies to shipped workflows and pipelines. Keep them identical across workspaces, and put anything workspace-specific in an `## Additional instructions` section at the end of the file (see [authoring pipelines](authoring/pipelines.md#additional-instructions)). Additional instructions can add inputs and stricter rules but never relax the shipped contract, and the rest of the file can be updated to a new kit version without losing them. Instructions that keep recurring across workspaces are good candidates for the next kit review.

## Things to watch

- **Stale shared facts.** Owners, `Last verified` dates, and periodic `context-review` runs.
- **Routing conflicts.** The top-level routing table is a single file. Put new workflows in the per-domain route files to keep edits small.
- **Secrets.** Runs stay out of Git, and shared runs are cleaned first. The kit's rule applies everywhere: no secrets or credentials in prompts, context, runs, or artifacts.
