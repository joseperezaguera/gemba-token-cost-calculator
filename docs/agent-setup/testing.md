# Behavior and verification

## Acceptance before implementation

Describe the observable outcome and important failure cases. For a behavior change,
write a failing acceptance/regression test and confirm it fails for the expected
reason before implementing the change, where automated reproduction is feasible.
For a bug, reproduce the symptom and investigate the root cause before patching.
If automation is impractical, record the reason and an explicit manual procedure.

Work in short test/implementation/refactor cycles. Keep existing green regressions
green: only the scenario requiring new behavior is expected to fail initially.
Use outside-in tests when an external interface expresses the requirement; use focused
unit tests for complex pure rules and invariants. Choose test layers by failure risk,
not a blanket instruction to test every private method or every layer identically.

## TDD cycle and test design

Start with a short test list derived from acceptance scenarios and relevant risks.
Select one behavior, then iterate:

1. Red: add the smallest test expressing the requirement. Run it and inspect the failure.
   A timeout, broken fixture, missing dependency or unrelated exception is not evidence
   that the intended behavior was tested. Resolve incidental failures first.
2. Green: implement the simplest sufficient behavior. Run the new test and affected
   regressions. Avoid adding untested generality or changing expected results to fit code.
3. Refactor: improve design with the suite green. Preserve behavior, keep steps small and
   follow the safe-refactoring procedure in code-style.md. Refactoring is part of the cycle.

For outside-in work, begin at the externally observable boundary and discover supporting
use cases/ports from the scenario. Supplement with focused tests of complex rules and
real adapter contracts. Do not force a mock for every collaborator or couple all tests
to private call sequences. Existing-code characterization precedes risky refactoring;
new behavior needs a test expressing its intended contract.

Tests must be independent, repeatable, order-independent and explicit about failures.
Use isolated state and controlled time/randomness. Parameterize cases when it clarifies
shared behavior; keep distinct rules discoverable. Treat flaky tests as defects: diagnose
and fix the source, or document a bounded quarantine with owner and replacement evidence.
A rerun that happens to pass does not resolve flakiness.

Use boundaries and error cases from the test list, not only the happy path. Verify test
sensitivity with the observed red phase; for important risks, mutation or a controlled
fault can add evidence that the assertion catches the intended defect. Keep checks free
of undeclared network/model dependencies and report integration prerequisites explicitly.
Coverage identifies unexercised areas; it does not prove meaningful assertions or replace
acceptance, contract and invariant checks.

## Evidence that can detect a defect

Assertions describe independently determined expected behavior, not values computed
by repeating the implementation. Prefer observable results to mock call counts unless
the interaction is the contract. Test real adapters and serialization at integration
boundaries. Mocks do not prove compatibility with an external service.

Cover relevant boundaries: invalid inputs, denied access, empty data, time limits,
partial failure, duplicate/reordered messages, concurrency and rollback. When flags
or parallel implementations are used, verify both old and new behavior and shared
invariants. Include a small set of important end-to-end journeys where applicable.

Keep fixtures minimal, explicit, valid for domain rules and free of private production
data. Prefer builders/mothers for repeated domain fixtures, following patterns.md; avoid
defaults that hide the condition under test. Control time, randomness, databases, ports and containers for reproducibility.

Map acceptance scenarios to test paths and report gaps. A behavior-map document without
executable tests is documentation, not a regression safety net. Use mutation testing,
contract tests or independently curated cases where the risk justifies their cost.

## Execution and reporting

Declare exact commands, working directory, setup and dependencies in project docs.
Run focused checks during iteration and required suites before delivery, locally or
in CI according to the project policy. Confirm the tested checkout and environment.
Record command, revision, result and any skipped or unavailable checks. Do not label
an unexecuted check as passing, weaken assertions to obtain green, or infer complete
correctness from coverage or test counts.

For a pure refactor, establish a green baseline and preserve behavior afterwards.
For documentation/configuration changes, use relevant validation rather than writing
artificial tests that merely duplicate the edited text.

## Integration precision

For relevant entrypoints, verify at least a representative successful path through the
real owned adapters and serialization; add failure paths according to risk. Mock external
boundaries instead of replacing the entire use case and calling that integration.

For repository/query tests, use a real database and distractor rows that must not match
(e.g. another account, status or time interval). Verify filtering, ordering and scope.
After writes, reload persisted state through a fresh read/session where needed so an
in-memory object cannot conceal a missing write. Assert relevant complete payloads and
exact interaction counts when those interactions are the contract. Avoid wildcard inputs
that make impossible values pass; use strict signature/spec checks for test doubles.

See contracts.md for shared real/fake and consumer/provider verification, and e2e.md
for multi-platform preparation, shared-state coordination and restoration after failures.
