package := parakeet

all:

test: .env/
	.env/bin/python -m pytest

.env/:
	python3 -m venv .env
	.env/bin/python -m pip install -e .
	.env/bin/python -m pip install pytest
	touch .env/

build:
	python3 -m build

test_build: build
	python3 -m venv .venv
	.venv/bin/python -m pip install pytest
	.venv/bin/python -m pip install --find-links=./dist $(package)
	.venv/bin/pytest
	rm -rf .venv

test_deployment:
	python3 -m venv .venv
	.venv/bin/python -m pip install pytest
	.venv/bin/python -m pip install $(package) --extra-index-url https://egoossen.github.io/python-package-server/
	.venv/bin/pytest
	rm -rf .venv

.PHONY: all test build test_build test_deployment
