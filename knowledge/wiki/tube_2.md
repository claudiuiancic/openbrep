---
id: wiki.generated.tube_2
type: wiki
category: 3d
commands: ["TUBE{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TUBE{2}

TUBE{2} top_material, bottom_material, cut_material, n, m, mask, u1, w1, s1, mat1,

... un, wn, sn, matn, x1, y1, z1, angle1,

... xm, ym, zm, anglem

Compatibility: introduced in Archicad 21. Extended version of the TUBE command:

- • holes can be defined within the contour base polygon
- • individual surfaces attribute for top, bottom polygons and cut areas
- • individual surface attribute for side polygons belonging to the same base polygon edge


- V axis, W axis, U axis: same meaning as in the TUBE command.


top_material: surface of the closing polygon. bottom_material: surface of the starting polygon. cut_material: surface of the cut areas. n, m, ui, wi: same meaning as in the TUBE command. xi, yi, zi, anglei: same meaning as in the TUBE command. Path can not contain arcs (segmentation is manual). mask: controls the existence of the bottom and top polygons’ surfaces and edges.

mask = j1 + 2*j2 + 16*j5 + 32*j6 + 256*j9 + 512*j10 + 1024*j11 + 2048*j12 + 4096*j13, where each j can be 0 or 1.

- j1: base surface is present,
- j2: end surface is present, j5: base edges (at x2, y2, z2) are visible, j6: end edges (at xm-1, ym-1, zm-1) are visible,


- j9: side edge and surface is smooth in curved sections of the profile,
- j10: base edges participate in line elimination (Compatibility: introduced in Archicad 23.),
- j11: end edges participate in line elimination (Compatibility: introduced in Archicad 23.),
- j12: longitudinal edges (which connect cross sections) participate in line elimination (Compatibility: introduced in Archicad 23.),
- j13: edges of cross sections participate in line elimination (Compatibility: introduced in Archicad 23.).


si: status of the lateral edges.

-1: indicates the last node of a hole within the base polygon (duplicated first node of the hole), or the closing node of the outside polygon in case of a base polygon containing holes. The matn parameter is ignored in these duplicated nodes with status -1, 0, 1, 2: same meaning as in the TUBE command.

mati: individual surface of the side polygons belonging to the edge starting from ui, wi node of the base polygon. Additional status codes allow you to create segments and arcs in the planar polyline using special constraints. Such polygon edges are automatically segmented during processing.

matEnds1 = 12 matEnds2 = 24 matCut = 15 matOuter = 10 matInner = 13

TUBE{2} matEnds1, matEnds2, matCut, 10, 4, 1 + 2 + 16 + 32, ! outside contour

- -0.01, 0.01, 0, matOuter,
- -0.01, -0.01, 0, matOuter, 0.01, -0.01, 0, matOuter, 0.01, 0.01, 0, matOuter,
- -0.01, 0.01, -1, matOuter, ! hole contour
- -0.008, 0.008, 0, matInner,
- -0.008, -0.008, 0, matInner, 0.008, -0.008, 0, matInner, 0.008, 0.008, 0, matInner,
- -0.008, 0.008, -1, matInner,


! path 0, 0, -1, 45, 0, 0, 0, 45, 0, 0, 1, 45, 0, 0, 2, 45