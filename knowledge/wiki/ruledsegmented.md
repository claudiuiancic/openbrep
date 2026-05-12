---
id: wiki.generated.ruledsegmented
type: wiki
category: 3d
commands: ["RULEDSEGMENTED"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RULEDSEGMENTED

RULEDSEGMENTED n, mask, x11, y11, z11, s1,..., x1n, y1n, z1n, sn, x21, y21, z21, ..., x2n, y2n, z2n

Compatibility: introduced in Archicad 21.

RULEDSEGMENTED creates a surface based on two arbitrary-shaped polyline in 3D space. The two polylines must consist of the same number of vertices. It generates a sequence of doubly ruled surfaces, like RULED, but with less restriction on input polylines and with a subdivision of better quality.

Corresponding vertices of the two profiles are connected with straight lines. Corresponding pair of skew segments of the profiles are connected by a doubly ruled surface (mathematically hyperbolic paraboloid), with segmentation in both directions, resulting much smoother renderings and cross-sections.

Conditions of profile polylines:

- • both are 3D polylines, does not need to be coplanar
- • each may be closed but, neither may contain holes
- • each may contain identical vertices, even multiple consecutive ones resulting in fan-shaped surface
- • if a profile polyline is closed and coplanar, closing polygon can be generated n: number of polyline nodes in each curve. x1i, y1i, z1i: 3D positions of vertices on first profile polyline. x2i, y2i, z2i: 3D positions of vertices on second profile polyline.


mask: controls the existence of the bottom, top and side polygon and the visibility of the edges on the generator polylines. The side polygon connects the first and last nodes of the curves, if any of them are not closed. mask = j1 + 2*j2 + 4*j3 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1. j1: base surface is present (not effective if the first polyline is not coplanar and j3 is not set), j2: top surface is present (not effective if the second polyline is not coplanar and j3 is not set), j3: closing side surface is present (surface on additional segments between the last and first nodes),

- j5: edges on the first profile polyline are visible,
- j6: edges on the second profile polyline are visible,
- j7: edges on the surface are visible, surface is not smooth.


si: status of the generatrices (lateral edges between one node on first profile polyline and corresponding node on second polyline).

- 0: generatrix is visible,
- 1: generatrix is used for showing the contour,


- 2: generatrix visible and defines a break in rendering.


Restriction of parameters: n > 1

Example: RULEDSEGMENTED 4, 16+32,

0, 0, 0, 2, 1, 0, 0, 2,

- 1, 1, 0, 2,
- 1, 1, 1, 2,

- 0, 0, 1,
- 0, 1, 1,
- 0, 1, 2,


- 1, 2, 2