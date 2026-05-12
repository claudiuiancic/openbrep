---
id: wiki.generated.hotspot
type: wiki
category: 3d
commands: ["HOTSPOT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### HOTSPOT

HOTSPOT x, y, z [, unID [, paramReference [, flags [, displayParam [, customDescription]]]]] A 3D hotspot in the point (x, y, z).

unID: the unique identifier of the hotspot in the 3D script. It is useful if you have a variable number of hotspots. paramReference: parameter that can be edited by this hotspot using the graphical hotspot based parameter editing method. displayParam: parameter to display in the information palette when editing the paramRefrence parameter. Members of arrays can be

passed as well.

customDescription: custom description of the displayed parameter in the information palette. When using this option, displayParam

must be set as well (use paramReference for default). See Graphical Editing Using Hotspots for using HOTSPOT.