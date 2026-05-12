---
id: wiki.generated.pen_of_rgb
type: wiki
category: other
commands: ["PEN_OF_RGB"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PEN_OF_RGB

n = REQUEST("PEN_OF_RGB", "r g b", penindex) Like the REQ function (but in just one call), returns in the specified variable the index of the pen corresponding to the given RGB values. Expression returns 0 containing dummy return values (empty string or 0) if used in parameter script, causing additional warning.