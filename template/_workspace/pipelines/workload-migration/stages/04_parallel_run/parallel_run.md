# Stage 04: Parallel run

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/03_prepare_target.md` | Prepared target |
| Layer 3 reference | `_workspace/context/reference/validation-evidence.md` | Evidence rules |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. With approval, deploy to the target without production traffic.
2. Validate function, performance, and observability against the source.

## Audit

- The target served no production traffic.
- Comparison evidence is recorded.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/04_parallel_run.md`.

## Gate

Stop after the parallel run for review.
