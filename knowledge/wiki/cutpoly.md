---
id: wiki.generated.cutpoly
type: wiki
category: 3d
commands: ["CUTPOLY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CUTPOLY

CUTPOLY n, x1, y1, ..., xn, yn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

Similarly to the CUTPLANE command, parameters of CUTPOLY refer to the current coordinate system. The polygon cannot be selfintersecting. The direction of cutting is the Z axis or an optional (x, y, z) vector can be specified. Mirroring transformations affect the cutting direction in an unexpected way - to get a more straightforward result, use the CUTFORM command.

- Example 1:


ROTX 90 MULZ -1 CUTPOLY 3,

0.5, 1, 2, 2, 3.5, 1,

-1.8, 0, 1

DEL 1 BPRISM_ "Brick-Red", "Brick-Red", "Brick-White",

4, 0.9, 7, 0.0, 0.0, 15, 6.0, 0.0, 15, 6.0, 3.0, 15, 0.0, 3.0, 15

CUTEND

- Example 2:


a=1.0 d=0.1 GOSUB "rect_cut"

- ROTX 90 GOSUB "rect_cut" DEL 1
- ROTY -90 GOSUB "rect_cut" DEL 1 BLOCK a, a, a CUTEND CUTEND CUTEND END "rect_cut":


CUTPOLY 4, d, d, a-d, d, a-d, a-d, d, a-d

RETURN

- Example 3:


ROTX 90 FOR i=1 TO 3

FOR j=1 TO 5

CUTPOLY 4, 0, 0, 1, 0, 1, 1, 0, 1

ADDX 1.2 NEXT j DEL 5 ADDY 1.2

NEXT i DEL NTR()-1 ADD -0.2, -0.2, 0 BRICK 6.2, 3.8, 1 FOR k=1 TO 15

CUTEND NEXT k DEL TOP