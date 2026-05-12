---
id: wiki.generated.label_position
type: wiki
category: other
commands: ["LABEL_POSITION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LABEL_POSITION position of the label

|2D| |3D| |UI| |Parameter| |Property| |Default|0|
|---|---|---|---|---|---|---|---|---|---|---|---|


array[3][2] containing the coordinates of the 3 points defining the label pointer and the starting position of the label GDL symbol. Compatibility: parameter and property script restrictions are introduced in Archicad 22. View-dependent value in case of "Fixed Angle" ON. Project-dependent in case "Label Orientation" is set to "Parallel" or "Perpendicular", and the parent element is moved, thus changing the value of the variable while not running the parameter script of the label itself (can not be stored as parameter).