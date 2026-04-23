.PHONY: autobuild

UV_RUN := uv run \
	--with-requirements esrum/requirements.txt \
	--exclude-newer=2026-04-23

# Runs sphinx-autobuild in a temporary directory, allowing real-time
# monitoring of changes to the documentation. Options -aE is needed since
# changes to certain files (css, js) may not not picked up otherwise.
# https://github.com/executablebooks/sphinx-autobuild#relevant-sphinx-bugs
autobuild-uv:
	$(UV_RUN) --with "sphinx-autobuild==2025.08.25" \
		sphinx-autobuild -qnaE "esrum/source" "$(shell mktemp --directory)"

autobuild:
	sphinx-autobuild -qnaE "esrum/source" "$(shell mktemp --directory)"

build-uv:
	$(UV_RUN) sphinx-build -M html "esrum/source" "esrum/build"

build:
	sphinx-build -M html "esrum/source" "esrum/build"

.PHONY: autobuild-uv autobuild build-uv build
