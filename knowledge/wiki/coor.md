---
id: wiki.generated.coor
type: wiki
category: 3d
commands: ["COOR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COOR

COOR wrap, vert1, vert2, vert3, vert4 Deprecated. See the COOR{3} command. Local coordinate system of a BODY for the fill and texture mapping. wrap: wrapping mode + projection type Wrapping modes:

- 1: planar box (deprecated),


- 2: box,
- 3: cylindrical,
- 4: spherical,
- 5: same as the cylindrical fill mapping, but in rendering the top and the bottom surface will get a circular mapping,
- 6: planar


Projection types: 256: the fill always starts at the origin of the local coordinate system, 1024: quadratic texture projection (recommended), 2048: linear texture projection based on the average distance, 4096: linear texture projection based on normal triangulation.

Note: The last three values are only effective with custom texture coordinate definitions (see the TEVE command). vert1: index of a VERT, representing the origin of the local coordinate system.

- vert2, vert3, vert4: indices of VERTs defining the three coordinate axes. Use a minus sign (-) before VERT indices if they are used only for defining the local coordinate system.


Example: For custom texture axes: CSLAB_ "Brick-White", "Brick-White", "Brick-White",

4, 0.5, 0, 0, 0, 15, 1, 0, 0, 15, 1, 1, 1, 15, 0, 1, 1, 15

BASE VERT 1, 0, 0 !#1 VERT 1, 1, 1 !#2

- VERT 0, 0, 0 !#3
- VERT 1, 0, 1 !#4 COOR 2, -1, -2, -3, -4 BODY 1


Z

Y

X'

Z'

X

Y'