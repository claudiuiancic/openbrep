---
id: wiki.generated.dim
type: wiki
category: other
commands: ["DIM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DIM

DIM var1[dim_1], var2[dim_1][dim_2], var3[ ], var4[ ][ ], var5[dim_1][ ], var5[ ][dim_2]

GDL supports one and two dimensional arrays. Variables become arrays after the above declaration statement, in which their dimensions are specified. (Dictionary type variables cannot be redeclared as arrays or vice versa.)

After the DIM keyword there can be any number of variable names separated by commas. var1, var2, ... are the array names, while the numbers between the brackets represent the dimensions of the array (numerical constants). Variable expressions cannot be used as dimensions. If they are missing, the array is declared to be dynamic (one or both dimensions).

Library part parameters can also be arrays. Their actual dimensions are specified in the library part dialog. Parameter arrays do not have to be declared in the script and they are dynamic by default. When referencing the library part using a CALL statement, the actual values of an array parameter can be an array with arbitrary dimensions.

The elements of the arrays can be referenced anywhere in the script but if they are variables, only after the declaration.

var1[num_expr] or var1 var2[num_expr1][num_expr2] or var2[num_expr1] or var2

Writing the array name without actual indices means referencing the whole array (or a line of a two-dimensional array) which is accepted in some cases (CALL, PRINT, LET, PUT, REQUEST, INPUT, OUTPUT, SPLIT statements). For dynamic arrays there is no limitation for the actual index value. During the interpretation, when a non-existing dynamic array element is given a value, the necessary quantity of memory is allocated and the missing elements are all set to 0 (numerical).

Warning! This may cause an unexpected out of memory error in some cases. Each index - even of a possibly wrong, huge value - is considered valid, since the interpreter is unable to detect the error condition. A non-existing dynamic array element is 0 (numerical).

Arrays having a fixed dimension are checked for the validity of the actual index on the fixed dimension. Array variables with fixed length cannot accept dynamic array values in assignments. However, dynamic arrays that are given whole array values will take on those values. This also applies to some statements where whole array references can be used as return parameters. (REQUEST, INPUT, SPLIT).

Array elements can be used in any numerical or string expression. They can be given string or numerical values. Indices start with 1, and any numerical expression can be used as an index. Array elements can be of different simple types (numerical, string, group). The type of the whole array (main type) is the type of its first element ([1] or [1][1]). Parameter and global variable arrays cannot be of mixed type.