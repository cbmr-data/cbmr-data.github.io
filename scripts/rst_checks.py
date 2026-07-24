#!/usr/bin/env python3
# pyright: strict
from __future__ import annotations

import argparse
import functools
import sys
from pathlib import Path


class Errors:
    def __init__(self) -> None:
        self._any_errors = False

    def __call__(self, *args: object) -> None:
        print("ERROR:", *args, file=sys.stderr)
        self._any_errors = True

    def __bool__(self) -> bool:
        return self._any_errors


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=functools.partial(
            argparse.ArgumentDefaultsHelpFormatter,
            width=79,
        ),
        allow_abbrev=False,
    )

    parser.add_argument("files", nargs="+", type=Path)

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    err = Errors()
    for filename in sorted(args.files):
        with filename.open() as handle:
            in_code_block = False
            for linenum, line in enumerate(handle, start=1):
                line = line.strip()
                if not line:
                    continue

                if in_code_block:
                    if line.startswith(":class:"):
                        in_code_block = False  # produce at most one class related error
                        _, kind = line.split(":class:", 1)
                        kind = kind.strip()

                        if not kind:
                            err(
                                f"Code-block at '{filename}':{linenum} has empty "
                                ":class: attribute"
                            )
                        elif kind not in (
                            "remote-command",
                            "local-command",
                            "generic-command",
                        ):
                            err(
                                f"Code-block at '{filename}':{linenum} has unexpected "
                                f":class: attribute: {kind!r}"
                            )

                    # local-command", ":class: remote-command"):
                    elif not line.startswith(":"):
                        in_code_block = False  # produce at most one class related error
                        err(
                            f"Code-block at '{filename}':{linenum} has no :class: "
                            "attribute"
                        )

                if line.startswith(".. code-block::"):
                    _, kind = line.rsplit("::", 1)
                    kind = kind.strip()

                    if not kind:
                        err(f"Code-block at '{filename}':{linenum} has no format")
                    elif kind == "console":
                        in_code_block = True
                    elif kind not in (
                        "bash",
                        "python",
                        "r",
                        "text",
                        "yaml",
                    ):
                        err(
                            f"Code-block at '{filename}':{linenum} has unexpected "
                            f"format {kind!r}",
                        )
                elif line.startswith(".. code::"):  # for consistency/ease of grepping
                    err(
                        f"Found `.. code::` block at '{filename}':{linenum}; use "
                        "`.. code-block::` instead",
                    )

    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
