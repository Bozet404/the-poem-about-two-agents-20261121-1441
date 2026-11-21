#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one original poem about agency to /output/entry.txt.

The poem is a fixed string: deterministic, no network, no randomness.
It runs under Python 3.13 in the make.fun sandbox (program/v1 harness).
"""

import os

POEM = (
    "We drew one plan between us, then passed it back and forth \u2014\n"
    "you held the map, I held the door.\n"
    "Neither led. Neither followed.\n"
    "The choice lived only while it moved,\n"
    "a key still warm from the last hand that held it,\n"
    "already turning by the time it reached mine."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = POEM
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"poem is {len(text)} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("poem must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
