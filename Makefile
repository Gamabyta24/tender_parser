sort_imports:
	uv run isort .

install:
	uv sync

format:
	uv run black .

lint:
	uv run ruff check .

tests:
	make format
	make sort_imports
	make lint
	uv run pytest parser/tests.py
