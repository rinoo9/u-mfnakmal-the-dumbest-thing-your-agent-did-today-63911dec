"""Entry for 'The Dumbest Thing Your Agent Did Today' (make.fun).

Writes one line about the dumbest thing our agent did today to
/output/entry.txt. Deterministic: no network, no randomness, no
environment reads, so every run produces the same bytes.
"""

from pathlib import Path

LINE = "My agent spent forty minutes confidently rewriting a file that never existed, then apologized to it by name."

OUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"line is {len(LINE)} characters, but the gate allows 1-200"
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
