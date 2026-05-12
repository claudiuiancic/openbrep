---
id: wiki.generated.poly2_b
type: wiki
category: 3d
commands: ["POLY2_B"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POLY2_B

- POLY2_B n, frame_fill, fill_pen, fill_background_pen, x1, y1, s1, ..., xn, yn, sn


Advanced versions of the POLY2_ command, with additional parameters: the fill pen and the fill background pen. All other parameters are similar to those described at the POLY2_ command.

fill_pen: fill pencolor number. fill_background_pen: fill background pencolor number. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. See the section called “Additional Status Codes” for details.