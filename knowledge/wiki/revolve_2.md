---
id: wiki.generated.revolve_2
type: wiki
category: 3d
commands: ["REVOLVE{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVE{2}

- REVOLVE{2} n, alphaOffset, alpha, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn


Advanced version of REVOLVE. The profile polygon will always be closed and may have holes. The start angle and the face materials are controllable. alphaOffset: rotation start angle.

alpha: rotation angle length in degrees, may be negative. mask: controls the existence of the bottom, top and (in the case of alpha < 360°) side polygons.

mask = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8 + 256*j9, where each j can be 0 or 1.

- j3: base closing side (in profile plane) is present,
- j4: end closing side (in revolved plane) is present,
- j5: base edges (in profile plane) are visible,
- j6: end edges (in revolved plane) are visible,
- j7: cross-section edges are visible, surface is articulated,
- j8: horizontal edge in line elimination,
- j9: vertical edge in line elimination.


sideMat: material of the closing faces. mati: material of the face generated from the i-th edge.