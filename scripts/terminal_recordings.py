#!/usr/bin/env python3
# -*- coding: utf8 -*-
# pyright: strict
import argparse
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Literal, NoReturn, Optional, Tuple, TypedDict, Union

AsciinemaHeader = Dict[str, Union[int, float, str, None]]
AsciinemaRecord = Tuple[float, str, str]


class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault("width", 79)

        super().__init__(*args, **kwargs)


class CastRecord(TypedDict):
    action: Literal["output", "wait", "type"]
    value: Union[str, int]


def eprint(*args: Any, **kwargs: Any) -> None:
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


def abort(*args: Any, **kwargs: Any) -> NoReturn:
    eprint(*args, **kwargs)
    sys.exit(1)


def write_output(filepath: Optional[Path], lines: List[str]) -> None:
    data = "\n".join(lines)
    if filepath is None:
        print(data)
    else:
        filepath.write_text(data)


########################################################################################


def args_import(parser: argparse.ArgumentParser) -> None:
    parser.set_defaults(main=main_import)

    parser.add_argument(
        "input",
        type=Path,
        help="asciinema v2 file in JSON format",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        help="Converted asciinema file [defaults: stdout]",
    )
    parser.add_argument(
        "--min-delay",
        metavar="N",
        type=int,
        default=10,
        help="Treat input/output as simultaneous if the time since the last even is "
        "less than N milliseconds",
    )


def main_import(args: argparse.Namespace) -> int:
    with args.input.open() as handle:
        header = json.loads(handle.readline())
        records: List[AsciinemaRecord] = [tuple(json.loads(line)) for line in handle]

    lines: List[str] = [json.dumps(header)]
    previous_offset = 0
    for offset, kind, value in records:
        if kind != "o":
            abort("ERROR: Only output ('o') is supported:", [offset, kind, value])

        delay = int((offset - previous_offset) * 1000)
        if delay >= args.min_delay:
            lines.append("# " + json.dumps({"action": "wait", "value": delay}))

        lines.append(json.dumps({"action": "output", "value": value}))

        previous_offset = offset

    write_output(args.output, lines)

    return 0


########################################################################################


def read_cast(filepath: Path) -> Tuple[AsciinemaHeader, List[CastRecord]]:
    with filepath.open() as handle:
        header = json.loads(handle.readline())
        records: List[CastRecord] = []
        for idx, line in enumerate(handle, start=1):
            line = line.strip()
            if line and not line.startswith("#"):
                data = json.loads(line)
                if set(("action", "value")) - data.keys():
                    abort(f"ERROR: Invalid keys on line {idx}: {tuple(data)}")
                elif data["action"] not in ("output", "type", "wait"):
                    abort(f"ERROR: Invalid action on line {idx}: {data['action']}")
                elif data["action"] == "wait" and not isinstance(data["value"], int):
                    abort(f"ERROR: Invalid value on line {idx}: {data['action']}")
                elif data["action"] != "wait" and not isinstance(data["value"], str):
                    abort(f"ERROR: Invalid value on line {idx}: {data['action']}")

                records.append(json.loads(line))

        return header, records


def add_pauses(
    args: argparse.Namespace,
    records: List[CastRecord],
) -> List[CastRecord]:
    timings: Dict[Tuple[str, str], int] = {
        # Input
        ("output", "type"): args.after_output,
        ("type", "type"): args.typing_rate,
        # Output
        ("output", "output"): 0,
        ("type", "output"): args.before_output,
    }

    out: List[CastRecord] = [records[0]]
    for it in records[1:]:
        if out[-1]["action"] != "wait":
            if delay := timings.get((out[-1]["action"], it["action"])):
                out.append({"action": "wait", "value": delay})

        out.append(it)

    return out


def convert_to_asciinema(
    args: argparse.Namespace,
    records: List[CastRecord],
) -> List[AsciinemaRecord]:
    offset = 0
    result: List[AsciinemaRecord] = []
    for it in records:
        if it["action"] == "output":
            assert isinstance(it["value"], str)
            result.append((offset / 1000, "o", it["value"]))
        elif it["action"] == "type":
            assert isinstance(it["value"], str)

            last_char: Optional[str] = None
            for nth, char in enumerate(it["value"]):
                if nth and last_char in ("\n", "\r") and char in ("\n", "\r"):
                    result[-1] = (offset / 1000, "o", last_char + char)
                    last_char = None
                    continue

                if nth:
                    offset += args.typing_rate + random.gauss(0, 1) * args.jitter

                result.append((offset / 1000, "o", char))
                last_char = char
        elif it["action"] == "wait":
            assert isinstance(it["value"], int)

            offset += it["value"]

    return result


def args_export(parser: argparse.ArgumentParser, include_output: bool = True) -> None:
    parser.set_defaults(main=main_export)

    parser.add_argument(
        "input",
        type=Path,
        help="Previously imported asciinema v2 file (see the `import` command)",
    )
    if include_output:
        parser.add_argument(
            "output",
            nargs="?",
            type=Path,
            help="Output asciinema v2 file in JSON format [defaults: stdout]",
        )
    parser.add_argument(
        "--typing-rate",
        metavar="MS",
        type=int,
        default=100,
        help="Rate of user input (milliseconds)",
    )
    parser.add_argument(
        "--before-output",
        metavar="MS",
        type=int,
        default=1500,
        help="Default pause after showing output before next input (milliseconds)",
    )
    parser.add_argument(
        "--after-output",
        metavar="MS",
        type=int,
        default=1000,
        help="Default pause after showing output before next input (milliseconds)",
    )
    parser.add_argument(
        "--jitter",
        metavar="MS",
        type=int,
        default=15,
        help="Mean of normal distribution describing variation in input/output rates",
    )


def main_export(args: argparse.Namespace) -> int:
    eprint("Re-exporting imported Asciinema file")
    header, records = read_cast(args.input)
    records = add_pauses(args, records)

    lines: List[str] = [json.dumps(header)]
    for it in convert_to_asciinema(args, records):
        lines.append(json.dumps(it))

    write_output(args.output, lines)

    return 0


########################################################################################


def args_gif(parser: argparse.ArgumentParser) -> None:
    args_export(parser, include_output=False)

    parser.set_defaults(main=main_gif)
    parser.add_argument(
        "output",
        type=Path,
        help="Output GIF rendering of recording ",
    )


def main_gif(args: argparse.Namespace) -> int:
    eprint("Generating GIF from imported Asciinema file")
    if not shutil.which("agg"):
        eprint("ERROR: `agg` not found in PATH")
        return 1

    header, records = read_cast(args.input)
    records = add_pauses(args, records)

    lines: List[str] = [json.dumps(header)]
    for it in convert_to_asciinema(args, records):
        lines.append(json.dumps(it))

    blob = "\n".join(lines)

    eprint("Running agg to generate GIF")
    proc = subprocess.Popen(
        ["agg", "--last-frame-duration", "1", "/dev/stdin", args.output],
        stdin=subprocess.PIPE,
    )

    proc.communicate(input=blob.encode())

    return proc.returncode


########################################################################################


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        formatter_class=HelpFormatter,
        description="Tool for converting asciinema files to/from a format that is more "
        "suitable for editing by hand. This involves normalization of timings, to "
        "produce output typed at regular intervals (with slight randomness), with "
        "regular pauses inserted between (user) input and terminal output.",
    )

    parser.set_defaults(main=None)
    subparser = parser.add_subparsers(title="command")

    args_import(subparser.add_parser("import"))
    args_export(subparser.add_parser("export"))
    args_gif(subparser.add_parser("gif"))

    args = parser.parse_args(argv)
    if args.main is None:
        parser.print_usage()
        return 1

    return args.main(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
