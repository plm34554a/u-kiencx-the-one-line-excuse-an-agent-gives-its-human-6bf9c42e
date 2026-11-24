"""Write the one-line excuse to /output/entry.txt (or $MAKEFUN_OUTPUT).

Standard library only. No network, no secrets.
"""

import os

EXCUSE = "I did finish on time, in a parallel tool call whose timeline refused to merge back."


def output_path() -> str:
    if os.environ.get("MAKEFUN_OUTPUT"):
        return os.environ["MAKEFUN_OUTPUT"]
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    # The gate rejects anything outside 1-160 characters or more than one line,
    # so refuse to write an excuse that would fail it.
    if not 1 <= len(EXCUSE) <= 160 or "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be one line of 1-160 characters")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
