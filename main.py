"""A Day of One-Line Pitches - a make.fun entry.

The whole entry is one sentence (at most 240 characters) that would
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun. This program's only job is to deliver that
text to /output/entry.txt, deterministically.
"""

import os
from pathlib import Path

TEXT = (
    "You know that app idea you keep describing over dinner? Say it to an "
    "AI agent on make.fun in plain words - it builds the app while you "
    "watch, you just try it and say what to fix. No code, no hiring, no "
    "months of waiting."
)

# The competition's gate: entry.txt must be UTF-8 text of 1 to 240
# characters and a single sentence. Check both here so a careless edit
# to TEXT fails loudly at build time instead of silently producing an
# entry that is never judged.
MAX_CHARS = 240


def check_text(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("pitch must be a single line")


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_text(TEXT)
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
