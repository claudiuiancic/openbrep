---
id: wiki.generated.matching_properties
type: wiki
category: other
commands: ["MATCHING_PROPERTIES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MATCHING_PROPERTIES

n = REQUEST("MATCHING_PROPERTIES", type, name1, name2, ...)

type: Selects which property library parts to request 1: individually associated. otherwise: associated by criteria.

namei: Returned library part names. If used in an associative label, the function returns the properties of the element the label is associated with. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.