"""Shared path constants for profile-banner tools."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
DIST = ROOT / "dist"
ASSETS = ROOT / "assets"
BANNER_SRC = SRC / "banner.svg"
BANNER_DIST = DIST / "banner.svg"
BANNER_MIN = DIST / "banner.min.svg"

PREVIEW_FILES = {
    "preview.png": DIST / "preview.png",
    "preview-dark.png": DIST / "preview-dark.png",
    "preview-light.png": DIST / "preview-light.png",
    "preview@2x.png": DIST / "preview@2x.png",
}
