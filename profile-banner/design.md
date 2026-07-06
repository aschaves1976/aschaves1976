# Design Specification

> **Architecture:** Single-file hybrid model. All visual specs below are implemented in `src/banner.svg`.

## Visual Identity

The banner communicates **senior engineering credibility** — the aesthetic of GitHub, Azure, and Stripe product surfaces. Not gaming. Not cyberpunk. Not neon excess.

### Mood Keywords

Sophisticated · Architectural · Calm · Precise · Enterprise · Evolving

---

## Canvas

| Property | Value |
|----------|-------|
| Width | 1400 px |
| Height | 350 px |
| Aspect ratio | 4:1 |
| Responsive | `width="100%"` via HTML wrapper; `viewBox` preserves scale |

---

## Official Palette

| Token | Hex | Usage |
|-------|-----|-------|
| Background | `#050816` | Base fill, deepest shadows |
| Dark Navy | `#08111F` | Mid-tone depth |
| Blue | `#0F2742` | Atmospheric depth |
| Primary | `#2563EB` | Brand, nodes, key accents |
| Secondary | `#38BDF8` | Grid, branches, highlights |
| Accent | `#5EEAD4` | Pulse nodes, migration flows |
| White | `#FFFFFF` | Node cores, card highlights |
| Text | `#CBD5E1` | Primary typography |
| Muted | `#94A3B8` | Subtitles, labels, particles |

No colors outside this palette.

---

## Typography

| Level | Font stack | Weight | Size | Color |
|-------|-----------|--------|------|-------|
| Title | Segoe UI, Inter, system-ui | 600 | 38px | `#FFFFFF` |
| Subtitle | Segoe UI, Inter, system-ui | 500 | 18px | `#CBD5E1` |
| Description | Segoe UI, Inter, system-ui | 400 | 13px | `#94A3B8` |
| Card label | Segoe UI, Inter, system-ui | 500 | 11px | `#CBD5E1` |
| Card role | Segoe UI, Inter, system-ui | 400 | 9px | `#94A3B8` |

Letter-spacing: title `-0.5px`, subtitle `0.3px`, labels `0.2px`.

---

## Layer Z-Order

```
9  animations (SMIL overlays)
8  cards
7  typography
6  decorations
5  circuits
4  tech-grid
3  lights
2  background (depth, noise, vignette)
1  background (solid + main gradient)
```

---

## Background System (ETAPA 2)

Eight composited sub-layers:

1. Solid `#050816`
2. `background-gradient-main`
3. `light-top-radial`
4. `light-bottom-radial`
5. `vignette-radial`
6. `pattern-noise-film` at ~3.5% opacity
7. `background-gradient-depth` with `mask-depth-layer`
8. Micro elliptical highlights (2–3 elements, &lt; 8% opacity)

---

## Tech Grid (ETAPA 3)

- Pattern: `pattern-tech-grid-fade`
- Mask: `mask-grid-content-fade`
- Max perceived opacity: **8%**
- Cell size: 40×40 px
- Fades to invisible near left typography block

---

## Circuits (ETAPA 4)

Organic **data-flow** paths — not PCB traces.

| Rule | Detail |
|------|--------|
| Curves | Cubic Bézier only |
| Stroke range | 0.75px – 2px |
| Nodes | `<use href="#symbol-node-*">` exclusively |
| Branching | Max 3 levels deep per flow |
| Placement | Left and right periphery; never over title |

---

## Technology Cards (ETAPA 7)

| Card | Label |
|------|-------|
| 1 | Oracle PL/SQL Developer |
| 2 | Python Developer |
| 3 | Oracle APEX Enthusiast |
| 4 | Data Migration Specialist |

| Property | Value |
|----------|-------|
| Size | 200 × 56 px |
| Radius | 10 px |
| Fill | `card-glass-gradient` |
| Border | `card-border-gradient`, 1px |
| Shadow | `filter-card-shadow` |
| Hover | `filter-card-hover-glow` via CSS in `<style>` |

---

## Animation Guidelines (ETAPA 9)

| Property | Range |
|----------|-------|
| Duration | 3s – 8s |
| Opacity delta | ≤ 0.3 |
| Motion | Vertical float ≤ 6px |
| Technology | SMIL only (`animate`, `animateTransform`, `animateMotion`) |

---

## Copy

| Element | Text |
|---------|------|
| Name | Alessandro Chaves |
| Subtitle | Oracle Technical Consultant |
| Description | Building reliable enterprise solutions through clean architecture, automation and continuous learning. |

---

## References

Visual inspiration (not imitation):

- GitHub profile headers — restraint and hierarchy
- Azure Portal dashboards — discrete grids
- Stripe documentation heroes — depth without noise
- Linear.app — precision typography
- Vercel — dark surfaces with subtle light

Reference assets: `assets/references/`
