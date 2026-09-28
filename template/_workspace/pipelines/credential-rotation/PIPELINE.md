# Pipeline: Credential Rotation

Rotate a secret, token, key, certificate, or credential through controlled introduction, cutover, revocation, and verification.

## Routing

| Stage | Contract | Outcome |
|---|---|---|
| 00 Scope | `stages/00_scope/scope.md` | Rotation boundary and constraints |
| 01 Consumers | `stages/01_consumers/consumers.md` | Producer/consumer map |
| 02 Rotation plan | `stages/02_rotation_plan/rotation_plan.md` | Overlap, cutover, and rollback plan |
| 03 Introduce | `stages/03_introduce/introduce.md` | New credential introduction evidence |
| 04 Cutover | `stages/04_cutover/cutover.md` | Consumer cutover evidence |
| 05 Revoke | `stages/05_revoke/revoke.md` | Old credential revocation evidence |
| 06 Verify | `stages/06_verify/verify.md` | Rotation verification |
| 07 Finalize | `stages/07_finalize/finalize.md` | Sanitized rotation record |

## Layers

| Layer | Purpose | Location |
|---|---|---|
| Layer 0 | Workspace and secret-safety policy | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing | this file |
| Layer 2 | Active stage contract | `stages/<NN_name>/<name>.md` |
| Layer 3 | Secrets, access, rollback, and observability procedures | applicable `_workspace/workflows/` files |
| Layer 4 | Sanitized run inputs, handoffs, and evidence | `_workspace/runs/active/<run-slug>/` |

## Route boundary

Use when credential lifecycle and staged revocation are primary. Use a secrets-rotation workflow for one-pass planning/review; never store secret values in the run.

## Operating rules

- Never record secret values, private keys, tokens, or sensitive authentication material.
- Introduction, cutover, and revocation are separate exact-operation safety gates.
- Do not revoke the old credential before approved cutover evidence passes.
- Keep sanitized support material under run `artifacts/`; use `final/` only on explicit finish.
