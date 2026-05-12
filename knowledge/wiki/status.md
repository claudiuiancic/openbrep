---
id: wiki.generated.status
type: wiki
category: other
commands: ["STATUS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### STATUS CODE SYNTAX

si: The si number is a binary integer (between 0 and 127) or -1. si = j1 + 2*j2 + 4*j3 + 8*j4 + 64*j7 [+ a_code] , where each j can be 0 or 1. The j1, j2, j3, j4 numbers represent whether the vertices and the sides are present (1) or omitted (0):

- j1: lower horizontal edge,
- j2: vertical edge,
- j3: upper horizontal edge,
- j4: side face, j7: special additional status value effective only when j2=1 and controls the viewpoint dependent visibility of the current vertical edge, a_code: additional status code (optional), which allows you to create segments and arcs in the polyline, j2=0: the vertical edge is always invisible j2=1 and j7=1: the vertical edge is only visible when it is a contour observed from the current direction of view j2=1 and j7=0: the vertical edge is always visible Possible status values (the heavy lines denote visible edges):


invisible surface visible surface

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7


- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15


si=-1 is used to define holes directly into the prism. It marks the end of the contour and the beginning of a hole inside of the contour. It is also used to indicate the end of one hole’s contour and the beginning of another. Coordinates before that value must be identical to the coordinates of the first point of the contour/hole. If you have used the -1 mask value, the last mask value in the parameter list must be -1, marking the end of the last hole.

The holes must be disjoint and internal intersections are forbidden in the polygon for a correct shading/rendering result.