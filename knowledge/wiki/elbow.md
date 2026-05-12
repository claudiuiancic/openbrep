---
id: wiki.generated.elbow
type: wiki
category: other
commands: ["ELBOW"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ELBOW

ELBOW r1, alpha, r2 A segmented elbow in the x-z plane. The radius of the arc is r1, the angle is alpha and the radius of the tube segment is r2. The alpha value is in degrees. Restriction of parameters:

r1 > r2

z

r1

alpha

x

r2

ELBOW 2.5, 180, 1 ADDZ -4 CYLIND 4, 1 ROTZ -90 MULZ -1 ELBOW 5, 180, 1 DEL 1 ADDX 10 CYLIND 4, 1 ADDZ 4 ROTZ 90 ELBOW 2.5, 180, 1