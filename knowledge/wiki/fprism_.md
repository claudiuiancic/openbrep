---
id: wiki.generated.fprism_
type: wiki
category: other
commands: ["FPRISM_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FPRISM_

FPRISM_ top_material, bottom_material, side_material, hill_material, n, thickness, angle, hill_height, x1, y1, s1,

... xn, yn, sn

Similar to the PRISM_ command, with the additional hill_material, angle and hill_height parameters for forming a ramp on the top. hill_material: the side material of the ramp part. angle: the inclination angle of the ramp side edges.

Restriction: 0 <= angle < 90. If angle = 0, the hill side edges seen from an orthogonal view form a quarter circle with the current resolution (see the RADIUS command, the RESOL command and the TOLER command).

hill_height: the height of the ramp. Note that the thickness parameter represents the whole height of the prism.

si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. Restriction of parameters:

n >= 3, hill_height < thickness See Status Codes for details.

angle

hill_height thickness

n

1

2

- Example 1: Prism with curved ramp


RESOL 10 FPRISM_ "Roof Tile", "Brick-Red", "Brick-White", "Roof Tile",

- 4, 1.5, 0, 1.0, !angle = 0 0, 0, 15,
- 5, 0, 15, 5, 4, 15,


- 0, 4, 15


- Example 2: Prism with straight ramp


FPRISM_ "Roof Tile", "Brick-Red", "Brick-White", "Roof Tile", 10, 2, 45, 1,

- 0, 0, 15, 6, 0, 15, 6, 5, 15,

0, 5, 15,

- 0, 0, -1,
- 1, 2, 15, 4, 2, 15, 4, 4, 15,


- 1, 4, 15,
- 1, 2, -1