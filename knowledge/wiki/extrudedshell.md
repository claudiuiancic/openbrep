---
id: wiki.generated.extrudedshell
type: wiki
category: 3d
commands: ["EXTRUDEDSHELL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### EXTRUDEDSHELL

EXTRUDEDSHELL topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, offset, thickness, flipped, trimmingBody, x_tb, y_tb, x_te, y_te, topz, tangle, x_bb, y_bb, x_be, y_be, bottomz, bangle, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThicakenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

Surface created by first extruding a polyline, then adding thickness to it. topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4: Materials on the top, bottom and four sides

of the object.

defaultMat: the numeric index of the "inner" material of the object. This material becomes visible at cut surfaces, e.g., if the object

is cut by a plane.

- n: number of profile base polyline vertices. offset: an offset for the thickness of the shell. Cannot be negative. thickness: the thickness of the shell.


flipped: 1: if the shell should be flipped, 0: otherwise.

trimmingBody: 1: if the shell is to be closed for trimming purposes, 0: otherwise.

x_tb, y_tb, x_te, y_te, topz, tangle: Specify the top plane of the extrusion. The meaning of the parameters is the same

as for the SPRISM_{2} command.

x_bb, y_bb, x_be, y_be, bottomz, bangle: Specify the bottom plane of the extrusion. The meaning of the parameters

is the same as for the SPRISM_{2} command. preThickenTran_i: a transformation executed before thickening. See the XFORM command for the meaning of parameters. x_i, y_i, s_i: X and Y coordinates and status values for the base profile polyline. See the EXTRUDE command for details. The

visibility of the sides cannot be controlled with the status.