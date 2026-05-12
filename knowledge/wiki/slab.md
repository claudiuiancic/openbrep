---
id: wiki.generated.slab
type: wiki
category: other
commands: ["SLAB"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SLAB

SLAB n, h, x1, y1, z1, ..., xn, yn, zn Oblique prism. The lateral faces are always perpendicular to the x-y plane. Its bases are flat polygons rotated about an axis parallel with the x-y plane. Negative h values can also be used. In that case the second base polygon is below the given one. No check is made as to whether the points are really on a plane. Apices not lying on a plane will result in strange shadings/ renderings. Restriction of parameters:

n >= 3

z

y

x