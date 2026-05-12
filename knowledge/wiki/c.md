---
id: wiki.generated.c
type: wiki
category: other
commands: ["C"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### C

CALL macro_name_string [,] PARAMETERS [ALL][name1=value1, ..., namen=valuen][[,] RETURNED_PARAMETERS r1, r2, ...]

CALL macro_name_string [,]PARAMETERS value1 or DEFAULT [, ..., valuen or DEFAULT]

CALL macro_name_string [, parameter_list] CALLFUNCTION (channel, function_name, parameter, variable1 [, variable2, ...]) CEIL (x) CIRCLE r CIRCLE2 x, y, r CLOSE channel CLOSEADDONSCOPE channel COMPONENT name, quantity, unit [, proportional_with, code, keycode, unitcode] CONE h, r1, r2, alpha1, alpha2 COONS n, m, mask,

x11, y11, z11, ..., x1n, y1n, z1n, x21, y21, z21, ..., x2n, y2n, z2n, x31, y31, z31, ..., x3m, y3m, z3m, x41, y41, z41, ..., x4m, y4m, z4m

COONS{2} n, m, mask,

x11, y11, z11, ..., x1n, y1n, z1n, x21, y21, z21, ..., x2n, y2n, z2n, x31, y31, z31, ..., x3m, y3m, z3m, x41, y41, z41, ..., x4m, y4m, z4m

COOR wrap, vert1, vert2, vert3, vert4 COOR{2} wrap_method, wrap_flags, vert1, vert2, vert3, vert4 COOR{3} wrapping_method, wrap_flags,

origin_X, origin_Y, origin_Z, endOfX_X, endOfX_Y, endOfX_Z, endOfY_X, endOfY_Y, endOfY_Z, endOfZ_X, endOfZ_Y, endOfZ_Z

COS (x) CPRISM_ top_material, bottom_material, side_material,

n, h, x1, y1, s1, ..., xn, yn, sn

- CPRISM_{2} top_material, bottom_material, side_material, n, h, x1, y1, alpha1, s1, mat1,

... xn, yn, alphan, sn, matn

- CPRISM_{3} top_material, bottom_material, side_material, mask, n, h, x1, y1, alpha1, s1, mat1,

... xn, yn, alphan, sn, matn

- CPRISM_{4} top_material, bottom_material, side_material, mask, n, h, x1, y1, alpha1, s1, mat1,


... xn, yn, alphan, sn, matn

CREATEGROUPWITHMATERIAL (g_expr, repl_directive, pen, material) CROOF_ top_material, bottom_material, side_material,

n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1,

... xn, yn, alphan, sn

- CROOF_{2} top_material, bottom_material, side_material, n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1, mat1,


... xn, yn, alphan, sn, matn

- CROOF_{3} top_material, bottom_material, side_material, mask, n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1, mat1,

... xn, yn, alphan, sn, matn

- CROOF_{4} top_material, bottom_material, side_material, mask, n, xb, yb, xe, ye, height, angle, thickness, x1, y1, alpha1, s1, mat1,


... xn, yn, alphan, sn, matn

CSLAB_ top_material, bottom_material, side_material, n, h, x1, y1, z1, s1, ..., xn, yn, zn, sn

CUTPLANE [x [, y [, z [, side [, status]]]]] [statement1 ... statementn] CUTEND

- CUTPLANE{2} angle [, status] [statement1 ... statementn] CUTEND
- CUTPLANE{3} [x [, y [, z [, side [, status]]]]] [statement1 ... statementn] CUTEND


CUTPOLY n, x1, y1, ..., xn, yn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

CUTPOLYA n, status, d, x1, y1, mask1, ..., xn, yn, maskn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

CUTSHAPE d [, status] [statement1 statement2 ... statementn] CUTEND

CUTFORM n, method, status, rx, ry, rz, d, x1, y1, mask1 [, mat1],

... xn, yn, maskn [, matn]

CUTFORM{2} n, method, status, rx, ry, rz, d, x1, y1, mask1 [, mat1],

... xn, yn, maskn [, matn]

CUTPLANE [x [, y [, z [, side [, status]]]]] [statement1 ... statementn] CUTEND

- CUTPLANE{2} angle [, status] [statement1 ... statementn] CUTEND
- CUTPLANE{3} [x [, y [, z [, side [, status]]]]] [statement1 ... statementn] CUTEND


CUTPOLY n, x1, y1, ..., xn, yn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

CUTPOLYA n, status, d, x1, y1, mask1, ..., xn, yn, maskn [, x, y, z]

[statement1 statement2

... statementn] CUTEND

CUTSHAPE d [, status] [statement1 statement2 ... statementn] CUTEND

CWALL_ left_material, right_material, side_material, height, x1, x2, x3, x4, t, mask1, mask2, mask3, mask4, n, x_start1, y_low1, x_end1, y_high1, frame_shown1,

... x_startn, y_lown, x_endn, y_highn, frame_shownn, m, a1, b1, c1, d1,

... am, bm, cm, dm

CYLIND h, r