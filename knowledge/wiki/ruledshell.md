---
id: wiki.generated.ruledshell
type: wiki
category: 3d
commands: ["RULEDSHELL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RULEDSHELL

RULEDSHELL topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, m, g, offset, thickness, flipped, trimmingBody, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, firstpolyX_1, firstpolyY_1, firstpolyS_1,

... firstpolyX_n, firstpolyY_n, firstpolyS_n, secondpolyX_1, secondpolyY_1, secondpolyS_1,

... secondpolyX_m, secondpolyY_m, secondpolyS_m, profile2Tran_11, profile2Tran_12, profile2Tran_13, profile2Tran_14 profile2Tran_21, profile2Tran_22, profile2Tran_23, profile2Tran_24 profile2Tran_31, profile2Tran_32, profile2Tran_33, profile2Tran 34 generatrixFirstIndex_1, generatrixSecondIndex_1,

... generatrixFirstIndex_g, generatrixSecondIndex_g

Surface created by connecting two polylines. topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4: Materials on the top, bottom and four sides

of the object.

defaultMat: the numeric index of the "inner" material of the object. This material becomes visible at cut surfaces, e.g., if the object

is cut by a plane.

n: number of vertices for first profile base polyline.

- m: number of vertices for second profile base polyline. g: number of generatrices. offset: an offset for the thickness of the shell. Cannot be negative. thickness: thickness of the shell. flipped:


1: if the shell should be flipped,

- 0: otherwise

preThickenTran: a transformation executed before thickening. See the XFORM command for the meaning of parameters. trimmingBody:

- 1: if the shell is to be closed for trimming purposes, 0: otherwise


firstpolyX, firstpolyY, firstpolyS: X and Y coordinates and status values for the first base profile polyline. See the

REVOLVE command for details.

secondpolyX, secondpolyY, secondpolyS: X and Y coordinates and status values for the second base profile polyline. See

the REVOLVE command for details.

profile2Tran: a transformation executed on the second profile. Use this transformation to position the second profile relative to the

first one. See the XFORM command for the meaning of parameters.