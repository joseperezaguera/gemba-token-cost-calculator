# Continuous delivery and deployment

## Promote a verified artifact

Separate merge readiness, artifact readiness and production acceptance. Build once from
a verified revision, publish an immutable artifact identity, then promote that artifact
across environments with environment-specific configuration. For OCI images verify the
registry manifest digest; do not trust a mutable tag or confuse it with an image config ID.
Libraries/static sites/mobile apps apply the equivalent package/bundle/release identity.

A release record links source revision, check results, artifact, configuration, migrations
and contract compatibility. Before deployment, check prerequisites and supported
consumer/provider versions. Unknown contract verification results must block a gate
claimed to establish compatibility. Use independent evidence for deployment order.

## Delivery steps

1. Verify required code, architecture, test, contract and security checks.
2. Build and exercise the actual deliverable; publish and record its immutable identity.
3. Verify target environment, configuration, access, migration and compatibility prerequisites.
4. Deploy the recorded artifact with the project's explicit approval/automation policy.
5. Wait for bounded readiness; execute meaningful smoke/acceptance checks against the
   deployed revision and inspect operational signals. Failure must stop promotion.
6. Record deployed versions and results, then observe agreed criteria before wider rollout.

Serialize competing deployments to the same environment. Define canary/gradual rollout
and stop conditions where risk warrants them. Feature flag activation is a delivery step
with both-path tests and evidence; flags need cleanup. Do not cancel an active migration
merely because a newer commit arrived.

## Migration and recovery

Use compatible expand/contract steps and consumer-before-producer changes. Record
backfill scope, validation, resumability, owner and irreversible transitions. Reverting
an image may not revert a schema or restore data. Define rollback versus forward-recovery
procedures, prerequisites and recovery verification before production changes.

The rollback artifact must remain compatible with current state/contracts. Exercise the
procedure in a representative safe environment when relevant. Cleanup is explicit and
limited to retired versions/flags belonging to the completed change.

## Verification boundary

The example pipeline tests local container promotion between isolated staging and
production-simulation instances. It does not deploy a real production service, configure
infrastructure, publish to a registry or certify operational recovery of a stateful system.
Real targets require project-owned deployment adapters and evidence. Installer adoption
never performs deployment or changes permissions/branch protection.
