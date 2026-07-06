"""SVG validation tests."""
from __future__ import annotations

import importlib.util
import sys

from lib.paths import BANNER_SRC, ROOT
from lib.svg_utils import read_text, validate_structure


def test_banner_source_exists():
    assert BANNER_SRC.is_file()


def test_utf8_encoding():
    text = read_text(BANNER_SRC)
    assert text.lstrip().startswith("<?xml")
    assert "<svg" in text
    assert len(text) > 50_000


def test_validate_structure_passes():
    result = validate_structure(BANNER_SRC)
    assert result.ok, result.errors


def test_no_duplicate_ids():
    from lib.svg_utils import collect_ids, parse_svg

    root = parse_svg(BANNER_SRC)
    ids = collect_ids(root)
    duplicates = [id_ for id_, count in ids.items() if count > 1]
    assert duplicates == []


def test_required_sections_present():
    text = read_text(BANNER_SRC)
    for section in (
        "SVG DEFINITIONS",
        "LAYER 01 - BACKGROUND",
        "LAYER 09 - ANIMATIONS",
        "FOOTER",
    ):
        assert section in text


def test_gradients_patterns_filters_present():
    text = read_text(BANNER_SRC)
    for token in ("linearGradient", "pattern", "filter", "clipPath", "mask", "symbol"):
        assert token in text


def test_accessibility_metadata():
    text = read_text(BANNER_SRC)
    assert 'role="img"' in text
    assert "aria-label=" in text
    assert "<title>" in text
    assert "<desc>" in text


def test_viewbox_dimensions():
    result = validate_structure(BANNER_SRC)
    assert "Unexpected viewBox" not in " ".join(result.errors)


def test_validate_cli_exit_zero(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["validate_svg.py"])
    validate = _load_validate_module()
    assert validate.main() == 0


def _load_validate_module():
    import importlib.util
    import sys

    path = ROOT / "tools" / "validate_svg.py"
    spec = importlib.util.spec_from_file_location("validate_svg", path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        spec.loader.exec_module(module)
    finally:
        tools_path = str(ROOT / "tools")
        if tools_path in sys.path:
            sys.path.remove(tools_path)
    return module
