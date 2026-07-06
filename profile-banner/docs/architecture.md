# Architecture

Technical architecture of the GitHub Profile Banner project.

## Hybrid Model

This project uses a **hybrid single-file architecture**:

| Principle | Implementation |
|-----------|----------------|
| Single source of truth | `src/banner.svg` (~1,090 lines) |
| Internal modularity | `<defs>`, `<symbol>`, named layers, section comments |
| Automation | Python tools in `tools/` |
| No fragmentation | No `defs/`, `layers/`, or merge scripts |

### Why Not Multi-File SVG?

| Multi-file problem | Hybrid solution |
|-------------------|-----------------|
| Merge complexity | No merge step |
| Duplicate IDs | Single ID namespace |
| Broken `url(#id)` across files | All references local |
| Hard validation | One XML document |
| Noisy Git diffs | Coherent history per change |

## Repository Layout

```
profile-banner/
├── src/banner.svg          # Source of truth (edit this)
├── dist/                   # Generated artifacts (never edit)
├── tools/                  # Validation and build pipeline
├── tests/                  # Automated test suite
├── docs/                   # Technical documentation
├── assets/references/      # Visual reference storage
└── .github/                # Templates and CI
```

## SVG Document Structure

```
banner.svg
│
├── XML declaration + root <svg> attributes
├── Metadata comment block (PROJECT, VERSION, STATUS)
├── <title> + <desc> (accessibility)
├── <defs>
│     ├── COLORS (<style> CSS classes)
│     ├── GRADIENTS
│     ├── FILTERS
│     ├── PATTERNS
│     ├── MASKS
│     ├── CLIP PATHS
│     ├── SYMBOLS (reusable components)
│     └── ANIMATIONS (motion paths + animation symbols)
├── Layer 01 — Background (8 sub-layers)
├── Layer 02 — Ambient Lights
├── Layer 03 — Tech Grid
├── Layer 04 — Organic Circuits (6 depth subgroups)
├── Layer 05 — Floating Geometry
├── Layer 06 — Typography
├── Layer 07 — Technology Cards
├── Layer 08 — Decorations
├── Layer 09 — Animations (SMIL overlays)
└── Footer comment
```

## Layer Responsibilities

| Layer | ID | Responsibility |
|-------|-----|----------------|
| 01 | `layer-background` | Depth surface: gradients, noise, vignette, micro highlights |
| 02 | `layer-ambient-lights` | Directional studio lighting + static glow positions |
| 03 | `layer-tech-grid` | Discrete grid pattern, max ~8% perceived opacity |
| 04 | `layer-organic-circuits` | Bézier data-flow paths, nodes, pads, terminals |
| 05 | `layer-floating-geometry` | Hexagons, particles, micro-dots (static instances) |
| 06 | `layer-typography` | Name, title, summary, technology badges |
| 07 | `layer-technology-cards` | Three glass cards with icons |
| 08 | `layer-decorations` | Dot matrix overlay, accent lines |
| 09 | `layer-animations` | SMIL pulse, glow, energy, particles, ambient |

Z-order: background (bottom) → animations (top). Typography and cards sit above circuits so text remains the focal point.

## Symbol System

All repeated geometry is declared once in `<defs>`:

```xml
<symbol id="primary-node" viewBox="0 0 16 16">...</symbol>

<use href="#primary-node" x="111" y="194" width="16" height="16"/>
```

**Rules:**

- Never draw nodes, cards, or icons inline when a symbol exists
- Each symbol includes `<title>` for accessibility
- Animation layer may hide static `<use>` instances (`opacity="0"`) and render animated copies

### Symbol Registry

| Category | Symbols |
|----------|---------|
| Circuit nodes | `primary-node`, `secondary-node`, `pulse-node`, `connection-node`, `anchor-node`, `micro-node` |
| Pads / terminals | `pad`, `pad-solid`, `pad-outline`, `pad-partial`, `terminal`, `terminal-rounded`, `terminal-mini` |
| Effects | `glow`, `particle`, `micro-dot` |
| Cards / icons | `technology-card`, `icon-python`, `icon-apex`, `icon-migration`, `icon-oracle` |
| Animation | `animation-energy-dot`, `animation-pulse-ring` |

## Defs Subsystems

### Gradients

Paint servers for backgrounds, cards, glow, and accent lines. Naming: `{purpose}-gradient-{variant}`.

Key gradients: `background-gradient-main`, `card-glass-gradient`, `card-border-gradient`, `accent-line-gradient`.

### Filters

SVG filter effects for glow, card shadow, and hover states. Naming: `filter-{effect}`.

Examples: `filter-glow-subtle`, `filter-card-shadow`, `filter-card-hover-glow`.

**Performance rule:** filters are static; never animate filter attributes.

### Patterns

`pattern-tech-grid-fade`, `pattern-dot-matrix`, `pattern-noise-film`.

### Masks

`mask-depth-layer`, `mask-grid-content-fade` — control where depth and grid are visible.

### Clip Paths

`clip-banner-bounds` — constrains background layers to canvas.

## Component Composition

Technology cards compose symbols:

```
technology-card-python/
  ├── use #technology-card (glass shell)
  ├── use #icon-python
  └── text (title + caption)
```

Circuits compose paths + node symbols across six depth subgroups (`circuit-layer-background` through `circuit-layer-highlights`).

## Build System

```
src/banner.svg
       │
       ▼
 validate_svg.py     XML, UTF-8, sections, IDs, hrefs, a11y warnings
       │
       ▼
 build_banner.py     → dist/banner.svg (exact copy)
       │
       ▼
 optimize_svg.py     → dist/banner.min.svg (whitespace trim)
       │
       ▼
 export_png.py       → dist/preview*.png (optional deps)
```

| Script | Modifies `src/`? | Output |
|--------|------------------|--------|
| `validate_svg.py` | No | Exit code + report |
| `validate_structure.py` | No | Repository structure check |
| `build_banner.py` | No | `dist/banner.svg` |
| `optimize_svg.py` | No | `dist/banner.min.svg` |
| `export_png.py` | No | PNG previews |
| `preview.py` | No | Local HTTP preview |
| `watch.py` | No | Full pipeline on file change |
| `clean.py` | No | Removes generated files |

## Test System

```
tests/
├── test_svg_validation.py   XML, structure, defs presence, a11y
├── test_build.py              Build + optimize pipeline
└── test_project_structure.py  Required files and directories
```

Run: `pytest tests/ -v` or `make test`.

CI (`.github/workflows/validate.yml`) runs validation, structure check, tests, build, and optimize on every push/PR.

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Layer | `layer-{name}` | `layer-organic-circuits` |
| Symbol | `{semantic-name}` | `pulse-node` |
| Element | `{semantic-name}` | `main-title`, `accent-bar` |
| Animation group | `animation-{purpose}` | `animation-energy-flow` |

## XML Comment Rule

SVG is XML. Comments **must not** contain `--`:

```xml
<!-- OK -->
<!-- ====== -->

<!-- INVALID: breaks XML parser -->
<!-- -------- -->
```

## Extension Points

| Change | Location |
|--------|----------|
| Palette | `<!-- COLORS -->` + gradient stops |
| Typography | `<!-- LAYER 06 -->` |
| New card | `<!-- LAYER 07 -->` + icon symbol |
| New circuit branch | `<!-- LAYER 04 -->` + existing node symbols |
| Animation | `<!-- LAYER 09 -->` per animation-guidelines |

## Design Trade-offs

| Decision | Rationale |
|----------|-----------|
| Single file vs modules | Simpler validation, no broken cross-file refs |
| SMIL vs CSS/JS animations | Works in standalone SVG on GitHub; no dependencies |
| Inline typography vs CSS classes | Precise optical kerning via `<tspan dx>`; classes kept for hover on cards |
| Static + animated duplicate `<use>` | Keeps animation logic isolated in layer 09 |

## Related Documentation

- [Visual Guidelines](visual-guidelines.md)
- [Design System](design-system.md)
- [Animation Guidelines](animation-guidelines.md)
- [Composition Guidelines](composition-guidelines.md)
- [Typography Guidelines](typography-guidelines.md)
- [Coding Standards](coding-standards.md)
