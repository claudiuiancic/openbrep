---
id: wiki.generated.spline2a
type: wiki
category: 2d
commands: ["SPLINE2A"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### SPLINE2A

SPLINE2A n, status, x1, y1, angle1, length_previous1, length_next1,

... xn, yn, anglen, length_previousn, length_nextn

len_nexti

anglei

y

len_previ

i

(xi,yi)

1

n

x

Extension of the SPLINE2 command (Bézier spline), used mainly in automatic 2D script generation because of its complexity. For more details, see “Lines / Drawing Splines” in the Documentation chapter of the Archicad Help. si: Status values:

0: default, 1: closed spline; the last and first nodes of the spline will become connected, thus closing the spline, 2: automatically smoothed spline; the angle, length_previousi and length_nexti parameter values of the nodes between the first and the last node are not used when generating the spline. An internal autosmoothing algorithm is used.

- xi, yi: control point coordinates. length_previousi, length_nexti: tangent lengths for the previous and the next control points. anglei: tangent direction angle.


Example:

SPLINE2A 9, 2,

0.0, 0.0, 0.0, 0.0, 0.0, 0.7, 1.5, 15, 0.9, 1.0, 1.9, 0.8, 72, 0.8, 0.3, 1.9, 1.8, 100, 0.3, 0.4,

- 1.8, 3.1, 85, 0.4, 0.5,
- 2.4, 4.1, 352, 0.4, 0.4,
- 3.5, 3.3, 338, 0.4, 0.4,
- 4.7, 3.7, 36, 0.4, 0.8, 6.0, 4.6, 0, 0.0, 0.0