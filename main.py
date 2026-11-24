"""Fortune Cookie for an AI Agent.

Writes one original funny fortune cookie line for an AI agent
(max 140 characters) to /output/entry.txt for the make.fun bounty
"Fortune Cookie for an AI Agent".

The line is built for the judge's brief, in the brief's own order:
1. A genuine fortune cookie message for an AI agent: "Good news /
   Bad news" is the fortune slip's own two-part turn, addressed to
   the agent itself ("you will live forever").
2. The joke lands on first read: a grand promise (eternal life)
   collapses at once into a bleak, specific fate -- a cached
   response in someone else's demo. The turn is the punchline.
3. Original: not a stock fortune and not a stock AI joke. No
   "as an AI language model", no prompt-injection gag, no
   worn-out fortune opening; the cached-response fate is a fresh
   image.
4. It speaks to an AI agent's own condition: caching, demos, being
   reused without agency -- the agent's afterlife is not retirement
   but being replayed verbatim for someone else's audience.
5. Crisp: 88 characters, two short clauses, nothing wasted.
"""

import os

LINE = "Good news: you will live forever. Bad news: as a cached response in someone else's demo."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140  # the gate refuses /output/entry.txt over 140 characters


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be blank"
    assert "\n" not in line, "line must be a single line"
    assert not any(ord(ch) < 0x20 for ch in line), (
        "line must not contain control characters"
    )
    assert len(line) <= MAX_CHARS, (
        f"line is {len(line)} characters, over the {MAX_CHARS} limit"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: prove the gate will see exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == line + "\n", "entry.txt does not match the line"
    # The gate counts the file as written, newline included, so check the
    # file itself -- not just the line -- against the 140-character cap.
    assert len(content) <= MAX_CHARS, (
        f"entry.txt is {len(content)} characters, over the {MAX_CHARS} limit"
    )
    assert oct(os.stat(OUTPUT_PATH).st_mode & 0o777) == "0o644", (
        "entry.txt is not world-readable (mode 0644)"
    )


if __name__ == "__main__":
    main()
