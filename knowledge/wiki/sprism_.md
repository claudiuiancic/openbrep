---
id: wiki.generated.sprism_
type: wiki
category: other
commands: ["SPRISM_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SPRISM_

SPRISM_ top_material, bottom_material, side_material, n, xb, yb, xe, ye, h, angle, x1, y1, s1,

... xn, yn, sn

Extension of the CPRISM_ command, with the possibility of setting the upper polygon non-parallel with the x-y plane. The upper plane definition is similar to the plane definition of the CROOF_ command. The height of the prism is defined at the reference line. Upper and lower polygon intersection is forbidden.

angle

n

h

(xb,yb)

(xe,ye)

1

2

xb, yb, xe, ye: reference line (vector) starting and end coordinates. angle: rotation angle of the upper polygon around the given oriented reference line in degrees (CCW). si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. See Status Codes for details. Note: All calculated z coordinates of the upper polygon nodes must be positive or 0.

Example:

SPRISM_ 'Grass', 'Earth', 'Earth', 6, 0, 0, 11, 6, 2, -10.0,

- 0, 0, 15, 10, 1, 15, 11, 6, 15, 5, 7, 15, 4.5, 5.5, 15,
- 1, 6, 15