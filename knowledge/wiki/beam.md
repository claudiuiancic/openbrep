---
id: wiki.generated.beam
type: wiki
category: other
commands: ["BEAM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BEAM

BEAM left_material, right_material, vertical_material, top_material, bottom_material, height,

- x1, x2, x3, x4,
- y1, y2, y3, y4, t, mask1, mask2, mask3, mask4


Beam definition. Parameters are similar to those of the XWALL_ element. top_material, bottom_material: top and bottom materials.

Example:

BEAM 1, 1, 1, 1, 1, 0.3, 0.0, 7.0, 7.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.5, 15, 15, 15, 15