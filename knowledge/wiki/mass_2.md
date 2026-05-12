---
id: wiki.generated.mass_2
type: wiki
category: 3d
commands: ["MASS{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MASS{2}

MASS{2} top_material, bottom_material, side_material, n, m, mask, h, x1, y1, z1, s1,

... xn, yn, zn, sn, xn+1, yn+1, zn+1, sn+1,

... xn+m, yn+m, zn+m, sn+m

Extension of the MASS command with an additional mask bit and the possibility of hiding all top edges of the mass. mask:

mask = j1 + 4*j3 + 16*j5 + 32*j6 + 64*j7 + 128*j8 + 256*j9 + 512*j10, where each j can be 0 or 1. j1: base surface is present,

- j3: side surfaces are present, j5: base and side edges are visible, j6: top edges are visible, j7: top edges are visible, top surface is not smooth, j8: all ridges will be sharp, but the surface is smooth. j9: edges participate in line elimination. j10: all top edges will be hidden.


PEN 1 mat = IND (MATERIAL, "Metal-Aluminium") FOR i=1 TO 2 STEP 1

MASS{2} mat, mat, mat, 5, 0, 1+4+16+32+64+256, -1, 0, 0, 0, 15, 2, 0, 0, 15, 2, 2, 0, 15, 0, 2, 0, 15, 0, 0, 0, -1

BODY -1 ADDX 2

NEXT i