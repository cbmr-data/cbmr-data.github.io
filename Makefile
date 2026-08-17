# Additional arguments to sphinx
SPHINX_ARGS :=

# Runs sphinx-autobuild in a temporary directory, allowing real-time
# monitoring of changes to the documentation. Options -aE is needed since
# changes to certain files (css, js) may not not picked up otherwise.
# https://github.com/executablebooks/sphinx-autobuild#relevant-sphinx-bugs
autobuild:
	uv run \
		sphinx-autobuild -qnaE "esrum/source" "$(shell mktemp --directory)" \
		$(SPHINX_ARGS)

build:
	uv run sphinx-build -M html "esrum/source" "esrum/build" $(SPHINX_ARGS)

format:
	uv run --only-dev docstrfmt esrum/

pre-commit:
	uv run --only-dev prek run -a

setup:
	uv run --only-dev prek install

.PHONY: autobuild build format pre-commit setup
