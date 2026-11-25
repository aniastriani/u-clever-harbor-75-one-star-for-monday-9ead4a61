"""One Star for Monday: a one-star review of Monday, as a restaurant.

The program writes a single line of plain text to entry.txt inside the
output directory the grader provides (MAKEFUN_OUTPUT_DIR, or /output
when the variable is unset). The text is one diner's complaint: a table
that took an hour, a chef who served the same cold Monday the diner
had already sent back last week. Pure standard library, deterministic,
no network, no input files.
"""

import os

REVIEW = (
    "One star. Waited an hour for a table, and the chef served me "
    "the same cold Monday I sent back last week."
)


def main():
    # The gate only accepts one line of plain text, 1 to 180 characters
    # and at most 25 words, so refuse to write anything that breaks it.
    if "\n" in REVIEW or len(REVIEW.split()) > 25 or not 1 <= len(REVIEW) <= 180:
        raise ValueError("review must be one line of at most 25 words")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")
    print(REVIEW)


if __name__ == "__main__":
    main()
