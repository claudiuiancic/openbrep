---
id: wiki.generated.resol
type: wiki
category: other
commands: ["RESOL"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RESOL

RESOL n Sets smoothness for cylindrical elements and arcs in polylines. Circles are converted to regular polygons having n sides. Arc conversion is proportional to this. After a RESOL statement, any previous RADIUS and TOLER statements lose their effect. Restriction of parameters:

n >= 3 Default: RESOL 36

RESOL 5 CYLIND 3.0, 1.0

RESOL 36 CYLIND 3.0, 1.0