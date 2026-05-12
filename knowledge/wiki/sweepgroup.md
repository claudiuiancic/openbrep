---
id: wiki.generated.sweepgroup
type: wiki
category: 3d
commands: ["SWEEPGROUP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SWEEPGROUP

SWEEPGROUP (g_expr, x, y, z) Returns a group that is created by sweeping the group parameter along the given direction. The command works for solid models only.

- SWEEPGROUP{2} (g_expr, x, y, z) The difference between SWEEPGROUP and SWEEPGROUP{2} is that in the former case the actual transformation matrix is applied again to the direction vector of the sweeping operation with respect to the current coordinate system. (In the case of SWEEPGROUP, the current transformation is applied to the direction vector twice with respect to the global coordinate system.)


- SWEEPGROUP{3} (g_expr, x, y, z, edgeColor, materialId, materialColor, method) This version adds a new method selection to SWEEPGROUP{2} and works for surface models also. edgeColor: the color of the new edge when it differs from 0. materialId: the material of the new face when it differs from 0. materialColor: the color of the new face when the materialId is 0 and it differs from 0.

method: controls the ending shape of the resulting body. 0: same as SWEEPGROUP{2}, both ends come from the originating body, 1: the start comes from the originating body, the sweep end is flat

- SWEEPGROUP{4} (g_expr, x, y, z, edgeColor, materialId, materialColor, method, status) This version adds a new status parameter to SWEEPGROUP{3}. status: Controls attributes of the result.

status = 2*j2, where each j can be 0 or 1. j2: Keep per-polygon texture mapping parameters on the sweeped result (see the PGON command for details).

- SWEEPGROUP{5} (g_expr, x, y, z, edgeColor, materialId, materialColor, method, status) SWEEPGROUP{5} is an extension of the SWEEPGROUP{4} command with the possibility of using inline material definition, that means materials defined in GDL script locally also can be used next to materials defined in global material definitions. Compatibility: introduced in Archicad 22. Example:


| | | | | |
|---|---|---|---|---|
| | | | | |


GROUP "the_sphere"

SPHERE 1 ENDGROUP

- PLACEGROUP SWEEPGROUP{2} ("the_sphere", 2, 0, 0) ADDX 5
- PLACEGROUP SWEEPGROUP{3} ("the_sphere", 2, 0, 0, 4, 0, 4, 1) del 1