---
id: wiki.generated.poly2
type: wiki
category: 3d
commands: ["POLY2"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2

POLY2 n, frame_fill, x1, y1, ..., xn, yn

An open or closed polygon with n nodes.

y

n

2

1

x

Restriction of parameters:

n >= 2 n: number of nodes. x1, y1, ..., xn, yn: coordinates of each nodes. frame_fill:

frame_fill = j1 + 2*j2 + 4*j3, where each j can be 0 or 1. j1: draw contour j2: draw fill j3: close an open polygon