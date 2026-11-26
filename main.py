#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes a single funny line (1-200 characters) to /output/entry.txt.
No external dependencies; standard library only.
"""

import os

# The one-liner: a decisive setup (hiring a hitman) undercut by the
# punchline landing on the very thing it was hired to kill.
LINE = "I hired a hitman to kill my procrastination. He's coming next week, probably."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
