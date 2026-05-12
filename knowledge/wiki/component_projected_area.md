---
id: wiki.generated.component_projected_area
type: wiki
category: other
commands: ["COMPONENT_PROJECTED_AREA"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_PROJECTED_AREA

n = REQUEST("COMPONENT_PROJECTED_AREA", idxSkin, projectedArea) Returns the projected area of the indexed skin. Available in property script only (other scripts return 0). Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. idxSkin: Possible values:

0: for basic elements 1- : index of the skin in composites 1- : index of the component in profiles

Example:

n = request ("COMPONENT_PROJECTED_AREA", 0, a) COMPONENT "Projected Area", a, "m2"

Used in property script, first request the area of the skin, then create a component using the returned value.