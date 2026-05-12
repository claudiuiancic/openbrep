---
id: wiki.generated.name_of_material
type: wiki
category: other
commands: ["NAME_OF_MATERIAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NAME_OF_MATERIAL

n = REQUEST("NAME_OF_MATERIAL", index, name) Returns in the variable the material name identified by index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

If index < 0, it refers to a material defined in the GDL script or the MASTER_GDL file. A call of a request with index = 0 returns in the variable the name of the default material. The return value of the request is the number of successfully retrieved values (1 if no error occurred, 0 for error when the index is not valid).