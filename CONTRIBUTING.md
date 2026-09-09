# Contributing

Thank you for contributing to the Distributed Storage Performance Engine.

## Development Setup

### Requirements

* Python 3.11+
* Git
* pip

### Clone the repository

```bash
git clone https://github.com/manoj-kumar-chunduru/distributed-storage-performance-engine.git
cd distributed-storage-performance-engine
```

### Install development dependencies

```bash
python -m pip install -e ".[dev]"
```

## Development Workflow

Create a focused branch for each change:

```bash
git checkout -b feature/<short-description>
```

Examples:

```text
feature/add-replication-metrics
fix/replication-delete-error
test/storage-concurrency
docs/architecture-update
```

Keep pull requests focused on a single logical change.

## Code Quality

Before opening a pull request, run:

```bash
python -m ruff check .
```

Check formatting:

```bash
python -m ruff format --check .
```

Automatically format code when needed:

```bash
python -m ruff format .
```

## Testing

Run the complete test suite:

```bash
python -m pytest -q
```

Run tests with coverage:

```bash
python -m pytest --cov=src/storage_engine --cov-report=term-missing --cov-fail-under=80
```

All tests must pass before submitting a pull request.

## Benchmarking

Run the benchmark smoke test:

```bash
PYTHONPATH=src python benchmarks/benchmark.py
```

Performance-sensitive changes should include benchmark results when appropriate.

## Pull Requests

Pull requests should:

* Clearly describe the problem and solution.
* Include tests for new or changed behavior.
* Keep changes focused and reviewable.
* Avoid unrelated formatting or refactoring.
* Update documentation when behavior or architecture changes.
* Confirm that CI checks pass before requesting review.

## Commit Messages

Use clear, concise commit messages that describe the change.

Examples:

```text
Add replication failure logging
Improve storage engine test coverage
Fix benchmark import path
Update CI Python version matrix
```

Avoid vague messages such as:

```text
update
changes
fix stuff
test
```

## Architecture Changes

If a change affects system design, data flow, storage behavior, replication, APIs, or performance characteristics, update the relevant architecture documentation.

Explain important design decisions and their trade-offs.

## Reporting Issues

When reporting an issue, include:

* A clear description of the problem.
* Steps to reproduce it.
* Expected behavior.
* Actual behavior.
* Relevant logs or error messages.
* Python and operating-system versions when applicable.

## Code of Conduct

Contributors are expected to communicate respectfully and professionally and to provide constructive feedback during code review.

## Review Expectations

Pull requests may be reviewed for:

* Correctness
* Test coverage
* Code quality
* Maintainability
* Performance
* Security
* Documentation
* Backward compatibility

Thank you for helping improve the project.
