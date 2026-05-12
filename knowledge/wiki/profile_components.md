---
id: wiki.generated.profile_components
type: wiki
category: other
commands: ["PROFILE_COMPONENTS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROFILE_COMPONENTS

n = REQUEST("PROFILE_COMPONENTS", name_or_index, nComponents, compType1, compType2, ..., compTypen) Returns the number (nComponents) and component types (compTypen) of the profile identified by name or index. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. compTypei: Possible values of profile component types:

0: core 1: finish 2: other

- Compatibility: introduced in Archicad 21.


Example:

_nComponents = 0 dim _componentTypes[] n = REQUEST ("PROFILE_COMPONENTS", myProfileIdx, _nComponents, _componentTypes