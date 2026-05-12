---
id: wiki.generated.coons
type: wiki
category: other
commands: ["COONS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COONS

COONS n, m, mask,

x11, y11, z11, ..., x1n, y1n, z1n, x21, y21, z21, ..., x2n, y2n, z2n, x31, y31, z31, ..., x3m, y3m, z3m, x41, y41, z41, ..., x4m, y4m, z4m

A Coons patch generated from four boundary curves. mask:

mask = 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j3: edges of the 1st boundary (x1, y1, z1) are visible (effective only if j7 is set),
- j4: edges of the 2nd boundary (x2, y2, z2) are visible (effective only if j7 is set),
- j5: edges of the 3rd boundary (x3, y3, z3) are visible (effective only if j7 is set),
- j6: edges of the 4th boundary (x4, y4, z4) are visible (effective only if j7 is set),
- j7: edges on surface are visible, surface is not smooth. In case the edges on the surface are invisible (bit j7 is set to zero), all boundary edges become visible, with the bits j3-j6 becoming ineffective. To define boundary edge visibility independent of surface edge visibility, use the COONS{2} command.


Z

Y

1(n)

4(m)

2(n)

3(m)

X

The orientation of the boundaries is obligatory: curves 1 and 2 must go from curve 3 towards 4, and curves 3 and 4 must go from curve 1 towards 2. The corner coordinates have to be the same in the respective curves. Restriction of parameters:

n > 1, m > 1

- 0, 0, 5,
- 1, 0, 4,
- 2, 0, 3,
- 3, 0, 2,
- 4, 0, 1,
- 5, 0, 0, ! 2nd boundary, n=6


- 0, 5, 0,
- 1, 5, 1,
- 2, 5, 2,
- 3, 5, 3,
- 4, 5, 4,
- 5, 5, 5, ! 3rd boundary, m=6


- 0, 0, 5,
- 0, 1, 4,
- 0, 2, 3,
- 0, 3, 2,
- 0, 4, 1,
- 0, 5, 0, ! 4th boundary, m=6


- 5, 0, 0,
- 5, 1, 1,
- 5, 2, 2,
- 5, 3, 3,
- 5, 4, 4,
- 5, 5, 5


1, 2, 0, 0.5, 1, 0, 0.2, 0.5, 0,

-0.5, 0, 0, 0.2, -0.5, 0, 0.5, -1, 0, 1, -2, 0, ! 2nd boundary, n=7

- 6, 10, -2, 6.5, 4, -1.5, 5, 1, -1.2,


- 4, 0, -1,
- 5, -1, -1.2, 6.5, -4, -1.5,
- 6, -10, -2, ! 3rd boundary, m=6


- 1, 2, 0,
- 2, 4, -0.5,
- 3, 6, -1,
- 4, 8, -1.5,
- 5, 9, -1.8,
- 6, 10, -2, ! 4th boundary, m=6


- 1, -2, 0,
- 2, -4, -0.5,
- 3, -6, -1,
- 4, -8, -1.5,
- 5, -9, -1.8,
- 6, -10, -2