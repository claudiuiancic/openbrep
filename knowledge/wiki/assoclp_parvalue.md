---
id: wiki.generated.assoclp_parvalue
type: wiki
category: other
commands: ["ASSOCLP_PARVALUE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ASSOCLP_PARVALUE

n = REQUEST("ASSOCLP_PARVALUE", expr, name_or_index, type, flags, dim1, dim2, p_values) Returns information in the given variables on the library part parameter with which the library part containing this request is associated. Can be used in property objects, labels and marker objects. The function return value is the number of successfully retrieved values, 0 if the specified parameter does not exist or an error occurred.

expr: the request’s object, associated library part parameter name or index expression. name_or_index: returns the index or the name of the parameter, depending on the previous expression type (returns index if a parameter

name, name if the index is specified).

type: parameter type, possible values:

- 1: boolean
- 2: integer
- 3: real number
- 4: string
- 5: length
- 6: angle
- 7: line
- 8: material
- 9: fill
- 10: pen color


- 11: light switch
- 12: rgb color
- 13: light intensity
- 14: separator
- 15: title
- 16: building material
- 17: profile Compatibility: introduced in Archicad 23


flags: flags = j1 + 2*j2 + 64*j7 + 128*j8, where each j can be 0 or 1. j1: child/indented in parameter list j2: with bold text in parameter list j7: disabled (locked in all contexts) j8: hidden in the parameter list

dim1, dim2: dim1 is the number of rows, dim2 the number of columns. dim1 = 0, dim2 = 0: simple, scalar value dim1 > 0, dim2 = 0: one dimensional array dim1 > 0, dim2 > 0: two dimensional array If dim2 > 0, then dim1 > 0.

p_values: returns the parameter value or array of values. The array elements are returned successively, row by row as a one dimensional array, independently of the dimensions of the variable specified to store it. If the variable is not a dynamic array, there are as many elements stored as there is room for (for a simple variable only one, the first element). If values is a two dimensional dynamic array, all elements are stored in the first row.