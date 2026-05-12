---
id: wiki.generated.window_door_zone_relev
type: wiki
category: other
commands: ["WINDOW_DOOR_ZONE_RELEV"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WINDOW_DOOR_ZONE_RELEV

n = REQUEST("WINDOW_DOOR_ZONE_RELEV", "", out_direction) Effective only for Doors and Windows. Use it as complement to the "ZONE_RELATIONS" REQUEST. out_direction: Returned Door/Window opening direction

1: is in that of the first room identified by the "ZONE_RELATIONS" REQUEST. 2: is towards the second room or there is only one room and the opening direction is to the outside.