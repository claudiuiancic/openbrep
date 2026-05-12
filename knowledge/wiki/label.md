---
id: wiki.generated.label
type: wiki
category: other
commands: ["LABEL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### LABEL

Any line can start with a label which is used as a reference for a subsequent statement. A label is an integer number or a constant string between quotation marks, followed by a colon (:). A string label is case sensitive. Labels are checked for single occurrence. The execution of the program can be continued from any label by using a GOTO or GOSUB statement.