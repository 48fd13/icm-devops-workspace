# Stage 01: Classify

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_detect.md` | Reviewed drift list |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- run `input/` and earlier handoffs already consumed by the previous stage, unless the Inputs table names them
- unrelated provider/tool notes, environments, or repositories

## Process

1. For each difference, find who made it and why (audit logs, tickets, incident runs).
2. Classify it as intended (keep and codify), unintended (revert), or unknown (ask the owner).

## Audit

- Each item has a classification and evidence, or an open question with an owner.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/01_classify.md`.

## Gate

Stop for classification review.
