---
id: wiki.generated.poly_
type: wiki
category: 3d
commands: ["POLY_"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY_

POLY_ n, x1, y1, s1, ..., xn, yn, sn Similar to the normal POLY statement, but any of the edges can be omitted. si: status code that allows you to control the visibility of polygon edges and side surfaces. You can also define holes and create segments

and arcs in the polyline using special constraints. si = 0: the edge starting from the (xi,yi) apex will be omitted, si = 1: the edge will be shown, si = -1: is used to define holes directly.

Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details.

y

n

1 2 3

x

y

n

1 2 3

x

Restriction of parameters: n >= 3