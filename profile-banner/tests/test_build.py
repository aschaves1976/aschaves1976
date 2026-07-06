"""Build pipeline tests."""
from __future__ import annotations

import importlib.util
import sys

import pytest

from lib.paths import BANNER_DIST, BANNER_MIN, BANNER_SRC, ROOT

TOOLS = ROOT / "tools"


def _load_tool_module(name: str):
    path = TOOLS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(TOOLS))
    try:
        spec.loader.exec_module(module)
    finally:
        if str(TOOLS) in sys.path:
            sys.path.remove(str(TOOLS))
    return module


def test_build_produces_dist_svg(monkeypatch):
    if BANNER_DIST.exists():
        BANNER_DIST.unlink()
    monkeypatch.setattr(sys, "argv", ["build_banner.py"])
    build = _load_tool_module("build_banner")
    assert build.main() == 0
    assert BANNER_DIST.is_file()
    assert BANNER_DIST.read_text(encoding="utf-8") == BANNER_SRC.read_text(encoding="utf-8")


def test_optimize_produces_minified_svg(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["build_banner.py"])
    build = _load_tool_module("build_banner")
    monkeypatch.setattr(sys, "argv", ["optimize_svg.py"])
    optimize = _load_tool_module("optimize_svg")
    assert build.main() == 0
    assert optimize.main() == 0
    assert BANNER_MIN.is_file()
    assert BANNER_MIN.stat().st_size <= BANNER_DIST.stat().st_size


def test_export_png_optional(monkeypatch):
    """PNG export is optional; skip when dependencies are unavailable."""
    monkeypatch.setattr(sys, "argv", ["export_png.py"])
    export = _load_tool_module("export_png")
    try:
        code = export.main()
    except OSError:
        pytest.skip("PNG export backend (Cairo) unavailable")
    if code != 0:
        pytest.skip("PNG export dependencies unavailable")
