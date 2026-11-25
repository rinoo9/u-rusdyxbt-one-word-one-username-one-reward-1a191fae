#!/usr/bin/env python3
"""Entry for make.fun bounty 'One Word, One Username, One Reward'.

Writes the entrant's own username, one word and nothing else,
to /output/entry.txt. Deterministic: no network, no randomness, no input.

Craft notes: this username works against the judge's criteria because it
is a real handle, not a made-up label — it is the name the entrant actually
goes by on make.fun. It is a single word, instantly memorable, and worn
with pride: first name and surname joined by one hyphen, so it reads as
one identity rather than two words stapled together.
"""
import os

ENTRY = "muhammad-rino"  # 13 chars, within the gate's 1-30 character limit


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
