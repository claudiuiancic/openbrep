---
type: concept
status: stable
tags: [3d, geometry, cylinder, primitives]
aliases: [CYLIND, cylinder, cylindrical primitive, cyl]
source: official:gdl.graphisoft.com/reference-guide/basic-shapes
---

# CYLIND

`CYLIND` creates a right circular cylinder aligned to the local Z axis. Use it for simple round legs, posts, rods, columns, pins, and similar circular primitives.

## Official Syntax

```gdl
CYLIND h, r
```

| Param | Type | Meaning |
|---|---|---|
| `h` | length | Height along the local Z axis |
| `r` | length | Radius of the circular section |

The base circle is centered on the local origin in the x-y plane. Move or rotate the cylinder with the transformation stack (`ADD`, `ROTX`, `ROTY`, `ROTZ`, `DEL`).

## Recommended OpenBrep Use

- Use `CYLIND h, r` only for straight cylinders.
- Use `ADD x, y, z` before `CYLIND` when the cylinder center must move.
- Use `ROTX 90` or `ROTY 90` before `CYLIND` for horizontal rods.
- Use [[CONE]] or higher-level polyline shapes for tapered geometry; do not invent a multi-radius `CYLIND`.
- Prefer [[BLOCK]] or [[PRISM_]] for rectangular or profiled members.

## Examples

### Vertical table leg

```gdl
ADD leg_x, leg_y, 0
CYLIND table_h, leg_r
DEL 1
```

### Horizontal round rail

```gdl
ADD 0, rail_y, rail_z
ROTY 90
CYLIND rail_len, rail_r
DEL 2
```

## Edge Cases & Traps

- Official syntax is `CYLIND h, r`; it is not `CYLIND x, y, r1, r2, h`.
- There is no official `segments` argument on `CYLIND`.
- If `h = 0`, Archicad generates a circle in the x-y plane.
- If `r = 0`, Archicad generates a line along the z axis.
- Both `h` and `r` should normally be positive for generated production objects.
- `CYLIND` does not set material by itself; set material before drawing if needed.

## Related

- [[BLOCK]] — simple rectangular primitive
- [[PRISM_]] — extruded polygon profile
- [[Transformation_Stack]] — positioning and orientation
