---
id: wiki.generated.toler
type: wiki
category: other
commands: ["TOLER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### TOLER

TOLER d Sets smoothness for cylindrical elements and arcs in polylines. The error of the arc approximation (i.e., the greatest distance between the theoretical arc and the generated chord) will be smaller than d. After a TOLER statement, any previous RADIUS and RESOL statements lose their effect.

TOLER 0.1 CYLIND 3.0, 1.0

TOLER 0.01 CYLIND 3.0, 1.0