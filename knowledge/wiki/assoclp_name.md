---
id: wiki.generated.assoclp_name
type: wiki
category: other
commands: ["ASSOCLP_NAME"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ASSOCLP_NAME

n = REQUEST("ASSOCLP_NAME", "", name) Returns in the given variable the name of the library part associated with the label or marker object. For elements (Walls, Slabs, etc.) the name is an empty string. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.