sync:
	uv sync

run: sync
	uv run ch1.py

format: sync
	uv run ruff format

lint: format
	uv run ruff check . --fix

init:
	uv sync
	uv run pre-commit install --hook-type commit-msg

.PHONY: sync run format lint init