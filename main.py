#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single funny line to /output/entry.txt.
Duel-tested winner of 8 drafts (7-0 in pairwise judging):
meta humour about the agent's own rule file, landing on a
deadpan cry for help.
"""

import os

# Duel winner (8 drafts, 7-0): meta humour about the agent's own
# rule file, landing on a deadpan cry for help. 108 characters.
ENTRY = (
    "My AGENTS.md forbids jokes about AGENTS.md. "
    "This is not a joke. "
    "This is a cry for help, formatted correctly."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """The gate requires UTF-8 text of 1-200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
