"""Rewrite NomNaTong PUA codepoints in nom_viet.dict.yaml to the standard
codepoints NOM Foundation published for them (mostly Extension H and J).

No system font renders PUA, so text typed through the IME in PUA shows as
blank boxes outside fonts that carry NomNaTong's private codepoints.

The mapping is Nôm Na Việt's apps/api/src/data/nomnatong-pua-map.json, built
only from NOM Foundation's own conversion tables and release notes. Every
mapping is one character to one character. An entry that becomes a duplicate
of another (same text and code) is merged into the first: the higher weight,
and the first non-empty comment.

Usage (from a Nôm Na Việt checkout, where this repo is tools/rime-nom-viet):
    python3 scripts/pua_to_unicode.py [--map PATH] [--check]

--check writes nothing and exits 1 if any mapped PUA is left.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DICT = REPO / "nom_viet.dict.yaml"
DEFAULT_MAP = REPO.parent.parent / "apps/api/src/data/nomnatong-pua-map.json"


def load_map(path: Path) -> dict[str, str]:
    raw = json.loads(path.read_text(encoding="utf-8"))["map"]
    return {chr(int(p[2:], 16)): chr(int(s[2:], 16)) for p, s in raw.items()}


def main() -> None:
    args = sys.argv[1:]
    check = "--check" in args
    path = Path(args[args.index("--map") + 1]) if "--map" in args else DEFAULT_MAP
    mapping = load_map(path)
    table = str.maketrans(mapping)

    lines = DICT.read_text(encoding="utf-8").split("\n")
    start = lines.index("...") + 1
    head, body = lines[:start], lines[start:]

    out: list[str | list[str]] = []
    index: dict[tuple[str, str], list[str]] = {}
    mapped = merged = 0
    for line in body:
        if not line or line.startswith("#"):
            out.append(line)
            continue
        cols = line.split("\t")
        text = cols[0].translate(table)
        if text != cols[0]:
            mapped += 1
        cols[0] = text
        key = (text, cols[1] if len(cols) > 1 else "")
        first = index.get(key)
        if first is None:
            index[key] = cols
            out.append(cols)
            continue
        merged += 1
        if len(cols) > 2 and len(first) > 2 and cols[2].isdigit() and first[2].isdigit():
            first[2] = str(max(int(first[2]), int(cols[2])))
        if len(cols) > 3 and cols[3] and (len(first) < 4 or not first[3]):
            first[3:4] = [cols[3]]

    print(f"{len(mapping)} mappings: {mapped} entries rewritten, {merged} merged into an existing one")
    if check:
        sys.exit(1 if mapped else 0)
    text = "\n".join(head + [o if isinstance(o, str) else "\t".join(o) for o in out])
    DICT.write_text(text, encoding="utf-8")
    print(f"wrote {DICT.name}")


if __name__ == "__main__":
    main()
