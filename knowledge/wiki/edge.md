---
id: wiki.generated.edge
type: wiki
category: 3d
commands: ["EDGE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### EDGE

EDGE vert1, vert2, pgon1, pgon2, status Definition of an edge.

- vert1, vert2: index of the endpoints. The vert1 and vert2 indices must be different and referenced to previously defined VERTs.


pgon1, pgon2: indices of the neighboring polygons. Zero and negative values have special meanings: 0: terminal or standalone edge, < 0: possible neighbors will be searched for,