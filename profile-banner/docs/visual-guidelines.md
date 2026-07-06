# Visual Guidelines

Visual language and design principles for the GitHub Profile Banner.

## Concept

The banner communicates **senior engineering credibility** — the aesthetic of
GitHub, Microsoft Azure, Stripe, Linear, and Vercel product surfaces.

It is **not** gaming, cyberpunk, or neon excess.

### Mood Keywords

Sophisticated · Architectural · Calm · Precise · Enterprise · Evolving

### Design North Star

The visitor should perceive a **living, premium surface** — never an
"animated banner." Motion is discovered, not announced.

## Minimalism

| Do | Don't |
|----|-------|
| Restrained palette (9 colors) | Extra accent colors |
| Few focal elements | Competing visual centers |
| Low-opacity decorative layers | Heavy ornamental noise |
| Purposeful negative space | Filling every pixel |

Maximum perceived opacity for decorative layers:

- Tech grid: **8%**
- Circuit highlights subgroup: **9%**
- Noise film: **< 3%**
- Micro highlights: **1.2% – 4%** fill-opacity range

## Visual Hierarchy

```
1. Name (Alessandro Chaves)     — primary focal point
2. Professional title             — positioning statement
3. Technology cards               — capability proof
4. Professional summary           — supporting context
5. Organic circuits               — ambient metaphor
6. Background depth               — atmosphere
```

Typography always wins. Circuits and particles never cross the name block
(left margin x = 72, title zone through y ≈ 180).

## Eye Flow

```
[Name] → [Accent bar] → [Title] → [Cards row] → [Summary]
                ↘                              ↗
            [Circuit left]              [Circuit right]
```

The eye enters at the name (largest, highest contrast), follows the accent
divider to the subtitle, scans the three cards for technology signals, then
reads the summary. Peripheral circuits frame the composition without pulling
focus.

## Color Palette

| Token | Hex | Role |
|-------|-----|------|
| Background | `#050816` | Canvas base |
| Dark Navy | `#08111F` | Depth mid-tone |
| Blue | `#0F2742` | Atmospheric layer |
| Primary | `#2563EB` | Brand, nodes |
| Secondary | `#38BDF8` | Grid, energy |
| Accent | `#5EEAD4` | Pulse, migration |
| White | `#FFFFFF` | Highlights |
| Text | `#CBD5E1` | Primary copy |
| Muted | `#94A3B8` | Secondary copy |

**Rule:** no colors outside this palette. Adjust opacity, not hue.

## Typography

Font stack: `Inter, Segoe UI, system-ui, sans-serif`.

| Level | Size | Weight | Color |
|-------|------|--------|-------|
| Name | 42px | 700 | `#FFFFFF` |
| Title | 16px | 500 | `#CBD5E1` @ 94% |
| Summary | 12.5px | 400 | `#94A3B8` @ 88% |
| Card title | 11px | 500 | `#CBD5E1` |
| Card caption | 9px | 400 | `#94A3B8` |

Optical kerning on the name via `<tspan dx>` adjustments.

See [typography-guidelines.md](typography-guidelines.md).

## Organic Circuits

Circuits represent **data flow**, not PCB traces.

| Rule | Detail |
|------|--------|
| Curves | Cubic Bézier only |
| Stroke | 0.75px – 2px |
| Nodes | `<use>` of node symbols exclusively |
| Placement | Left and right periphery |
| Depth | Six subgroups with decreasing opacity |

Layer opacities (PR #5 composition):

- Background paths: reduced for subtlety
- Primary flows: visible but subordinate to typography
- Highlights: 9% group opacity

## Technology Cards

Premium **glassmorphism** panels:

- Frosted gradient fill (`card-glass-gradient`)
- Gradient border (`card-border-gradient`)
- Inner top highlight (5% white)
- Icon inset area with subtle stroke
- Bottom edge line for depth

Three cards only: Python, Oracle APEX, Data Migration.

Cards do **not** float, scale, or swing. Optional opacity shimmer only.

## Glassmorphism

Achieved without external libraries:

1. Semi-transparent gradient fill
2. White overlay rects at 3–5% opacity
3. Subtle border gradient
4. `filter-card-shadow` for elevation
5. Hover glow via CSS filter (when SVG embedded in HTML)

## Lighting

Three lighting systems work together:

1. **Background ambient lights** — upper-left, lower-right, center radials
2. **Layer 02 ambient lights** — studio-style top/bottom radials + glow orbs
3. **Micro highlights** — small ellipses preventing flat appearance

Glow orbs breathe via opacity animation (8–12s cycles).

## Composition

Canvas: **1400 × 350** (4:1 ratio).

| Zone | X range | Purpose |
|------|---------|---------|
| Content | 72 – 680 | Typography + cards |
| Right visual | 700 – 1400 | Circuits + glow |
| Vertical name | y 108 | Optical center above midline |

Base margin: **x = 72** on all primary content.

See [composition-guidelines.md](composition-guidelines.md).

## Depth

Depth is built through **layer stacking**, not heavy shadows:

1. Solid base → tonal gradient → volume → depth blob
2. Masked depth sweep → ambient lights → noise → vignette
3. Micro highlights → grid → circuits → floating geometry
4. Typography → cards → decorations → animations

## Spacing

Consistent rhythm:

- 72px left margin
- 16px between cards
- ~18px between typography levels
- 88px accent bar width (proportional to name)

## Rules for Future Changes

1. **Never compete with the name** — if a change draws the eye before
   "Alessandro Chaves", reduce it
2. **Opacity before size** — prefer lowering opacity over enlarging elements
3. **Reuse symbols** — new nodes/cards must use the symbol system
4. **One layer per concern** — do not mix typography into circuit layers
5. **Animation in layer 09** — see animation-guidelines.md
6. **Validate after every change** — `python tools/validate_svg.py`

## Visual References

Inspiration only (never copy):

- GitHub profile headers — restraint and hierarchy
- Azure Portal — discrete grids and depth
- Stripe documentation heroes — calm surfaces
- Linear — precision typography
- Vercel — dark surfaces with subtle light

Reference assets: `assets/references/`

## Related Documentation

- [Design System](design-system.md)
- [Composition Guidelines](composition-guidelines.md)
- [Animation Guidelines](animation-guidelines.md)
