---
id: wiki.generated.nurbssurface
type: wiki
category: other
commands: ["NURBSSURFACE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NURBSSURFACE

NURBSSURFACE degree_u, degree_v, nu, nv, knot_u_1, knot_u_2, ..., knot_u_mu, knot_v_1, knot_v_2, ..., knot_v_mv, cPoint_1_1_x, cPoint_1_1_y, cPoint_1_1_z, weight_1_1, cPoint_1_2_x, cPoint_1_2_y, cPoint_1_2_z, weight_1_2, ..., cPoint_1_nv_x, cPoint_1_nv_y, cPoint_1_nv_z, weight_1_nv, cPoint_2_1_x, cPoint_2_1_y, cPoint_2_1_z, weight_2_1,

..., cPoint_nu_nv_x, cPoint_nu_nv_y, cPoint_nu_nv_z, weight_nu_nv

3-dimensional NURBS surface with u-v parameter space, given degree, knotvectors in u and v directions and given controlpoint, weigth net. Degrees are one less than orders of surface (order_u = degree_u + 1), degrees are positive.

degree_u: degree of surface in the u parameter direction degree_v: degree of surface in the v parameter direction nu, nv: number of control points in u and v directions, greater than degree (not less than order) of then surface in given direction

- knot_u_i, knot_v_i: index i knot value in u and v directions

- • their number (the size of knot vector) is given by the following: mu = degree_u + 1 + nu
- • knots are in non-descending order (knot_u_i <= knot_u_{i+1}, knot_v_i <= knot_v_{i+1})
- • equal knot values are allowed, with multiplicity up to degree, or with multiplicity up to degree+1 for the first and last knot.


cPoint_i_j_x, cPoint_i_j_y, cPoint_i_j_z: control point on the control point net, index i in the u direction, index j in

the v direction

weight_i_j: weight for control point cPoint_ij, positive

Surfaces may be periodic in either (u or v) direction or in both directions. Periodic surfaces are not handled separately, but described as floating (not clamped) NURBS surfaces which are geometrically closed and have appropriately continuous connection at the the ends. This is ensured the same way as in case of curves.

The usable domain of a surface is the cross product of the closed intervals between knot_u_{degree_u + 1}, knot_u_{mu - degree_u} and

- knot_v_{degree_v + 1}, knot_v_{mv - degree_v} respectively.