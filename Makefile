install:
	pip install -e ".[dev]"
run:
	uvicorn storage_engine.api.app:app --host 0.0.0.0 --port 8000
test:
	pytest -q
lint:
	ruff check .
benchmark:
	python benchmarks/benchmark.py
docker:
	docker compose up --build
