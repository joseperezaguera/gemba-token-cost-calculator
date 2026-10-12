# Containers and reproducible environments

## Build and runtime contract

For containerized projects, declare build context, Dockerfile/target, supported platforms,
runtime command, ports, writable paths, configuration and dependency lifecycle.
Libraries and static projects can declare container runtime inapplicable with a reason.
Containerization controls the environment but does not alone guarantee reproducible builds.

Use dependency lockfiles and reviewed base-image versions/digests. Define an update policy:
a pinned old image does not receive fixes by itself. Prefer multi-stage builds when they
separate compilation/test tooling from runtime. Ship required runtime files only.
Use .dockerignore to exclude secrets, local state and unnecessary build context.

Use a non-root runtime where possible, least privileges and explicit writable locations.
Keep credentials out of image layers, build arguments and ordinary environment instructions;
use build secret mounts and runtime secret mechanisms when needed. Never log secret values.
Do not expose the container engine socket to application/agent runtime as a convenience.

Label artifacts with source revision. Test the final runtime image, not only a build stage.
Identify a published artifact by digest; tags are convenient aliases and can move.
An image config ID, archive checksum and registry manifest digest are different identities:
record which one is compared, and verify the registry digest after publishing when applicable.

## Start, readiness and stop

Declare start/readiness/stop commands and bounded deadlines. Distinguish process liveness
from ability to serve required work. Readiness must reflect indispensable dependencies;
a green health route that never checks a required database can conceal a broken service.
Use exec-form entrypoints, correct signal propagation and graceful shutdown. Verify a stop
finishes within the budget and does not drop acknowledged work where that is guaranteed.

Keep environment configuration outside the image so the same artifact can be promoted.
Do not rebuild for staging versus production. Schema/data migration is a coordinated
step with its own compatibility and recovery evidence, not a hidden startup side effect.

## Isolation and verification

Use unique project/container/network names, dynamic or allocated ports and isolated
schemas/volumes per task or run. Verify the tested revision and endpoint. Tear down only
resources created by this run; never use broad pruning or remove another session's state.
For Compose, set a task-specific project name rather than a fixed name shared by worktrees.

Required evidence for the declared runtime: successful build, expected user/files,
readiness, meaningful smoke/contract checks and bounded shutdown. Include vulnerability
checks according to project policy. Record architecture/platform limits and failures.
