---
id: wiki.generated.nurbsface_2
type: wiki
category: other
commands: ["NURBSFACE{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSFACE{2}

NURBSFACE{2} n, surface, tolerance, wrap_method, wrap_flags, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4,

trim1, trim2, ..., trimn Similar to the NURBSFACE command, extended with the ability to describe texture mapping on the NURBS face like in the PGON{3} command.

n, surface, tolerance: same as the NURBSFACE command. wrap_method: same as the PGON{3} command.

- • 0: the global wrapping mode is applied (x1 ... z4 parameters are required but will be ignored)
- • > 0: same as the PGON{3} command


wrap_flags: similar to the the PGON{3} command, except that projection type flags (j3, j4 and j5) are ignored (texture coordinates can

not be applied on NURBS faces).

x1, y1, z1 ... x4, y4, z4: coordinates defining the coordinate system of the texture mapping for the NURBS face (these

parameters are effective only if wrap_method > 0).

trim1 ... trimn: same as the NURBSFACE command.