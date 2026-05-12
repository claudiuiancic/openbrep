---
id: wiki.generated.armc
type: wiki
category: other
commands: ["ARMC"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ARMC

ARMC r1, r2, l, h, d, alpha

z

alpha

r2

l

h

x y

|r1| | |
|---|---|---|
| | | |


d

x

A piece of tube starting from another tube; parameters according to the figure (penetration curves are also calculated and drawn). The alpha value is in degrees. Restriction of parameters:

r1 >= r2 + d r1 <= l*sin(alpha) - r2*cos(alpha)

CYLIND 10,1 ADDZ 6 ARMC 1, 0.9, 3, 0, 0, 45 ADDZ -1 ROTZ -90 ARMC 1, 0.75, 3, 0, 0, 90 ADDZ -1 ROTZ -90 ARMC 1, 0.6, 3, 0, 0, 135