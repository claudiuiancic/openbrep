---
id: wiki.generated.output
type: wiki
category: other
commands: ["OUTPUT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### OUTPUT

OUTPUT channel, recordID, fieldID, expression1 [, expression2, ...] Writes as many values into the file identified by the channel value from the given position as there are defined expressions. There has to be at least one expression. The type of values is the same as those of the expressions.

recordID, fieldID: the string or numeric type starting position of the writing; its contents are interpreted by the extension.