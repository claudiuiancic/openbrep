---
id: wiki.generated.s
type: wiki
category: other
commands: ["S"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### S

SECT_ATTRS fill, fill_background_pen,

fill_pen, contour_pen [, line_type] SECT_ATTRS{2} contour_pen [, line_type] SECT_FILL fill, fill_background_pen,

fill_pen, contour_pen [SET] STYLE name_string [SET] STYLE index [SET] MATERIAL name_or_index [SET] BUILDING_MATERIAL name_or_index

[, cut_fill_pen [, cut_fill_bkgd_pen, [iOverrideFlag]]]

[SET] FILL name_string [SET] FILL index [SET] LINE_TYPE name_string [SET] LINE_TYPE index SETMIGRATIONGUID guid SGN (x) SHADOW casting [, catching] SIN (x) SLAB n, h, x1, y1, z1, ..., xn, yn, zn SLAB_ n, h, x1, y1, z1, s1, ..., xn, yn, zn, sn MODEL SOLID SPHERE r SPLINE2 n, status, x1, y1,

angle1, ..., xn, yn, anglen SPLINE2A n, status, x1, y1, angle1, length_previous1, length_next1,

... xn, yn, anglen, length_previousn, length_nextn

SPLIT (string, format, variable1 [, variable2, ..., variablen]) SPRISM_ top_material, bottom_material, side_material,

n, xb, yb, xe, ye, h, angle, x1, y1, s1,

... xn, yn, sn

- SPRISM_{2} top_material, bottom_material, side_material, n,


xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,

... xn, yn, sn, matn

- SPRISM_{3} top_material, bottom_material, side_material, mask, n, xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,

... xn, yn, sn, matn

- SPRISM_{4} top_material, bottom_material, side_material, mask, n, xtb, ytb, xte, yte, topz, tangle, xbb, ybb, xbe, ybe, bottomz, bangle, x1, y1, s1, mat1,


... xn, yn, sn, matn

SQR (x) FOR variable_name = initial_value TO end_value [ STEP step_value ] NEXT variable_name STORED_PAR_VALUE ("oldparname", outputvalue) STR (numeric_expression, length, fractions) STR (format_string, numeric_expression) STRLEN (string_expression) STRSTR (string_expression1, string_expression2[, case_insensitivity]) STRSUB (string_expression, start_position, characters_number) STRTOLOWER (string_expression)

STRTOUPPER (string_expression) STR{2} (format_string, numeric_expression [, extra_accuracy_string]) STW (string_expression) [SET] STYLE name_string [SET] STYLE index IND (STYLE, name_string) SUBGROUP (g_expr1, g_expr2) SUBGROUP{2} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) SUBGROUP{3} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) MODEL SURFACE SURFACE3D () SWEEP n, m, alpha, scale, mask,

u1, v1, s1, ..., un, vn, sn, x1, y1, z1, ..., xm, ym, zm

SWEEPGROUP (g_expr, x, y, z) SWEEPGROUP{2} (g_expr, x, y, z) SWEEPGROUP{3} (g_expr, x, y, z, edgeColor, materialId, materialColor, method) SWEEPGROUP{4} (g_expr, x, y, z, edgeColor, materialId, materialColor, method, status) SWEEPGROUP{5} (g_expr, x, y, z, edgeColor, materialId, materialColor, method, status)

- T TAN (x) TEVE x, y, z, u, v TEXT d, 0, expression


TEXT2 x, y, expression TEXTBLOCK name width, anchor, angle, width_factor, charspace_factor, fixed_height,

'string_expr1' [, 'string_expr2', ...] TEXTBLOCK_ name width, anchor, angle, width_factor, charspace_factor, fixed_height, n,

'expr_1' [, 'expr_2', ..., 'expr_n'] IND (TEXTURE, name_string)

IF condition THEN label IF condition GOTO label IF condition GOSUB label

IF condition THEN statement [ELSE statement] IF condition THEN

[statement1 statement2

... statementn]

[ELSE statementn+1 statementn+2 ... statementn+m]

ENDIF FOR variable_name = initial_value TO end_value [ STEP step_value ] NEXT variable_name TOLER d DEL TOP TUBE n, m, mask,

u1, w1, s1,

... un, wn, sn,

x1, y1, z1, angle1,

... xm, ym, zm, anglem

TUBEA n, m, mask, u1, w1, s1,

... un, wn, sn, x1, y1, z1, ... xm, ym, zm

TUBE{2} top_material, bottom_material, cut_material, n, m, mask, u1, w1, s1, mat1,

... un, wn, sn, matn, x1, y1, z1, angle1,

... xm, ym, zm, anglem

- U UI_BUTTON type, text, x, y [, width, height, id [, url]] UI_BUTTON type, text, x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ]


UI_COLORPICKER "redParamName", "greenParamName", "blueParamName", x0, y0 [, width [,

height]] UI_COLORPICKER{2} redParamName, greenParamName, blueParamName, x0, y0 [, width [, height]] UI_CURRENT_PAGE index UI_CUSTOM_POPUP_INFIELD "name", x, y, width, height,

storeHiddenId, treeDepth, groupingMethod, selectedValDescription,

value1, value2, valuesArray1, .... valuen, valuesArrayn

UI_CUSTOM_POPUP_INFIELD "name", x, y, width, height , extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_INFIELD{2} name, x, y, width, height, storeHiddenId, treeDepth, groupingMethod, selectedValDescription, value1, value2, valuesArray1, .... valuen, valuesArrayn

UI_CUSTOM_POPUP_INFIELD{2} name, x, y, width, height , extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM itemID, fieldID, "name", childFlag, image, paramDesc,

storeHiddenId, treeDepth, groupingMethod, selectedValDescription, value1, value2, valuesArray1, .... valuen, valuesArrayn

UI_CUSTOM_POPUP_LISTITEM itemID, fieldID, "name", childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM{2} itemID, fieldID, name, childFlag, image, paramDesc,

storeHiddenId, treeDepth, groupingMethod, selectedValDescription, value1, value2, valuesArray1, .... valuen, valuesArrayn

UI_CUSTOM_POPUP_LISTITEM{2} itemID, fieldID, name, childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_DIALOG title [, size_x, size_y] UI_GROUPBOX text, x, y, width, height UI_INFIELD "name", x, y, width, height [,

method, picture_name, images_number, rows_number, cell_x, cell_y, image_x, image_y, expression_image1, text1,

... expression_imagen, textn]

UI_INFIELD "name", x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ]

- UI_INFIELD{2} name, x, y, width, height [, method, picture_name, images_number, rows_number, cell_x, cell_y, image_x, image_y, expression_image1, text1,


... expression_imagen, textn]

- UI_INFIELD{2} name, x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ]
- UI_INFIELD{3} name, x, y, width, height [, method, picture_name, images_number, rows_number, cell_x, cell_y, image_x, image_y, expression_image1, text1, value_definition1,


... [picIdxArray, textArray, valuesArray,

...] expression_imagen, textn, value_definitionn]

- UI_INFIELD{3} name, x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ]
- UI_INFIELD{4} "name", x, y, width, height [, method, picture_name, images_number, rows_number, cell_x, cell_y, image_x, image_y, expression_image1, text1, value_definition1,


... [picIdxArray, textArray, valuesArray,

...] expression_imagen, textn, value_definitionn]

- UI_INFIELD{4} "name", x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ]


UI_LISTFIELD fieldID, x, y, width, height [, iconFlag [, description_header [, value_header]]]

UI_LISTFIELD fieldID, x, y, width, height [, iconFlag [, description_header [, value_header]]] [ UI_TOOLTIP tooltiptext ]

UI_LISTITEM itemID, fieldID, "name" [, childFlag [, image [, paramDesc]]] UI_LISTITEM itemID, fieldID, "name" [, childFlag [, image [, paramDesc]]]

[ UI_TOOLTIP tooltiptext ]

UI_LISTITEM{2} itemID, fieldID, name [, childFlag [, image [, paramDesc]]] UI_LISTITEM{2} itemID, fieldID, name [, childFlag [, image [, paramDesc]]]

[ UI_TOOLTIP tooltiptext ] UI_OUTFIELD expression, x, y [, width, height [, flags]]

UI_OUTFIELD expression, x, y, width, height [, flags] [ UI_TOOLTIP tooltiptext ] UI_PAGE page_number [, parent_id, page_title [, image]] UI_PICT picture_reference, x, y [, width, height [, mask]] UI_PICT expression, x, y [, width, height [, mask]] [ UI_TOOLTIP tooltiptext ] UI_PICT_BUTTON type, text, picture_reference,

x, y, width, height [, id [, url]] UI_PICT_BUTTON type, text, picture_reference,

x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ] UI_PICT_PUSHCHECKBUTTON name, text, picture_reference,

frameFlag, x, y, width, height [UI_TOOLTIP tooltip] UI_PICT_PUSHCHECKBUTTON{2} "name", text, picture_reference,

frameFlag, x, y, width, height [UI_TOOLTIP tooltip] UI_PICT_RADIOBUTTON name, value, text,

picture_reference, x, y, width, height [UI_TOOLTIP tooltip] UI_PICT_RADIOBUTTON{2} "name", value, text,

picture_reference, x, y, width, height [UI_TOOLTIP tooltip] UI_RADIOBUTTON name, value, text, x, y, width, height UI_RADIOBUTTON name, value, text, x, y, width, height [ UI_TOOLTIP tooltiptext ] UI_RADIOBUTTON{2} "name", value, text, x, y, width, height UI_SEPARATOR x1, y1, x2, y2 UI_SLIDER "name", x0, y0, width, height [, nSegments [, sliderStyle]] UI_SLIDER{2} name, x0, y0, width, height [, nSegments [, sliderStyle]] UI_STYLE fontsize, face_code UI_TEXTSTYLE_INFIELD name, faceCodeMask, x, y,

buttonWidth, buttonHeight[, buttonOffsetX]

UI_TEXTSTYLE_INFIELD{2} "name", faceCodeMask, x, y,

buttonWidth, buttonHeight [, buttonOffsetX] UI_BUTTON type, text, x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ] UI_PICT_BUTTON type, text, picture_reference,

x, y, width, height [, id [, url]] [ UI_TOOLTIP tooltiptext ] UI_INFIELD "name", x, y, width, height [, extra parameters ... ]

[ UI_TOOLTIP tooltiptext ] UI_INFIELD{2} name, x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ] UI_INFIELD{3} name, x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ] UI_INFIELD{4} "name", x, y, width, height [, extra parameters ... ] [ UI_TOOLTIP tooltiptext ] UI_CUSTOM_POPUP_INFIELD "name", x, y, width, height , extra parameters ... [ UI_TOOLTIP tooltiptext ] UI_CUSTOM_POPUP_INFIELD{2} name, x, y, width, height , extra parameters ...

[ UI_TOOLTIP tooltiptext ] UI_RADIOBUTTON name, value, text, x, y, width, height [ UI_TOOLTIP tooltiptext ] UI_OUTFIELD expression, x, y, width, height [, flags] [ UI_TOOLTIP tooltiptext ] UI_PICT expression, x, y [, width, height [, mask]] [ UI_TOOLTIP tooltiptext ] UI_LISTFIELD fieldID, x, y, width, height [, iconFlag [, description_header [,

value_header]]] [ UI_TOOLTIP tooltiptext ]

UI_LISTITEM itemID, fieldID, "name" [, childFlag [, image [, paramDesc]]] [ UI_TOOLTIP tooltiptext ]

UI_LISTITEM{2} itemID, fieldID, name [, childFlag [, image [, paramDesc]]] [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM itemID, fieldID, "name", childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

UI_CUSTOM_POPUP_LISTITEM{2} itemID, fieldID, name, childFlag , image , paramDesc, extra parameters ... [ UI_TOOLTIP tooltiptext ]

REPEAT [statement1 statement2

... statementn]

UNTIL condition USE (n)

- V VALUES "parameter_name" [,]value_definition1 [, value_definition2, ...]


VALUES "fill_parameter_name" [[,] FILLTYPES_MASK fill_types], value_definition1 [, value_definition2, ...]

VALUES "profile_parameter_name" [[,] PROFILETYPES_MASK profile_types], value_definition1 [, value_definition2, ...]

VALUES{2} "parameter_name" [,]num_expression1, description1, [, num_expression2, description2, ...]

VALUES{2} "parameter_name" [,]num_values_array1, descriptions_array1

[, num_values_array2, descriptions_array2, ...] VARDIM1 (expr) VARDIM2 (expr) VARTYPE (expression) VECT x, y, z

VERT x, y, z VERT x, y, z, hard VOLUME3D ()

- W WALLARC2 x, y, r, alpha, beta


WALLBLOCK2 n, fill_control, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, fillAngle, x1, y1, s1,

... xn, yn, sn

WALLBLOCK2{2} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, innerRadius, x1, y1, s1,

... xn, yn, sn

WALLHOLE n, status, x1, y1, mask1,

... xn, yn, maskn [, x, y, z]

WALLHOLE2 n, fill_control, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, fillAngle, x1, y1, s1,

... xn, yn, sn

WALLHOLE2{2} n, frame_fill, fillcategory, distortion_flags, fill_pen, fill_background_pen, fillOrigoX, fillOrigoY, mxx, mxy, myx, myy, innerRadius, x1, y1, s1,

... xn, yn, sn

WALLLINE2 x1, y1, x2, y2 WALLNICHE n, method, status,

rx, ry, rz, d, x1, y1, mask1, [mat1,]

... xn, yn, maskn[, matn]

DO [statment1 statement2

... statementn]

WHILE condition WHILE condition DO

[statement1 statement2

... statementn]

ENDWHILE MODEL WIRE