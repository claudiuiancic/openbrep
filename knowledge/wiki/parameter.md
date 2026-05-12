---
id: wiki.generated.parameter
type: wiki
category: other
commands: ["PARAMETER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### PARAMETER BUFFER MANIPULATION

The parameter buffer is a built-in data structure that may be used if some values (coordinates, for example) change after a definite rule that can be described using a mathematical expression. This is useful if, for instance, you want to store the current values of your variables.

| | |
|---|---|
| | |


| | | | | | |
|---|---|---|---|---|---|


PUT

| | | | | | | |
|---|---|---|---|---|---|---|


NSP = NSP+1

The parameter buffer is an infinitely long array in which you can store numeric values using the PUT command. PUT stores the given values at the end of the buffer. These values can later be used (by the GET and USE commands) in the order in which they were entered (i.e., the first stored value will be the first one used). A GET(n) or USE(n) command is equivalent with n values separated by commas. This way, they can be used in any GDL parameter list where n values are needed.

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |


GET NSP = NSP-1

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |


| | | | | | | |
|---|---|---|---|---|---|---|


USE

NSP = NSP