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
	uv run pytest tender_parser/tests/tests.py
	make lint
run:
	uv run python -m tender_parser.main

tests_ci:
	uv run pytest tender_parser/tests/tests.py