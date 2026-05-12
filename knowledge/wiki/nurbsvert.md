---
id: wiki.generated.nurbsvert
type: wiki
category: other
commands: ["NURBSVERT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSVERT

NURBSVERT x, y, z, hard, tolerance Vertex, a node of a NURBS body. Different from any vertex created by the VERT command, indexed separately from those. Can be used in NURBS bodies only, excluding planar-face bodies.

x, y, z: coordinates of vertex hard:

1: if the vertex should define a break when rendering smooth surfaces, 0: otherwise.

tolerance: maximum geometric distance between NURBS vertex and other entities (NURBS edge, NURBS face) which are topologically

connected to it. If negative, tolerance will be some predefined default.