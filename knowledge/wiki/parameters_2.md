---
id: wiki.generated.parameters
type: wiki
category: param
commands: ["PARAMETERS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PARAMETERS

PARAMETERS name1 = expression1 [, name2 = expression2, ..., namen = expressionn]

namei: the name of the parameter. expressioni: the new value of the parameter. Using this command, the parameter values of a Library Part can be modified by the Parameter Script. The modification will only be effective for the next interpretation. Commands in macros refer to the caller’s parameters. If the parameter is a value list, the value chosen will be either an existing value, the custom value, or the first value from the value list. In addition, the global string variable GLOB_MODPAR_NAME contains the name of the last user-modified parameter.