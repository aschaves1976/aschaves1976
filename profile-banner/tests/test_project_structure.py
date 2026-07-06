"""Repository structure tests."""
from __future__ import annotations

from lib.project_structure import validate_project_structure
from lib.paths import ROOT


def test_required_paths_exist():
    result = validate_project_structure(ROOT)
    assert result.ok, result.errors
