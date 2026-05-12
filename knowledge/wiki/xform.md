---
id: wiki.generated.xform
type: wiki
category: 3d
commands: ["XFORM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### XFORM

XFORM newx_x, newy_x, newz_x, offset_x,

- newx_y, newy_y, newz_y, offset_y,
- newx_z, newy_z, newz_z, offset_z


Defines a complete transformation matrix. It is mainly used in automatic GDL code generation. It has only one entry in the stack.

- x' = newx_x * x + newy_x * y + newz_x * z + offset_x
- y' = newx_y * x + newy_y * y + newz_y * z + offset_y
- z' = newx_z * x + newy_z * y + newz_z * z + offset_z


- A=60
- B=30 XFORM 2, COS(A), COS(B)*0.6, 0,


0, SIN(A), SIN(B)*0.6, 0, 0, 0, 1, 0

BLOCK 1, 1, 1

MANAGING THE TRANSFORMATION STACK