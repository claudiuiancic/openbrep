---
id: wiki.generated.wallhole2
type: wiki
category: 2d
commands: ["WALLHOLE2"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WALLHOLE2

WALLHOLE2 n, fill_control, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, fillAngle, x1, y1, s1,

... xn, yn, sn

Wall opening definition for the plan view coupled with a cover polygon. Only the cut part of the wall is affected, view wall polygons stay intact. The cover polygon has no contour.

The parameterization of the command is mainly the same as the one of the POLY2_B{2} command. fill_control:

fill_control = 2*j2 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1. j2: draw cover fill on the polygon,

- j4: local fill orientation,
- j5: local fill should align with the wall direction (fill origin is at the wall origin and directions are matching),
- j6: fill is cut fill (default is drafting fill),
- j7: fill is cover fill (only if j6 = 0, default is drafting fill).