# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-06

First public release. Professional GitHub profile banner with full tooling,
documentation, and CI.

### Added

#### PR #7 — Open Source Readiness
- Complete documentation suite in `docs/`
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- GitHub issue templates, PR template, CI workflow (`validate.yml`)
- Automated test suite in `tests/`
- `Makefile`, `pyproject.toml`, `.gitignore`
- `tools/validate_structure.py` for repository structure checks
- SVG accessibility: `<title>`, `<desc>`, accessibility validation warnings
- `docs/validation-report.md`

#### PR #6 — SVG Animation System
- `layer-animations` with SMIL-only motion (pulse, glow, energy flow, particles, ambient)
- Animation symbols: `animation-energy-dot`, `animation-pulse-ring`
- Energy motion paths: `energy-path-left-primary`, `energy-path-right-primary`, `energy-path-left-branch`
- Card opacity shimmer (no float/scale)
- Micro highlight opacity breathe
- `docs/animation-guidelines.md`

#### PR #5 — Visual Composition
- Repositioned typography and cards (margin x=72, name y=108, cards y=224)
- Rebalanced circuit and decoration opacities
- Fixed layer comment duplication

#### PR #4 — Technology Cards
- Premium glassmorphism `technology-card` symbol (200×64, rx=12)
- Redesigned icons: `icon-python`, `icon-apex`, `icon-migration`
- Three cards: Python, Oracle APEX, Data Migration

#### PR #3 — Typography
- Refactored `layer-typography` with four hierarchy levels
- Optical kerning on name via `<tspan dx>`
- IDs: `main-title`, `professional-title`, `professional-summary`

#### PR #2 — Organic Circuits
- Redesigned `layer-organic-circuits` with six depth subgroups
- New node symbols: `connection-node`, `anchor-node`, `micro-node`, pad variants, terminal variants
- Organic Bézier paths replacing PCB-style traces

#### PR #1 — Background
- Enhanced `layer-background`: 7-stop gradient, ambient lights, vignette, noise pattern, micro highlights

#### Infrastructure
- Hybrid single-file architecture (`src/banner.svg`)
- Tool pipeline: validate, build, optimize, export, preview, watch, clean
- `tools/lib/svg_utils.py` validation engine
- MIT License

### Changed

- Migrated from deprecated multi-file defs/layers structure to single-file hybrid model
- Project status: Released (v1.0.0)

## [0.1.0] - Deprecated

Initial modular architecture with fragmented `src/defs/`, `src/layers/`, and
`scripts/merge_defs.py`. Replaced by hybrid model in v1.0.0.

[1.0.0]: https://github.com/OWNER/REPO/releases/tag/v1.0.0
