# Changelog

## [Unreleased]

### Changed

- **Architecture migration** — Adopted hybrid single-file model
  - `src/banner.svg` is now the sole source of truth
  - Removed fragmented `src/defs/`, `src/layers/`, `scripts/merge_defs.py`
  - Added `tools/` automation pipeline (validate, build, optimize, export, preview, watch, clean)
  - Added `dist/` for generated artifacts

### Added

- Complete banner with 9 internal layers in single SVG
- Project metadata header inside `<svg>`
- Reusable symbols: `primary-node`, `secondary-node`, `pulse-node`, `terminal`, `pad`, `technology-card`, `glow`, `particle`, icons
- `tools/validate_svg.py` — XML, UTF-8, ID, href, section validation
- `tools/build_banner.py` — distribution build
- `tools/optimize_svg.py` — whitespace optimization
- `tools/export_png.py` — PNG export (cairosvg / svglib / inkscape)
- `tools/preview.py` — local preview server
- `tools/watch.py` — file watcher pipeline
- `tools/clean.py` — artifact cleanup
- `requirements.txt` — optional PNG export dependencies

## [1.0.0] - Initial modular architecture (deprecated)

- Multi-file defs/layers structure (replaced by hybrid model)
