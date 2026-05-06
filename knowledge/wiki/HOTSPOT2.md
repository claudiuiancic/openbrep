---
type: concept
status: stable
tags: [hotspot, stretch, plan, 2d, drawing, interactive, editing]
aliases: [HOTSPOT2, hotspot, stretch hotspot, 2d hotspot]
source: raw/ccgdl_dev_doc/docs/GDL_11_2D_Advanced.md
---

# HOTSPOT2

`HOTSPOT2` defines an interactive hotspot in the 2D plan view. Hotspots are the draggable points that users see when they select a GDL object in the ArchiCAD floor plan — they enable direct parametric editing through the mouse.

## Why HOTSPOT2?

Parameters are powerful, but changing a value in the dialog box is slow. With `HOTSPOT2`, users can click and drag geometry directly in the plan view. The hotspot movement is automatically linked to a parameter, making the object feel like a native ArchiCAD element.

## Syntax

```gdl
HOTSPOT2 x, y [, unID [, paramReference [, flags [, displayParam [, "customDescription"]]]]]
```

| Param               | Type    | Description                                                   |
|---------------------|---------|---------------------------------------------------------------|
| `x, y`              | length  | Position in 2D plan coordinates                               |
| `unID`              | integer | Unique hotspot identifier in the 2D Script                    |
| `paramReference`    | param   | Parameter edited by graphical hotspot editing                 |
| `flags`             | integer | Hotspot type and attributes                                   |
| `displayParam`      | param   | Parameter displayed in the information palette while editing  |
| `customDescription` | string  | Custom label for the displayed parameter                      |

When only `x, y` are given, the hotspot is a fixed selection/reference point. Editable hotspots require the official graphical-editing pattern: length editing needs base, moving and reference hotspots with matching `paramReference` and appropriate `flags`.

## Examples

### Rectangle with editable width and depth

```gdl
HOTSPOT2 0, 0, 1
HOTSPOT2 A, 0, 2
HOTSPOT2 A, -0.1, 3, A, 3
HOTSPOT2 A, 0, 4, A, 2
```

### Corner hotspot

```gdl
! A single corner stretch for a rectangular column
HOTSPOT2 0, 0, 1
HOTSPOT2 A, 0, 2
HOTSPOT2 A, B, 3
HOTSPOT2 0, B, 4
```

## Edge Cases & Traps

- **HOTSPOT2 in 3D script**: hotspots only work in the 2D script. Placing them in the 3D script has no effect.
- **Overlapping hotspots**: if two hotspots share the same position, the last one defined takes precedence for dragging. This can cause confusing behavior — avoid duplicates.
- **Parameter type**: the linked `paramReference` must be a compatible numeric parameter. Boolean parameters cannot be driven by stretch hotspots.
- **Editable hotspots require a set**: for length editing, define base, moving and reference hotspots. A single `HOTSPOT2 x, y, "A"` is not the official editable pattern.
- **Angle hotspots**: for angle parameters, place the hotspot at the endpoint of a radius and link the rotation to the angle parameter in the Parameter script.
- **No visual feedback**: hotspots themselves are just invisible interaction points. Draw visible geometry ([[PROJECT2]], `RECT2`, etc.) separately to show the user what they're dragging.
- **Coordinate system**: hotspot positions are in the 2D script's coordinate space, which may differ from the 3D script's [[Transformation_Stack]].

## Convention: Complete set

A well-designed GDL object provides hotspots for every primary dimension parameter. At minimum, include:

```gdl
! Origin (always)
HOTSPOT2 0, 0
! Width stretch: base/reference/moving pattern
HOTSPOT2 A, 0, 11, A, 1
HOTSPOT2 A, -0.1, 12, A, 3
HOTSPOT2 A, 0, 13, A, 2
```

## Related

- [[PROJECT2]] — drawing 2D representations of 3D geometry
- [[Paramlist_XML]] — defining parameters that hotspots link to
- [[BLOCK]] — 3D geometry that hotspots control indirectly
