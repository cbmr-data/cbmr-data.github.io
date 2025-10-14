# CBMR Data Analytics Documentation

This repository contains sources for public documentation and files related to usage of the esrum Esrum cluster administered by CBMR data analytics. The documentation can be read at [cbmr-data.github.io](https://cbmr-data.github.io).

## Writing documentation

Documentation in automatically deployed to `cbmr-data.github.io/`:

1. Files in the `root/` folder are deployed directly to the root of `cbmr-data.github.io/`.
2. The [sphinx](https://www.sphinx-doc.org/en/master/) project in the `esrum/` folder is deployed to `cbmr-data.github.io/esrum/`.

To add additional sources of documentation, modify `.github/workflows/default.yaml`.

## Tools for writing documentation

### Automatically rebuild documentation

The `sphinx-autobuild` command can be used to automatically rebuild the documentation when you make changes. If [uv](https://docs.astral.sh/uv/) is installed, then simply run `make` in the documentation root to run `sphinx-autobuild` in an ephemeral virtual environment.

Alternatively, requirements can be installed and run as follows:

```console
pip install --user sphinx-autobuild furo==2024.1.29
cd /path/to/cbmr-data.github.io/esrum
pip install -r requirements.txt
# -a to disable incremental builds as this does not work for all file types
# -q to slice output when autobuild triggers
sphinx-autobuild ./source ./build -aq
```

Then go to [127.0.0.1:8000](http://127.0.0.1:8000/). The page automatically refreshes when you save changes to the documentation.

### Automatically format RST files

The `rstfmt` command can be used to automatically format `.rst` files for consistency. Currently, this requires a custom version of `rstfmt`that supports the `code-block` directive. This can be installed any `pip` compatible tool:

```console
pip install git+https://github.com/MikkelSchubert/rstfmt.git
```

This can be run as follows

```console
cd /path/to/cbmr-data.github.io/esrum
find -name '*.rst' -exec rstfmt "{}" +
```

If using VSCode, the [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters) extension can be used to enable automatic formatting of documentation. This requires merging the following configuration into your workspace configuration:

```json
{
  "customLocalFormatters.formatters": [
    {
      "command": "/path/to/rstfmt",
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
