---
id: wiki.generated.i
type: wiki
category: other
commands: ["I"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### I

IF condition THEN label IF condition GOTO label IF condition GOSUB label

IF condition THEN label IF condition GOTO label IF condition GOSUB label

IF condition THEN label IF condition GOTO label IF condition GOSUB label

IF condition THEN statement [ELSE statement] IF condition THEN

[statement1 statement2

... statementn]

[ELSE

statementn+1 statementn+2

... statementn+m]

ENDIF IND (MATERIAL, name_string) IND (BUILDING_MATERIAL, name_string) IND (FILL, name_string) IND (LINE_TYPE, name_string) IND (STYLE, name_string) IND (TEXTURE, name_string) IND (PROFILE_ATTR, name_string, index) INITADDONSCOPE (extension, parameter_string1, parameter_string2) INPUT (channel, recordID, fieldID, variable1 [, variable2, ...]) INT (x) ISECTGROUP (g_expr1, g_expr2) ISECTGROUP{2} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) ISECTGROUP{3} (g_expr1, g_expr2, edgeColor, materialId, materialColor [, operationStatus]) ISECTLINES (g_expr1, g_expr2)

- K KILLGROUP g_expr
- L [LET] varnam = n LGT (x) LIBRARYGLOBAL (object_name, parameter, value)


LIGHT red, green, blue, shadow, radius, alpha, beta, angle_falloff, distance1, distance2, distance_falloff [[,] ADDITIONAL_DATA name1 = value1, name2 = value2, ...]

LINE2 x1, y1, x2, y2 LINE_PROPERTY expr [SET] LINE_TYPE name_string [SET] LINE_TYPE index IND (LINE_TYPE, name_string) LIN_ x1, y1, z1, x2, y2, z2 LOCK "name1" [, "name2", ..., "namen"] LOCK ALL ["name1" [, "name2", ..., "namen"]] LOG (x)