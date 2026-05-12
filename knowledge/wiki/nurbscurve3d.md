---
id: wiki.generated.nurbscurve3d
type: wiki
category: other
commands: ["NURBSCURVE3D"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSCURVE3D

- NURBSCURVE3D degree, nControlPoints, knot_1, knot_2, ..., knot_m, cPoint_1_x, cPoint_1_y, cPoint_1_z, weight_1, cPoint_2_x, cPoint_2_y, cPoint_2_z, weight_2,


..., cPoint_n_x, cPoint_n_y, cPoint_n_z, weight_n

- 2 and 3 dimensional NURBS curves with given degree, knotvector, controlpoints and weigths. degree: degree of NURBS curve, one less than order of curve (order = degree + 1), positive nControlPoints: number of control points (n), greater than the degree of the curve (not less than the order) knot_i: index i knot value


- • number of knot values (m, the size of knot vector) is given by the following: m = degree + 1 + n
- • knots are in non-descending order (knot_i <= knot_{i+1})
- • equal knot values are allowed, with multiplicity up to degree, or with multiplicity up to degree+1 for the first and last knot.

cPoint_i_x, cPoint_i_y, cPoint_i_z: coordinates of index i control point weight_i: weigth of index i control point, positive

Periodic curves are not handled separately, but described as floating (not clamped) NURBS curves which are geometrically closed and have appropriately continuous connection at the the ends. This is ensured by repeating sufficient number of control points and knot-intervals at the end:

- • the last degree many control points are duplicates of the first degree many control points (not in reverse order),
- • the first twice-the-degree number of knot-differences (knot_1-knot_0, knot_2-knot_1, ...) are the same as the last ones in the knot vector (these are the knots which are in connection with the first (or last) degree many control points).


The usable domain of a curve is the closed interval between knot_{degree + 1} and knot_{m - degree}.