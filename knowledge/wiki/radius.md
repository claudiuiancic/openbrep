---
id: wiki.generated.radius
type: wiki
category: other
commands: ["RADIUS"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### RADIUS

RADIUS radius_min, radius_max Sets smoothness for cylindrical elements and arcs in polylines. A circle with a radius of r is represented:

- • if r < radius_min, by a hexagon,
- • if r >= radius_max, by a 36-edged polygon,
- • if radius_min < r < radius_max, by a polygon of (6+30*(r-radius_min)/(radius_max-radius_min)) edges. Arc conversion is proportional to this. After a RADIUS statement, all previous RESOL and TOLER statements lose their effect. Restriction of parameters:


r_min <= r_max

RADIUS 1.1, 1.15 CYLIND 3.0, 1.0

RADIUS 0.9, 1.15 CYLIND 3.0, 1.0