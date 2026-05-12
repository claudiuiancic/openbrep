---
id: wiki.generated.conventions
type: wiki
category: other
commands: ["CONVENTIONS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### CONVENTIONS USED IN THIS BOOK

[aaa] Square brackets mean that the enclosed elements are optional (if they are bold, they must be entered as shown). {n} command version number

... Previous element may be repeated | Exclusive or relation between parameters of a command variable Any GDL variable name prompt Any character string (must not contain quote character) bold_string UPPERCASE_STRING special characters Must be entered as shown other_lowercase_string_in_parameter_list Any GDL expression

## COORDINATE TRANSFORMATIONS

This chapter tells you about the types of transformations available in GDL (moving, scaling and rotating the coordinate system) and the way they are interpreted and managed. About Transformations

In GDL, all the geometric elements are linked strictly to the local coordinate system. GDL uses a right-handed coordinate system. For example, one corner of a block is in the origin and its sides are in the x-y, x-z and y-z planes.

Placing a geometric element in the desired position requires two steps. First, move the coordinate system to the desired position. Second, generate the element. Every movement, rotation or stretching of the coordinate system along or around an axis is called a transformation. Transformations are stored in a stack; interpretation starts from the last one backwards. Scripts inherit this stack; they can insert new elements onto it but can only delete the locally defined ones. It is possible to delete one, more or all of the transformations defined in the current script. After returning from a script, the locally defined transformations are removed from the stack.