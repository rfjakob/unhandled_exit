.PHONY: all
all: build test

.PHONY: build
build:
	hatch build

.PHONY: test
test:
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
format:
	python -m autopep8 -r -i .
