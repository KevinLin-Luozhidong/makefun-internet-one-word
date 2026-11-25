#!/usr/bin/env python3
"""make.fun entry: The Internet in One Word.

Writes one word describing the whole internet to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only;
no network, no files outside this repository.

The word: Labyrinth. The internet is a maze you wander for hours —
every corridor promises an exit, every turn opens three more corridors,
and you emerge somewhere you never meant to go, carrying something you
never meant to find. Funny because it is true, and true of the whole
internet rather than one app or one mood.
"""

import os

WORD = "Labyrinth"


def main():
    if len(WORD.split()) != 1:
        raise SystemExit(f"entry is {len(WORD.split())} words, the gate wants exactly one")
    if not 1 <= len(WORD) <= 30:
        raise SystemExit(f"entry is {len(WORD)} characters, the gate wants 1-30")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
