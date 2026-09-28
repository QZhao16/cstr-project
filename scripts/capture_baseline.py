"""Capture a baseline; --plain-python bypasses an unavailable Jupyter kernel."""

import asyncio
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.metadata
import io
import json
import os
from pathlib import Path
import shutil
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "results" / "baseline"
RUNTIME = ROOT / ".runtime"
for name, subdir in (
    ("JUPYTER_RUNTIME_DIR", "jupyter"),
    ("IPYTHONDIR", "ipython"),
    ("MPLCONFIGDIR", "matplotlib"),
):
    directory = RUNTIME / subdir
    directory.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(directory)
os.environ["MPLBACKEND"] = "Agg"
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import nbformat
from nbclient import NotebookClient


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if BASELINE.exists():
        raise SystemExit(f"Baseline already exists; preserve it: {BASELINE}")
    notebook_path = ROOT / "notebooks" / "cstr_exploration.ipynb"
    parameter_path = ROOT / "data" / "reactor_parameters.yml"
    original_hash = sha256(notebook_path)
    notebook = nbformat.read(notebook_path, as_version=4)
    plain_python = "--plain-python" in sys.argv[1:]
    transcript = []
    if plain_python:
        os.chdir(ROOT)
        namespace = {"__name__": "__main__"}
        for index, cell in enumerate(notebook.cells):
            if cell.cell_type != "code":
                continue
            stream = io.StringIO()
            with redirect_stdout(stream), redirect_stderr(stream):
                exec(compile(cell.source, f"notebook-cell-{index}", "exec"), namespace)
            transcript.append(f"Cell {index}: {stream.getvalue()}")
        execution = (
            "Fresh Python process; unchanged code cells executed in order. "
            "No Jupyter kernel; rich displays and notebook kernel execution are unverified."
        )
    else:
        client = NotebookClient(
            notebook,
            timeout=180,
            kernel_name="python3",
            resources={"metadata": {"path": str(ROOT)}},
        )
        client.execute()
        execution = "nbclient, fresh python3 kernel; original cells unchanged"
        for index, cell in enumerate(notebook.cells):
            for output in cell.get("outputs", []):
                if output.output_type == "stream":
                    transcript.append(f"Cell {index}: {output.text}")
    if sha256(notebook_path) != original_hash:
        raise RuntimeError("The inherited notebook source changed during execution.")
    BASELINE.mkdir(parents=True)
    if plain_python:
        shutil.copy2(notebook_path, BASELINE / "cstr_exploration.original.ipynb")
    else:
        nbformat.write(notebook, BASELINE / "cstr_exploration.executed.ipynb")
    (BASELINE / "execution.txt").write_text("\n".join(transcript), encoding="utf-8")
    for filename in ("steady_states.csv", "steady_state_locus.png"):
        shutil.copy2(ROOT / "results" / filename, BASELINE / filename)
    versions = {
        name: importlib.metadata.version(name)
        for name in (
            "numpy", "scipy", "pandas", "matplotlib", "PyYAML",
            "nbclient", "nbformat", "ipykernel", "jupyterlab", "pytest",
        )
    }
    manifest = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "working_directory": str(ROOT),
        "python_executable": sys.executable,
        "python_version": sys.version,
        "packages": versions,
        "source_sha256": {
            "notebooks/cstr_exploration.ipynb": original_hash,
            "data/reactor_parameters.yml": sha256(parameter_path),
        },
        "output_sha256": {
            path.name: sha256(path) for path in BASELINE.iterdir() if path.is_file()
        },
        "execution": execution,
    }
    (BASELINE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("\n".join(transcript))
    print(f"\nBaseline saved to {BASELINE}")


if __name__ == "__main__":
    main()
