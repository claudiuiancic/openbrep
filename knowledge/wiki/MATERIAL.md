---
type: reference
status: stable
tags: [material, attribute, surface, 3d]
aliases: [MATERIAL, material command, surface material]
source: knowledge/GDL_3d_commands.md
---

# MATERIAL

`MATERIAL` sets the current surface material for subsequent 3D geometry.

## Syntax

```gdl
[SET] MATERIAL name_string
[SET] MATERIAL index
```

The `SET` keyword is optional in GDL command syntax. For generated OpenBrep objects, prefer a Material parameter from `paramlist.xml` as the value used after `MATERIAL`, not a hard-coded attribute index. This keeps objects editable across Archicad projects.

## Example

```gdl
MATERIAL mat_body
BLOCK A, B, ZZYZX
```

## Recommended Use

- Use separate material parameters for visually distinct parts, such as body, frame, shelf, glass, or front panel.
- Set `MATERIAL` immediately before the geometry it affects.
- Avoid hard-coded numeric materials unless the object is intentionally tied to a specific Archicad attribute set.

## Edge Cases & Traps

- `MATERIAL` affects geometry generated after the command until another material is set.
- If there is no material statement, the official default is `MATERIAL 0`.
- Material index `0` means surfaces use the current pen color with a matte appearance.
- A missing material parameter in `paramlist.xml` can compile or runtime-fail depending on the generated HSF structure.
- Do not use `MATERIAL` as a substitute for semantic part separation; still name parameters and geometry blocks clearly.

## Related

- [[BLOCK]] — common primitive affected by current material
- [[PRISM_]] — extruded profiles affected by current material
- [[Paramlist_XML]] — defining material parameters
