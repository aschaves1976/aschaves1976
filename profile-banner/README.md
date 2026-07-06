# Profile Banner

Premium SVG banner for the GitHub profile of **Alessandro Chaves**.

## Architecture (Hybrid)

This project uses a **single source of truth**:

```
src/banner.svg   ← edit this file only
```

All organization happens **inside** the SVG via documented sections, `<symbol>` components, and `<use>` references. Python tools in `tools/` handle validation, build, optimization, and export — they never modify the source SVG.

```
src/banner.svg
    │
    ├── tools/validate_svg.py
    ├── tools/build_banner.py      → dist/banner.svg
    ├── tools/optimize_svg.py      → dist/banner.min.svg
    └── tools/export_png.py        → dist/preview*.png
```

See [`architecture.md`](architecture.md) for the full internal section map.

## Quick Start

```bash
# Validate source SVG
python tools/validate_svg.py

# Build distribution artifacts
python tools/build_banner.py

# Optimize for production
python tools/optimize_svg.py

# Export PNG previews (requires optional deps)
pip install -r requirements.txt
python tools/export_png.py

# Live preview in browser
python tools/preview.py

# Watch mode (validate → build → optimize → export)
python tools/watch.py

# Clean generated files
python tools/clean.py
```

## Project Structure

```
profile-banner/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── architecture.md
├── design.md
├── requirements.txt
│
├── src/
│   └── banner.svg          # Single source of truth (~535 lines)
│
├── tools/
│   ├── build_banner.py
│   ├── validate_svg.py
│   ├── optimize_svg.py
│   ├── export_png.py
│   ├── preview.py
│   ├── watch.py
│   ├── clean.py
│   └── lib/
│
├── dist/                   # Generated artifacts (do not edit)
│   ├── banner.svg
│   ├── banner.min.svg
│   └── preview*.png
│
└── assets/
    └── references/
```

## Internal SVG Organization

| Section | Content |
|---------|---------|
| Metadata | Project header after `<svg>` |
| SVG Definitions | Colors, gradients, filters, patterns, masks, clip paths, symbols, animations |
| Layer 01 | Background (8 sub-layers) |
| Layer 02 | Ambient lights |
| Layer 03 | Tech grid |
| Layer 04 | Organic circuits (Bézier + symbols) |
| Layer 05 | Floating geometry |
| Layer 06 | Typography |
| Layer 07 | Technology cards |
| Layer 08 | Decorations |
| Layer 09 | SMIL animations |
| Footer | End marker |

## Reusable Components

All complex elements are declared as `<symbol>` in `<defs>`:

| Symbol | Purpose |
|--------|---------|
| `primary-node` | Main circuit junction |
| `secondary-node` | Branch junction |
| `pulse-node` | Active data node |
| `terminal` | Endpoint connector |
| `pad` | Connection pad |
| `technology-card` | Glass card shell |
| `glow` | Ambient light orb |
| `particle` | Micro particle |
| `icon-oracle` | Oracle icon |
| `icon-python` | Python icon |
| `icon-apex` | APEX icon |
| `icon-migration` | Migration icon |

Instantiate exclusively via `<use href="#symbol-id">`.

## How to Modify

| Task | Location |
|------|----------|
| Change colors | `<!-- COLORS -->` style block + gradient stops in `<defs>` |
| Change copy | `<!-- LAYER 06 - TYPOGRAPHY -->` |
| Add technology card | `<!-- LAYER 07 -->` + new icon symbol |
| Add circuit branch | `<!-- LAYER 04 -->` using existing node symbols |
| Adjust animations | `<!-- LAYER 09 -->` or animation symbols |

**Important:** XML comments must not contain `--` (double hyphen). Use `====` delimiters only.

## Distribution

Generated files in `dist/`:

| File | Description |
|------|-------------|
| `banner.svg` | Exact copy of source |
| `banner.min.svg` | Whitespace-optimized |
| `preview.png` | 1400px preview |
| `preview@2x.png` | 2800px retina |
| `preview-dark.png` | Dark background variant |
| `preview-light.png` | Light background variant |

## GitHub Integration

```html
<img src="./profile-banner/dist/banner.svg"
     alt="Alessandro Chaves - Oracle Technical Consultant"
     width="100%"/>
```

## License

MIT — see [LICENSE](LICENSE).
