<!-- agentic-project-setup:begin -->
## Shared agent setup

Personal repository only. Never write to Mercadona or corporate repositories.
Use this repository's accepted decisions and conventions before copying existing patterns.
Read `.agent-setup/project.json` for purpose, conventions, generated paths and environment.
Read `docs/agent-setup/principles.md` before implementation and delivery.
Load relevant convention documents on demand; surface contradictions instead of guessing.
Preserve local work and repository controls. Keep changes within the authorized scope.
Verify with declared commands; report executed evidence and pending checks truthfully.
Use `docs/agent-setup/task.md` for task-specific handoffs when work spans sessions.
Superpowers is the selected everyday framework when installed; this setup also works alone.
Product Factory is research; Control Tower is paused. Neither is activated by this setup.

### Declared project commands

- verify: `.venv/bin/python -m unittest discover tests -v`
- test: `.venv/bin/python -m unittest discover tests -v`
- lint: `git diff --check`
<!-- agentic-project-setup:end -->
