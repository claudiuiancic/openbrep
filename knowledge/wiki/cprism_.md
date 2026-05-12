---
id: wiki.generated.cprism_
type: wiki
category: other
commands: ["CPRISM_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CPRISM_

CPRISM_ top_material, bottom_material, side_material, n, h, x1, y1, s1, ..., xn, yn, sn

Extension of the PRISM_ command. The first three parameters are used for the material name/index of the top, bottom and side surfaces. The other parameters are the same as above in the PRISM_ command. Restriction of parameters:

n >= 3 See also the section called “Materials”. si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. See Status Codes for details.

Example: Material referencing a predefined material by name, index and global variable

CPRISM_ "Mtl-Iron", 0, SYMB_MAT, 13, 0.2, 0, 0, 15, 2, 0, 15, 2, 2, 15, 0, 2, 15, 0, 0, -1, !end of the contour

- 0.2, 0.2, 15,
- 1.8, 0.2, 15,


- 1.0, 0.9, 15, 0.2, 0.2, -1, !end of first hole 0.2, 1.8, 15, 1.8, 1.8, 15,
- 1.0, 1.1, 15, 0.2, 1.8, -1 !end of second hole