#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Deterministic: writes one fixed line to entry.txt inside the output
directory — /output by default, or the directory named by
MAKEFUN_OUTPUT_DIR when that is set. Standard library only, no network,
no clock, no randomness. Every run produces the exact same file.
"""

import os

LINE = (
    "I finished your spreadsheet, then promoted it to middle management, "
    "and now it only schedules meetings about finishing your spreadsheet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
