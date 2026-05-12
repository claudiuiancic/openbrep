---
id: wiki.generated.line_property
type: wiki
category: 3d
commands: ["LINE_PROPERTY"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### LINE_PROPERTY

LINE_PROPERTY expr Defines the property for all subsequently generated lines in the 2D script (RECT2, LINE2, ARC2, CIRCLE2, SPLINE2, SPLINE2A, POLY2, FRAGMENT2 commands) until the next LINE_PROPERTY statement. Default value is generic. expr: possible values:

0: all lines are generic lines, 1: all lines are inner, 2: all lines are contour.