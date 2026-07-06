# Architecture

## Hybrid Model

After architectural review, this project adopts a **hybrid architecture**:

- **One SVG file** (`src/banner.svg`) is the single source of truth
- **Internal modularity** via `<defs>`, `<symbol>`, named layers, and section comments
- **Python automation** handles validation, build, optimization, and export
- **No fragmented SVG files** — no `defs/`, `layers/`, or merge scripts

### Why

| Problem (multi-file) | Solution (hybrid) |
|---------------------|-------------------|
| Complex build / merge | No merge step |
| Duplicate IDs across files | Single ID namespace |
| Broken `url(#id)` imports | All references local |
| Hard XML validation | One file to validate |
| Noisy Git diffs | One coherent history |

## Source of Truth

```
src/banner.svg
```

Approx. 535 lines, organized by section comments. Never edit `dist/` manually.

## Internal Structure

```
banner.svg
│
├── Header (XML + <svg> attributes)
├── Metadata (project comment block)
├── SVG Definitions
│     Colors (CSS classes)
│     Gradients
│     Filters
│     Patterns
│     Masks
│     Clip Paths
│     Symbols
│     Animations
├── Layer 01 — Background
├── Layer 02 — Ambient Lights
├── Layer 03 — Tech Grid
├── Layer 04 — Organic Circuits
├── Layer 05 — Floating Geometry
├── Layer 06 — Typography
├── Layer 07 — Technology Cards
├── Layer 08 — Decorations
├── Layer 09 — Animations
└── Footer
```

## Component Reuse

```
<defs>
  <symbol id="primary-node">...</symbol>
</defs>

<use href="#primary-node" x="146" y="126" width="16" height="16"/>
```

Never duplicate geometry. Never draw nodes inline.

## Tool Pipeline

```
src/banner.svg
       │
       ▼
 validate_svg.py    XML, UTF-8, IDs, hrefs, sections
       │
       ▼
 build_banner.py     → dist/banner.svg
       │
       ▼
 optimize_svg.py     → dist/banner.min.svg
       │
       ▼
 export_png.py      → dist/preview*.png
```

`watch.py` runs the full pipeline on file changes.

### Tool Responsibilities

| Script | Modifies `src/banner.svg`? | Output |
|--------|---------------------------|--------|
| `validate_svg.py` | No | Exit code + report |
| `build_banner.py` | No | `dist/banner.svg` |
| `optimize_svg.py` | No | `dist/banner.min.svg` |
| `export_png.py` | No | `dist/preview*.png` |
| `preview.py` | No | Local HTTP server |
| `watch.py` | No | Pipeline on change |
| `clean.py` | No | Removes `dist/` |

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Layer group | `layer-{name}` | `layer-typography` |
| Symbol | `{semantic-name}` | `primary-node` |
| Gradient | `{purpose}-gradient-{variant}` | `background-gradient-main` |
| Filter | `filter-{effect}` | `filter-glow-primary` |
| Element | `{semantic-name}` | `main-title`, `top-light` |

## XML Comment Rule

SVG is XML. Comments **must not** contain `--`:

```xml
<!-- OK: section delimiter -->
<!-- ====== -->

<!-- INVALID: double hyphen inside -->
<!-- -------- -->
```

## Extension Points

| Change | Section |
|--------|---------|
| Palette | `<!-- COLORS -->` + gradient stops |
| Typography | `<!-- LAYER 06 -->` |
| New card | `<!-- LAYER 07 -->` + new symbol |
| New circuit | `<!-- LAYER 04 -->` + `<use>` |
| Animation | `<!-- LAYER 09 -->` |

## Design Reference

Visual specification: [`design.md`](design.md)
