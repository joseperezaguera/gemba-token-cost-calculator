# Continuous integration

## Project-owned verification interface

Declare meaningful commands and working directories for applicable format/style, types,
architecture, unit/integration tests, contracts, build and security checks. Commands can
be scripts or any build system; the engineering contract does not prescribe a language.
Use delivery-profile-template.md to record commands, prerequisites, required jobs and
inapplicable checks with reasons. No-op commands are not compliance evidence.

Run checks on the actual PR revision and preserve logs/results. Expensive suites can run
in parallel or only in CI according to project policy, but a required gate must not turn
green because a path filter, empty file list or missing input skipped all relevant work.
Caches improve speed; a cache key must reflect runtime and dependency locks, and cached
outputs must not bypass required verification.

Automate important dependency rules and declared exceptions. Run integration tests with
real owned adapters/databases, controlled external dependencies and isolated state.
Contract verification must test provider code rather than only generated mocks.
Use testing.md for precise assertions, strict test doubles and persisted-state checks.

For buildable projects, build the deliverable and test its runtime/package behavior.
Record checks, commit, artifact identity and environment; test counts alone do not show
acceptance. Publish reports even on failures where possible and make job failures visible.

## Gates and execution permissions

List required checks in branch protection/rulesets and verify they are actually configured.
A workflow file alone does not enforce merge policy. Decide review and exception rules
explicitly; do not bypass them or weaken tests to merge. Keep agent review distinct from
deterministic checks and evaluate it before making it blocking.

Use least-privilege pipeline access, pinned reviewed actions/workflows and short-lived
credentials when supported. Untrusted PR code must not run with deployment credentials.
Build secret handling and dependency/image scanning follow the project's security policy.
Declare scanner scope/threshold and evidence; absence of a scanner is a pending check.

## Reuse and portability

Keep shared mechanics versioned, with explicit inputs, while project commands and policies
remain local. GitHub Actions reusable workflows are one optional adapter, not the standard.
Do not copy stack-specific jobs into every repository or automatically enable remote writes.
The provided reusable-checks workflow executes declared commands in the caller checkout;
the caller owns runtime/dependency setup. Pin a reviewed revision when calling across repos.
For a private workflow source, configure GitHub access explicitly before relying on reuse.
