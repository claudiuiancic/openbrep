---
id: wiki.generated.del
type: wiki
category: 3d
commands: ["DEL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DEL

DEL n [, begin_with] Deletes n entries from the transformation stack. If the begin_with parameter is not specified, deletes the previous n entries in the transformation stack. The local coordinate system moves back to a previous position. If the begin_with transformation is specified, deletes n entries forward, beginning with the one denoted by begin_with. Numbering starts with

1. If the begin_with parameter is specified and n is negative, deletes backward. If fewer transformations were issued in the current script than denoted by the given n number argument, then only the issued transformations are deleted.

###### DEL TOP

DEL TOP Deletes all current transformations in the current script.