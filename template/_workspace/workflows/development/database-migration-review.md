# Workflow: Database Migration Review

Use for schema migrations, data migrations, backfills, index changes, migration ordering, and application/database compatibility risks.

## Required context

- migration files and related application code
- target database/environment when known
- deployment order and rollback/fix-forward expectations
- data safety, backup, and maintenance-window notes when relevant

## Process

1. Identify migration type: schema, data, index, constraint, backfill, cleanup, or mixed.
2. Check compatibility with current and next application versions, including expand/contract sequencing.
3. Review locking, runtime, table size, batching, transaction behavior, and online/offline migration implications.
4. Check data-loss risk, irreversible operations, default values, nullable/non-null changes, and constraint validation timing.
5. Define validation: local migration test, dry run, schema diff, explain/analyze, staging test, or application compatibility checks.
6. Define rollback or fix-forward plan, including backup/restore assumptions and post-migration monitoring.

## Stop gates

Ask before running migrations, changing production/shared data, dropping/renaming columns/tables, destructive backfills, long-lock operations, or irreversible data operations.

## Result

Return:

- migration summary and type
- compatibility/risk assessment
- validation plan/results
- rollback/fix-forward notes
- blocking issues/questions
