---
id: wiki.generated.poly2_b_2
type: wiki
category: 3d
commands: ["POLY2_B{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_B{2}

- POLY2_B{2} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, fillAngle, x1, y1, s1, ..., xn, yn, sn


Advanced version of the POLY2_B command where the hatching origin and direction can be defined. frame_fill:

frame_fill = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j1: draw contour
- j2: draw fill
- j3: close an open polygon
- j4: local fill orientation
- j5: global fill origin (effective only if j4 is set)
- j6: fill in cut category (distinctive with j7, drafting category if none is set)
- j7: fill in cover category (distinctive with j6, drafting category if none is set).


fillOrigoX: X coordinate of the fill origin. fillOrigoY: Y coordinate of the fill origin. fillAngle: direction angle of fill.

Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details.