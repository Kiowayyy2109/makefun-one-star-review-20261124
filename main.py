#!/usr/bin/env python3
"""make.fun entry: u-0xb3e689-one-star-review-of-something-essential-c7234629.

Writes a single one-star review of something essential - sleep - to
/output/entry.txt. One line, no trailing newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

REVIEW = "One star. I spend a third of my life asleep and wake up tired anyway."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_review(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not 1 <= len(text) <= 160:
        raise ValueError("review must be 1-160 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_review(REVIEW)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW)
    if path.read_text(encoding="utf-8") != REVIEW:
        raise IOError("written entry does not match the review")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
