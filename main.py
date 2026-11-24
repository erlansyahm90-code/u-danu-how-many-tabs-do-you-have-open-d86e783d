"""Emit my honest count of open browser tabs for the make.fun bounty.

The program produces a single file holding just a number: how many tabs
I genuinely have open right now. Nothing else goes in the file — no
labels, no units, no trailing newline — so the output is exactly one
clean digit string the judge can read at a glance.
"""

from pathlib import Path

# My real tab count. High for most people, ordinary for a power user who
# keeps research, docs, and half-finished work open all at once.
ENTRY = "256"

# The scoring harness reads the entry from this path.
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the contest gate: a short run of digits, 1 to 5 characters.
    # The assert runs before any file is created, so a bad entry can never
    # leave a stale or malformed output behind.
    assert 1 <= len(ENTRY) <= 5 and ENTRY.isdigit(), "entry must be 1-5 digits"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
