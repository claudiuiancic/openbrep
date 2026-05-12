---
id: wiki.generated.rgb_of_pen
type: wiki
category: other
commands: ["RGB_OF_PEN"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RGB_OF_PEN

n = REQUEST("RGB_OF_PEN", penindex, r, g, b) Like the REQ function (but in just one call), returns in the specified variables the value of the r, g, b components of the pen. Expression returns

- 0 containing dummy return values (empty string or 0) if used in parameter script, causing additional warning.