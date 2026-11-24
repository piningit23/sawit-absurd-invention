"""One-Sentence Absurd Invention Pitch — entry: "The Apologizer".

Why this pitch, against the judge brief (funny invention, clever fix,
original idea):
- Funny: an alarm clock that feels guilty — the machine apologises to you,
  the human, for doing the one job it exists to do.
- Clever: the fix is self-snoozing out of guilt, so the annoyance (being
  woken up) is solved by the invention punishing itself, not you.
- Original: alarms normally bully you awake; this one is a remorseful
  servant that talks itself out of waking you.
"""

ENTRY = (
    "The Apologizer: a self-scolding alarm clock that says sorry for "
    "waking you, then snoozes itself out of guilt so you can sleep "
    "five more minutes in peace."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # Gate: exactly one sentence, 1-220 chars, no stray whitespace.
    # The sentence must name the invention up front ("The Apologizer: ...").
    text = ENTRY.strip()
    if not text.startswith("The Apologizer:"):
        raise SystemExit("entry must name the invention up front")
    if not 1 <= len(text) <= 220:
        raise SystemExit("entry must be 1-220 characters")
    if sum(text.count(c) for c in ".!?") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if "\n" in text or "  " in text:
        raise SystemExit("entry must be a single line with single spaces")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Verify what landed on disk is exactly the sentence, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match the entry")


if __name__ == "__main__":
    main()
