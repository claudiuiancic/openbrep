---
type: concept
status: stable
tags: [3d, geometry, cutting, cutplane, boolean, section]
aliases: [CUTPLANE, CUTPLANE2, CUTPLANE3, CUTEND, cut plane]
source: official:gdl.graphisoft.com/reference-guide/cutting-in-3d
---

# CUTPLANE

`CUTPLANE` is a 3D cutting command. It removes parts of enclosed 3D shapes between `CUTPLANE` and `CUTEND`. It is not a floor-plan projection setting and should not be used as a substitute for [[PROJECT2]].

## Official Syntax

```gdl
CUTPLANE [x [, y [, z [, side [, status]]]]]
    statement1
    ...
CUTEND

CUTPLANE{2} angle [, status]
    statement1
    ...
CUTEND

CUTPLANE{3} [x [, y [, z [, side [, status]]]]]
    statement1
    ...
CUTEND
```

Parameter interpretation for `CUTPLANE` / `CUTPLANE{3}`:

| Argument count | Meaning |
|---|---|
| 0 | x-y plane |
| 1 | Plane crosses x axis; value is angle from x-y plane |
| 2 | Plane parallel to z axis, crossing x and y axes at the given values |
| 3 | Plane crosses x, y, and z axes at the given values |
| 4 | Adds `side` to choose which side is removed |
| 5 | Adds `status` for generated cut surfaces |

`side = 0` removes parts above the cutting plane. `side = 1` removes parts below the cutting plane.

## Recommended OpenBrep Use

- Prefer `CUTPLANE{3}` for new generated code when a parameterized cut plane is needed.
- Always close each cut with `CUTEND`.
- Keep transforms used only to position the cutting plane outside the cut body block; remove them before drawing the shape to cut.
- Use `CUTPLANE` only when actual 3D geometry must be trimmed. For 2D symbols, use [[PROJECT2]], [[HOTSPOT2]], and explicit 2D primitives.

## Examples

### Cut the top of a block

```gdl
CUTPLANE{3} 0, 0, cut_z, 0
BLOCK A, B, ZZYZX
CUTEND
```

### Nested cuts

```gdl
CUTPLANE 0, 0, top_cut_z
CUTPLANE 0, side_cut_y, 0, 1
BLOCK A, B, ZZYZX
CUTEND
CUTEND
```

## Edge Cases & Traps

- Missing `CUTEND` can make the cut affect every following shape until the end of the script.
- `CUTPLANE` parameters refer to the current coordinate system at the moment the cut plane is defined.
- Transformations between `CUTPLANE` and `CUTEND` do not move that already-defined cutting plane; they move the geometry being cut.
- `CUTPLANE` in a macro affects only the macro geometry.
- Do not write `CUTPLANE x, y, z, nx, ny, nz`; that point-plus-normal form is not the official GDL syntax.
- Do not claim `CUTPLANE` defines the floor plan cut height. Use project globals and 2D projection logic for floor-plan representation.

## Related

- [[PROJECT2]] — 2D projection of 3D geometry
- [[Transformation_Stack]] — positioning the plane and the cut body
- [[BLOCK]] — common shape used in cut examples
