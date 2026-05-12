---
id: wiki.generated.ruledsegmented_2
type: wiki
category: 3d
commands: ["RULEDSEGMENTED{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RULEDSEGMENTED{2}

RULEDSEGMENTED{2} top_material, bottom_material, n, mask, textureMode, x11, y11, z11, s1, mat1..., x1n, y1n, z1n, sn, matn, x21, y21, z21, ..., x2n, y2n, z2n

Compatibility: introduced in Archicad 23. RULEDSEGMENTED{2} is an extension of the RULEDSEGMENTED command with the possibility of controlling the surface attributes of the generated surfaces in segment detail and applying custom texture projection. Additional parameters: top_material: surface attribute index of the base surface (if the first polyline is coplanar and j1+j3 are set). bottom_material: surface attribute index of the top surface (if the second polyline is coplanar and j2+j3 are set). textureMode: texture projection mode

0: automatic, optimized for curved surfaces, the same as with the RULEDSEGMENTED command. 1: custom, defined by the COOR command.

mati: surface attribute index of generated surface segment i.

Example:

_topMatIndex = 22 _bottomMatIndex = 34 _segmentMatIndex_1 = 55 _segmentMatIndex_2 = 44

RULEDSEGMENTED{2} _topMatIndex, _bottomMatIndex, 4, 1+2+16+32, 0, 0, 0, 0, 2, _segmentMatIndex_1, 1, 0, 0, 2, _segmentMatIndex_2, 1, 1, 0, 2, _segmentMatIndex_1,

- 0, 1, 0, 2, _segmentMatIndex_2,
- 1, 0, 1, 1, 1, 1, 0, 1, 1,


0, 0, 1