#!/usr/bin/env python3
"""Export PNG previews from banner SVG."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from lib.paths import BANNER_DIST, BANNER_SRC, DIST, PREVIEW_FILES


def export_with_cairosvg(svg_path: Path, output: Path, width: int, background: str | None) -> bool:
    try:
        import cairosvg
    except (ImportError, OSError):
        return False

    try:
        kwargs = {"url": str(svg_path), "write_to": str(output), "output_width": width}
        if background:
            kwargs["background_color"] = background
        cairosvg.svg2png(**kwargs)
        return True
    except OSError:
        return False


def export_with_svglib(svg_path: Path, output: Path, width: int) -> bool:
    try:
        from reportlab.graphics import renderPM
        from svglib.svglib import svg2rlg
    except ImportError:
        return False

    drawing = svg2rlg(str(svg_path))
    if drawing is None:
        return False
    scale = width / max(float(drawing.width or 1400), 1.0)
    drawing.width *= scale
    drawing.height *= scale
    drawing.scale(scale, scale)
    renderPM.drawToFile(drawing, str(output), fmt="PNG")
    return True


def export_with_inkscape(svg_path: Path, output: Path, width: int) -> bool:
    inkscape = shutil.which("inkscape")
    if not inkscape:
        return False
    subprocess.run(
        [
            inkscape,
            str(svg_path),
            "--export-type=png",
            f"--export-filename={output}",
            f"--export-width={width}",
        ],
        check=True,
        capture_output=True,
    )
    return True


def export_png(svg_path: Path, output: Path, width: int, background: str | None = None) -> None:
    if export_with_cairosvg(svg_path, output, width, background):
        return
    if background is None and export_with_svglib(svg_path, output, width):
        return
    if export_with_inkscape(svg_path, output, width):
        return
    raise RuntimeError(
        "No PNG exporter available. Install optional deps: pip install cairosvg OR svglib reportlab"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export PNG previews")
    parser.add_argument("--input", default=str(BANNER_DIST if BANNER_DIST.exists() else BANNER_SRC))
    args = parser.parse_args()

    svg_path = Path(args.input)
    if not svg_path.exists():
        print(f"ERROR: SVG not found: {svg_path}")
        return 1

    DIST.mkdir(parents=True, exist_ok=True)

    exports = [
        (PREVIEW_FILES["preview.png"], 1400, None),
        (PREVIEW_FILES["preview@2x.png"], 2800, None),
        (PREVIEW_FILES["preview-dark.png"], 1400, "#050816"),
        (PREVIEW_FILES["preview-light.png"], 1400, "#f8fafc"),
    ]

    try:
        for output, width, bg in exports:
            export_png(svg_path, output, width, bg)
            print(f"Exported: {output} ({width}px)")
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: Inkscape export failed: {exc.stderr.decode(errors='replace')}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
