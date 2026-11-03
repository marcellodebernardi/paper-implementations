.PHONY: setup format lint check new-paper

setup:
	uv sync
	uv run pre-commit install --install-hooks

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

check:
	uv run ruff format --check .
	uv run ruff check .

new-paper:
	@paper="$${PAPER:-}"; \
	case "$$paper" in \
		[0-9][0-9][0-9][0-9]-*) ;; \
		*) echo "Usage: make new-paper PAPER=<year>-<slug>" >&2; exit 2 ;; \
	esac; \
	slug="$${paper#????-}"; \
	case "$$slug" in \
		""|-*|*-|*--*|*[!a-z0-9-]*) echo "PAPER must use the format <year>-<slug>" >&2; exit 2 ;; \
	esac; \
	destination="papers/$$paper"; \
	if [ -e "$$destination" ]; then echo "$$destination already exists" >&2; exit 1; fi; \
	mkdir "$$destination"; \
	cp resources/templates/paper-readme.md "$$destination/README.md"; \
	echo "Created $$destination"
