---
id: wiki.generated.simple
type: wiki
category: other
commands: ["SIMPLE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### SIMPLE TYPES

Variables, parameters and expressions can be of two simple types: numeric or string.

Numeric expressions are constant numbers, numeric variables or parameters, functions that return numeric values, and any combination of these in operations. Numeric expressions can be integer or real. Integer expressions are integer constants, variables or parameters, functions that return integer values, and any combination of these in operations which results in integers. Real expressions are real constants, variables or parameters, functions that return real values, and any combination of these (or integer expressions) in operations which results in reals. A numeric expression

being an integer or a real is determined during the compilation process and depends only on the constants, variables, parameters and the operations used to combine them. Real and integer expressions can be used the same way at any place where a numeric expression is required, however, in cases where a combination of these may result in precision problems, a compiler warning appears (comparison of reals or reals and integers using relational operators '=' or '<>', or boolean operators AND, OR, EXOR; IF or GOTO statements with real label expressions).

String expressions are constant strings, string variables or parameters, functions that return strings, and any combination of these in operations which result in strings.