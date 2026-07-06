# Animation Guidelines

Professional animation system for the GitHub Profile Banner.

## Concept

The banner should feel **alive**, never **animated**.

Animations are perceived only after several seconds of observation. Motion is slow, organic, and desynchronized — inspired by Azure, GitHub, Stripe, Linear, and Vercel dashboards.

## Objectives

- Convey life and sophistication without distraction
- Reinforce data-flow metaphor on circuits
- Never compete with typography (focal point: **Alessandro Chaves**)
- Maintain excellent SVG performance
- Use **native SMIL only** (no JavaScript, no external CSS)

## Principles

| Principle | Rule |
|-----------|------|
| Subtlety | Opacity deltas ≤ 0.15; scale ≤ 1.06 |
| Slowness | 5–18s durations; no fast motion |
| Desync | Unique `begin` offsets per group |
| Reuse | Animate existing `<symbol>` via `<use>` |
| Isolation | All motion logic in `layer-animations` |
| Accessibility | Smooth easing; no strobing |

## Architecture

```
layer-animations/
├── animation-pulse-group      Pulse Animations
├── animation-glow-group       Glow Animations
├── animation-energy-flow      Energy Flow
├── animation-particles        Particles
└── animation-ambient          Ambient Animations
```

Companion animations on existing elements:
- **Technology cards** — opacity shimmer only (in `layer-technology-cards`)
- **Micro highlights** — opacity breathe (in `layer-background`)

Static instances hidden (`opacity="0"`) where animation layer renders the same symbol.

## Animation Catalog

### 1. Pulse Animations (`animation-pulse-group`)

| Target | Symbol | Scale | Duration | Begin |
|--------|--------|-------|----------|-------|
| Primary node left | `primary-node` | 1.00–1.06 | 6.8s | 0s |
| Primary node right | `primary-node` | 1.00–1.05 | 7.6s | 2.1s |
| Pulse node left | `pulse-node` + ring | 1.00–1.06 | 5.5s | 1.4s |
| Pulse node right | `pulse-node` + ring | 1.00–1.05 | 8.2s | 3.7s |

Easing: `spline 0.4 0 0.2 1`

### 2. Glow Animations (`animation-glow-group`)

| Target | Symbol | Opacity range | Duration | Begin |
|--------|--------|---------------|----------|-------|
| Glow top-right | `glow` | 0.18–0.28 | 10.5s | 0s |
| Glow bottom-left | `glow` | 0.11–0.19 | 11.8s | 4.2s |

### 3. Energy Flow (`animation-energy-flow`)

| Dot | Path | Duration | Begin |
|-----|------|----------|-------|
| 1 | `energy-path-left-primary` | 13s | 0.5s |
| 2 | `energy-path-right-primary` | 14.5s | 5.8s |
| 3 | `energy-path-left-branch` | 11s | 8.3s |

Uses `animateMotion` + `mpath`. Dots fade in/out at path ends.

### 4. Particle Drift (`animation-particles`)

| Instance | Symbol | Movement | Duration | Begin |
|----------|--------|----------|----------|-------|
| Geometry 1 | `particle` | ±2px vertical | 14s | 0.3s |
| Geometry 2 | `particle` | ±2.5px diagonal | 16s | 2.8s |
| Decoration 1 | `particle` | ±2px diagonal | 15s | 6.1s |
| Decoration 2 | `particle` | ±2.5px diagonal | 17s | 9.4s |
| Micro-dot 1 | `micro-dot` | ±2px vertical | 13.5s | 1.9s |
| Micro-dot 2 | `micro-dot` | ±2px diagonal | 18s | 7.6s |

### 5. Ambient Animations (`animation-ambient`)

Circuit highlight dots — opacity breathe only (9–10.2s).

### 6. Cards (in-place)

| Card | Opacity range | Duration | Begin |
|------|---------------|----------|-------|
| Python | 1.00–0.94 | 11s | 1.2s |
| APEX | 1.00–0.95 | 12.5s | 3.4s |
| Migration | 1.00–0.93 | 10.8s | 5.1s |

No float, scale, or position animation on cards.

### 7. Micro Highlights (in-place)

Four background ellipses — `fill-opacity` oscillation (9–12s).

## Timing Reference

| Type | Duration |
|------|----------|
| Pulse | 5–9s |
| Glow | 8–12s |
| Energy flow | 8–15s |
| Particles | 12–18s |
| Cards | 10–12.5s |

## Desynchronization

Every group uses unique `begin` values: `0s`, `0.3s`, `0.5s`, `1.1s`, `1.2s`, `1.4s`, `1.9s`, `2.1s`, `2.3s`, `2.8s`, `3.4s`, `3.7s`, `3.9s`, `4.2s`, `5.1s`, `5.8s`, `6.1s`, `6.2s`, `7.6s`, `8.3s`, `9.4s`.

## Performance

| Metric | Estimate |
|--------|----------|
| Active `<animate>` elements | ~35 |
| `animateMotion` instances | 3 |
| Animated filters | 0 |
| File size impact | +~3 KB |
| Render impact | Negligible on modern browsers |

Avoid: animated filters, hundreds of nodes, fast intervals.

## Browser Compatibility

| Browser | SMIL support |
|---------|--------------|
| Chrome | Yes |
| Edge | Yes |
| Firefox | Yes |
| Safari | Yes |

`animateMotion` + `mpath` tested pattern; fallback is static banner (graceful degradation).

## How to Add an Animation

1. Identify an **existing symbol** and position
2. Hide static instance: `opacity="0"` on original `<use>`
3. Add animated `<use>` in appropriate `animation-*` group inside `layer-animations`
4. Set unique `dur` and `begin` values
5. Keep amplitude minimal
6. Update this document
7. Run `python tools/validate_svg.py`

## How to Remove an Animation

1. Delete animation group in `layer-animations`
2. Restore static instance: remove `opacity="0"`
3. Remove unused defs (`energy-path-*`, symbols)
4. Update this document
5. Validate

## Accessibility Notes

- No rapid flashing
- No high-frequency oscillation
- Consider `prefers-reduced-motion` via HTML wrapper in profile README for future enhancement
- Typography contrast unaffected

## Symbols (defs)

| ID | Purpose |
|----|---------|
| `energy-path-left-primary` | Motion path |
| `energy-path-right-primary` | Motion path |
| `energy-path-left-branch` | Motion path |
| `animation-energy-dot` | Traveling dot |
| `animation-pulse-ring` | Node ring pulse |
