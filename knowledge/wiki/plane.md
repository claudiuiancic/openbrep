---
id: wiki.generated.plane
type: wiki
category: 3d
commands: ["PLANE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PLANE

PLANE n, x1, y1, z1, ..., xn, yn, zn A polygon with n edges on an arbitrary plane. The coordinates of nodei are (xi, yi, zi). The polygon must be planar in order to get a correct shading/rendering result, but the interpreter does not check this condition. Restriction of parameters:

n >= 3