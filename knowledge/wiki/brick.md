---
id: wiki.generated.brick
type: wiki
category: 3d
commands: ["BRICK"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### BRICK a, b, c

z

b

c

a

y

x

The first corner of the block is in the local origin and the edges with lengths a, b and c are along the x-, y- and z-axes, respectively. Zero values create degenerated blocks (rectangle or line). Restriction of parameters:

a >= 0, b >= 0, c >= 0 a + b + c > 0