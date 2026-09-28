# Context Review Workflow

Use for re-checking `_workspace/context/project/` against reality. One pass, no stage review.

Facts here are loaded as authoritative constraints. Stale entries do not fail loudly — they produce confident wrong answers — so this workflow exists to catch drift before it compounds.

Run it periodically, or whenever a run discovers that a recorded fact is wrong.

1. List the files in `_workspace/context/project/` with their `**Last verified:**` dates, oldest first. Treat any file missing the line as the oldest.
2. Pick the oldest few. Do not review everything in one pass — a short, honest review beats a long, shallow one.
3. For each selected file, list the specific checkable claims it makes: versions, paths, names, counts, IP addresses, ownership, endpoints, and anything else that could have changed since the date.
4. Verify each claim against the current state of the target, using read-only inspection. Do not mutate anything to test a claim.
5. Classify each claim as confirmed, changed, or no longer applicable.
6. Apply the results:
   - Confirmed: leave the text as is.
   - Changed: correct the text in place so the old claim no longer stands.
   - No longer applicable: remove it, and note what replaced it if anything did.
7. Update `**Last verified:**` to today's date on every file reviewed — including files where nothing changed, since the date records verification and not modification.
8. Send anything you could not verify to `_workspace/backlog/items/` rather than leaving an unverified claim in place.
9. Summarize what was reviewed, what changed, and what remains unverified.

## Result

Produce a context-review summary listing reviewed files, corrected or confirmed facts, updated verification dates, and unresolved items.

Ask before correcting a fact when the right value is ambiguous. Record the open question instead of guessing.
