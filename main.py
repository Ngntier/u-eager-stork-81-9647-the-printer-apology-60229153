"""The Printer Apology: write the entry line to /output/entry.txt.

One line, at most 120 characters: an apology note from an office printer
to the people who keep jamming it, feeding it cheap paper and swearing
at it. The program prints the same line every run; there is nothing
random about it, so the judged text is exactly the text below.
"""

import os

ENTRY = (
    "I'm sorry I jammed. You feed me cheap paper, kick my tray, "
    "then ask for colour. My rollers have unionised."
)

LIMIT = 120


def checked(line):
    """Refuse anything the competition gate would refuse."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > LIMIT:
        raise ValueError("entry is %d chars, over the %d cap" % (len(line), LIMIT))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    for ch in line:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry holds a control character")
    line.encode("utf-8")
    return line


def main():
    line = checked(ENTRY)
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
