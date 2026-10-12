# Project delivery profile — project-owned template

Copy into existing canonical project docs; populate with actual commands and decisions.
Keep credentials out. Mark inapplicable concerns with reasons, never a dummy passing job.

## Verification interface
| Concern | Command + working directory | Prerequisites | Required job / evidence |
|---|---|---|---|
| Style/format | | | |
| Types | | | |
| Architecture | | | |
| Unit/integration | | | |
| Contract consumer/provider | | | |
| Security/dependencies/image | | | |
| Build and deliverable smoke | | | |
| Critical E2E | | | |

## Runtime and artifact
- Build context/target/platform, dependency locks and base-image update policy:
- Runtime identity/user, writable paths and secret/config mechanisms:
- Start/readiness/stop commands, signals and deadlines:
- Per-run isolation and cleanup ownership:
- Published artifact identity and check-to-artifact traceability:

## CI/CD policy
- PR triggers, actual revision, required checks and branch/ruleset evidence:
- Pipeline permissions, pinned reusable components and cache policy:
- Deployment targets, serialization and approval/automation policy:
- Contract compatibility versions and evidence required before deploy:
- Migration order/backfill, rollout conditions and smoke/observability commands:
- Rollback artifact, data compatibility, forward recovery and verification:
- Release record: source/artifact/config/deployed versions/results:
