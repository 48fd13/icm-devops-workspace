# Stage 00: Release Scope

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/input/` | Release candidate, change summary, and supplied evidence |
| Layer 3 reference | `_workspace/workflows/ci-cd/release-readiness-review.md` | Scope procedure |

## Do NOT load

- later stage folders
- `_workspace/workflows/` files not named in the Inputs table
- unrelated provider/tool notes, environments, or repositories

## Process

1. Fix artifact/version, target environments, owners, dependencies, intended impact, exclusions, and desired evidence.
2. Flag an ambiguous or mutable candidate identity.

## Audit

- Candidate and target are immutable or exactly identified.
- Scope and non-goals are explicit.

## Artifacts

Write `_workspace/runs/active/<run-slug>/stages/00_release_scope.md`.

## Gate

Stop for release-scope review.
