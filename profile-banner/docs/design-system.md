# Design System

Component-level specification for the GitHub Profile Banner. All values reflect
the current implementation in `src/banner.svg`.

## Design Tokens

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `background` | `#050816` | Deepest base, shadows |
| `dark-navy` | `#08111F` | Mid-tone depth |
| `blue-depth` | `#0F2742` | Atmospheric depth |
| `primary` | `#2563EB` | Brand, nodes, key accents |
| `secondary` | `#38BDF8` | Grid, branches, highlights |
| `accent` | `#5EEAD4` | Pulse nodes, migration flows |
| `white` | `#FFFFFF` | Node cores, card highlights |
| `text-primary` | `#CBD5E1` | Titles, card labels |
| `text-muted` | `#94A3B8` | Subtitles, captions, particles |

No colors outside this palette.

### Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `margin-x` | 72px | Left content margin |
| `card-gap` | 16px | Gap between technology cards |
| `card-y` | 224px | Cards row baseline |
| `name-y` | 108px | Main title baseline |
| `grid-cell` | 40×40px | Tech grid cell size |

### Radius

| Component | Radius |
|-----------|--------|
| Technology card | 12px (`rx="12"`) |
| Card icon container | 8px |
| Accent bar | 1px (`rx="1"`) |
| Circuit terminals | Rounded via `terminal-rounded` symbol |

### Shadows and Borders

| Effect | Implementation |
|--------|----------------|
| Card shadow | `filter-card-shadow` on `#technology-card` |
| Card hover glow | `filter-card-hover-glow` via CSS `.technology-card:hover` |
| Subtle glow | `filter-glow-subtle` on micro highlights |
| Card border | `card-border-gradient`, 1px stroke |

## Technology Cards

### Shell (`#technology-card`)

| Property | Value |
|----------|-------|
| Size | 200 × 64 px |
| Fill | `url(#card-glass-gradient)` |
| Border | `url(#card-border-gradient)`, 1px |
| Shadow | `url(#filter-card-shadow)` |
| Top highlight | White rect at 5% opacity |
| Icon area | 32×32 inset at (14, 16) |

### Active Cards (Layer 07)

| ID | Label | Caption | Icon |
|----|-------|---------|------|
| `technology-card-python` | Python Developer | Automation and ETL | `#icon-python` |
| `technology-card-apex` | Oracle APEX Enthusiast | Low-Code Applications | `#icon-apex` |
| `technology-card-migration` | Data Migration Specialist | Enterprise Data Pipelines | `#icon-migration` |

Position: `translate(72, 224)` with 216px horizontal offset per card (200 + 16 gap).

Animation: opacity shimmer only (1.00 → 0.93–0.95). No float or scale.

## Circuit Nodes

| Symbol | Size | Description |
|--------|------|-------------|
| `primary-node` | 16×16 | Main junction, blue fill + white core |
| `secondary-node` | 12×12 | Branch junction |
| `pulse-node` | 20×20 | Active data node, accent ring |
| `connection-node` | 14×14 | Hub connector |
| `anchor-node` | 10×10 | Path anchor |
| `micro-node` | 6×6 | Fine junction |

Pads: `pad-solid`, `pad-outline`, `pad-partial` (8×8).
Terminals: `terminal`, `terminal-rounded`, `terminal-mini`.

**Rule:** instantiate only via `<use href="#symbol-id">`.

## Particles and Glow

### `#particle` (4×4)

Small square accent used in floating geometry and decorations layer.

### `#micro-dot` (6×6)

Slightly larger ambient dot for depth accents.

### `#glow` (40×40)

Radial soft orb for ambient lighting. Animated via opacity breathe in layer 09.

## Typography Components

See [typography-guidelines.md](typography-guidelines.md) for full spec.

| Level | ID | Size | Weight |
|-------|-----|------|--------|
| Name | `main-title` | 42px | 700 |
| Title | `professional-title` | 16px | 500 |
| Summary | `professional-summary` | 12.5px | 400 |
| Card title | `card-*-title` | 11px | 500 |
| Card caption | `card-*-caption` | 9px | 400 |

## Reusable Component Checklist

When creating a new symbol:

1. Define in `<defs>` with unique `id`
2. Set explicit `viewBox`
3. Add `<title>` (required) and `<desc>` (when non-obvious)
4. Document in this file
5. Instantiate via `<use>` only

## Animation Symbols

| Symbol | Purpose |
|--------|---------|
| `animation-energy-dot` | Traveling light point on circuit paths |
| `animation-pulse-ring` | Expanding ring on pulse nodes |

Motion paths (`energy-path-*`) are invisible defs used by `animateMotion`.

## CSS Classes (defs style block)

| Class | Purpose |
|-------|---------|
| `.circuit-path` | Stroke caps and joins for circuit paths |
| `.technology-card` | Hover transition to glow filter |

Typography uses inline attributes in layer 06 for precise control; CSS classes
in the style block are legacy references for card hover behavior.

## Related Documentation

- [Visual Guidelines](visual-guidelines.md)
- [Composition Guidelines](composition-guidelines.md)
- [Animation Guidelines](animation-guidelines.md)
