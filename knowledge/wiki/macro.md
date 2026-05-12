---
id: wiki.generated.macro
type: wiki
category: other
commands: ["MACRO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

#### MACRO OBJECTS

Although the 3D objects you may need can always be broken down into complex or primitive elements, sometimes it is desirable to define these complex elements specifically for certain applications. These individually defined elements are called macros. A GDL macro has its own environment which depends on its calling order. The current values of the MODEL, RADIUS, RESOL, TOLER, PEN, LINE_TYPE, MATERIAL, FILL, STYLE, SHADOW options and the current transformation are all valid in the macro. You can use or modify them, but the modifications will only have an effect locally. They do not take effect on the level the macro was called from. Giving parameters to a macro call means an implicit value assignment on the macro’s level. The parameters A and B are generally used for resizing objects.