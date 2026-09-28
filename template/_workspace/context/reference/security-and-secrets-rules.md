# Security and Secrets Rules

- Never paste secrets, tokens, private keys, passwords, or live credentials into workspace files.
- Use placeholders such as `<SECRET_NAME>` or `<ACCOUNT_ID>`.
- Treat IAM, RBAC, KMS, secret storage, auth, network exposure, and CI/CD credentials as approval-gated.
- Prefer least privilege, short-lived credentials, clear ownership, and auditable access paths.
- For a secret, record only its name or logical reference, storage system, consumers, and rotation owner.
- If secret handling is unknown, flag it as an open question.
