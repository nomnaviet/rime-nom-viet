"""Rewrite NomNaTong PUA codepoints in nom_viet.dict.yaml to the standard
codepoints NOM Foundation published for them (mostly Extension H and J).

No system font renders PUA, so text typed through the IME in PUA shows as
blank boxes outside fonts that carry NomNaTong's private codepoints.

The mapping is Nôm Na Việt's apps/api/src/data/nomnatong-pua-map.json, built
only from NOM Foundation's own conversion tables, release notes and PUA
roadmap. A PUA character maps to one standard character, or to a sequence: a
base character plus a variation selector (IVS) or plus the cá/nháy reading
mark (U+16FF0/U+16FF1). A sequence is one character to the user and stays
together as one entry text. An entry the rewrite turns into a
duplicate of another (same text and code) is merged into the first: the higher
weight, and the first non-empty comment. Duplicates the file already had are
left alone.

Usage (from a Nôm Na Việt checkout, where this repo is tools/rime-nom-viet):
    python3 scripts/pua_to_unicode.py [--map PATH] [--check]

--check writes nothing and exits 1 if a run would change the file.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DICT = REPO / "nom_viet.dict.yaml"
DEFAULT_MAP = REPO.parent.parent / "apps/api/src/data/nomnatong-pua-map.json"


def load_map(path: Path) -> dict[str, str]:
    raw = json.loads(path.read_text(encoding="utf-8"))["map"]
    # A target is "U+XXXX" or a space-separated sequence of them.
    def codepoint(token: str, key: str) -> str:
        if not re.fullmatch(r"U\+[0-9A-Fa-f]{4,6}", token):
            sys.exit(f"{path}: bad codepoint {token!r} in the mapping for {key}")
        return chr(int(token[2:], 16))

    return {codepoint(p, p): "".join(codepoint(t, p) for t in s.split()) for p, s in raw.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--map", type=Path, default=DEFAULT_MAP,
                        help="nomnatong-pua-map.json (default: the Nôm Na Việt checkout this repo sits in)")
    parser.add_argument("--check", action="store_true", help="write nothing; exit 1 if a run would change the file")
    args = parser.parse_args()
    if not args.map.exists():
        sys.exit(f"mapping not found at {args.map}: run this from a Nôm Na Việt checkout (tools/rime-nom-viet), "
                 "or pass --map pointing at its apps/api/src/data/nomnatong-pua-map.json")
    mapping = load_map(args.map)
    table = str.maketrans(mapping)

    lines = DICT.read_text(encoding="utf-8").split("\n")
    start = lines.index("...") + 1
    head, body = lines[:start], lines[start:]

    out: list[str | list[str]] = []
    # (text, code) -> the first entry with it, and whether that entry was rewritten.
    index: dict[tuple[str, str], tuple[list[str], bool]] = {}
    mapped = merged = 0
    for line in body:
        if not line or line.startswith("#"):
            out.append(line)
            continue
        cols = line.split("\t")
        text = cols[0].translate(table)
        rewritten = text != cols[0]
        mapped += rewritten
        cols[0] = text
        key = (text, cols[1] if len(cols) > 1 else "")
        seen = index.get(key)
        # Only a rewrite can create a duplicate: duplicates the file already had are left alone.
        if seen is None or not (rewritten or seen[1]):
            index.setdefault(key, (cols, rewritten))
            out.append(cols)
            continue
        first = seen[0]
        merged += 1
        if len(cols) > 2 and len(first) > 2 and cols[2].isdigit() and first[2].isdigit():
            first[2] = str(max(int(first[2]), int(cols[2])))
        if len(cols) > 3 and cols[3] and (len(first) < 4 or not first[3]):
            first[3:4] = [cols[3]]

    print(f"{len(mapping)} mappings: {mapped} entries rewritten, {merged} merged into an existing one")
    if args.check:
        sys.exit(1 if mapped or merged else 0)
    text = "\n".join(head + [o if isinstance(o, str) else "\t".join(o) for o in out])
    DICT.write_text(text, encoding="utf-8")
    print(f"wrote {DICT.name}")


if __name__ == "__main__":
    main()
