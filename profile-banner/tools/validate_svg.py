#!/usr/bin/env python3
"""Validate banner.svg structure, XML, IDs, and references."""
from __future__ import annotations

import argparse
import sys

from lib.paths import BANNER_SRC
from lib.svg_utils import ValidationResult, read_text, validate_structure


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate profile banner SVG")
    parser.add_argument("--file", type=str, default=str(BANNER_SRC), help="SVG file path")
    args = parser.parse_args()

    path = BANNER_SRC if args.file == str(BANNER_SRC) else __import__("pathlib").Path(args.file)

    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return 1

    print(f"Validating {path} ...")

    try:
        read_text(path)
        print("  [ok] UTF-8 encoding")
        print("  [ok] No NULL bytes")
    except ValueError as exc:
        print(f"  [fail] {exc}")
        return 1

    result = validate_structure(path)

    checks = [
        ("Gradients", "linearGradient"),
        ("Patterns", "pattern"),
        ("Filters", "filter"),
        ("ClipPaths", "clipPath"),
        ("Masks", "mask"),
        ("Symbols", "symbol"),
    ]
    text = read_text(path)
    for label, token in checks:
        status = "ok" if token in text else "warn"
        print(f"  [{status}] {label}")

    for warning in result.warnings:
        print(f"  [warn] {warning}")

    if result.errors:
        for error in result.errors:
            print(f"  [fail] {error}")
        print("\nValidation FAILED")
        return 1

    print("\nValidation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
