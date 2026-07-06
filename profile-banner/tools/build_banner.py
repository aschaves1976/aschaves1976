#!/usr/bin/env python3
"""Build distribution artifacts from src/banner.svg."""
from __future__ import annotations

import argparse
import shutil
import sys

from lib.paths import BANNER_DIST, BANNER_SRC, DIST, ROOT


def main() -> int:
    parser = argparse.ArgumentParser(description="Build profile banner distribution")
    parser.add_argument("--skip-validate", action="store_true", help="Skip validation step")
    args = parser.parse_args()

    if not BANNER_SRC.exists():
        print(f"ERROR: Source not found: {BANNER_SRC}")
        return 1

    if not args.skip_validate:
        from validate_svg import main as validate_main

        if validate_main() != 0:
            print("Build aborted due to validation errors.")
            return 1

    DIST.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BANNER_SRC, BANNER_DIST)

    print(f"Built: {BANNER_DIST}")
    print(f"Project root: {ROOT}")
    print("Next: python tools/optimize_svg.py && python tools/export_png.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
