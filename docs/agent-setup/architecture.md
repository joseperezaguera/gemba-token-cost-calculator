# Architecture and dependency boundaries

Read patterns.md for the preferred domain-application profile and explicit checks
for DDD, hexagonal architecture, CQRS, repositories, buses, outbox, event sourcing
and microservices. Record the project's adoption and exceptions in its conventions.

## Required engineering outcomes

Maintain a map of responsibilities, entrypoints, public interfaces, dependency
direction and state ownership. A contributor must know where a change belongs and
which dependencies are forbidden. Document the architecture actually in use and
its intended evolution separately. Existing code can contain legacy exceptions.

Choose the simplest structure that meets the problem. Cohesive modules, explicit
interfaces and controlled coupling matter at every scale. Hexagonal architecture,
DDD, layered architecture and command/query separation are project decisions,
not universal directory layouts imposed by this setup.

Keep business decisions separate from transport and persistence details when that
separation is useful. Introduce interfaces at meaningful external or volatile
boundaries; do not add abstractions without a concrete need. Compose dependencies
at explicit entrypoints. Avoid hidden global state and circular module dependencies.

For each important boundary, record caller, owner, input/output/error contract,
compatibility expectations and verification. Across services or contexts, prefer
explicit contracts over importing another component's internal implementation.
Document shared-kernel ownership and permitted dependencies instead of letting a
shared module become an unrestricted collection of unrelated code.

## Data and side effects

Define transaction boundaries and consistency invariants before changing writes.
Where aggregates are used, preserve their invariants as a unit. Document how
persistence and emitted events remain consistent; an outbox is one possible choice,
not a requirement for every project. Specify failure, duplication and ordering
semantics for asynchronous work. Do not assume exactly-once delivery.

Use explicit seams for time, randomness and external services where determinism
or failure simulation is needed. Keep domain concepts distinct from database and
API representations when their lifecycles or rules differ.

Apply SOLID contract and dependency criteria from code-style.md when designing or
reviewing these boundaries; class counts and injection frameworks are not evidence.

## Verification

Enforce important dependency rules with the project's appropriate checker in CI.
The language-specific checker is an adapter to the shared policy. Record justified
exceptions with owner, rationale and review/removal condition; identify obsolete
exceptions. A prose rule or an agent review is not equivalent to an automated gate.
Check contracts and representative integration behavior alongside dependency rules.

Before a structural change, identify affected boundaries and accepted ADRs. Review
whether it increases coupling, splits an invariant, duplicates ownership or adds
operational complexity. Record meaningful trade-offs in an ADR.
