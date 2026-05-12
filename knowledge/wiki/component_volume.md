---
id: wiki.generated.component_volume
type: wiki
category: other
commands: ["COMPONENT_VOLUME"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_VOLUME

n = REQUEST("COMPONENT_VOLUME", idxSkin, skinVolume)

Returns the volume of the indexed skin/component. Available in property script only (other scripts return 0). Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. idxSkin: Possible values:

0: for basic elements 1- : index of the skin in composites 1- : index of the component in profiles

Example:

n = request ("COMPONENT_VOLUME", 0, v) COMPONENT "Volume", v, "m3"

Used in property script, first request the volume of the skin, then create a component using the returned value.