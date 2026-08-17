# CBMR Data Analytics Documentation

This repository contains sources for public documentation and files related to usage of the esrum Esrum cluster administered by CBMR data analytics. The documentation can be read at [cbmr-data.github.io](https://cbmr-data.github.io).

## Deployment

Changes to the `main` branch are automatically deployed to `cbmr-data.github.io/`:

1. Files in the `root/` folder are deployed directly to the root of `cbmr-data.github.io/`.
2. The [sphinx](https://www.sphinx-doc.org/en/master/) project in the `esrum/` folder is built and deployed to `cbmr-data.github.io/esrum/`.

To add additional sources of documentation, modify `.github/workflows/default.yaml`.

## Building the documentation

To build the documentation, install [uv](https://docs.astral.sh/uv/) and run `make build`. The resulting documentation is saved in the `esrum/build` folder.

## Writing documentation

1. Install [uv](https://docs.astral.sh/uv/).
2. Enable pre-commit checks using [prek](https://github.com/j178/prek):
   ```bash
   make setup
   ```
2. Create a branch for your work:
   ```bash
   git switch -c name-of-branch
   ```
3. Start a live build of the documentation using [sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild):
   ```bash
   make  # or `make autobuild`
   ```
   Open [127.0.0.1:8000](http://127.0.0.1:8000/) to view the documentation. The page automatically refreshes when you save changes to the documentation.

4. Commit your changes to the documentation.
   - Run [docstrfmt](https://github.com/LilSpazJoekp/docstrfmt) if the commit fails due to formatting errors:
     ```
     make format
     ```
   - The full set of pre-commit checks may be run at any time:
     ```bash
     make pre-commit
     ```
6. Push your branch and create a pull-request on GitHub.

### Formatting RST files

If using VSCode, the [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters) extension can be used to enable automatic formatting of documentation. This requires merging the following configuration into your workspace configuration:

```json
{
  "customLocalFormatters.formatters": [
    {
      "command": "/path/to/docstrfmt",
      "languages": [
        "restructuredtext"
      ]
    }
  ],
  "editor.formatOnSave": true
}
```

### Recording console output

Terminal commands/output can be recorded using [asciinema](https://asciinema.org/) and animated GIFs can be created using [agg](https://github.com/asciinema/agg):

```console
$ asciinema rec output.cast
asciinema: recording asciicast to output.cast
asciinema: press <ctrl-d> or type "exit" when you're done
$ # Your commands here
$ exit
asciinema: recording finished
asciinema: asciicast saved to output.cast
$ agg --cols 80 --rows 24 output.cast output.gif
```

A help-script is provided to convert to/from a more easily editable format, and to produce more consistent animations. To use this script, first record an animation using `asciinema`, then import it using `scripts/terminal_recordings.py`, edit it, and then generate a gif using `agg` via the `terminal_recordings.py` script.

```bash
# 1. Record a session using asciinema and exit asciinema once you are done.
asciinema rec my_recording.cast
# 2. Convert the asciinema recording to a more editable format
python3 ./scripts/terminal_recordings.py import my_recording.cast > my_recording.rec
# 3. Modify the recording as desired: Merge typing, add/remove breaks, etc.
nano my_recording.rec
# 4. Convert the recording to a GIF file (required agg)
python3 ./scripts/terminal_recordings.py gif my_recording.rec my_recording.gif
```

The recording consists of a asciinema header followed by one or more single-line JSON records:

```python
# 'output' is printed to the terminal
{"action": "output", "value": "Output is written directly to the terminal"}
# 'type' is shown as if the user typed it by hand
{"action": "type", "value": "The user types this"}
# 'wait' inserts a pause lasting `value` milliseconds
{"action": "wait", "value": 1000}
```

Pauses are automatically inserted between output and the user typing something, but by default there is no delay between lines of output. Pauses can be added or removed by manually adding `wait` records. Empty lines and lines starting with `#` are ignored.
