---
id: wiki.generated.values
type: wiki
category: param
commands: ["VALUES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### VALUES

VALUES "parameter_name" [,]value_definition1 [, value_definition2, ...] VALUES "fill_parameter_name" [[,] FILLTYPES_MASK fill_types], value_definition1

[, value_definition2, ...]

VALUES "profile_parameter_name" [[,] PROFILETYPES_MASK profile_types], value_definition1

[, value_definition2, ...] Defines a value restriction for a parameter (except dictionary types). The command has a special syntax for fill type and profile type parameters. If used on an array parameter, the restriction will be applied to all items individually.

parameter_name: name of an existing parameter fill_parameter_name: name of an existing fillpattern type parameter fill_types:

fill_types = j1 + 2*j2 + 4*j3, where each j can be 0 or 1. j1: cut fills, j2: cover fills, j3: drafting fills.

Can be used for fill-pattern type parameters only. The fill popup for this parameter will contain only those types of fills which are specified by the bits set to 1. Default is all fills (0).

profile_parameter_name: name of an existing profile type parameter profile_types:

profile_types = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5, where each j can be 0 or 1.

- j1: wall,
- j2: beam,
- j3: column,
- j4: handrail,
- j5: other.


Can be set for profile type parameters only. The value list for any profile type parameter includes all existing profiles of the planfile automatically, no individual VALUES definition is needed. Using VALUES without masking (0) has the exact same result. Using VALUES with masking can filter the value list, leaving only the corresponding profiles of the bits set to 1. Individual profile indexes can be listed as regular value definitions as well.

value_definitioni: value definition, can be: expression: numerical or string expression, or CUSTOM: keyword, meaning that any custom value can be entered, or RANGE: range definition, with optional step RANGE left_delimiter[lower_limit], [upper_limit]right_delimiter [STEP step_start_value, step_value] left_delimiter: [, meaning >=, or (, meaning >; lower_limit: lower limit expression; upper_limit: upper limit expression; right_delimiter: ], meaning <=, or ), meaning <; step_start_value: starting value; step_value: step value. If value_definition1 is a numerical expression with explicit '+' sign, the ',' after the parameter name must be added.