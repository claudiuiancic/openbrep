---
id: wiki.generated.name_of_building_material
type: wiki
category: other
commands: ["NAME_OF_BUILDING_MATERIAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NAME_OF_BUILDING_MATERIAL

n = REQUEST("NAME_OF_BUILDING_MATERIAL", index, name) Returns in the variable the building material name identified by index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. The return value of the request is the number of successfully retrieved values (1 if no error occurred, 0 for error when the index is not valid).