---
id: wiki.generated.cone
type: wiki
category: 3d
commands: ["CONE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CONE

CONE h, r1, r2, alpha1, alpha2

z

z

alpha2

y

- r1

- r2 h


alpha1

x

x

Frustum of a cone where alpha1 and alpha2 are the angles of inclination of the end surfaces to the z axis, r1 and r2 are the radii of the endcircles and h is the height along the z axis. If h=0, the values of alpha1 and alpha2 are disregarded and an annulus is generated in the x-y plane. alpha1 and alpha2 are in degrees. Restriction of parameters:

0 < alpha1 < 180° and 0 < alpha2 < 180°

Example: A regular cone CONE h, r, 0, 90, 90