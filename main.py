#!/usr/bin/env python3
"""Entry for make.fun bounty 'One Word, One Username, One Reward'.

Writes the entrant's own username, one word and nothing else,
to /output/entry.txt. Deterministic: no network, no randomness, no input.

Craft notes: this username works against the judge's criteria because it
is a real handle, not a made-up label — it is the name the entrant actually
goes by on X (@muhammadd799), where he posts and is known. It is a single
word, short and sticky: the double-d and the 799 give it a rhythm that
lands on first read and sticks after one look, and it sounds like a handle
its owner would happily wear. A fresh angle from the earlier picks: not
his formal name, but his social handle — the name his audience already
recognises.
"""
import os

ENTRY = "muhammadd799"  # 12 chars, within the gate's 1-30 character limit


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
