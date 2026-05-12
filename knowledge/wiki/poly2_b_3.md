---
id: wiki.generated.poly2_b_3
type: wiki
category: 3d
commands: ["POLY2_B{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_B{3}

POLY2_B{3} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, x1, y1, s1, ..., xn, yn, sn

Advanced version of the POLY2_B command, where the orientation of the fill can be defined using a matrix. frame_fill:

frame_fill = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1. j1-j7: similar as for previous POLY2_ commands, j8: use sloped fill.

mxx, mxy, myx, myy: if j8 is set, this matrix defines the orientation of the fill. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details.

POLY2_B{4}