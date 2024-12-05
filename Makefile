.PHONY: install test benchmark clean build publish dev-install lint format

# Development setup
install:
	poetry install

# Run tests
test:
	poetry run pytest tests/test_basic.py -v

# Run benchmarks
benchmark:
	poetry run pytest tests/test_benchmark.py -v --benchmark-only

# Clean build artifacts
clean:
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf target/
	find . -type d -name __pycache__ -exec rm -rf {} +

# Build package
build: clean
	poetry build

# Publish to PyPI
publish: clean build
	poetry publish

# Install in development mode
dev-install:
	poetry install --with dev

# Run linting
lint:
	poetry run flake8 rustils tests
	poetry run isort --check-only rustils tests

# Format code
format:
	poetry run black rustils tests
	poetry run isort rustils tests

# Run all checks (lint, format, test)
check: lint test benchmark

# Build and install locally
local-install: clean build
	pip install dist/*.whl

# Update dependencies
update:
	poetry update

# Show dependency tree
deps:
	poetry show --tree

# Run development shell
shell:
	poetry shell

# Help target
help:
	@echo "Available targets:"
	@echo "  install       - Install project dependencies"
	@echo "  test         - Run tests"
	@echo "  benchmark    - Run benchmarks"
	@echo "  clean        - Clean build artifacts"
	@echo "  build        - Build package"
	@echo "  publish      - Publish to PyPI"
	@echo "  dev-install  - Install in development mode"
	@echo "  lint         - Run linting"
	@echo "  format       - Format code"
	@echo "  check        - Run all checks"
	@echo "  local-install- Build and install locally"
	@echo "  update       - Update dependencies"
	@echo "  deps         - Show dependency tree"
	@echo "  shell        - Run development shell"

# Default target
.DEFAULT_GOAL := help
