.PHONY: setup format lint check

setup:
	uv sync

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

check:
	uv run ruff format --check .
	uv run ruff check .
