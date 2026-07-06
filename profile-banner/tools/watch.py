#!/usr/bin/env python3
"""Watch banner.svg and run validate, build, optimize, export pipeline."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

from lib.paths import BANNER_SRC, ROOT


def run_step(script: str) -> bool:
    result = subprocess.run([sys.executable, str(ROOT / "tools" / script)], cwd=ROOT)
    return result.returncode == 0


def pipeline() -> bool:
    print("\n--- Pipeline start ---")
    steps = [
        "validate_svg.py",
        "build_banner.py",
        "optimize_svg.py",
        "export_png.py",
    ]
    for step in steps:
        print(f"\n>> {step}")
        if not run_step(step):
            print(f"Pipeline stopped at {step}")
            return False
    print("\n--- Pipeline complete ---")
    return True


def main() -> int:
    if not BANNER_SRC.exists():
        print(f"ERROR: {BANNER_SRC} not found")
        return 1

    print(f"Watching {BANNER_SRC}")
    print("Press Ctrl+C to stop.\n")

    last_mtime: float | None = None
    pipeline()

    try:
        while True:
            mtime = BANNER_SRC.stat().st_mtime
            if last_mtime is None:
                last_mtime = mtime
            elif mtime != last_mtime:
                last_mtime = mtime
                print(f"\nChange detected in {BANNER_SRC.name}")
                pipeline()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nWatch stopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
