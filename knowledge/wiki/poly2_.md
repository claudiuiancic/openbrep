---
id: wiki.generated.poly2_
type: wiki
category: 3d
commands: ["POLY2_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_

POLY2_ n, frame_fill, x1, y1, s1, ..., xn, yn, sn

y

|n|
|---|


2

1

x

Similar to the POLY2 command, but any of the edges can be omitted. If si = 0, the edge starting from the (xi,yi) apex will be omitted. If si = 1, the vertex should be shown. si = -1 is used to define holes directly. You can also define arcs and segments in the polyline using additional status code values.

Restriction of parameters: n >= 2

n: number of nodes.

- x1, y1, ..., xn, yn: coordinates of each nodes. frame_fill:


frame_fill = j1 + 2*j2 + 4*j3 + 8*j4 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j1: draw contour,
- j2: draw fill,
- j3: close an open polygon,
- j4: local fill orientation, j6: fill is cut fill (default is drafting fill), j7: fill is cover fill (only if j6 = 0, default is drafting fill).


si: Status values: si = j1 + 16*j5 + 32*j6, where each j can be 0 or 1. j1: next segment is visible, j5: next segment is inner line (if 0, generic line), j6: next segment is contour line (effective only if j5 is not set),

-1: end of a contour. Default line property for POLY2_ lines is 0 (generic line), the LINE_PROPERTY command has no effect on POLY2_ edges. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details.