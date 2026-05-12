---
id: wiki.generated.m
type: wiki
category: other
commands: ["M"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### M

MASS top_material, bottom_material, side_material, n, m, mask, h, x1, y1, z1, s1,

... xn, yn, zn, sn, xn+1, yn+1, zn+1, sn+1,

... xn+m, yn+m, zn+m, sn+m

MASS{2} top_material, bottom_material, side_material, n, m, mask, h, x1, y1, z1, s1,

...

xn, yn, zn, sn, xn+1, yn+1, zn+1, sn+1,

... xn+m, yn+m, zn+m, sn+m

[SET] MATERIAL name_or_index IND (MATERIAL, name_string) MAX (x1, x2, ..., xn) MESH a, b, m, n, mask,

z11, z12, ..., z1m, z21, z22, ..., z2m, ... zn1, zn2, ..., znm

MIN (x1, x2, ..., xn) MODEL WIRE MODEL SURFACE MODEL SOLID MUL mx, my, mz MUL2 x, y MULX mx MULY my MULZ mz

- N NEWPARAMETER "name", "type" [, dim1 [, dim2]] FOR variable_name = initial_value TO end_value [ STEP step_value ] NEXT variable_name NOT (x)


NSP NTR () NURBSBODY shadowStatus, smoothnessMin, smoothnessMax

- NURBSCURVE2D degree, nControlPoints, knot_1, knot_2, ..., knot_m, cPoint_1_x, cPoint_1_y, weight_1, cPoint_2_x, cPoint_2_y, weight_2,

..., cPoint_n_x, cPoint_n_y, weight_n

- NURBSCURVE3D degree, nControlPoints, knot_1, knot_2, ..., knot_m, cPoint_1_x, cPoint_1_y, cPoint_1_z, weight_1, cPoint_2_x, cPoint_2_y, cPoint_2_z, weight_2,


..., cPoint_n_x, cPoint_n_y, cPoint_n_z, weight_n

NURBSEDGE vert1, vert2, curve, curveDomainBeg, curveDomainEnd, status, tolerance NURBSFACE n, surface, tolerance,

trim1, trim2, ..., trimn

NURBSFACE{2} n, surface, tolerance, wrap_method, wrap_flags, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4,

trim1, trim2, ..., trimn NURBSLUMP n, face1, face2, ..., facen NURBSSURFACE degree_u, degree_v, nu, nv,

knot_u_1, knot_u_2, ..., knot_u_mu, knot_v_1, knot_v_2, ..., knot_v_mv,

cPoint_1_1_x, cPoint_1_1_y, cPoint_1_1_z, weight_1_1, cPoint_1_2_x, cPoint_1_2_y, cPoint_1_2_z, weight_1_2, ..., cPoint_1_nv_x, cPoint_1_nv_y, cPoint_1_nv_z, weight_1_nv, cPoint_2_1_x, cPoint_2_1_y, cPoint_2_1_z, weight_2_1,

..., cPoint_nu_nv_x, cPoint_nu_nv_y, cPoint_nu_nv_z, weight_nu_nv

NURBSTRIM edge, curve, curveDomainBeg, curveDomainEnd, tolerance NURBSTRIMSINGULAR vertex, curve, curveDomainBeg, curveDomainEnd, tolerance NURBSVERT x, y, z, hard, tolerance

- O OPEN (filter, filename, parameter_string) OUTPUT channel, recordID, fieldID, expression1 [, expression2, ...]
- P


PARAGRAPH name alignment, firstline_indent, left_indent, right_indent, line_spacing [, tab_position1, ...]

[PEN index]

- [[SET] STYLE style1] [[SET] MATERIAL index] 'string1' 'string2'

... 'string n' [PEN index]

- [[SET] STYLE style2] [[SET] MATERIAL index] 'string1'


'string2'

... 'string n'

... ENDPARAGRAPH PARAMETERS name1 = expression1 [,

name2 = expression2, ..., namen = expressionn]

CALL macro_name_string [,] PARAMETERS [ALL][name1=value1, ..., namen=valuen][[,] RETURNED_PARAMETERS r1, r2, ...]

CALL macro_name_string [,]PARAMETERS value1 or DEFAULT [, ..., valuen or DEFAULT]

PARVALUE_DESCRIPTION (parname [, ind1 [, ind2]]) PEN n PGON n, vect, status, edge1, edge2, ..., edgen PGON{2} n, vect, status, wrap, edge_or_wrap1, ..., edge_or_wrapn PGON{3} n, vect, status, wrap_method, wrap_flags, edge_or_wrap1, ..., edge_or_wrapn PI PICTURE expression, a, b, mask PICTURE2 expression, a, b, mask PICTURE2{2} expression, a, b, mask PIPG expression, a, b, mask, n, vect, status,

edge1, edge2, ..., edgen PLACEGROUP g_expr

PLANE n, x1, y1, z1, ..., xn, yn, zn PLANE_ n, x1, y1, z1, s1, ..., xn, yn, zn, sn POINTCLOUD "data_file_name" POLY n, x1, y1, ..., xn, yn POLY2 n, frame_fill, x1, y1, ..., xn, yn POLY2_ n, frame_fill, x1, y1, s1, ..., xn, yn, sn POLY2_A n, frame_fill, fill_pen,

x1, y1, s1, ..., xn, yn, sn

POLY2_B n, frame_fill, fill_pen, fill_background_pen, x1, y1, s1, ..., xn, yn, sn

- POLY2_B{2} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, fillAngle, x1, y1, s1, ..., xn, yn, sn
- POLY2_B{3} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, x1, y1, s1, ..., xn, yn, sn
- POLY2_B{4} n, frame_fill, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, ..., xn, yn, sn
- POLY2_B{5} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY,


mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, ..., xn, yn, sn

- POLY2_B{6} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, gradientInnerRadius, x1, y1, s1, pen1, linetype1, ..., xn, yn, sn, penn, linetypen


POLYROOF defaultMat, k, m, n, offset, thickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,

... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{2} defaultMat, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,


... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{3} defaultMat, mask, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,

... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m, roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

- POLYROOF{4} defaultMat, mask, k, m, n, offset, thickness, totalThickness, applyContourInsidePivot, z_1, ..., z_k, pivotX_1, pivotY_1, pivotMask_1, roofAngle_11, gableOverhang_11, topMat_11, bottomMat_11,


... roofAngle_1k, gableOverhang_1k, topMat_1k, bottomMat_1k,

... pivotX_m, pivotY_m, pivotMask_m,

roofAngle_m1, gableOverhang_m1, topMat_m1, bottomMat_m1,

... roofAngle_mk, gableOverhang_mk, topMat_mk, bottomMat_mk, contourX_1, contourY_1, contourMask_1, edgeTrim_1, edgeAngle_1, edgeMat_1,

... contourX_n, contourY_n, contourMask_n, edgeTrim_n, edgeAngle_n, edgeMat_n

POLY_ n, x1, y1, s1, ..., xn, yn, sn POSITION position_keyword PREPAREFUNCTION channel, function_name, expression1 [, expression2, ...] PRINT expression [, expression, ...] PRISM n, h, x1, y1, ..., xn, yn PRISM_ n, h, x1, y1, s1, ..., xn, yn, sn VALUES "profile_parameter_name" [[,] PROFILETYPES_MASK profile_types], value_definition1

[, value_definition2, ...] IND (PROFILE_ATTR, name_string, index) PROJECT2 projection_code, angle, method

- PROJECT2{2} projection_code, angle, method [, backgroundColor, fillOrigoX, fillOrigoY, filldirection]
- PROJECT2{3} projection_code, angle, method, parts [, backgroundColor, fillOrigoX, fillOrigoY, filldirection][[,] PARAMETERS name1=value1, ..., namen=valuen]
- PROJECT2{4} projection_code, angle, useTransparency, statusParts, numCutplanes, cutplaneHeight1, ..., cutplaneHeightn, method1, parts1, cutFillIndex1, cutFillFgPen1, cutFillBgPen1,


cutFillOrigoX1, cutFillOrigoY1, cutFillDirection1, cutLinePen1, cutLineType1, projectedFillIndex1, projectedFillFgPen1, projectedFillBgPen1, projectedFillOrigoX1, projectedFillOrigoY1, projectedFillDirection1, projectedLinePen1, projectedLineType1,

... method(numCutplanes+1)), parts(numCutplanes+1), cutFillIndex(numCutplanes+1), cutFillFgPen(numCutplanes+1), cutFillBgPen(numCutplanes+1), cutFillOrigoX(numCutplanes+1), cutFillOrigoY(numCutplanes+1), cutFillDirection(numCutplanes+1), cutLinePen(numCutplanes+1), cutLineType(numCutplanes+1), projectedFillIndex(numCutplanes+1), projectedFillFgPen(numCutplanes+1), projectedFillBgPen(numCutplanes+1), projectedFillOrigoX(numCutplanes+1), projectedFillOrigoY(numCutplanes+1), projectedFillDirection(numCutplanes+1), projectedLinePen(numCutplanes+1), projectedLineType(numCutplanes+1)

PUT expression [, expression, ...] PYRAMID n, h, mask, x1, y1, s1, ..., xn, yn, sn

- R RADIUS radius_min, radius_max RECT a, b RECT2 x1, y1, x2, y2 REF COMPONENT code [, keycode [, numeric_expression]] REF DESCRIPTOR code [, keycode] REMOVEKEY (dictionary.key)


REPEAT [statement1 statement2

... statementn]

UNTIL condition REQ (parameter_string) REQUEST (question_name, name | index, variable1 [, variable2, ...]) RESOL n RETURN CALL macro_name_string [,]

PARAMETERS [ALL][name1=value1, ..., namen=valuen][[,] RETURNED_PARAMETERS r1, r2, ...]

REVOLVE n, alpha, mask, x1, y1, s1, ..., xn, yn, sn REVOLVEDSHELL topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4,

defaultMat, n, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

REVOLVEDSHELLANGULAR topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23,

preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

REVOLVEDSHELLANGULAR{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

REVOLVEDSHELLANGULAR{3} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, segmentationType, nOfSegments, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

REVOLVEDSHELL{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

REVOLVEDSHELL{3} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, status, offset, thickness, flipped, trimmingBody, alphaOffset, alpha, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, x_1, y_1, s_1,

... x_n, y_n, s_n

- REVOLVE{2} n, alphaOffset, alpha, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn
- REVOLVE{3} n, alphaOffset, alpha, betaOffset, beta, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn
- REVOLVE{4} n, alphaOffset, alpha, betaOffset, beta, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn
- REVOLVE{5}n, alphaOffset, alpha, betaOffset, beta, mask, sideMat, x1, y1, s1, mat1, ..., xn, yn, sn, matn


RICHTEXT x, y,

height, 0, textblock_name RICHTEXT2 x, y, textblock_name

RND (x) ROT x, y, z, alpha ROT2 alpha ROTX alphax ROTY alphay ROTZ alphaz ROUND_INT (x) RULED n, mask,

u1, v1, s1, ..., un, vn, sn, x1, y1, z1, ..., xn, yn, zn

RULEDSEGMENTED n, mask, x11, y11, z11, s1,..., x1n, y1n, z1n, sn, x21, y21, z21, ..., x2n, y2n, z2n

RULEDSEGMENTED{2} top_material, bottom_material, n, mask, textureMode, x11, y11, z11, s1, mat1..., x1n, y1n, z1n, sn, matn, x21, y21, z21, ..., x2n, y2n, z2n

RULEDSHELL topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, m, g, offset, thickness, flipped, trimmingBody, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, firstpolyX_1, firstpolyY_1, firstpolyS_1,

... firstpolyX_n, firstpolyY_n, firstpolyS_n, secondpolyX_1, secondpolyY_1, secondpolyS_1,

... secondpolyX_m, secondpolyY_m, secondpolyS_m, profile2Tran_11, profile2Tran_12, profile2Tran_13, profile2Tran_14 profile2Tran_21, profile2Tran_22, profile2Tran_23, profile2Tran_24 profile2Tran_31, profile2Tran_32, profile2Tran_33, profile2Tran 34 generatrixFirstIndex_1, generatrixSecondIndex_1,

... generatrixFirstIndex_g, generatrixSecondIndex_g

- RULEDSHELL{2} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, m, g, status, offset, thickness, flipped, trimmingBody, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14, preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, firstpolyX_1, firstpolyY_1, firstpolyS_1,

... firstpolyX_n, firstpolyY_n, firstpolyS_n, secondpolyX_1, secondpolyY_1, secondpolyS_1,

... secondpolyX_m, secondpolyY_m, secondpolyS_m, profile2Tran_11, profile2Tran_12, profile2Tran_13, profile2Tran_14 profile2Tran_21, profile2Tran_22, profile2Tran_23, profile2Tran_24 profile2Tran_31, profile2Tran_32, profile2Tran_33, profile2Tran 34 generatrixFirstIndex_1, generatrixSecondIndex_1,

... generatrixFirstIndex_g, generatrixSecondIndex_g

- RULEDSHELL{3} topMat, bottomMat, sideMat_1, sideMat_2, sideMat_3, sideMat_4, defaultMat, n, m, g, status, offset, thickness, flipped, trimmingBody, preThickenTran_11, preThickenTran_12, preThickenTran_13, preThickenTran_14,


preThickenTran_21, preThickenTran_22, preThickenTran_23, preThickenTran_24, preThickenTran_31, preThickenTran_32, preThickenTran_33, preThickenTran_34, firstpolyX_1, firstpolyY_1, firstpolyS_1,

... firstpolyX_n, firstpolyY_n, firstpolyS_n, secondpolyX_1, secondpolyY_1, secondpolyS_1,

... secondpolyX_m, secondpolyY_m, secondpolyS_m, profile2Tran_11, profile2Tran_12, profile2Tran_13, profile2Tran_14 profile2Tran_21, profile2Tran_22, profile2Tran_23, profile2Tran_24 profile2Tran_31, profile2Tran_32, profile2Tran_33, profile2Tran 34 generatrixFirstIndex_1, generatrixSecondIndex_1,

... generatrixFirstIndex_g, generatrixSecondIndex_g

RULED{2} n, mask, u1, v1, s1, ..., un, vn, sn, x1, y1, z1, ..., xn, yn, zn