# Stage 06: Source cleanup

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/05_cutover.md` | Cutover outcome |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. After the agreed stability window, request approval to remove the source, or hand removal to `service-decommission`.
2. Remove only what is approved.

## Audit

- The stability window passed before removal.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/06_source_cleanup.md`.

## Gate

Stop after cleanup for review.
