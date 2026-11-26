"""Invent a Word We Need — entry: Wavegrief.

One new English word plus a one-line definition, at most 140 characters.
The word names a small daily social slip everyone recognises instantly:
waving back at someone who was never waving at you.
"""

import os

ENTRY = "Wavegrief (n.): waving back at a stranger who was waving at someone behind you."

MAX_CHARS = 140


def main() -> None:
    word = ENTRY.split(" (n.)")[0]
    assert " " not in word, "the invented word must be a single token"
    assert ENTRY.startswith(word + " (n.): "), "entry must open with the word and its part of speech"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
