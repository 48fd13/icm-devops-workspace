# Project Context

Reviewed, stable project reference that future work can rely on.

Examples:

- project summary
- architecture notes
- tooling map
- environment map
- service inventory
- dependency map
- validation map

Use `_workspace/backlog/items/` for unresolved questions, deferred follow-ups, risks to revisit, and next actions.

## Verification

Every file here starts with a verification line:

```markdown
**Last verified:** YYYY-MM-DD
```

Set it when the fact is first promoted, and update it whenever the fact is re-checked against reality. Facts here are loaded as authoritative, so a stale entry does not fail loudly — it quietly produces confident wrong answers.

Re-check the oldest entries periodically with `_workspace/workflows/context-review.md`. When a fact is superseded, correct it in place and bump the date; do not leave the old claim standing.
