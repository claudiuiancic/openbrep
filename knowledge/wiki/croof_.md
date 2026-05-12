---
id: wiki.generated.croof_
type: wiki
category: other
commands: ["CROOF_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CROOF_

CROOF_ top_material, bottom_material, side_material, n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1,

... xn, yn, alphan, sn

A sloped roof pitch with custom angle ridges. top_material, bottom_material, side_material: name/index of the top, bottom and side material.

- n: the number of nodes in the roof polygon. xb, yb, xe, ye: reference line (vector).


height: the height of the roof at the reference line (lower surface). angle: the rotation angle of the roof plane around the given oriented reference line in degrees (CCW). thickness: the thickness of the roof measured perpendicularly to the plane of the roof. xi, yi: the coordinates of the nodes of the roof’s lower polygon. alphai: the angle between the face belonging to the edge i of the roof and the plane perpendicular to the roof plane, -90° < alphai <

90°. Looking in the direction of the edge of the properly oriented roof polygon, the CCW rotation angle is positive. The edges of the roof polygon are oriented properly if, in top view, the contour is sequenced CCW and the holes are sequenced CW.

si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints.

z

alphai

y

(xe, ye) angle

height

x

(xb, yb)

See Status Codes for details. Restriction of parameters:

n >= 3

CROOF_ 1, 1, 1, ! materials

- 9,

- 0, 0,
- 1, 0, ! reference line (xb,yb)(xe,ye) 0.0, ! height

-30, ! angle 2.5, ! thickness 0, 0, -60, 15, 10, 0, 0, 15, 10, 20, -30, 15, 0, 20, 0, 15, 0, 0, 0, -1,

- 2, 5, 0, 15, 8, 5, 0, 15, 5, 15, 0, 15,




- 2, 5, 0, -1


L=0.25 r=(0.6^2+L^2)/(2*L) a=ASN(0.6/r) CROOF_ "Roof Tile", "Pine", "Pine",

16, 2, 0, 0, 0, 0, 45, -0.2*SQR(2), 0, 0, 0, 15, 3.5, 0, 0, 15, 3.5, 3, -45, 15, 0, 3, 0, 15, 0, 0, 0, -1,

- 0.65, 1, -45, 15,
- 1.85, 1, 0, 15,
- 1.85, 2.4-L, 0, 13,


- 1.25, 2.4-r, 0, 900, 0, 2*a, 0, 4015, 0.65, 1, 0, -1,
- 2.5, 2, 45, 15,


- 3, 2, 0, 15, 3, 2.5, -45, 15, 2.5, 2.5, 0, 15, 2.5, 2, 0, -1