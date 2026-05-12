---
id: wiki.generated.nurbsedge
type: wiki
category: other
commands: ["NURBSEDGE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSEDGE

NURBSEDGE vert1, vert2, curve, curveDomainBeg, curveDomainEnd, status, tolerance Edge of a NURBS body. Different from any edge created by the EDGE command, indexed separately from those. Can be used in NURBS bodies only, excluding planar-face bodies. vert1, vert2: gdl-index of begin and end NURBS vertices

- • vert1 and vert2 can be equal. In this case the edge is a loop edge (and its curve is closed or has a closed part)
- • vert1 and vert2 can be zero for a ring edge (which has no vertices and its curve is closed or has a closed part)


curve: gdl-index of NURBS curve for the geometry of edge. Positive index, orientation of edge always coincide with orientation of the curve. curveDomainBeg, curveDomainEnd: definition of the part of curve which geometrically represents the edge. The curveDomainEnd

must be greater than curveDomainBeg, they must not coincide, and both value must be in the usable domain of the curve.

status: status control of the edge: status = j1 + 2*j2 + 4*j3, where each j can be 0 or 1. j1: invisible edge (may be set only if j2 is not set). j2: edge only visible if contour (may be set only if j1 is not set). j3: smooth edge (edge does not define a break when rendering smooth surfaces). If both j1 and j2 are set, the edge will produce an error causing the whole NURBS-body to vanish.

tolerance: maximum geometric distance between NURBS edge and other entities (NURBS face) which are topologically connected to

it. If negative, tolerance will be some predefined default.

The curve evaluated at each endpoint should coincide with the position of the appropriate vertex. The edge can be a ring edge with no vertex. In this case the edge restricted to [curveDomainBeg, curveDomainEnd] must be closed, i.e. it evaluates equally at each endpoints. Any number of edges can be attached to a vertex. The color of a NURBS edge is defined by the last PEN statement.