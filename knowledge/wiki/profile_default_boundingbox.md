---
id: wiki.generated.profile_default_boundingbox
type: wiki
category: other
commands: ["PROFILE_DEFAULT_BOUNDINGBOX"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROFILE_DEFAULT_BOUNDINGBOX

n = REQUEST("PROFILE_DEFAULT_BOUNDINGBOX", name_or_index, xmin, ymin, xmax, ymax) Returns the 2 defining coordinate point of the original bounding rectangle relative to the origo of the profile identified by name or index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility: introduced in Archicad 21.