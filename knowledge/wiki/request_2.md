---
id: wiki.generated.request
type: wiki
category: param
commands: ["REQUEST"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### REQUEST OPTIONS

n = REQUEST (question_name, name_or_index, variable1 [, variable2, ...]) n = REQUEST{2} (question_name, name_or_index, name, variable1 [, variable2, ...]) n = REQUEST{3} (question_name, name, name_or_index_array, variable1 [, variable2, ...]) n = REQUEST{4} (question_name, name_or_index, index, name, variable1 [, variable2, ...])

The first parameter represents the question string while the second (or more) represents the object of the question (if it exists). The other parameters are variable names in which the return values (the answers) are stored. The function’s return value is the number of the answer (in the case of a badly formulated question or a nonexistent name, the value will be 0).

Archicad identifies the order and number of the input parameters by either the version of the REQUEST command, or the exact name (as string constant) of the request option. This means that using the first or both of the following options is the safest:

- • name of the request is always a constant string
- • version is added to the command