---
id: wiki.generated.spline2
type: wiki
category: 2d
commands: ["SPLINE2"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SPLINE2

SPLINE2 n, status, x1, y1,

angle1, ..., xn, yn, anglen

anglei

y

i

(xi,yi)

1

n

x

Spline, with n control points. The tangent of the spline in the control point (xi, yi) is defined by anglei, the angle with the x axis in degrees. Restriction of parameters:

n >= 2

si: Status values:

- 0: default,
- 1: closed spline; the last and first nodes of the spline will become connected, thus closing the spline,
- 2: automatically smoothed spline; the angle parameter value of the nodes between the first and the last node is not used when generating the spline. An internal autosmoothing algorithm is used.


Example 1: SPLINE2 5, 2,

0, 0, 60, 1, 2, 30, 1.5, 1.5, -30, 3, 4, 45, 4, 3, -45

Example 2:

n = 5 FOR i = 1 TO n

SPLINE2 4, 0, 0.0, 2.0, 135.0,

-1.0, 1.8, 240.0, -1.0, 1.0, 290.0, 0.0, 0.0, 45.0

MUL2 -1.0, 1.0 SPLINE2 4, 0,

0.0, 2.0, 135.0,

-1.0, 1.8, 240.0, -1.0, 1.0, 290.0, 0.0, 0.0, 45.0

DEL 1 SPLINE2 4, 0,

0.0, 2.0, 100.0, 0.0, 2.5, 0.0, 0.0, 2.4, 270.0, 0.0, 2.0, 270.0

ADD2 2.5, 0 NEXT i