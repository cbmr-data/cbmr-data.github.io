.PHONY: autobuild

UV_RUN := uv run \
	--with-requirements esrum/requirements.txt \
	--exclude-newer=2026-04-23

# Additional arguments to sphinx
SPHINX_ARGS :=

# Runs sphinx-autobuild in a temporary directory, allowing real-time
# monitoring of changes to the documentation. Options -aE is needed since
# changes to certain files (css, js) may not not picked up otherwise.
# https://github.com/executablebooks/sphinx-autobuild#relevant-sphinx-bugs
autobuild-uv:
	$(UV_RUN) --with "sphinx-autobuild==2025.08.25" \
		sphinx-autobuild -qnaE "esrum/source" "$(shell mktemp --directory)" \
		$(SPHINX_ARGS)

autobuild:
	sphinx-autobuild -qnaE "esrum/source" "$(shell mktemp --directory)" \
		$(SPHINX_ARGS)

build-uv:
	$(UV_RUN) sphinx-build -M html "esrum/source" "esrum/build" \
		$(SPHINX_ARGS)

build:
	sphinx-build -M html "esrum/source" "esrum/build" $(SPHINX_ARGS)

.PHONY: autobuild-uv autobuild build-uv build
