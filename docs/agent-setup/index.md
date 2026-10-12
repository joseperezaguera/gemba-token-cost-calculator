# Engineering guide index

This is the shared engineering standard. It has no workflow-framework dependency.
Agent Skills is the official development workflow; read [workflow.md](workflow.md)
for lifecycle, host adoption and verification limits.
Read principles first, then the relevant topics. Project-owned documents supply the
actual paths, examples, commands and accepted choices; do not manufacture them.
Use existing authoritative documents rather than creating a competing copy.

| When changing or reviewing | Read | Project evidence to locate |
|---|---|---|
| Choosing or applying architecture/development patterns | patterns.md | Adopted patterns, applicability decisions, exceptions and evidence |
| Public interfaces and adapter/provider compatibility | contracts.md | Contract inventory, consumer/provider versions and verification |
| Container build/runtime or isolation | containers.md | Build inputs, final-image tests, readiness and shutdown |
| Pipeline checks and required merge gates | ci.md | Actual commands, required jobs and branch protection evidence |
| Artifact publication, promotion or recovery | cd.md | Immutable artifact, compatibility, rollout and recovery evidence |
| Critical journeys or shared test state | e2e.md | Fixtures, single-writer ownership and restoration |
| Modules, dependencies, persistence, integrations | architecture.md | Module map, boundaries, contracts, accepted ADRs |
| Significant trade-offs or exceptions | decisions.md | ADR index and decisions applicable to changed paths |
| Behavior, bugs, tests or fixtures | testing.md | Acceptance scenarios, test locations, verification commands |
| SOLID, Clean Code, implementation or refactoring | code-style.md | Formatter, lint/type settings, representative current examples |
| Business rules or state transitions | domain.md | Glossary, invariants, behavior map |
| Branches, PRs, releases or migrations | delivery.md | Delivery policy, compatibility and rollout plan |
| Runtime, diagnostics or performance | operations.md | Environment lifecycle, dashboards, runbooks, budgets |
| External inputs, permissions or sensitive data | security.md | Trust boundaries, access policy, automated checks |

Templates are starting points, not extra canonical sources:
- project-context-template.md: copy to a project-owned document or fill existing conventions.
- adr-template.md: copy into the project's ADR directory for a real decision.
- change-template.md: use for changes with meaningful uncertainty or coordinated delivery.
- review-template.md: use for proportional review and completion evidence.
- contract-template.md: copy into the existing contract directory for a concrete interface.
- delivery-profile-template.md: connect checks, containers and release policy to actual commands.
- task.md: use for task-specific session handoffs.

A small library may need a compact project document. A distributed service may need
separate contracts and runbooks. Scale documentation to risk; do not create empty
folders. Use patterns.md explicitly to select and apply practices; record architectural
choices instead of omitting patterns that require judgment.
