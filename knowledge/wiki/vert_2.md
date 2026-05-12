---
id: wiki.generated.vert_2
type: wiki
category: 3d
commands: ["VERT{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### VERT{2}

VERT x, y, z, hard

Extension of the VERT command including a possibility to declare a node to be hard vertex. A hard vertex defines a break when rendering smooth surfaces.

x, y, z: coordinates of the node. hard:

1: if the vertex should define a break when rendering smooth surfaces 0: otherwise