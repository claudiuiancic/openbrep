---
id: wiki.generated.stw
type: wiki
category: other
commands: ["STW"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### STW

STW (string_expression) Returns the (real) width of the string in millimeters displayed in the current style. The width in meters, at current scale, is STW (string_expression) / 1000 * GLOB_SCALE.

Example:

| |
|---|


DEFINE STYLE "own" "Gabriola", 180000 / GLOB_SCALE, 1, 0 SET STYLE "own" string = "abcd" width = STW (string) / 1000 * GLOB_SCALE n = REQUEST ("HEIGHT_OF_STYLE", "own", height) height = height / 1000 * GLOB_SCALE TEXT2 0,0, string RECT2 0,0, width, -height