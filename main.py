# SPDX-License-Identifier: MIT
"""The Internet in One Word — funniest, most fitting single word wins.

Writes the winning word to /output/entry.txt (UTF-8, 1-30 chars).
Tournament (in-session): 9 candidates drafted; winner chosen for
laugh, fit to the whole internet, surprise, and one-beat readability.
"""
import os

LINE = "Procrastopia"


def main() -> None:
    assert 1 <= len(LINE) <= 30, len(LINE)
    # Gate plus judge criterion 1: exactly one word, no spaces or newline.
    assert LINE.isalpha() and LINE == LINE.strip() and "\n" not in LINE
    out = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(LINE)
    except OSError:
        print(LINE)


if __name__ == "__main__":
    main()
