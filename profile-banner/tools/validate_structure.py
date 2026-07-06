#!/usr/bin/env python3
"""Validate repository structure for open-source readiness."""
from __future__ import annotations

import sys

from lib.project_structure import validate_project_structure
from lib.paths import ROOT


def main() -> int:
    print(f"Validating project structure at {ROOT} ...")
    result = validate_project_structure(ROOT)

    if result.errors:
        for error in result.errors:
            print(f"  [fail] {error}")
        print("\nStructure validation FAILED")
        return 1

    print("  [ok] All required paths present")
    print("\nStructure validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
