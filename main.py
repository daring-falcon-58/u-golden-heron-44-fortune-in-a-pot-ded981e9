#!/usr/bin/env python3
"""Fortune in a Pot entry: one kind, funny fortune for a houseplant.

The fortune (97 characters, under the 120-character cap):

    Your keeper talks to you when no one is listening. This week,
    you answer -- with a brand-new leaf.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

FORTUNE = (
    "Your keeper talks to you when no one is listening. "
    "This week, you answer \u2014 with a brand-new leaf."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
# Writing the fixed fortune string (never re-generated) is what makes
# the two grader runs produce identical bytes.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def validate_fortune(text: str) -> None:
    """Enforce the brief's own gate; fail loudly instead of shipping bad text."""
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune is {len(text)} chars, cap is 120")
    if not text.strip():
        raise ValueError("fortune must not be only white space")
    if any(ord(ch) < 32 and ch not in "\t" for ch in text):
        raise ValueError("fortune must not hold control characters")


def main() -> None:
    # The brief's own gate, enforced by the program itself: UTF-8 text
    # of 1 to 120 characters, a single line, not only white space.
    # A fortune that broke any rule would fail loudly here instead of
    # shipping silently.
    validate_fortune(FORTUNE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(FORTUNE + "\n", encoding="utf-8")
    print(f"Wrote {TARGET} ({len(FORTUNE)} characters)")


if __name__ == "__main__":
    main()
