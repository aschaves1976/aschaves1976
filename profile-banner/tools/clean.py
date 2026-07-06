#!/usr/bin/env python3
"""Remove generated artifacts and temporary files."""
from __future__ import annotations

import argparse
import shutil
import sys

from lib.paths import DIST, ROOT


TEMP_PATTERNS = [
    ROOT / "preview.html",
    ROOT / "tools" / "__pycache__",
    ROOT / "tools" / "lib" / "__pycache__",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean generated artifacts")
    parser.add_argument("--dist-only", action="store_true", help="Only clean dist/")
    args = parser.parse_args()

    if DIST.exists():
        shutil.rmtree(DIST)
        print(f"Removed: {DIST}")
    DIST.mkdir(parents=True, exist_ok=True)

    if not args.dist_only:
        for path in TEMP_PATTERNS:
            if path.is_dir():
                shutil.rmtree(path, ignore_errors=True)
                print(f"Removed: {path}")
            elif path.exists():
                path.unlink()
                print(f"Removed: {path}")

    print("Clean complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
