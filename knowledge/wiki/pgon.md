---
id: wiki.generated.pgon
type: wiki
category: 3d
commands: ["PGON"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PGON

PGON n, vect, status, edge1, edge2, ..., edgen Polygon definition.

- n: number of edges in the edge list. vect: index of the normal vector. It must refer to a previously defined VECT. Note: If vect = 0, the program will calculate the normal vector during the analysis.


edge1, edge2, ..., edgen: these indices must refer to previously defined EDGEs. A zero value means the beginning or the end of a hole definition. A negative index changes the direction of the stored normal vector or edge to the opposite in the polygon. (The stored vector or edge does not change; other polygons can refer to it using the original orientation with a positive index.)