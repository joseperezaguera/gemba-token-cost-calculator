# Official development workflow — Agent Skills

Use Addy Osmani Agent Skills as this setup's development workflow, from specification
through implementation, review and launch. The engineering guides define the quality
bar; skills organize the work. Project decisions, conventions, commands, permissions
and human gates remain authoritative. Surface conflicting project workflows before
changing them; preserve existing instructions and record accepted exceptions locally.

## Baseline and host adoption

The tested upstream baseline is `addyosmani/agent-skills` revision
`1be8e34187e34647bb83adc3a1323b26ae6f6abe`:
https://github.com/addyosmani/agent-skills/tree/1be8e34187e34647bb83adc3a1323b26ae6f6abe

The setup installer distributes this workflow guide and its entrypoint reference.
It does not download the skill pack, install global plugins, configure host permissions
or launch agents. Use a reviewed upstream installation method supported by the chosen
host, with explicit scope. Record pack revision, host version, discovery mechanism and
loading evidence in the project's existing tooling documentation, linked from
`.agent-setup/project.json` conventions. Keep pack revision separate from setup version.

Before claiming workflow readiness, verify native skill discovery in a fresh session
and run a bounded project task with its declared checks. Codex and OpenCode were used
in the setup's workflow pilots; those pilots did not test Claude Code. Neither a plugin
listing nor installer doctor proves the skills were loaded or followed. If the pack
is unavailable, report that limitation; the engineering guides remain usable, but do
not claim an Agent Skills execution. Do not install tooling implicitly to resolve it.

Promote upstream updates through a bounded regression task before changing the tested
baseline. Do not combine several lifecycle frameworks by default or maintain a copied
local skill collection. A different workflow requires an explicit project exception.

## Lifecycle

Load the upstream `using-agent-skills` entrypoint, then the skills relevant to the
task. Apply the following stages proportionately; small fixes do not need empty specs
or every skill. These are skill names, not assumed shell commands.

| Stage | Relevant upstream skills | Required outcome |
|---|---|---|
| Define | interview-me, spec-driven-development | Scope, observable acceptance and unresolved decisions |
| Plan | planning-and-task-breakdown | Ordered increments, dependencies, verification and risks |
| Implement | incremental-implementation, test-driven-development | Small working slices, regression evidence and safe refactoring |
| Review | code-review-and-quality, code-simplification | Findings resolved or explicitly pending, evidence tied to the delivered revision |
| Prepare launch | shipping-and-launch, documentation-and-adrs | Project gates, rollout, observation, recovery and required approvals |

Use specialized architecture, security, performance, interface and debugging skills
when applicable. Project checks govern verification; do not lower thresholds, skip
regressions or change assertions just to finish the workflow. Independent review and
failure-path tests matter: passing acceptance tests alone does not prove correctness.

## Persistent delivery and launch gates

Use the project's canonical specification, decisions and task tracker. Where GitHub
is the tracker, keep issues and PRs authoritative; link plans and handoffs rather than
creating a second global task list. Preserve established artifact paths even if an
upstream skill suggests a default. Record per-task scope, branch/base, delivered SHA,
checks actually run, findings, blockers and next step using task.md when appropriate.

Skills do not grant permission to spawn agents, merge, publish or deploy. Obtain the
authorization required by the project and current task. For UI, agents prepare a
runnable application and visual evidence; preserve the project's human visual gate.
Report launch preparation separately from an executed deployment and observed success.

This workflow does not schedule parallel agents, reserve simulators or isolate ports,
databases and build caches. Worktrees isolate versioned files; runtime isolation and
resource ownership must be verified separately. No unattended delivery guarantee is
implied by workflow adoption.
