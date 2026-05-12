---
id: wiki.generated.text
type: wiki
category: other
commands: ["TEXT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TEXT

TEXT d, 0, expression A 3D representation of the value of a string or numeric type expression in the current style. See the [SET] STYLE command and the DEFINE STYLE command. d: thickness of the characters in meters. In the current version of GDL, the second parameter is always zero. Note: For compatibility with the 2D GDL script, character heights are always interpreted in millimeters in DEFINE STYLE statements.

- Example 1:


DEFINE STYLE "aa" "New York", 3, 7, 0 SET STYLE "aa" TEXT 0.005, 0, "3D Text"

- Example 2:


name = "Grand" ROTX 90 ROTY -30 TEXT 0.003, 0, name ADDX STW (name)/1000 ROTY 60 TEXT 0.003, 0, "Hotel"