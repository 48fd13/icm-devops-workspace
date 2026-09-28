# Stage 01: Inventory

## Inputs

| Layer | Path | Use |
|---|---|---|
| Layer 4 working | `_workspace/runs/active/<run-slug>/stages/00_intake.md` | Reviewed scope |
| Layer 3 reference | `_workspace/context/reference/discovery-checklist.md` | Read-only discovery and inventory checklist |

## Do NOT load

- later stage folders
- raw active run input unless intake is insufficient

## Process

1. Inventory services, environments, repos, cloud accounts/projects, IaC, CI/CD, observability, owners, and open questions.
2. Separate known facts from assumptions.

## Audit

Run these checks before saving the stage handoff. If any fail, fix before writing the artifact.

| Check | Pass condition |
|---|---|
| Facts vs assumptions | Known facts and assumptions are listed separately |
| Inventory complete | Services, environments, repos, accounts, IaC, CI/CD, observability, and owners are each covered or marked unknown |

## Artifacts

Write `01_inventory.md` to `_workspace/runs/active/<run-slug>/stages/`.

## Review gate

Stop for review before relationships.
