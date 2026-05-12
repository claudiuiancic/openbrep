---
id: wiki.generated.plane_
type: wiki
category: 3d
commands: ["PLANE_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PLANE_

PLANE_ n, x1, y1, z1, s1, ..., xn, yn, zn, sn Similar to the PLANE command, but any of the edges can be omitted as in the POLY_ command. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes”. Restriction of parameters:

n >= 3