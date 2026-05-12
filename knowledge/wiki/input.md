---
id: wiki.generated.input
type: wiki
category: other
commands: ["INPUT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### INPUT

INPUT (channel, recordID, fieldID, variable1 [, variable2, ...])

The number of given parameters defines the number of values from the starting position read from the file identified by the channel value. The parameter list must contain at least one value. This function puts the read values into the parameters as ordered. These values can be of numeric or string type, independent of the parameter type defined for storage.

The return value is the number of the successfully read values. When encountering an end of file character, -1 is returned. recordID, fieldID: the string or numeric type starting position of the reading, its contents are interpreted by the extension.