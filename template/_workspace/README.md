---
kind: workspace
template: devops
kit_version: 0.1.0
initialized:
---

# Cloud DevOps Workspace

Advanced all-in-one DevOps/cloud workspace.

`initialized` is stamped by `init-workspace.py`; set it by hand only if this workspace was created another way. Update `kit_version` only when intentionally aligning it with a kit release.

- `map/`: routing, naming, and workspace map
- `context/reference/`: template-provided DevOps/cloud principles plus provider/tool notes
- `context/project/`: project-specific context discovered after initialization
- `workflows/`: reusable one-pass procedures that can run standalone or support a pipeline stage
- `pipelines/`: repeatable staged processes for discovery, changes, rollouts, migrations, recovery, incidents, security, readiness, and optimization
- `backlog/`: deferred follow-ups, operational risks, and open action items
- `runs/`: standalone task, workflow, and pipeline run state
- `artifacts/`: promoted documents others need after a run, such as change packets and incident notes

Keep this workspace stack agnostic. Load provider/tool notes only when relevant to the active task.
