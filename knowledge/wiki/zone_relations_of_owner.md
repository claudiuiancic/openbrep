---
id: wiki.generated.zone_relations_of_owner
type: wiki
category: other
commands: ["ZONE_RELATIONS_OF_OWNER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ZONE_RELATIONS_OF_OWNER

n = REQUEST("ZONE_RELATIONS_OF_OWNER", "", category_name, code, name, number [, category_name2, code2, name2, number2])

Returns in the given variables the category name & code and the zone name & number of the zone where the owner of the object is located. So, it is meaningful, if the library part has owner (door-window labels and door-window markers, etc.). In case of a door label, its owner is the door. For doors and windows, there can be a maximum of two related zones. The return value of the request is the number of successfully retrieved values (0 if the object has no owner, or its owner is not inside any zone). Causes warning if used in parameter script.