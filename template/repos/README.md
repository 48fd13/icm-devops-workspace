# Repositories

Clone or link the repositories this workspace works on here, one folder per repository:

```text
repos/
├── network-infra/
├── platform-k8s/
└── checkout-service/
```

The workspace lives beside your code, never inside it, so no code repository needs to know about `AGENTS.md` or `_workspace/`. Each checkout keeps its own Git history; the workspace's `.gitignore` excludes everything here except this file.

Describe each repository in `_workspace/map/workspace-map.md` so routes and stages can name the right one.
