---
id: wiki.generated.revolve_4
type: wiki
category: 3d
commands: ["REVOLVE{4}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVE{4}

REVOLVE{4} n, alphaOffset, alpha, betaOffset, beta, mask, sideMat,

x1, y1, s1, mat1, ..., xn, yn, sn, matn REVOLVE{4} is an extension of the REVOLVE{3} command with the possibility of hiding all edges. mask: controls the existence of the bottom, top and (in the case of alpha < 360°) side polygons.

mask = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8 + 256*j9 + 512*j10 + 1024*j11, where each j can be 0 or 1.

- j3: base closing side (in profile plane) is present,
- j4: end closing side (in revolved plane) is present,
- j5: base edges (in profile plane) are visible,
- j6: end edges (in revolved plane) are visible,
- j7: cross-section edges are visible, surface is articulated,
- j8: horizontal edge in line elimination,
- j9: vertical edge in line elimination,
- j10: hide all edges of revolve,
- j11: side edge and surface is smooth in curved sections of the profile. Compatibility: introduced in Archicad 21.


REVOLVE{5}

REVOLVE{5}n, alphaOffset, alpha, betaOffset, beta, mask, sideMat,

x1, y1, s1, mat1, ..., xn, yn, sn, matn