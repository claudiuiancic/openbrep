---
id: wiki.generated.window_door_zone_relev_of_owner
type: wiki
category: other
commands: ["WINDOW_DOOR_ZONE_RELEV_OF_OWNER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WINDOW_DOOR_ZONE_RELEV_OF_OWNER

n = REQUEST("WINDOW_DOOR_ZONE_RELEV_OF_OWNER", "", out_direction) Effective only if the library part’s parent is a door or a window (markers, labels). Use it as a complement to the "ZONE_RELATIONS_OF_OWNER" REQUEST. out_direction: Returned Door/Window opening direction

1: is in that of the first room identified by the "ZONE_RELATIONS_OF_OWNER" REQUEST. 2: is towards the second room or there is only one room and the opening direction is to the outside.

Causes warning if used in parameter script.