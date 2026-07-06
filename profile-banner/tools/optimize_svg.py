#!/usr/bin/env python3
"""Optimize banner SVG for distribution without changing semantics."""
from __future__ import annotations

import argparse
import re
import sys

from lib.paths import BANNER_DIST, BANNER_MIN, BANNER_SRC, DIST
from lib.svg_utils import read_text


def optimize_svg(text: str) -> str:
    """Reduce redundant whitespace while preserving comments and structure."""
    lines = text.splitlines()
    optimized: list[str] = []
    previous_blank = False

    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            if not previous_blank:
                optimized.append("")
            previous_blank = True
            continue
        previous_blank = False
        optimized.append(stripped)

    result = "\n".join(optimized).strip() + "\n"
    result = re.sub(r"  +", " ", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Optimize banner SVG")
    parser.add_argument("--input", default=str(BANNER_SRC))
    parser.add_argument("--output", default=str(BANNER_MIN))
    args = parser.parse_args()

    from pathlib import Path

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERROR: Input not found: {input_path}")
        return 1

    DIST.mkdir(parents=True, exist_ok=True)
    source = read_text(input_path)
    optimized = optimize_svg(source)
    output_path.write_text(optimized, encoding="utf-8", newline="\n")

    print(f"Optimized: {output_path}")
    print(f"  Original : {len(source):,} bytes")
    print(f"  Optimized: {len(optimized):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
