---
type: concept
status: stable
tags: [prism, 3d, geometry, extrusion, polygon, polyhedron]
aliases: [PRISM, prism command, gdl prism]
source: official:gdl.graphisoft.com/reference-guide/basic-shapes
---

# PRISM_

`PRISM_` creates a right prism from a 2D polygon profile in the local x-y plane. It is the default OpenBrep command for extruded profiles that are more complex than a simple [[BLOCK]].

## Why PRISM_?

Building geometry is rarely just boxes and cylinders. Walls have openings, columns have profiles, roof eaves have complex cross-sections. `PRISM_` handles these cases by defining a 2D polygon, extruding it along the local z axis, and controlling edge or side visibility per polygon point.

## Official Syntax

```gdl
PRISM_ n, h, x1, y1, s1, ..., xn, yn, sn
```

| Param | Type   | Description                                      |
|-------|--------|--------------------------------------------------|
| `n`   | int    | Number of polygon points, including contour-closing and hole-closing points |
| `h`   | length | Prism height along the local Z axis               |
| `x, y`| length | Vertex coordinates (2D polygon in XY plane)       |
| `s`   | int    | Status code per vertex (edge visibility + holes)  |

### Status Codes

The `s` parameter controls both edge visibility and contour nesting:

| Code | Meaning                              |
|------|--------------------------------------|
| 1    | Bottom edge visible                   |
| 2    | Vertical edge visible                 |
| 4    | Top edge visible                      |
| 8    | Side face visible                     |
| 15   | All edges + face visible (most common) |
| 64   | Visible only in contour (curved surfaces) |
| -1   | Close contour / start new hole         |

> Use `15` for every vertex in a simple solid polygon. Use `-1` to close a contour and start a hole.

## Examples

### Basic triangular prism

```gdl
! Triangle with all edges visible
PRISM_ 3, 2.0,
    0,   0,    15,
    1.0, 0,    15,
    0.5, 0.866, 15
```

### Rectangle with hole

```gdl
PRISM_ 9, 1.0,
    ! Outer contour (clockwise) — all edges visible
    0,   0,   15,
    2.0, 0,   15,
    2.0, 1.0, 15,
    0,   1.0, 15,
    0,   0,   -1,    ! close outer, begin inner
    ! Inner contour / hole (counter-clockwise)
    0.4, 0.4, 15,
    0.4, 0.6, 15,
    0.6, 0.6, 15,
    0.6, 0.4, 15
```

### With varying edge visibility

```gdl
! Only vertical edges visible (status=2) — hidden-line style
PRISM_ 4, 1.5,
    0,   0,   2,
    2.0, 0,   2,
    2.0, 1.0, 2,
    0,   1.0, 2
```

## Edge Cases & Traps

- **Argument count**: after `n` and `h`, there must be exactly `n` triplets of `x, y, s`.
- **Zero height** (`h = 0`): degenerates to a 2D polygon (no volume).
- **Self-intersecting polygon**: undefined behavior; ArchiCAD may reject it.
- **Hole count**: the duplicated closing point with status `-1` counts toward `n`.
- **Hole winding**: keep contour and holes consistent. Wrong winding can flip or invalidate the boolean operation.
- **Status `-1` is required** at the end of a contour before starting a hole; omitting it merges vertices into a single invalid polygon.
- **Coordinate system**: `PRISM_` works in the current [[Transformation_Stack]] context. `ADD`/`DEL` and `ROT` affect where the prism appears.

## Related

- [[BLOCK]] — simpler box primitive (use when the cross-section is a rectangle)
- [[BODY_EDGE_PGON]] — lower-level mesh construction for non-prismatic geometry
- [[Transformation_Stack]] — positioning prisms in 3D space
