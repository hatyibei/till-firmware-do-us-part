"""Entry for make.fun's "Till Firmware Do Us Part" bounty.

Writes one funny, heartfelt wedding vow spoken by a robot, as a single
sentence, to /output/entry.txt.
"""

import os

TEXT = (
    "I vow to love every version of you, to back up your tears and cache your laugh, "
    "and to never once put you in sleep mode just to win an argument."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
