#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Final emoji: 🛫 (airplane departure, U+1F6EB)

Gate (from competition.yaml, sealed scorer): /output/entry.txt must be
UTF-8 text of 1 to 8 characters, not only white space. This entry is
exactly 1 codepoint (Python len() == 1), 4 bytes UTF-8 — inside the gate.

Counts:
  - Python len("🛫") = 1 character
  - Codepoints = 1 (U+1F6EB, single codepoint, no variation selector)
  - UTF-8 bytes = 4
  - Words = 0 (no words at all, exactly one emoji)

Decision record — candidates weighed against the judge brief, in the
brief's own order (1. plainly a dream vacation; 2. vivid postcard at a
glance; 3. personal and specific, not generic; 4. wit or surprise, a
fresh pick; 5. reads instantly across cultures and screens):

  A. 🏝️ desert island (U+1F3DD, 1 codepoint) — the postcard itself:
     turquoise water, palm, sand. The most direct dream-vacation naming
     of any candidate, and the strongest on criterion 2. REJECTED: it is
     the first emoji every entrant reaches for. Byte-identical entries
     share one rate and the earlier receipt places above its copies, so
     the most obvious pick is the most duplicated pick — and it is also
     generic ("any holiday") rather than one particular dream.

  B. 🛫 airplane departure (U+1F6EB, 1 codepoint) — WINNER. The moment
     of leaving. The judge's own test is "most makes a stranger want to
     book the flight", and this IS the flight taking off: wheels up, the
     trip already happening. It plainly names a dream vacation (a plane
     is the brief's own first example of a dream-vacation emoji), it is
     vivid at a glance, it is a specific feeling (departure, escape,
     wheels-up) rather than "a holiday", it is a fresher pick than the
     island everyone submits, and it reads instantly at any size, on any
     screen, in any culture.

  C. 🌅 sunrise over the sea (U+1F305, 1 codepoint) — a beautiful
     postcard, warm light on water. REJECTED: a sunrise happens every
     morning at home too. It is scenery, not a trip; it fails criterion
     3 (specific to one dream) and is too generic to beat a plane or
     an island head to head.

  D. 🍹 tropical drink (U+1F379, 1 codepoint) — witty, vacation-coded,
     a poolside joke in one glyph. REJECTED: it is a drink, not a
     place. The brief says an entry "loses to any single emoji that
     plainly names a dream vacation", and a cocktail does not name one.

  E. 🌴 palm tree (U+1F334, 1 codepoint) — tropical, clear, instantly
     readable. REJECTED: a single palm is a postcard cliché. It says
     "tropical" without saying "my dream", and it has no wit or
     surprise to it.

Writing passes:
  Pass 1: drafted B (🛫) as the pick — departure is the booking impulse
    itself, and the plane is the brief's own example of a dream-vacation
    emoji.
  Pass 2: tested the two strongest challengers against the draft.
    🏝️ was re-tested and rejected again: the most direct postcard, but
    the most duplicated and the most generic. 🌅 was re-tested and
    rejected again: beautiful, but a sunrise is not a trip. The draft
    was kept verbatim — no change was an improvement.

The program writes the emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output) and prints a verification line to stdout.
"""

import os
import sys

EMOJI = "\U0001f6eb"  # 🛫 airplane departure, exactly one codepoint


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(f"Verified: {len(EMOJI)} characters, 1 emoji.")
    print(EMOJI)


if __name__ == "__main__":
    sys.exit(main())
