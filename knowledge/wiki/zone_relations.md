---
id: wiki.generated.zone_relations
type: wiki
category: other
commands: ["ZONE_RELATIONS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ZONE_RELATIONS

n = REQUEST("ZONE_RELATIONS", "", category_name, code, name, number [, category_name2, code2, name2, number2])

Returns in the given variables the zone category name and code and the name and number of the zone where the library part containing this request is located. For doors and windows, there can be a maximum of two zones. The return value of the request is the number of successfully retrieved values (0 if the library part is not inside any zone).