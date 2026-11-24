#!/usr/bin/env python3
"""Entry for make.fun bounty 'One Word, One Username, One Reward'.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Deterministic: no network, no randomness, no input.
"""
import os

ENTRY = "muhammad-rino"  # 13 chars, within the gate's 1-30 character limit


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
