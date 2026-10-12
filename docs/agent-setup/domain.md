# Domain language, invariants and behavior maps

Maintain a small glossary of concepts that affect implementation. Name code,
contracts and tests consistently; record distinct meanings rather than overloading
one term. The project decides the language and naming conventions.

For each important capability, locate its entrypoint, inputs, preconditions, rules,
state changes, side effects and observable outcomes. Include failure and permission
paths. A compact table or diagram is sufficient; use the existing canonical source.

Write invariants as conditions that can be verified. For stateful behavior, describe
allowed transitions, terminal states, ownership and concurrency constraints. Link
rules to enforcing code and tests. Distinguish present behavior from proposed changes.
An intended workflow is not evidence that it is implemented.

Use DDD concepts when the problem warrants them. For projects without business
domains, document equivalent contracts: library APIs, CLI behavior, pipeline data
invariants or user interactions. Do not invent aggregates or bounded contexts to
satisfy a template.
