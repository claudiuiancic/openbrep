---
id: wiki.generated.project2_4
type: wiki
category: 2d
commands: ["PROJECT2{4}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROJECT2{4}

- PROJECT2{4} projection_code, angle, useTransparency, statusParts, numCutplanes, cutplaneHeight1, ..., cutplaneHeightn,


method1, parts1, cutFillIndex1, cutFillFgPen1, cutFillBgPen1, cutFillOrigoX1, cutFillOrigoY1, cutFillDirection1, cutLinePen1, cutLineType1, projectedFillIndex1, projectedFillFgPen1, projectedFillBgPen1, projectedFillOrigoX1, projectedFillOrigoY1, projectedFillDirection1, projectedLinePen1, projectedLineType1,

... method(numCutplanes+1)), parts(numCutplanes+1), cutFillIndex(numCutplanes+1), cutFillFgPen(numCutplanes+1), cutFillBgPen(numCutplanes+1), cutFillOrigoX(numCutplanes+1), cutFillOrigoY(numCutplanes+1), cutFillDirection(numCutplanes+1), cutLinePen(numCutplanes+1), cutLineType(numCutplanes+1), projectedFillIndex(numCutplanes+1), projectedFillFgPen(numCutplanes+1), projectedFillBgPen(numCutplanes+1), projectedFillOrigoX(numCutplanes+1), projectedFillOrigoY(numCutplanes+1), projectedFillDirection(numCutplanes+1), projectedLinePen(numCutplanes+1), projectedLineType(numCutplanes+1)

Compatibility: introduced in Archicad 20.

Creates a projection of the 3D script in the same library part and adds the generated lines to the 2D parametric symbol. The fourth version,

- PROJECT2{4}, adds the possibility to define multiple cutting planes parallel to the X-Y plane, and to control the attributes of the cut and projected parts of the slices, including the line type, pens and fills. The number of cutplanes can be zero, creating exactly one uncut slice (numCutplanes+1). useTransparency: can be 0 (no transparency) or positive integer (1: transparency enabled). statusParts: defines the status parts to generate (hotlines, hotspots, hotarcs). The 1+2 value means all parts. Setting is applied for all slices.


statusParts = j1 + 2*j2, where each j can be 0 or 1. The j1, j2 numbers represent whether the corresponding status parts of the projected model are present (1) or omitted (0):

j1: project 3D hotspots as static 2D hotspots, j2: project 3D hotlines and hotarcs (including related 3D hotspots converted to static 2D hotspots).

numCutplanes: the number of defined cutplanes. Can be zero, but preferably more. cutplaneHeighti: the position of each individually defined cutplane. Measured as length perpendicularly from the X-Y plane of the

object.

method: the chosen imaging method. If invalid or none is set, the default is hidden lines (2). 0: the current slice is not part of the projection, 1: wireframe, 2: hidden lines (analytic), 3: shading, 4: hidden lines with polygon: the polygon does not eliminate any polygon or line belonging to parts created with shading method, but will cover/eliminate polygons and lines belonging to other wireframe/hidden line parts. Set it to Air Space for best result. Such exploded polygons will behave in 2D according to slice order (will cover, but not eliminate shaded parts). 16: addition modifier: draws vectorial hatches (effective only in hidden line modes and shaded mode), 32: addition modifier: use current attributes instead of attributes from 3D (effective only in shading mode and hidden line with polygon mode), 64: addition modifier: local fill orientation (effective only in shading mode and hidden line with polygon mode), 128: addition modifier: lines are all inner lines (effective only together with 32). Default is generic. 256: addition modifier: lines are all contour lines (effective only together with 32, if 128 is not set). Default is generic. 512: addition modifier: fills are all cut (effective only together with 32). Default is drafting fills. 1024: addition modifier: fills are all cover (effective only together with 32, if 512 is not set). Default is drafting fills. 2048: addition modifier: modifiers 16, 32, 64, 128, 256, 512, 1024 and fill attribute parameters are effective only for the view part of the projection. By default they are effective for all parts.

projection. By default they are effective for all parts. 8192: addition modifier: cut fills are slanted.

partsi: defines the parts to generate. The 1+2+4+8+64 value means all parts. partsi = j1 + 2*j2 + 4*j3 + 8*j4 + 64*j7, where each j can be 0 or 1. The j1, j2, j3, j4, j7 numbers represent whether the corresponding parts of the projected model are present (1) or omitted (0):

j1: cut polygons (effective only in shading mode), j2: cut polygon edges, j3: view polygons, j4: view polygon edges, j7: project pointclouds.

cutFillIndexi: fill type index of the cut part of the current slice. cutFillFgPeni: fill pen of the cut part of the current slice. cutFillBgPeni: fill background pen of the cut part of the current slice. cutFillOrigoXi: X coordinate of the cut fill origin of the current slice. cutFillOrigoYi: Y coordinate of the cut fill origin of the current slice. cutFillDirectioni: direction angle of the cut fill of the current slice. cutLinePeni: pen index of cut lines of the current slice. cutLineTypei: line type of cut lines of the current slice. projectedFillIndexi: fill type index of the projected part of the current slice. projectedFillFgPeni: fill pen of the projected part of the current slice. projectedFillBgPeni: fill background pen of the projected part of the current slice. projectedFillOrigoXi: X coordinate of the projected fill origin of the current slice. projectedFillOrigoYi: Y coordinate of the projected fill origin of the current slice. projectedFillDirectioni: direction angle of the projected fill of the current slice. projectedLinePeni: pen index of projected lines of the current slice. projectedLineTypei: line type of projected lines of the current slice.