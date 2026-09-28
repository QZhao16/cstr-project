# Research log

Record decisions and evidence, not just a list of edited files. Entries written by
an assistant describe its implementation decisions; they do not claim to know the
researcher's unstated thoughts. Git history supplies the corresponding diffs.

## 2026-09-28 — Establish the GitHub workflow

**User's stated intent:** Use `QZhao16/cstr-project` as the Workshop 1 source; track
code changes, retain the reasoning behind them, and save changes to GitHub.

**Decision:** Work in the existing `workshop1` branch, with descriptive commits and
this research log. Preserve `main` as the inherited starting point until a merge
is requested. Add project instructions so subsequent editing sessions follow the
same workflow.

**Starting evidence:** The inherited repository commit is `701d458`. The notebook
and YAML match the earlier Downloads-based working copy after normalizing line
endings; parsed notebook JSON is identical.

**Baseline:** Import the previously captured artifacts without rerunning or
overwriting them. The unchanged code produced 145 rows for 61 coolant temperatures.
At Tc = 300 K it found reactor temperatures 311.9589775, 348.9249258, and 385.1305120 K.
The baseline manifest records versions, hashes, execution mode, and original paths.
The full scientific audit is in `audit.md`.

**Limitation:** Jupyter kernel startup failed in the existing ZeroMQ installation.
The successful execution was a fresh Python process, not a fresh notebook kernel.
No model refactor, new scientific analysis, or stability calculation has occurred.

**Verification for this checkpoint:** Recorded artifact SHA-256 hashes matched;
the inherited notebook matched the saved original as parsed JSON; the runner's
syntax parsed successfully; and the CSV contained 145 finite rows at 61 conditions.
Baseline bytes are preserved, including Windows newlines and captured whitespace.
Git whitespace checks allow that recorded formatting only for the evidence files.
The assistant's completion report records the push outcome and commit link.

**Next question:** Which isolated environment will reliably run the original
notebook in a fresh kernel before module extraction?

## Template for the next entry

- Date and question:
- User's stated goal:
- Change and reason:
- Alternatives considered, if relevant:
- Command/environment and checks performed:
- Result and limits:
- Open question or next step:
