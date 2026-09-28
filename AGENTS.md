# Project collaboration

Use this repository as the source of truth for Workshop 1. The owner has requested
Git version control, a record of decisions, and saving requested changes to GitHub.

- Inspect Git status and relevant instructions before editing; preserve others' work.
- Work on `workshop1` unless the user requests another branch. Do not force-push.
- Keep changes focused. Record the purpose, important decisions, validation, and
  remaining questions in `docs/research-log.md`. Distinguish the user's stated
  intent from agent implementation decisions; never invent the user's reasoning.
- Use descriptive commits that explain what changed and why. After appropriate
  verification, commit the requested work and push the working branch to `origin`.
  If authentication or permissions block a push, preserve the local commit and
  report exactly what remains unsynced.
- Do not commit credentials, `.env` files, environments, caches, or temporary runtime
  connection files. Do not publish unrelated files.
- Treat `results/baseline/` as immutable evidence. It was captured in a fresh Python
  process, not a functioning Jupyter kernel. Preserve this distinction.
- Before refactoring the model, read `docs/audit.md` and complete the pending
  environment and fresh-kernel checks. Compare against the saved baseline.
- Do not merge into `main` or alter repository visibility unless requested.

See `docs/workflow.md` for how to review and save changes.
