# Safety and Lifecycle

`template/AGENTS.md` is the only enforceable source for both topics. This page explains it; it does not add rules. If they ever disagree, `AGENTS.md` is right and this page is wrong.

## Safety gates

`AGENTS.md` has two sections:

- **`Safety gates`**: general gates that apply in any workspace. Destructive or irreversible operations, installs and dependency changes, external mutations, push/publish/deploy/release, shared infrastructure, secrets/auth/security, billing, external contract breaks, irreversible data operations, and machine-wide configuration.
- **`Additional safety gates`**: DevOps-specific gates. Terraform/OpenTofu apply, destroy, import, and state changes; Kubernetes and Helm mutations; cloud resource mutations; IAM, auth, and secrets; DNS, TLS, and network; CI/CD deployment gates; production and shared environments; billing and cost.

A gate means the agent stops and asks before acting. It applies in every process, including a direct answer that turns into an action.

How the processes reinforce the gates:

- Discovery and planning stages are read-only, and their audits check that nothing was changed.
- Entering an execution stage (deploy, stabilize, execute) is not approval. The approval must name the exact operation, candidate, and target.
- Incident urgency does not bypass a gate. `incident-response` stops for approval of the exact mitigation.
- Secrets and credentials are never written into prompts, context, runs, artifacts, or examples.

To tighten the gates for your organization, add to `## Additional safety gates` in your workspace's `AGENTS.md`. Do not loosen the general section.

## Run lifecycle

| Transition | Happens when | Result |
|---|---|---|
| Open | A routed request needs more than a direct answer | `_workspace/runs/active/<YYYY-MM-DD>-<slug>/` with `RUN.md` written before the work |
| Work | Each workflow pass or pipeline stage | Material in `input/`, `stages/`, `artifacts/`; `RUN.md` kept current |
| Review | After every pipeline stage, and after a workflow's result | You read and edit; your edits are authoritative |
| Finish | Only when you explicitly say the run is finished | See below |
| Archive | Only on a separate explicit instruction | The run moves to `_workspace/runs/archive/` |

On finish the agent:

1. writes the approved content to the run's `final/`; the run itself is the record;
2. applies only the promotions the process declares, which a pipeline's finalize stage lists under `## Promotion`. A standalone task or workflow declares none, so the agent asks whether anything should be promoted;
3. uses these destinations for promotions: `_workspace/artifacts/<family>/` for documents others need after the run, `_workspace/context/project/` for reviewed stable facts with a `Last verified` date and `_workspace/backlog/items/` for deferred follow-ups and risks;
4. records the promoted paths in `RUN.md`, or `None`;
5. sets `Finished:` in the `RUN.md` metadata.

A finished run stays in `active/` until you archive it, so it is easy to find while its results are still fresh.

## `RUN.md`

Copy `_workspace/runs/run-template.md`. It records the process type, start and finish dates, route, request, assumptions, plan, current step, expected artifacts, open questions, promoted artifact paths, and notes. The agent updates it before substantive work, so the file always says what is happening and why.
