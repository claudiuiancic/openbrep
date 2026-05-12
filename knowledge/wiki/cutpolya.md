---
id: wiki.generated.cutpolya
type: wiki
category: 3d
commands: ["CUTPOLYA"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CUTPOLYA

CUTPOLYA n, status, d, x1, y1, mask1, ..., xn, yn, maskn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

Similar to the CUTPOLY command, but with the possibility to control the visibility of the edges of the generated polygons. The cutting form is a half-infinite tube with the defined polygonal cross-section. If the end of the cutting form hangs down into the body, it will cut out the corresponding area.

Z

j j

2 3

Y

i

j

1

i+1

X

status: controls the treatment of the generated cut polygons. 1: use the attributes of the body for the generated polygons and edges, 2: generated cut polygons will be treated as normal polygons.

d: the distance between the local origin and the end of the half-infinite tube.

0: means a cut with an infinite tube.

maski: similar to the PRISM_ command.

maski = j1 + 2*j2 + 4*j3 + 64*j7, where each j can be 0 or 1.

Example:

ROTX 90 FOR i=1 TO 3

FOR j=1 TO 5

CUTPOLYA 6, 1, 0, 1, 0.15, 5, 0.15, 0.15, 900, 0, 90, 4007, 0, 0.85, 5, 0.85, 0.85, 900, 0, 90, 4007

ADDX 1 NEXT j DEL 5 ADDY 1

NEXT i DEL NTR()-1 ADD -0.2, -0.2, 0 BRICK 5.4, 3.4, 0.5 FOR k=1 TO 15

CUTEND NEXT k DEL TOP