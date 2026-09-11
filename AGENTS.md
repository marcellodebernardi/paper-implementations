# Repository Guidelines

## Project Structure & Module Organization

- `papers/<year>-<slug>/`: one self-contained paper implementation, including its core algorithm, training and
  evaluation entry points, and a local `README.md`.
- `common/`: infrastructure genuinely shared across multiple reproductions.
- `notebooks/`: exploratory Jupyter notebooks and quick experiments.
- `resources/templates/`: reusable starting points for paper documentation.
- `pyproject.toml` and `uv.lock`: Python configuration and pinned dependencies.

Keep paper-specific code inside its paper directory. Do not move speculative abstractions into `common/` until more than
one implementation needs them.

## Setup and Development Commands

- `uv venv`: create the local virtual environment.
- `make setup`: install locked runtime and development dependencies.
- `uv run jupyter lab`: start JupyterLab for notebook work.
- `make format`: format Python files and apply safe lint fixes.
- `make lint`: run lint checks.
- `make check`: verify formatting and linting without changing files.
- `make new-paper PAPER=2015-residual-learning`: create a paper directory from the README template.
- `uv run pre-commit run --all-files`: run all configured repository checks.

There is currently no package build step.

## Starting a Paper

Run `make new-paper PAPER=<year>-<slug>`, then adapt the implementation layout to the paper rather than creating unused
standard directories. Agents should use this command when scaffolding a paper and run `make check` after code changes.
When consulting the paper, use a local `paper.pdf` if present; otherwise, follow the immutable paper link in that
directory's `README.md`.

## Coding Style & Naming Conventions

The project targets Python 3.13. Ruff enforces a 120-character line length, import ordering, Google-style docstrings,
formatting, and the lint rules configured in `pyproject.toml`. Paper directories follow
`papers/<year>-<short-paper-slug>/`, for example `papers/2017-attention-is-all-you-need/`.

## Testing Guidelines

No test framework or coverage threshold is configured yet. Keep paper-specific tests with their implementation and
shared tests with `common/`. Document reproduction, training, and evaluation commands in each paper's `README.md`.

## Commit & Pull Request Guidelines

Use the concise Conventional Commit style found in the history, such as `chore: basic dependencies` or
`docs: add project philosophy to readme`. Pull requests should explain the change, list validation commands, link the
relevant paper or issue, and include key metrics or plots when experimental behavior changes.

## Agent-Specific Instructions

Preserve the repository's pedagogical boundary: agents may implement scaffolding, maintenance, and shared boilerplate,
but must not write the core paper-specific training/evaluation logic or the author's reproduction analysis. Those parts
are intentionally completed by the human learner.
