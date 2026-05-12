---
id: wiki.generated.name_of_fill
type: wiki
category: other
commands: ["NAME_OF_FILL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NAME_OF_FILL

n = REQUEST("NAME_OF_FILL", index, name) Returns in the name variable the fill name identified by index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

If index < 0, it refers to a fill defined in the GDL script or the MASTER_GDL file. A call of a request with index = 0 returns an empty string. The return value of the request is the number of successfully retrieved values (1 if no error occurred, 0 for error when the index is not valid).