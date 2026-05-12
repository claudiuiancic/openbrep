---
id: wiki.generated.revolve_3
type: wiki
category: 3d
commands: ["REVOLVE{3}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REVOLVE{3}

- REVOLVE{3} n, alphaOffset, alpha, betaOffset, beta, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn


- REVOLVE{3} is an extension of the REVOLVE{2} command with the possibility of defining two snap position. During the revolution the path of each point of the base polyline is a circular arc, which is approximated by a polyline. With REVOLVE{3} two snap location can be defined where polyline exactly fits the circle. With REVOLVE{2} this two snap locations are at the beginning and the end of the revolution. With REVOLVE{3} the end points are not necessarily on the circle but simply cut at end planes. betaOffset: Angle defining the first snap location. The defined angle need not be in the range of revolution.


beta: Angle defining the second snap location relative to the first snap location. May be negative. The defined angle need not be in the

range of revolution.

Example:

revolve{2} snap positions at ends revolve{3} custom snap positions

resol 8 revolve{2} 4,

10, 335, ! alphaOffset, alpha 444, 2, 0, 4, 2, 2, 3, 4, 2, 2, 3, 6, 2, 2, 0, 6, 2, 2

! reference circle resol 72 revolve{2} 4,

0, 360, ! alphaOffset, alpha 444, 0,

- -0.01, 3.99, 2, 0, 0, 3.99, 2, 0, 0, 4, 2, 0,
- -0.01, 4, 2, 0


resol 8 revolve{3} 4,

10, 335, ! alphaOffset, alpha 67.5, 100, ! betaOffset, beta 444, 2, 0, 4, 2, 2, 3, 4, 2, 2, 3, 6, 2, 2, 0, 6, 2, 2

! reference circle resol 72 revolve{2} 4,

0, 360, ! alphaOffset, alpha 444, 0,

- -0.01, 3.99, 2, 0, 0, 3.99, 2, 0, 0, 4, 2, 0,
- -0.01, 4, 2, 0