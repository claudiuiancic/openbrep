---
id: wiki.generated.pgon_2
type: wiki
category: 3d
commands: ["PGON{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PGON{2}

- PGON{2} n, vect, status, wrap, edge_or_wrap1, ..., edge_or_wrapn The first three parameters are similar to the ones at the PGON command. wrap: wrapping mode + projection type.

- 0: the global wrapping mode is applied, > 0: the meaning is the same as it is in the COOR command.


edge_or_wrap1, ..., edge_or_wrapn: The number and meaning of these parameters are based on the wrap definition: edge1, ..., edgen: if wrap is 0; in this case edgen means the same as at the PGON command, and globally defined texture mapping will be applied; x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, edge1, ..., edgen: if wrapping mode is not 0 in wrap; in this case xi, yi, zi coordinates defining the coordinate system of the texture mapping for the polygon; edge1, u1, v1, ..., edgen, un, vn: if wrapping mode is 0 but projection type is not 0 in wrap; in this case ui, vi texture space coordinates are the same as at the TEVE command; the mapping will affect the currently defined polygon only.

- PGON{3}