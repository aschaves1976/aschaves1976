# Profile Banner

[![Validate](https://github.com/OWNER/REPO/actions/workflows/validate.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/validate.yml)

Premium SVG banner for the GitHub profile of **Alessandro Chaves** — Oracle
Technical Consultant.

![Banner preview](dist/banner.svg)

## Description

A professional, enterprise-grade GitHub profile banner built as a **software
engineering project**. The SVG is organized into documented layers, reusable
symbols, and a Python automation pipeline — not a one-off graphic file.

## Objectives

- Communicate senior engineering credibility through visual restraint
- Maintain a single source of truth with automated validation
- Enable safe contributions via documented architecture and design system
- Deliver a banner that feels alive without appearing animated

## Motivation

GitHub profile banners are often unstructured SVGs or raster images that are
hard to maintain. This project treats the banner like production code: layered
architecture, reusable components, CI validation, and comprehensive
documentation.

## Demo

```bash
python tools/preview.py
```

Opens a local preview with dark/light background variants.

Or embed directly:

```html
<img src="./profile-banner/dist/banner.svg"
     alt="Alessandro Chaves - Oracle Technical Consultant"
     width="100%"/>
```

For users who prefer reduced motion, serve a static PNG fallback:

```html
<picture>
  <source srcset="dist/banner.svg" media="(prefers-reduced-motion: no-preference)">
  <img src="dist/preview.png" alt="Alessandro Chaves - Oracle Technical Consultant" width="100%">
</picture>
```

## Project Structure

```
profile-banner/
├── .github/              # Issue templates, PR template, CI
├── assets/references/    # Visual reference storage
├── dist/                 # Generated artifacts (do not edit)
├── docs/                 # Technical documentation
├── src/
│   └── banner.svg        # Single source of truth
├── tests/                # Automated test suite
├── tools/                # Validation and build pipeline
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
└── SECURITY.md
```

## Architecture

**Hybrid single-file model:** all visual content lives in `src/banner.svg`.
Internal modularity is achieved through `<defs>`, `<symbol>`, named layers, and
section comments. Python tools validate and distribute — they never modify the
source.

```
src/banner.svg
    │
    ├── tools/validate_svg.py
    ├── tools/build_banner.py      → dist/banner.svg
    ├── tools/optimize_svg.py      → dist/banner.min.svg
    └── tools/export_png.py        → dist/preview*.png
```

Full details: [`docs/architecture.md`](docs/architecture.md)

## SVG Organization

| Layer | ID | Content |
|-------|-----|---------|
| 01 | `layer-background` | Depth surface, noise, vignette |
| 02 | `layer-ambient-lights` | Studio lighting |
| 03 | `layer-tech-grid` | Discrete grid pattern |
| 04 | `layer-organic-circuits` | Bézier data-flow paths |
| 05 | `layer-floating-geometry` | Particles, micro-dots |
| 06 | `layer-typography` | Name, title, summary |
| 07 | `layer-technology-cards` | Python, APEX, Migration |
| 08 | `layer-decorations` | Final polish |
| 09 | `layer-animations` | SMIL ambient motion |

## Technologies

| Technology | Role |
|------------|------|
| SVG 1.1 | Banner format |
| SMIL | Native animations (no JavaScript) |
| Python 3.10+ | Validation and build tooling |
| pytest | Automated tests |
| GitHub Actions | CI pipeline |

## Tools

| Script | Purpose |
|--------|---------|
| `validate_svg.py` | XML, UTF-8, IDs, hrefs, sections, accessibility |
| `validate_structure.py` | Repository structure check |
| `build_banner.py` | Copy source → `dist/banner.svg` |
| `optimize_svg.py` | Whitespace optimization → `dist/banner.min.svg` |
| `export_png.py` | PNG previews (optional deps) |
| `preview.py` | Local browser preview server |
| `watch.py` | Auto-rebuild on source change |
| `clean.py` | Remove generated artifacts |

## Quick Start

### Prerequisites

- Python 3.10 or later
- Optional: `svglib` + `reportlab` for PNG export

### Validate

```bash
python tools/validate_svg.py
```

### Build

```bash
python tools/build_banner.py
python tools/optimize_svg.py
```

### Test

```bash
pip install pytest
pytest tests/ -v
```

### Export PNG

```bash
pip install -r requirements.txt
python tools/export_png.py
```

### Make (all targets)

```bash
make all
```

## Documentation

| Document | Topic |
|----------|-------|
| [architecture.md](docs/architecture.md) | SVG structure, layers, build system |
| [visual-guidelines.md](docs/visual-guidelines.md) | Design principles and visual language |
| [design-system.md](docs/design-system.md) | Components, tokens, symbols |
| [typography-guidelines.md](docs/typography-guidelines.md) | Type hierarchy and kerning |
| [composition-guidelines.md](docs/composition-guidelines.md) | Spatial layout and balance |
| [animation-guidelines.md](docs/animation-guidelines.md) | SMIL animation system |
| [coding-standards.md](docs/coding-standards.md) | Engineering conventions |
| [validation-report.md](docs/validation-report.md) | Latest validation results |

## Roadmap

Future evolution ideas (not committed):

- [ ] Automated PNG export in CI
- [ ] Responsive banner variants (mobile crop)
- [ ] Alternative color themes (light variant)
- [ ] CLI wrapper (`banner-cli validate|build|export`)
- [ ] Visual editor for non-SVG contributors
- [ ] `prefers-reduced-motion` static SVG variant

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). By participating, you agree to our
[Code of Conduct](CODE_OF_CONDUCT.md).

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

## License

MIT — Copyright (c) 2026 Alessandro Chaves. See [LICENSE](LICENSE).

## Author

**Alessandro Chaves** — Oracle Technical Consultant

Building reliable enterprise solutions through clean architecture, automation,
and continuous learning.
