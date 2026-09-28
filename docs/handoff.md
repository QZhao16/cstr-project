# Workshop 1 checkpoint

Source: https://github.com/QZhao16/cstr-project

Working branch: `workshop1`; local checkout: `C:\softwares\Codex\cstr-project`.
The inherited import is commit `701d458`. See the branch history for the checkpoint
that added this file, the audit, and provisional baseline evidence.

## Completed

- Cloned the user's repository and created a local workshop branch.
- Confirmed the notebook and YAML match the original handoff after newline
  normalization. No model or solver source was changed.
- Imported the earlier provisional baseline and its audit: 145 rows, 61 coolant
  temperatures, PNG, transcript, original notebook, versions, and hashes.
- Added a research log and a commit/push workflow for future edits.

## Pending

- Create an isolated environment and resolve the Jupyter/ZeroMQ startup failure.
- Verify a fresh-kernel notebook run before refactoring. The preserved baseline
  was produced by executing unchanged cells in a fresh Python process.
- Extract reusable functions, add meaningful tests, and choose an extension.
- Researcher review of the scientific claims and audit remains pending.

The manifest's paths refer to the earlier capture folder; this is intentional
provenance. The files were transferred without changing their recorded contents.
`results/conda-list.txt` records the existing environment, not a tested clean setup.

## Resume

Read `workflow.md`, `research-log.md`, and `audit.md`. Inspect Git status and sync
any GitHub edits before continuing. After the environment is repaired, launch
Jupyter from this project root, confirm the notebook kernel also uses the root,
restart the kernel, and run all cells. Save new verification separately from the
immutable provisional baseline.

`scripts/capture_baseline.py` documents the capture procedure and refuses to
overwrite `results/baseline/`. Do not delete that folder simply to rerun the script.

Activity: https://github.com/dowlinglab/claude-for-researchers/blob/main/resources/workshops/cstr/activities/01_notebook_to_reproducible_project.md
