# Project engineering context — project-owned template

Copy/adapt into existing canonical project docs; do not edit this managed template.
Replace prompts with real paths and decisions. Mark inapplicable concerns with reasons.
This is a discovery aid, not a requirement to duplicate an existing documentation set.

## Purpose and behavior
- Users and capabilities; scope and quality constraints:
- Glossary, invariants and behavior-map links:
- Important acceptance scenarios and their test paths:

## Architecture
- Module/responsibility map and hard-to-find entrypoints:
- Allowed/forbidden dependency directions and their automated checks:
- State ownership, transaction boundaries and external contracts:
- Adopted patterns, applicability decisions, exceptions and verification (patterns.md):
- Accepted ADR index; legacy exceptions and intended evolution:

## Implementation and verification
- Naming/style conventions and representative current code examples:
- Test strategy, fixtures, focused/full-suite commands and CI policy:
- Setup, runtime, working directories, start/readiness/stop and isolation:
- Generated paths and regeneration commands:

## Delivery and operation
- Branch, commit, PR, attribution and required-check policies:
- Contract inventory and provider/consumer verification (contracts.md):
- Container build/runtime, CI checks and artifact promotion (delivery-profile-template.md):
- E2E platform coverage and shared-state restoration:
- Compatibility, migration, release and recovery policy:
- Observability, important budgets, owners and runbooks:
- Security boundaries, permission tests and automated checks:

## Evidence and maintenance
- Source/revision/date for facts; unresolved discrepancies:
- Owner and review trigger for each durable document:
- Applicability decisions and known verification gaps:
