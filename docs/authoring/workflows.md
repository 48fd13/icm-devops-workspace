# Authoring Workflows

A workflow is a one-pass procedure for recurring work that needs no review between steps: a Terraform review, a DNS/TLS review, a runbook draft.

## Shape

```markdown
# Terraform / OpenTofu Review Workflow

## Required context

- `_workspace/context/reference/iac-principles.md`
- `_workspace/context/reference/tool-notes/terraform-opentofu.md`

## Process

1. Identify backend/state/workspace/environment.
2. Review providers, modules, variables, secrets, outputs, and resource lifecycle.
3. Review plan or diff for create/update/delete/replace and blast radius.
4. Flag apply/destroy/import/state operations as approval-gated.

## Result

Produce a Terraform/OpenTofu review containing findings, blast radius, safety gates, validation gaps, and open questions.
```

- **Required context** names concrete files. Do not write "relevant docs".
- **Process** is a short numbered list. Mark any step that would mutate something as approval-gated; the gates themselves live in `AGENTS.md`.
- **Result** says what the workflow produces, not where to save it. A standalone run saves it under the run's `artifacts/`; a pipeline stage that reuses the workflow decides its own path.

## Adding one

1. Create `_workspace/workflows/<group>/<name>.md` in the group that fits: `development/`, `infrastructure/`, `ci-cd/`, `operations/`, or `knowledge-transfer/`.
2. Add an entry to the matching `_workspace/map/routes/<group>.md` with `Use when`, `Go to`, and `Context`.
3. If the workflow needs stable rules, put them in `_workspace/context/reference/` and name the file. Do not inline long rules into the workflow.
4. Run `python3 scripts/validate-kit.py`. It fails if a named path does not exist or a workflow is not reachable from any route file.

## When a pipeline reuses it

A pipeline stage may name a workflow in its `Inputs`. The stage then uses only the workflow's procedure and audit criteria. It does not start another run, and it writes where the stage says, not where a standalone run would. If the two disagree, the stage contract wins. Write workflows so they still make sense when used this way: no assumptions about which run or path they are in.

## Workspace additions

To add workspace-specific inputs or stricter rules to a shipped workflow without editing its steps, append an `## Additional instructions` section at the end of the file. The rules are the same as for pipelines; see [authoring pipelines](pipelines.md#additional-instructions).

## Workflow or pipeline?

Use a workflow when one pass is enough and a mistake is cheap to catch afterwards. Use a pipeline when a human should see an intermediate result, such as the discovery or the plan, before the next step builds on it.
