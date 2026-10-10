# Shared working principles

## Context and authority

Start with AGENTS.md, the project profile and the repository's existing conventions.
Load only the documents relevant to the task. Cite paths when explaining decisions.
Distinguish the code's current behavior from intended behavior in specifications.
Accepted decisions and project conventions govern new work; existing code may be legacy.
Do not silently reconcile contradictory instructions. Surface the conflict.
Never turn rejected or superseded decisions into requirements.

## Scope and evidence

Understand the requested outcome and acceptance criteria before implementation.
Plan in proportion to uncertainty and impact. Small, clear changes need a short plan.
Work in small, independently verifiable increments. Avoid unrelated refactoring.
For behavioral changes, reproduce the symptom or establish an acceptance test first.
Preserve passing regression cases; do not demand that every test fail on the baseline.
Use the project's declared commands and working directories, not guessed commands.
Report what ran, what passed, what failed and what remains unverified.
A green suite is evidence about those tests, not proof of complete conformance.
Do not weaken tests, gates or requirements to make a result pass.

## Environment and delivery

Respect the repository's branch, commit, PR and deployment policies and the user's authorization.
Preserve uncommitted work. Keep generated files under their owning generator.
Verify isolation of databases, ports and containers when using worktrees.
Use focused local checks; run full suites when the project's policy calls for them.
Keep credentials and private data out of documentation, logs and commits.
Review changes and verification evidence before delivery.

## Durable learning

Record discoveries in their existing authoritative document, with evidence and date.
Document only the project's differences from the common base.
Store task state in a task-specific handoff, including pending checks and decisions.
Retire stale guidance rather than accumulating contradictory copies.
Measure useful delivery and human intervention; counts of tests or PRs alone are insufficient.
