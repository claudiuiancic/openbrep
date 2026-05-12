---
id: wiki.generated.values_2
type: wiki
category: param
commands: ["VALUES{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### VALUES{2}

VALUES{2} "parameter_name" [,]num_expression1, description1,

[, num_expression2, description2, ...]

VALUES{2} "parameter_name" [,]num_values_array1, descriptions_array1

[, num_values_array2, descriptions_array2, ...] parameter_name: name of an existing angle, length, real, or integer type parameter num_expressioni, num_values_arrayi: simple value definition for a numerical parameter, or array expression containing

multiple numerical values. If num_expression1 has an explicit '+' sign, the ',' after the parameter name must be added.

descriptioni, descriptions_arrayi: description string of the numerical value i, or array expression containing multiple

description strings of the values defined by num_values_arrayi (array dimensions must match). Available only for VALUES{2}

Example 1: Simple value lists

- VALUES "par1" 1, 2, 3
- VALUES "par2" "a", "b"
- VALUES "par3" 1, CUSTOM, SIN (30)
- VALUES "par4" 4, RANGE(5, 10], 12, RANGE(,20] STEP 14.5, 0.5, CUSTOM


Example 2: Read all string values from a file for use in a value list DIM sarray[] ! file in the library, containing parameter data filename = "ProjectNotes.txt" ch1 = OPEN ("text", filename, "MODE=RO, LIBRARY") i = 1 j = 1 sarray[1] = "" ! collect all strings DO

n = INPUT (ch1, i, 1, var) IF n > 0 AND VARTYPE (var) = 2 THEN

sarray[j] = var j = j + 1

ENDIF i = i + 1

WHILE n > 0 CLOSE ch1 ! parameter popup with strings read from the file VALUES "RefNote" sarray