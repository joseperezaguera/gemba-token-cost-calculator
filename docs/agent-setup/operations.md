# Environments, observability and production verification

Document reproducible setup, runtime versions, start/readiness/stop commands, required
services and environment variables without secret values. Identify generated files
and their generators. Declare relevant verification commands and working directories.

For worktrees or concurrent sessions, isolate ports, database/schema, temporary files,
containers and compose project names. Confirm tests execute against the intended
revision and environment. A worktree alone does not provide runtime isolation.

At integration boundaries, define timeouts, bounded retries, idempotency, cancellation
and fallback where applicable. Do not retry non-idempotent work blindly. Identify
what partial failures leave behind and how operators recover. Make resource and
latency budgets measurable for performance-sensitive work.

Use logs, metrics and traces for different questions. Distinguish durable business
audit from operational metrics and analytics; avoid contradictory sources of truth.
Do not put sensitive data in telemetry. Bound metric cardinality. Each important
metric/alert needs a purpose, owner and interpretation; temporary signals need a
retirement condition.

Verify actual deployed revision and configuration before testing a release. Check
acceptance behavior, representative failures and operational signals after rollout.
Use controlled fixtures or simulators when production-like integration is needed.
Document cleanup and environment safeguards for diagnostic scripts. Do not report a
successful deployment as proof of correct behavior.

Libraries, local CLIs and static projects can mark service-specific items inapplicable
with a reason. They still need reproducible execution and failure diagnostics.
