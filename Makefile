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

run_redis:
	docker ps -a -f name=redis -q | xargs -r docker stop
	docker ps -a -f name=redis -q | xargs -r docker rm
	docker run -d -p 6379:6379 --name redis redis

run:
	make run_redis
	uv run python -m tender_parser.main

tests_ci:
	uv run pytest tender_parser/tests/tests.py