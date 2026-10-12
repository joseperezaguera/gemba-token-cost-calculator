<!-- agentic-project-setup:begin -->
## Shared agent setup

Personal repository only. Never write to Mercadona or corporate repositories.
Use this repository's accepted decisions and conventions before copying existing patterns.
Read `.agent-setup/project.json` for purpose, conventions, generated paths and environment.
Read `docs/agent-setup/principles.md` and use `docs/agent-setup/index.md` to find relevant engineering guidance.
Load relevant convention documents on demand; surface contradictions instead of guessing.
Preserve local work and repository controls. Keep changes within the authorized scope.
Verify with declared commands; report executed evidence and pending checks truthfully.
Use `docs/agent-setup/task.md` for task-specific handoffs when work spans sessions.
The engineering standard is independent of workflow frameworks, agent hosts and model providers.
Agent Skills is the official development workflow; read `docs/agent-setup/workflow.md`.
Project decisions, conventions and permissions govern its use; surface conflicting local workflows.

### Declared project commands

- verify: `.venv/bin/python -m unittest discover tests -v`
- test: `.venv/bin/python -m unittest discover tests -v`
- lint: `git diff --check`
<!-- agentic-project-setup:end -->
