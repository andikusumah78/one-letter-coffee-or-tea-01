"""One-letter entry for 'One Letter: Coffee or Tea' on make.fun.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

LETTER = "A"


def main() -> None:
    # The gate requires exactly 1 character, not only whitespace.
    if len(LETTER) != 1 or not LETTER.strip():
        raise SystemExit("entry must be exactly one non-blank letter")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
