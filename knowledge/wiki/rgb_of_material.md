---
id: wiki.generated.rgb_of_material
type: wiki
category: other
commands: ["RGB_OF_MATERIAL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RGB_OF_MATERIAL

n = REQUEST("RGB_OF_MATERIAL", name, r, g, b) Like the REQ function (but in just one call), returns in the specified variables the value of the r, g, b components of the material. Expression returns 0 containing dummy return values (empty string or 0) if used in parameter script, causing additional warning.