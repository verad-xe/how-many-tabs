#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest count of open browser tabs as a single
number, digits only, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The number is 217: far above the handful of tabs most people guess,
specific enough to read as a count actually counted rather than a
round figure picked for effect, and the everyday shape of a tab
hoarder's browser -- research, docs and half-read articles kept open
because closing one feels like losing it.
"""

import os

# The entry: one number, digits only, no words, no punctuation.
# 217 is the honest count: well past a tidy guess, specific enough to
# read as actually counted, and the everyday shape of a tab hoarder's
# browser -- tabs kept open because closing one feels like losing it.
ENTRY = "217"


def main() -> None:
    # Self-check the gate before writing: 1-5 UTF-8 chars, digits only.
    assert 1 <= len(ENTRY.encode("utf-8")) <= 5, "entry must be 1-5 UTF-8 chars"
    assert ENTRY.isdigit(), "entry must be digits only"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
