# Architecture and development pattern catalog

## Policy and applicability

These practices are part of the engineering foundation, not omitted because they
require architectural judgment. Use them as the reference repertoire for design,
implementation and review. A project records adopted defaults, applicable conditions,
exceptions and evidence in its canonical conventions and accepted ADRs.

For domain-oriented applications, the preferred starting point is DDD with explicit
hexagonal boundaries, command/query separation, repositories at persistence boundaries
and outside-in TDD. Preserve a brownfield project's accepted architecture; changing
it requires an explicit migration decision, not an opportunistic rewrite.
For small libraries, scripts or different programming paradigms, record adaptations.

Microservices, event sourcing and outbox have explicit design checkpoints below.
Evaluate and record their applicability; inclusion in the catalog is not an instruction
to introduce distribution or an event store into every project. Existing adopted
patterns must be followed. Exceptions to project defaults must be justified.

## Domain modeling and hexagonal architecture

DDD: use ubiquitous language and bounded contexts to distinguish concepts and ownership.
Model entities by identity and value objects by meaning, equality and validated values.
Favor immutable value objects. Aggregates protect consistency invariants; repositories
persist the aggregate as a unit rather than bypassing it to mutate internal elements.
Test invalid values and transitions, identity/equality and invariants under concurrency.
Avoid forcing an entity/aggregate model onto work without domain complexity.

Hexagonal architecture: keep domain rules independent of frameworks, storage and
transport. Application use cases orchestrate domain behavior through ports; adapters
implement external interactions. Infrastructure must not leak into domain/application
imports. Put dependency composition at explicit entrypoints. Verify boundaries with
the language's checker and behavior with adapter/contract tests. Identify legacy exceptions.

Actions/application services: express one coherent use case, with explicit parameter
and result types. Prefer immutable inputs and clear errors. Controllers/handlers translate
transport inputs and invoke use cases; do not duplicate business rules in views.
Use cases must not become an unrestricted home for logic that belongs to the domain.

Repository pattern: expose domain-oriented operations, hide persistence mechanics and
respect transactional ownership. Define concurrency and failure semantics. Verify the
real adapter contract; an in-memory fake is not evidence that database behavior matches.

Collections: encapsulate domain operations when a collection has rules of its own.
Avoid exposing mutable internals that let callers bypass invariants. Record ordering,
uniqueness and equality semantics; do not impose one language's dict/list representation.

Identity, time and audit: choose identifiers with documented generation and ordering
properties. Keep identity separate from incidental database representation. Use an
injectable clock where time affects behavior. Record who/what/when for business audit
when required; a timestamp or operational log alone is not an equivalent audit trail.
Test time boundaries and actor attribution; UUID version selection is a project decision.

## Commands, queries, buses and events

CQRS: separate state-changing commands from read-only queries in responsibilities and
interfaces. A shared database is compatible with this separation. Separate read models
or stores when justified, documenting staleness and projection rebuilding. Verify that
queries do not accidentally mutate state and that projections meet their stated contract.

Buses: give commands, queries and events explicit routing, registration and failure
semantics. A bus can be in-process; it is not automatically a broker or microservice.
Test handler declarations/registration and dispatch behavior. Keep cross-context
collaboration behind the accepted contract instead of importing internal implementations.

Domain events: name completed facts in the past tense and define when they occur.
Distinguish a request/command from a fact/event. Decide event granularity, ownership,
payload/versioning, correlation and publication timing. Instrument handlers. Define
retries, duplicate handling, ordering and dead-letter recovery for asynchronous delivery.
Retire consumers through active -> draining -> inactive -> removal where applicable;
verify queued work and external callers before deletion.

Outbox: when a committed write must reliably produce a message, evaluate a transactional
outbox or another explicit consistency mechanism. Persist business change and pending
publication atomically, then relay with retries; consumers still need duplicate handling.
Test failures before/after commit and publication, relay recovery and retention cleanup.
Record ordering and latency guarantees. A direct publish after commit leaves a failure
window unless another mechanism closes it.

Event sourcing: evaluate where reconstructable history and domain transitions justify
making the event stream authoritative. Distinguish it from publishing events or keeping
an audit log. Define stream identity, append concurrency, event evolution, replay,
projections and any snapshot policy. Verify reconstruction and concurrent writes;
prevent replay from repeating external effects. Record retention/privacy requirements,
recovery and operational cost in an ADR before adopting it.

Microservices: evaluate independent ownership, deployment and scaling against the cost
of distributed contracts and operations. Define service boundaries, data ownership,
compatibility and failure isolation. Test remote contracts, partial failure and coordinated
rollout. Explain distributed consistency, observability and recovery. A modular monolith
is a valid alternative to compare in the ADR; deployment count is not a quality metric.

## Development discipline and code design

Read code-style.md for the detailed SOLID, Clean Code and safe-refactoring criteria,
and testing.md for the complete red/green/refactor cycle and test-quality criteria.

Outside-in TDD: start with observable acceptance behavior, discover use cases and ports
from that scenario, implement in small red -> green -> refactor steps. Test one new
behavior at a time; keep prior regressions green. Use focused unit/property tests to
exercise complex rules and integration tests for real adapters. Manual evidence must
be explicit when automated reproduction is infeasible.

Builders and Object Mothers: use builders for controlled variation and mothers for
named valid scenarios. Keep relevant values visible, avoid magical defaults and ensure
fixtures satisfy unrelated domain rules. Assertions must not derive expected results
by repeating the implementation. Validate real-reference fixtures without private data.

Object calisthenics and Law of Demeter: favor small cohesive units, limited nesting,
encapsulated collections and meaningful types over primitive ambiguity. Avoid reaching
through an object's collaborators to manipulate their internals; ask the responsible
object to perform the operation. Fluent APIs are not automatically Demeter violations.
Use the discipline to expose misplaced responsibilities, not to add wrappers mechanically.

One class per file: default to one substantive class per file when the language supports
it, with project naming/location tables. Declare exceptions for closely related value
types, events, errors, schemas or language conventions. Verify navigation and cohesion,
not merely class counts. This reflects source practice without discarding its exceptions.

Avoid else and explanatory comments by default: prefer guard clauses, small methods,
meaningful names and explicit types. Refactor comments that merely narrate business
steps into expressive code. Preserve essential rationale, protocol constraints and
safety explanations when code alone cannot express them. Projects may adopt a stricter
no-else/no-comment convention explicitly; do not silently relax an accepted local rule.

Tidy First / XP / YAGNI: establish a green baseline for structural cleanup, keep cleanup
and behavior changes separately reviewable, favor small feedback cycles and simple
design, and avoid speculative features. Follow deleted symbols through callers,
registrations, schedules and instrumentation so orphaned behavior is removed completely.

## Compatible evolution and review

Parallel Changes: retain the legacy contract while introducing the new path, verify
both paths and shared invariants, activate using defined rollout evidence, then remove
only the legacy belonging to that change. Flags need owner, default and cleanup step.
Schema/API/event changes need compatible deployment order and recovery limits.

Strategy diagrams: for multi-increment changes, show trigger, decision/old-new behavior,
unchanged invariants, delivery order and cleanup. Link the diagram in each PR so a reviewer
can place the current increment in the whole. Choose a format readable in the project;
ASCII is useful where terminal/plain-text reading matters.

Conventional Commits and concise PRs: use the project's declared title/commit policy,
particularly when squash titles become history. Make purpose, scope, acceptance evidence,
risks and rollout understandable. Document attribution without hardcoding an agent vendor.

Review lenses: separate architecture/conventions/testing/security concerns, ground each
finding in changed code and an applicable requirement, and propose an actionable correction.
A second filtering pass can reduce noise. Evaluate automated reviewers against known
findings before trusting them; absence of findings is not an approval or proof of safety.
