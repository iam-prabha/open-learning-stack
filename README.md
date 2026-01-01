# What Am I Learning? — Quick, Action-Oriented Guide 🚀

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

TL;DR
- Purpose: A compact, practical collection of code, notes, and projects for Python, Data Science, ML, Deep Learning, DSA, and related tooling.
- Goal: Help you get working fast — run examples, follow the learning path, and contribute improvements.

Get started (fast)
1. Clone:
   - `git clone git@github.com:iam-prabha/what-am-i-learning.git`
   - `cd what-am-i-learning`
2. Choose environment:
   - Preferred (project uses `uv`): `uv sync`
   - Alternative (standard Python venv + pip):
     - `python -m venv .venv && . .venv/bin/activate`
     - `pip install -r requirements.txt` (if present)
3. Run examples:
   - Run a script: `uv run python python/01-data_types.py` (or `python python/01-data_types.py` inside a venv)
   - Open notebooks: `uv run jupyter lab` or `uv run jupyter notebook`

Core commands (common)
- Install deps (uv): `uv add package_name`
- Install dev deps (uv): `uv add --group dev package_name`
- Sync / install from lock: `uv sync`
- Format / lint / test:
  - `uv run black .`
  - `uv run flake8 .`
  - `uv run mypy .`
  - `uv run pytest tests/`

If you prefer not to use `uv`
- Create a venv and install packages with `pip`.
- I recommend keeping `pyproject.toml` / `requirements.txt` in sync for reproducibility.

Repository layout (action-first)
- `python/` — Python fundamentals, examples, and notebooks (start here).
- `ml/` — Supervised & unsupervised learning examples.
- `deep_learning/` — PyTorch notebooks and models.
- `dsa/` — Data structures & algorithms implementations.
- `sql/` — SQL examples and exercises.
- `projects/` — End-to-end project workflows and templates.
- `data/` — Sample datasets used by examples.
- `tests/` — Unit tests (when present).

Recommended learning path (short)
1. `python/` — Basics → OOP → data libraries (NumPy, Pandas).
2. `statistics/` → core stats concepts used in ML.
3. `ml/` → supervised algorithms → model evaluation.
4. `deep_learning/` → neural network fundamentals → CNNs/RNNs.
5. `projects/` → apply end-to-end.

How I expect you to use this repo
- Explore directory READMEs for hands-on steps.
- Run notebooks to reproduce examples.
- Use `projects/` templates to practice end-to-end workflows.
- Open issues or PRs with small, focused improvements.

Troubleshooting (quick fixes)
- `uv` command not found: install via the documented installer or `pip install uv`.
- Python version mismatch: install and point `uv` to the required Python or use a venv with the correct interpreter.
- Jupyter kernel missing: `uv run python -m ipykernel install --user --name=what-am-i-learning`
- Import errors: ensure `uv sync` ran successfully or your venv is active.

Code quality & checks
- I run formatting, linting, and type checks as part of the workflow. Use:
  - `uv run black .`
  - `uv run flake8 .`
  - `uv run mypy .`
  - `uv run pytest tests/` (where tests exist)

Contributing (brief)
- Everyone is welcome to contribute — feel free to open issues or pull requests.
- Fork → branch → commit focused changes.
- Run quality checks before opening a PR.
- Suggested PR checklist:
  - Adds value or fixes an issue
  - Includes tests where appropriate
  - Passes `black`, `flake8`, and `mypy`
  - Includes short description & usage notes in PR body

License & contact
- License: MIT (see `LICENSE`)
- GitHub: https://github.com/iam-prabha/what-am-i-learning
- Issues & PRs: use the repository issue tracker for suggestions and bugs.

Notes & extras
- I keep notebooks and examples organized by topic and difficulty.
- Sample datasets live in `data/` — refer to each project README for dataset specifics.
- If you want a more minimal README (just a launcher), tell me and I will shorten it further.

Happy learning — jump into `python/` to start today! 🎓✨