"""Project structure validation for CI and local checks."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .paths import ROOT

REQUIRED_PATHS = [
    "src/banner.svg",
    "tools/validate_svg.py",
    "tools/build_banner.py",
    "tools/optimize_svg.py",
    "tools/export_png.py",
    "tools/preview.py",
    "tools/watch.py",
    "tools/clean.py",
    "tools/lib/svg_utils.py",
    "tools/lib/paths.py",
    "docs/architecture.md",
    "docs/animation-guidelines.md",
    "docs/composition-guidelines.md",
    "docs/design-system.md",
    "docs/typography-guidelines.md",
    "docs/visual-guidelines.md",
    "docs/coding-standards.md",
    "docs/validation-report.md",
    "tests/test_svg_validation.py",
    "tests/test_build.py",
    "tests/test_project_structure.py",
    ".github/workflows/validate.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "LICENSE",
    "CHANGELOG.md",
    "Makefile",
    "pyproject.toml",
    "README.md",
]

REQUIRED_DIRS = [
    "src",
    "dist",
    "docs",
    "tools",
    "tools/lib",
    "tests",
    "assets",
    ".github",
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
]


@dataclass
class StructureResult:
    ok: bool = True
    errors: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.ok = False
        self.errors.append(message)


def validate_project_structure(root: Path | None = None) -> StructureResult:
    """Verify required files and directories exist."""
    base = root or ROOT
    result = StructureResult()

    for rel in REQUIRED_DIRS:
        path = base / rel
        if not path.is_dir():
            result.error(f"Missing directory: {rel}")

    for rel in REQUIRED_PATHS:
        path = base / rel
        if not path.is_file():
            result.error(f"Missing file: {rel}")

    return result
