---
id: wiki.generated.ruled_2
type: wiki
category: 3d
commands: ["RULED{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RULED{2}

RULED{2} n, mask, u1, v1, s1, ..., un, vn, sn, x1, y1, z1, ..., xn, yn, zn

Z

2

j2

j6

1

n

j3

Y

n X

j1

1

j5

2

RULED is a surface based on a planar curve and a space curve having the same number of nodes. The planar curve polyline cannot have any holes. Straight segments connect the corresponding nodes of the two polylines. This is the only GDL element allowing the neighboring nodes to overlap.

The second version, RULED{2}, checks the direction (clockwise or counterclockwise) in which the points of both the top polygon and base polygon were defined, and reverses the direction if necessary. (The original RULED command takes only the base polygon into account, which can lead to errors.)

n: number of polyline nodes in each curve. ui, vi: coordinates of the planar curve nodes. xi, yi, zi: coordinates of the space curve nodes. mask: controls the existence of the bottom, top and side polygon and the visibility of the edges on the generator polylines. The side polygon

connects the first and last nodes of the curves, if any of them are not closed. mask = j1 + 2*j2 + 4*j3 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j1: base surface is present,
- j2: top surface is present (not effective if the top surface is not planar),


- j3: side surface is present (a planar quadrangle or two triangles), j5: edges on the planar curve are visible, j6: edges on the space curve are visible, j7: edges on the surface are visible, surface is not smooth.


si: status of the lateral edges. 0: lateral edges starting from the node are all visible, 1: lateral edges starting from the node are used for showing the contour.

Restriction of parameters: n > 1

Example:

R=3 RULED 16, 1+2+4+16+32,

cos(22.5)*R, sin(22.5)*R, 0, cos(45)*R, sin(45)*R, 0, cos(67.5)*R, sin(67.5)*R, 0, cos(90)*R, sin(90)*R, 0, cos(112.5)*R, sin(112.5)*R, 0, cos(135)*R, sin(135)*R, 0, cos(157.5)*R, sin(157.5)*R, 0, cos(180)*R, sin(180)*R, 0, cos(202.5)*R, sin(202.5)*R, 0, cos(225)*R, sin(225)*R, 0, cos(247.5)*R, sin(247.5)*R, 0, cos(270)*R, sin(270)*R, 0, cos(292.5)*R, sin(292.5)*R, 0, cos(315)*R, sin(315)*R, 0, cos(337.5)*R, sin(337.5)*R, 0, cos(360)*R, sin(360)*R, 0, cos(112.5)*R, sin(112.5)*R, 10, cos(135)*R, sin(135)*R, 10, cos(157.5)*R, sin(157.5)*R, 10, cos(180)*R, sin(180)*R, 10, cos(202.5)*R, sin(202.5)*R, 10, cos(225)*R, sin(225)*R, 10, cos(247.5)*R, sin(247.5)*R, 10, cos(270)*R, sin(270)*R, 10, cos(292.5)*R, sin(292.5)*R, 10, cos(315)*R, sin(315)*R, 10, cos(337.5)*R, sin(337.5)*R, 10, cos(360)*R, sin(360)*R, 10, cos(22.5)*R, sin(22.5)*R, 10, cos(45)*R, sin(45)*R, 10, cos(67.5)*R, sin(67.5)*R, 10, cos(90)*R, sin(90)*R, 10