---
id: wiki.generated.expressions
type: wiki
category: math
commands: ["EXPRESSIONS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### EXPRESSIONS

You can write compound expressions in GDL statements. Expressions can be of numerical and string type. They are constants, variables, parameters or function calls and any combination of these in operators. Round bracket pairs (( )) (precedence 1) are used to override the default precedence of the operators.

Simple type variables can be given numerical and string values, even in the same script, and can be used in numerical and string type expressions respectively. Operations resulting in strings CANNOT be used directly as macro names in macro calls, or as attribute names in material, fill, line type or style definitions. Variables given a string value will be treated as such and can be used wherever string values are required. If later in the script the same variable is given a numerical value, it will be usable in numerical expressions only until it is given a string value again. Where possible, in the precompilation process the type of the expressions is checked.