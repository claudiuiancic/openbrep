---
id: wiki.generated.door_show_dim
type: wiki
category: control
commands: ["DOOR_SHOW_DIM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### DOOR_SHOW_DIM

n = REQUEST("DOOR_SHOW_DIM", "", show) Returns 1 in the show variable if in the Model View Options > Door options the "with Markers" is checked, 0 otherwise. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.