.PHONY: all
all: test build

.PHONY: syntax
syntax:
	python -m compileall -q .

.PHONY: build
build: syntax
	hatch build

.PHONY: test
test: syntax
	hatch run test

.PHONY: clean
clean:
	hatch clean

.PHONY: publish
publish:
	hatch clean
	hatch build
	hatch publish

.PHONY: format
format: syntax
	python -m autopep8 -r -i .
