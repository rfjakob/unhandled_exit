.PHONY: build
build:
	python3 -m build

.PHONY: test
test: build
	pytest tests/tests.py
