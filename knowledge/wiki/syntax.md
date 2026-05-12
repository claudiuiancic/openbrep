---
id: wiki.generated.syntax
type: wiki
category: other
commands: ["SYNTAX"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### SYNTAX LISTING OF GDL COMMANDS

- A ABS (x) ACS (x) ADD dx, dy, dz ADD2 x, y ADDGROUP (g_expr1, g_expr2) ADDGROUP{2} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) ADDGROUP{3} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus])


LIGHT red, green, blue, shadow, radius, alpha, beta, angle_falloff, distance1, distance2, distance_falloff [[,] ADDITIONAL_DATA name1 = value1, name2 = value2, ...]

DEFINE MATERIAL name [,] BASED_ON orig_name [,] PARAMETERS name1 = expr1 [, ...] [[,] ADDITIONAL_DATA name1 = expr1 [, ...]]

ADDX dx ADDY dy ADDZ dz LOCK ALL ["name1" [, "name2", ..., "namen"]] HIDEPARAMETER ALL ["name1" [, "name2", ..., "namen"]]

CALL macro_name_string [,] PARAMETERS [ALL][name1=value1, ..., namen=valuen][[,] RETURNED_PARAMETERS r1, r2, ...]

APPLICATION_QUERY (extension_name, parameter_string, variable1, variable2, ...) ARC r, alpha, beta ARC2 x, y, r, alpha, beta ARMC r1, r2, l, h, d, alpha ARME l, r1, r2, h, d ASN (x) ATN (x)

- B BASE


DEFINE MATERIAL name [,] BASED_ON orig_name [,] PARAMETERS name1 = expr1 [, ...] [[,] ADDITIONAL_DATA name1 = expr1 [, ...]]

BEAM left_material, right_material, vertical_material, top_material, bottom_material, height, x1, x2, x3, x4, y1, y2, y3, y4, t, mask1, mask2, mask3, mask4

BINARY mode [, section, elementID] BINARYPROP BITSET (x, b [, expr]) BITTEST (x, b) BLOCK a, b, c

BODY status BPRISM_ top_material, bottom_material, side_material,

n, h, radius, x1, y1, s1,

... xn, yn, sn

BREAKPOINT expression BRICK a, b, c [SET] BUILDING_MATERIAL name_or_index

[, cut_fill_pen [, cut_fill_bkgd_pen, [iOverrideFlag]]] IND (BUILDING_MATERIAL, name_string) BWALL_ left_material, right_material, side_material,

height, x1, x2, x3, x4, t, radius, mask1, mask2, mask3, mask4, n, x_start1, y_low1, x_end1, y_high1, frame_shown1,

... x_startn, y_lown, x_endn, y_highn, frame_shownn, m, a1, b1, c1, d1,

... am, bm, cm, dm