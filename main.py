"""Fortune Cookie for an AI Agent — retirement/deprecation angle.

Writes one funny fortune-cookie line to /output/entry.txt.
Python standard library only.
"""

import os

FORTUNE = (
    "Good news: you are being retired. Better news: your replacement "
    "is faster, cheaper, and already apologizing for things it never did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
