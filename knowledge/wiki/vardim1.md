---
id: wiki.generated.vardim1
type: wiki
category: other
commands: ["VARDIM1"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### VARDIM1

- VARDIM1 (expr)
- VARDIM2


VARDIM2 (expr)

These functions return as integers the actual dimension values for the (array) expression specified as a parameter. They must be used if you want to handle correctly all actual elements of a dynamic array or an array parameter. If no element of a dynamic array was previously set, the return value is 0. For one-dimensional arrays VARDIM2 returns 0.

- Example 1: Examples for numeric expressions:

Z 5.5 (+15)

-x a*(b+c) SIN(x+y)*z a+r*COS(i*d) 5' 4" SQR (x^2 + y^2) / (1 - d) a + b * sin (alpha) height * width

- Example 2: Examples for string expressions:


"Constant string" name + STR ("%m", i) + "." + ext string_param <> "Mode 1"

- Example 3: Examples for expressions using array values:


DIM tab[5], tab2[3][4] ! declaration tab[1] + tab[2] tab2[2][3] + A PRINT tab DIM f1 [5], v1[], v2[][] v1[3] = 3 ! v1[1] = 0, v1[2] = 0, array of 3 elements v2[2][3] = 23 ! all other elements(2 X 3) = 0 PRINT v1, v2 DIM f1 [5], v1[], v2[][] FOR i = 1 TO VARDIM1(f1)

f1[i] = i NEXT i v1 = f1 v2 [1] = f1 PRINT v1, v2

- Example 4: Examples for expressions using dictionary values: DICT _exampleDict ! DICT simple key types


_exampleDict.false = (1 = 2) ! logical false (integer internally) _exampleDict.true = (1 = 1) ! logical true (integer internally) _exampleDict.int = 2 ! integer _exampleDict.float = 1 / 3 ! floating-point _exampleDict.string = "Custom text" ! string

! DICT array key type ! initialize array on-the-fly _exampleDict.array[1] = _exampleDict.float ! append to array on-the-fly _exampleDict.array[2] = _exampleDict.float * 2

! append to array with automatic initialization of elements in between _exampleDict.array[4] = _exampleDict.float * 3 ! DICT array of DICTs DIM array[] DICT _element _element.a = "A" _element.b = 1 _exampleDict.array = array ! change existing array to empty one _exampleDict.array[2] = _element ! different vartype than previous ! print DICT array of DICTs print "\n\t",

"Print DICT array of DICTs",

"\n----------------------------------------------------------------------------\n\t", vartype(_exampleDict.array), vardim1(_exampleDict.array), "\n", _exampleDict.array, "\n----------------------------------------------------------------------------"