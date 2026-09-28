# Editing and remembering your work

Repository: https://github.com/QZhao16/cstr-project

Working branch: `workshop1`. GitHub shows `main` by default, so select `workshop1`
to see the workshop changes. The local checkout is `C:\softwares\Codex\cstr-project`.

## What gets saved

Each commit is a named snapshot. Its diff shows exactly which lines changed.
`docs/research-log.md` records the question, reason for a decision, evidence, and
remaining uncertainty. Together they preserve both the code and the context.

For every meaningful change:

1. State the question or desired behavior.
2. Edit the code and check the result.
3. Add a dated research-log entry explaining the decision and checks.
4. Review the diff, then commit with a specific message.
5. Push to GitHub and verify that the commit appears on `workshop1`.

A saved local file is not yet a commit, and a local commit is not on GitHub until
it is pushed. When asking the assistant for repository edits, the default project
workflow is to complete these steps and report any block to syncing.

## Edit directly on GitHub

Open the `workshop1` branch, select a text/code file, and use its edit control.
For several files, press `.` while viewing the repository to open GitHub's web
editor. Use its Source Control view to stage files and choose Commit & Push.
Commit to `workshop1` with a message that explains the purpose. Edit
`docs/research-log.md` alongside the code. Browser commits are already on GitHub.

Before continuing locally after browser edits, fetch and fast-forward the local
branch. If there are local changes or divergent commits, reconcile them before
editing further; do not overwrite either history.

Notebook files are JSON internally; use Jupyter for running cells and inspecting
plots. A browser edit alone does not verify that the notebook runs.
GitHub's [web editor documentation](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)
describes this workflow. The lightweight web editor does not run Python code.

## Find earlier changes

- Branch history: https://github.com/QZhao16/cstr-project/commits/workshop1
- Research log: https://github.com/QZhao16/cstr-project/blob/workshop1/docs/research-log.md
- Changes relative to the original: https://github.com/QZhao16/cstr-project/compare/main...workshop1

Select a commit to inspect its message and diff. A file's History view narrows the
history to that file. Prefer a new revert commit to undo a shared change, so its
history remains visible.

## Local Git commands

With Git available on PATH, use these from the project root:

```powershell
git status
git pull --ff-only
# Edit code, check results, and update the research log.
git diff
git add <specific-files>
git commit -m "Describe the change and its purpose"
git push
```

This machine currently uses Git bundled with GitHub Desktop. If `git` is not on
PATH, use GitHub Desktop or this PowerShell helper for the commands above:

```powershell
function git {
    & 'C:\Users\QINGHUA ZHAO\AppData\Local\GitHubDesktop\app-3.6.6\resources\app\git\cmd\git.exe' '--exec-path=C:\Users\QINGHUA ZHAO\AppData\Local\GitHubDesktop\app-3.6.6\resources\app\git\mingw64\bin' @args
}
```

The bundled path can change when GitHub Desktop updates.
