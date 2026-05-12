---
id: wiki.generated.mep_route_attributes
type: wiki
category: other
commands: ["MEP_ROUTE_ATTRIBUTES"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### MEP_ROUTE_ATTRIBUTES

n = REQUEST("MEP_ROUTE_ATTRIBUTES", InputAttributes, MEPRouteAttributes) Returns attributes specific to the MEP routing tool. Can be used only in MEP routing. Expression returns 0 and contains dummy return values (empty dictionary) if used in parameter script, causing additional warning.