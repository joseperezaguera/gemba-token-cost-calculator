# Implementation, refactoring and cleanup

Follow the project's formatter, linter, type conventions and naming rules. Record
representative current examples by path; do not copy stale patterns unquestioningly.
Prefer explicit inputs, clear control flow and names from the project glossary.
Keep functions/modules cohesive and avoid unnecessary indirection or cleverness.
Comments explain non-obvious reasons and constraints; avoid narrating obvious code.
Use the defaults in patterns.md: one substantive class per file where applicable,
guard clauses over unnecessary else, expressive code over explanatory comments,
Object Calisthenics and Law of Demeter. Record exceptions in project conventions.
Do not weaken a stricter accepted local rule without an explicit decision.

Implement the requested capability without speculative frameworks or unrelated
refactoring. Prefer small changes with a clear reason. Separate behavior-preserving
cleanup from behavioral changes when that makes review and verification clearer.
Establish a green baseline before refactoring, and verify it afterwards.

For deletion, remove implementations and references together. Search for imports,
callers, registrations, scheduled work, configuration, tests and instrumentation.
Follow the chain to newly orphaned components; verify external consumers before
removing a public contract. Update affected docs and generated outputs through their
owning generator. Never remove tests merely because they expose a real regression.

Reuse dependencies deliberately: inspect maintenance, compatibility, scope and
operational cost. Document major choices in an ADR. Keep dependency versions and
lockfiles consistent with the repo's policy; avoid an implicit dependency upgrade
inside an unrelated feature.

## SOLID as design and review criteria

Apply these principles to the project's modules, functions and contracts; they do not
require classes or an interface for every implementation. Review real change pressures
and observable behavior, not compliance by counting classes or abstraction layers.

| Principle | Application | Review evidence |
|---|---|---|
| Single Responsibility | Keep a cohesive responsibility with a clear reason to change; separate business rules from serialization, persistence and delivery details. | A domain-rule change should not require editing unrelated transport/storage behavior. |
| Open/Closed | At established variation points, support new behavior through composition or a stable extension contract. Avoid speculative extension systems. | Adding a real variant should preserve existing variants and not duplicate selection logic throughout the code. |
| Liskov Substitution | Implementations honor their shared behavioral contract, including preconditions, results, errors and relevant side effects. Do not strengthen preconditions or weaken guarantees. | Run shared contract tests against substitutes; a fake and real adapter must not disagree on behavior clients rely on. |
| Interface Segregation | Expose cohesive contracts shaped by client needs. Do not force callers or implementations to depend on unrelated operations. | Callers should not require dummy methods, unsupported-operation failures or unused capabilities to use a relevant contract. |
| Dependency Inversion | Keep high-level policy independent of volatile implementation details through owned contracts and explicit composition. | Domain/application dependencies respect the declared boundary; external adapters can be replaced without moving business rules. |

Example: a checkout use case depends on a payment contract; provider adapters implement
it and share success/failure contract tests. The use case does not select providers,
parse HTTP responses or log credentials. Dependency injection alone does not establish
SOLID if the exposed contract still leaks provider internals.

## Clean Code as maintainability criteria

- Use intention-revealing domain names and consistent vocabulary. Replace ambiguous
  primitive values or boolean arguments with meaningful types/options when ambiguity matters.
- Keep one coherent level of abstraction within an operation. Extract meaningful domain
  steps instead of mixing workflow policy with parsing, SQL or transport mechanics.
- Keep functions and modules cohesive, with explicit inputs/results and limited nesting.
  Size is a diagnostic signal, not a universal line-count gate.
- Make mutation and side effects visible. A query should not unexpectedly write, send a
  message or change hidden global state. Do not hide substantial work in getters.
- Encapsulate state and protect invariants. Prefer composition to inheritance used merely
  for code reuse; choose inheritance when the behavioral substitution contract is valid.
- Remove duplicate knowledge: the same business rule should have an authoritative owner.
  Similar syntax alone is not a reason to merge concepts that evolve independently.
- Handle errors deliberately. Distinguish expected domain failures from technical failures;
  preserve useful diagnostic context, avoid silent catches and define cleanup of resources.
- Keep tests readable through clear setup/action/assertion and scenario names. Avoid
  fixtures or mocks that make the intended behavior difficult to understand.
- Remove dead code and misleading names/comments. Follow the project's style discipline
  and explain justified exceptions in its canonical conventions.

Review smells such as divergent changes, shotgun edits, feature envy, primitive obsession,
long parameter lists, deeply nested decisions, temporal coupling and speculative generality.
A smell prompts investigation, not an automatic rewrite. State the concrete maintenance
problem and make the smallest improvement within the authorized scope.

Example: replace calculate(value, true) with a named domain operation or explicit option
when the flag hides the meaning. Do not introduce a generic strategy registry for one
simple branch without a demonstrated variation need.

## Safe refactoring

Refactoring changes structure while preserving observable behavior. Record what must
remain unchanged: public contracts, outputs, errors, side effects and relevant timing,
ordering or performance guarantees. Deliberate changes to these are behavioral changes.

1. Establish the baseline with relevant checks. Reproduce unrelated failures and report
   them; do not describe a failing or unexecuted baseline as green.
2. For legacy code with inadequate tests, add characterization tests around affected
   observable behavior. Preserve evidence of existing behavior without treating a known
   bug as a desired permanent requirement; fix that bug as a separate behavioral change.
3. Choose a small transformation: rename, extract/move a responsibility, simplify control
   flow, introduce a seam or remove duplication. Explain the smell and expected benefit.
4. Run relevant checks after each coherent step. Preserve external behavior and verify
   architectural dependencies alongside tests when responsibilities move.
5. Separate structural cleanup and behavior changes into distinct reviewable steps or
   commits where practical. Do not combine a dependency upgrade or broad rewrite silently.
6. Complete the reference/registration/generated-output cleanup described above. Run the
   required broader checks, inspect the diff and record any remaining uncertainty.

When behavioral tests survive a restructuring unchanged, they provide stronger evidence
than replacing every test with tests coupled to the new implementation. Update tests
when their old coupling is incidental; retain their acceptance obligations. Avoid
unrequested cleanup campaigns and record broader follow-up separately.
