---
id: wiki.generated.pyramid
type: wiki
category: 3d
commands: ["PYRAMID"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PYRAMID

PYRAMID n, h, mask, x1, y1, s1, ..., xn, yn, sn

z

h

j3

y

n

j1

1

x

j5

2

Pyramid based on a polyline in the x-y plane. The peak of the pyramid is located at (0, 0, h). n: number of polyline nodes. mask: controls the existence of the bottom and (in the case of an open polyline) side polygon.

mask = j1 + 4*j3 + 16*j5, where each j can be 0 or 1. j1: base surface is present, j3: side (closing) surface is present, j5: base edges are visible. si: status of the lateral edges.

- 0: lateral edges starting from the node are all visible,
- 1: lateral edges starting from the node are used for showing the contour.


Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details. Restriction of parameters:

h > 0 and n > 2

Example:

PYRAMID 4, 1.5, 1+4+16,

- -2, -2, 0,
- -2, 2, 0, 2, 2, 0, 2, -2, 0


PYRAMID 4, 4, 21,

- -1, -1, 0, 1, -1, 0, 1, 1, 0,
- -1, 1, 0


for i = 1 to 4 ! four peaks ADD -1.4, -1.4, 0 PYRAMID 4, 1.5, 21,

-0.25, -0.25, 0, 0.25, -0.25, 0, 0.25, 0.25, 0, -0.25, 0.25, 0

DEL 1 ROTZ 90

next i del 4