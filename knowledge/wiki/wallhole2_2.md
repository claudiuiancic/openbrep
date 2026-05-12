---
id: wiki.generated.wallhole2_2
type: wiki
category: 2d
commands: ["WALLHOLE2{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WALLHOLE2{2}

WALLHOLE2{2} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, innerRadius, x1, y1, s1,

... xn, yn, sn

Advanced version of WALLHOLE2, where fill distortion can be controlled in an enhanced way. It is equivalent to the POLY2_B{5} command in the geometric definition. distortion_flags:

distortion_flags = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1. The valid value for distortion_flags is between 0 and 255. Don’t use value out of this range.

j1-j7: similar to the POLY2_B{5} command, j8: local fill should align with the wall direction (fill origin is at the wall origin and directions are matching), meaningful only when j4 is set. Distortion matrix (mij parameters) are omitted.

Extending the wall polygon