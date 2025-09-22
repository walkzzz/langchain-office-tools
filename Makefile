.PHONY: help install test clean format lint type-check pre-commit-install prompt-template-example

help:
	@echo "Available targets:"
	@echo "  install          - Install the package in development mode"
	@echo "  test             - Run tests"
	@echo "  clean            - Clean build artifacts"
	@echo "  format           - Format code with black"
	@echo "  lint             - Lint code with flake8"
	@echo "  type-check       - Run mypy type checking"
	@echo "  pre-commit-install - Install pre-commit hooks"
	@echo "  prompt-template-example - Run prompt template example"

install:
	pip install -e .

test:
	python simple_test.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

format:
	black .

lint:
	flake8 .

type-check:
	mypy .

pre-commit-install:
	pre-commit install

prompt-template-example:
	python examples/prompt_template_example.py