---
id: wiki.generated.height_of_style
type: wiki
category: other
commands: ["HEIGHT_OF_STYLE"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### HEIGHT_OF_STYLE

n = REQUEST("HEIGHT_OF_STYLE", name, height [, descent, leading]) name: Name of the style to query. height: Returns the total height of the style measured in millimeters (height in meters is height / 1000 * GLOB_SCALE). descent: Returns the descent (the distance in millimeters from the text base line to the descent line). leading: Returns he leading (the distance in millimeters from the descent line to the ascent line).