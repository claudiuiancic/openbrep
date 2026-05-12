---
id: wiki.generated.arme
type: wiki
category: other
commands: ["ARME"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ARME

ARME l, r1, r2, h, d

r2

z

d

l

h

y

r1

A piece of tube starting from an ellipsoid in the y-z plane; parameters according to the figure (penetration lines are also calculated and drawn). Restriction of parameters:

r1 >= r2+d l >= h*sqrt(1-(r2-d)2/r12)

ELLIPS 3,4 FOR i=1 TO 6

ARME 6,4,0.5,3,3.7-0.2*i ROTZ 30

NEXT i