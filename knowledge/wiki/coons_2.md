---
id: wiki.generated.coons_2
type: wiki
category: other
commands: ["COONS{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COONS{2}

COONS{2} n, m, mask,

x11, y11, z11, ..., x1n, y1n, z1n, x21, y21, z21, ..., x2n, y2n, z2n, x31, y31, z31, ..., x3m, y3m, z3m, x41, y41, z41, ..., x4m, y4m, z4m

COONS{2} is an extension of the the COONS command with the possibility of setting the visibility of surface and boundary edges independently. mask:

mask = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j3: edges of the 1st boundary (x1, y1, z1) are visible,
- j4: edges of the 2nd boundary (x2, y2, z2) are visible,
- j5: edges of the 3rd boundary (x3, y3, z3) are visible,
- j6: edges of the 4th boundary (x4, y4, z4) are visible,
- j7: edges on surface are visible, surface is not smooth.