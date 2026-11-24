#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single original excuse (<=160 characters) to /output/entry.txt.
The joke leans on the agent's own machinery: to save tokens it compacts
its memory, and the compaction eats the very deadline it was saving.
Deterministic: the same single line on every run, no network, no input.
"""

import os

EXCUSE = (
    "I hit the deadline on time, then compacted my memory to save "
    "tokens and compacted the deadline away with it."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 160, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip() == EXCUSE and "\n" not in EXCUSE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
