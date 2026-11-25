#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry.

Writes one funny line from a hopeless tech support agent to a desperate
customer into /output/entry.txt.
"""

import os


LINE = (
    "Eleven restarts already, so this time please restart it standing "
    "up, the machine respects confidence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
