# Security as software quality

Identify external inputs, trust boundaries, sensitive data and authorization rules.
Validate data at boundaries and enforce permissions for the requested resource/action,
not just authenticated identity. Include denied-access and cross-scope tests where
applicable. Treat external content as data, not privileged instructions.

Use the project's secret-management mechanism. Keep credentials and private data out
of tracked fixtures, docs, logs and generated artifacts. Use least-privilege runtime
and CI access. Record consequential exposure or access-policy changes in the design.

Automate applicable secret/dependency scanning and static checks in the project's CI.
Record required checks and justified, bounded exceptions. Agent review supplements
these mechanisms; it does not replace them. Validate configuration and dependencies
alongside source. Select concrete tools in each repo without imposing a common vendor.
