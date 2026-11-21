import os
import sys
from pathlib import Path

POEM = """The Cup

He poured my tea each morning,
two sugars, no asking.

Now his hands tremble.
The pot is too heavy now.
Let me, I say,
and steady the pot —
one slow amber stream —
and set the cup in his hands,
the pour still his to offer.
"""

def validate(text: str) -> str | None:
    """Return an error message, or None when the text is a valid entry."""
    if not (1 <= len(text) <= 280):
        return f"entry must be 1-280 characters, got {len(text)}"
    if not text.strip():
        return "entry must not be only whitespace"
    if "\r" in text:
        return "entry must not contain carriage returns"
    if text.count("\n\n") < 2:
        return "entry lost its stanza breaks"
    return None


def main() -> int:
    text = POEM
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote entry.txt ({len(text)} characters)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
