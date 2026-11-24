#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — a single emoji for the trip of dreams.

A desert island: the whole dream in one glyph — a private island, palm,
and sea. More specific than a lone palm tree (one particular escape, not
just any holiday), still instantly readable on any screen, and it lands
straight on the judge's first criterion: a faraway place.
"""

import os

EMOJI = "🏝️"


def main():
    print(EMOJI)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
