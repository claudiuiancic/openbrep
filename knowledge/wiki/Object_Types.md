---
type: reference
status: stable
tags: [object-type, subtype, wall, door, window, object, host, library-part]
aliases: [Object_Types, object subtype, library part type, door, window, object, wall-hosted]
source: official:gdl.graphisoft.com/reference-guide/global-variables
---

# Object_Types

In OpenBrep, object type should normally mean the library part's intended subtype and host behavior, not a generated `SYMBOL` integer table.

The most important distinction for generated GDL objects is whether the object is a generic placed object, a wall-hosted door/window, or another specialized library part.

## Recommended OpenBrep Types

| Type | Typical Use | Notes |
|---|---|---|
| Generic object | Furniture, casework, fixtures, equipment | Best default for OpenBrep-created parametric objects |
| Door | Wall-hosted door | Requires door/window subtype metadata and wall opening behavior |
| Window | Wall-hosted window | Requires door/window subtype metadata and wall opening behavior |
| Label / marker | Annotation | Different script and context expectations |
| Curtain wall part | Panel, frame, junction | Specialized host context; do not generate by default |

## Recommended OpenBrep Use

- Use generic object behavior unless the user explicitly asks for a door, window, label, marker, or host-specific object.
- Do not try to change object type from GDL script at runtime.
- Do not infer object type from a fake `GLOBALS SYMBOL` declaration.
- For furniture and cabinet generation, rely on explicit parameters `A`, `B`, `ZZYZX`, material parameters, and manual 2D/HOTSPOT2 behavior.
- For door/window generation, plan for host-wall assumptions, opening behavior, sill/head parameters, and wall thickness globals.

## Example: Generic Object Fallback

```gdl
! Generic furniture/object behavior.
! Dimensions are explicit parameters, not inferred from host type.
BLOCK A, B, ZZYZX
```

## Example: Host-Aware Depth Fallback

```gdl
IF WALL_THICKNESS > 0 THEN
    _depth = WALL_THICKNESS
ELSE
    _depth = B
ENDIF
```

## Edge Cases & Traps

- A generated GDL script cannot turn a generic object into a proper Archicad door or window by setting a variable.
- Door/window behavior depends on subtype and library part metadata, not only on script text.
- Host globals such as `WALL_THICKNESS` only make sense in compatible contexts.
- Always include a generic fallback when using host-dependent information.
- Avoid hard-coded `SYMBOL` tables unless they are verified against the target Archicad version and object subtype.

## Related

- [[GLOBALS]] — using official global variables
- [[Paramlist_XML]] — explicit object parameters
- [[HOTSPOT2]] — user-editable 2D controls
