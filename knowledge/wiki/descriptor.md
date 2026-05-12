---
id: wiki.generated.descriptor
type: wiki
category: other
commands: ["DESCRIPTOR"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DESCRIPTOR

DESCRIPTOR name [, code, keycode] Local descriptor definition. Scripts can include any number of DESCRIPTORs.

name: can extend to more than one line. New lines can be defined by the character '\n' and tabulators by '\t'. Adding '\' to the end of a line allows you to continue the string in the next line without adding a new line. Inside the string, if the '\' character is doubled (\\), it will lose its control function and simply mean '\'. The length of the string (including the new line characters) cannot exceed 255 characters: additional characters will be simply cut by the compiler. If you need a longer text, use several DESCRIPTORs.

code: string, defines a code for the descriptor. keycode: string, reference to a key in an external database. The key will be assigned to the descriptor.