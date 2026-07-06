# Composition Guidelines

Spatial layout and balance rules for the 1400×350 banner canvas.

## Canvas

| Property | Value |
|----------|-------|
| Width | 1400 px |
| Height | 350 px |
| Aspect ratio | 4:1 |
| viewBox | `0 0 1400 350` |
| Responsive | `width="100%"` in HTML; viewBox preserves proportions |

## Content Grid

Primary content aligns to a **72px left margin**:

```
x = 72   — name, title, summary, cards
x = 216  — second card (72 + 200 + 16 gap... actually cards at 0, 216, 432 relative to row)
```

Cards row: `transform="translate(72, 224)"` on `#technology-cards-row`.

## Vertical Rhythm

| Element | Y position | Notes |
|---------|-------------|-------|
| `main-title` | 108 | Primary focal baseline |
| `main-title-shadow` | 109 | +1px depth offset |
| `accent-bar` | 120 | 2px height divider |
| `professional-title` | 146 | 26px below accent |
| `professional-summary` | 170 | Two-line block |
| Technology cards | 224 | 64px card height → ends at y 288 |

Name sits **above vertical center** (175) to leave room for cards below.

## Horizontal Zones

```
|←—— 72px ——→|←—— Content 608px ——→|←—— Visual field 720px ——→|
|   margin    |   typography+cards   |   circuits + glow        |
```

**Rule:** circuits and decorative elements stay in the right visual field
(x > 400 for primary flows). No circuit stroke crosses the name bounding box.

## Layer Opacity Balance (PR #5)

Composition PR adjusted opacities only — no geometry changes:

| Layer / group | Approach |
|---------------|----------|
| `layer-organic-circuits` | Reduced path opacities for subtlety |
| `layer-decorations` | `opacity="0.42"` on group |
| `layer-floating-geometry` | Peripheral placement, low contrast |
| `circuit-layer-highlights` | Group `opacity="0.09"` |

## Technology Cards Layout

```
Card 1 (Python)     x = 0     (absolute x = 72)
Card 2 (APEX)       x = 216   (200 + 16 gap)
Card 3 (Migration)  x = 432
```

Each card: 200×64px. Total row width: 632px (fits within content zone).

## Circuit Placement

Left cluster originates from canvas edge, flows toward center:

- Primary left path: y ≈ 198–248 zone
- Pulse node left: (422, 142)

Right cluster mirrors from right edge:

- Primary right path: y ≈ 132–142 zone
- Pulse node right: (968, 146)

Energy flow paths follow these primary Bézier curves.

## Floating Geometry

Particles and micro-dots placed at periphery:

- Upper area (y < 80): sparse, low opacity
- Lower-right (y > 300): balance visual weight
- Static instances hidden when animated copies render in layer 09

## Focal Point Protection

The name block occupies approximately:

```
x: 72 – 420
y: 80 – 185
```

No element in layers 04–08 should exceed **30% perceived opacity** within
this zone.

## Balance Checklist

Before merging composition changes:

- [ ] Name is the brightest element in the left third
- [ ] Cards form a clear horizontal scan line
- [ ] Right side has visual weight without symmetry
- [ ] No orphaned bright pixels near typography
- [ ] Vertical spacing feels even (18–28px between text levels)
- [ ] 62px minimum clearance between summary and cards

## Related Documentation

- [Visual Guidelines](visual-guidelines.md)
- [Design System](design-system.md)
- [Architecture](architecture.md)
