---
id: wiki.generated.extrude
type: wiki
category: 3d
commands: ["EXTRUDE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### EXTRUDE

EXTRUDE n, dx, dy, dz, mask,

x1, y1, s1,

... xn, yn, sn

z

j6

j2

j3

y

n

j1

1

x

j5

2

General prism using a polyline base in the x-y plane.

The displacement vector between bases is (dx, dy, dz). This is a generalization of the PRISM command and the SLAB command. The base polyline is not necessarily closed, as the lateral edges are not always perpendicular to the x-y plane. The base polyline may include holes, just like PRISM_. It is possible to control the visibility of the contour edges.

- n: the number of polyline nodes. mask: controls the existence of the bottom, top and (in case of an open polyline) side polygon.


mask = j1 + 2*j2 + 4*j3 + 16*j5 + 32*j6 + 64*j7 + 128*j8, where each j can be 0 or 1.

- j1: base surface is present,
- j2: top surface is present,
- j3: side (closing) surface is present,


- j5: base edges are visible,
- j6: top edges are visible.
- j7: cross-section edges are visible, surface is articulated,
- j8: cross-section edges are sharp, the surface smoothing will stop here in OpenGL and rendering.


si: status of the lateral edges or marks the end of the polygon or of a hole. You can also define arcs and segments in the polyline using additional status code values: 0: lateral edge starting from the node is visible, 1: lateral edges starting from the node are used for showing the contour,

-1: marks the end of the enclosing polygon or a hole, and means that the next node will be the first vertex of another hole. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details. Restriction of parameters:

n > 2

EXTRUDE 14, 1, 1, 4, 1+2+4+16+32,

- 0, 0, 0,
- 1, -3, 0,
- 2, -2, 1,
- 3, -4, 0,
- 4, -2, 1,
- 5, -3, 0,
- 6, 0, 0, 3, 4, 0, 0, 0, -1, 2, 0, 0, 3, 2, 0, 4, 0, 0, 3, -2, 0, 2, 0, -1


A=5: B=5: R=2: S=1: C=R-S : D=A-R : E=B-R EXTRUDE 28, -1, 0, 4, 1+2+4+16+32,

0, 0, 0,

- D+R*sin(0), R-R*cos(0), 1,

- D+R*sin(15), R-R*cos(15), 1,

- D+R*sin(30), R-R*cos(30), 1,

- D+R*sin(45), R-R*cos(45), 1,

- D+R*sin(60), R-R*cos(60), 1,

- D+R*sin(75), R-R*cos(75), 1,

- D+R*sin(90), R-R*cos(90), 1, A, B, 0, 0, B, 0, 0, 0, -1, C, C, 0,
- D+S*sin(0), R-S*cos(0), 1,


- D+S*sin(15), R-S*cos(15), 1,


- D+S*sin(30), R-S*cos(30), 1,


- D+S*sin(45), R-S*cos(45), 1,


- D+S*sin(60), R-S*cos(60), 1,


- D+S*sin(75), R-S*cos(75), 1,


- D+S*sin(90), R-S*cos(90), 1, A-C,B-C,0, R-S*cos(90), E+S*sin(90), 1, R-S*cos(75), E+S*sin(75), 1, R-S*cos(60), E+S*sin(60), 1, R-S*cos(45), E+S*sin(45), 1, R-S*cos(30), E+S*sin(30), 1, R-S*cos(15), E+S*sin(15), 1, R-S*cos(0), E+S*sin(0), 1, C, C, -1