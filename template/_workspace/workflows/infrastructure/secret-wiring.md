# Secret Wiring Workflow

## Required context

- `_workspace/context/reference/security-and-secrets-rules.md`
- `_workspace/context/reference/tool-notes/kubernetes.md`

## Process

1. List the secrets the service needs, by logical name only: purpose, consumer, environment, storage system, and owner.
2. Write the references for the workspace's mechanism (External Secrets `ExternalSecret`, Sealed Secrets, CSI driver, or CI secret references) and mount or inject them into the workload.
3. Never write, print, or commit secret values. Use placeholders, and note who creates each secret in the store.
4. Validate that the manifests render and that every reference has a named owner. Creating or rotating secret values is approval-gated and outside this workflow.

## Result

Produce the secret references and workload wiring, a table of required secrets and owners, and open questions.
