---
id: wiki.generated.end
type: wiki
category: control
commands: ["END"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### END / EXIT

END [v1, v2, ..., vn] EXIT [v1, v2, ..., vn]

End of the current GDL script. The program terminates or returns to the level above. It is possible to use several ENDs or EXITs in a GDL file. If the optional list of values is specified, the current script will pass these return values to its caller.

Note: the number of possible returned elements is limited at 32767 items. See the description of receiving returned parameters at the CALL command.