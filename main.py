"""One Word, First Thought — entry: 'sonder'.

Sonder: the realisation that every random passerby is living a life
as vivid and complex as your own. It was the first word that came to
mind, which is the whole game: one word, no second draft.
"""

import os

ENTRY = "sonder"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
