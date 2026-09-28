# Active Runs

Active runs plus finished runs awaiting explicit archive.

Folder name:

```text
YYYY-MM-DD-topic-slug/
```

Standalone task or workflow run shape:

```text
YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── artifacts/
└── final/
```

Pipeline run shape:

```text
YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── stages/
│   ├── 00_stage-name.md
│   └── 01_stage-name.md
├── artifacts/
└── final/
```

Use `artifacts/` for generated working artifacts in every run. Use `stages/` for formal pipeline handoffs.

Keep the run here through drafting and review. Explicit finish writes approved content under the run's `final/` and applies only the declared or approved promotions. Ask before archiving, moving, or deleting run folders.
