# Change design, review and delivery

## Prepare and implement

Read relevant conventions and accepted decisions. Establish the outcome, acceptance
scenarios, dependencies, scope and risks. For uncertain or coordinated work, record
alternatives and a design before coding; use change-template.md or existing artifacts.
A workflow tool may organize these artifacts but does not determine their authority.

Use the project's branch policy and preserve unrelated local edits. Deliver small,
coherent increments that can be reviewed and verified independently. For a multi-step
change, show the current step's place in the whole and the remaining work. Avoid fixed
line/word quotas masquerading as universal quality rules.

## Compatibility and rollout

Inventory consumers before changing an API, event or schema. Identify additive versus
breaking changes, deployment order and the actual release cadence of each component.
Use expand/contract or parallel changes when uninterrupted compatibility needs it:
prepare compatible consumers before switching producers, verify, then remove legacy.
Do not impose flags on every small or purely additive change.

When a flag is used, record owner, default, rollout conditions, both-path tests and
cleanup step. When migrating data, record scope, dry-run checks, resumability,
backfill validation and recovery limitations. Do not edit generated artifacts by hand.
A schema/data migration may make rollback impossible: distinguish reverting code from
restoring data or recovering forward, and document the point of no return.

A rollout plan links each step to a detectable signal, verification, owner and gate.
Set observation windows and thresholds from the project's risk rather than copying
another system's durations. Retire temporary code, flags and metrics after verification.

## Review and completion

A PR/change summary explains the problem, resulting behavior, design decisions,
verification evidence and material risks. Link durable design docs instead of copying
them. Use the project's commit/title/attribution policy; no provider is hardcoded.

Review correctness, architecture, contracts, tests, security and delivery implications.
Automated/agent reviewers must cite actual code and applicable written requirements,
avoid speculative findings and distinguish advice from blocking checks. Keep review
proportionate; deterministic gates verify what can be automated.

A change is complete when its acceptance evidence and required gates are satisfied,
affected contracts/docs are updated and delivery obligations are explicit. Merge,
deployment and production acceptance are different events; do not conflate them.
