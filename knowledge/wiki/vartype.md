---
id: wiki.generated.vartype
type: wiki
category: other
commands: ["VARTYPE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### VARTYPE

VARTYPE (expression) Returns the type of the expression:

- • 1 - numerical
- • 2 - string
- • 3 - group (as result of the ADDGROUP command and such)
- • 4 - dictionary Useful when reading values in variables with the INPUT command, which can change between type 1 and 2 according to the current values. The type of these variables is not checked during the compilation process.