---
id: wiki.generated.glob_mvo_stair_floor_plan_comp
type: wiki
category: other
commands: ["GLOB_MVO_STAIR_FLOOR_PLAN_COMP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GLOB_MVO_STAIR_FLOOR_PLAN_COMP Stair MVO Component bitset

|2D| |3D| |UI| |Parameter| |Property| |Default|1|
|---|---|---|---|---|---|---|---|---|---|---|---|


mask: returns information about the visible stair components of the floor plan mask = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7 + 128*j8 + 256*j9, where each j can be 0 or 1. j1: walking line j2: numbering j3: up/down text j4: description j5: tread accessories j6: structure - beam j7: structure - stringers j8: structure - cantilevered j9: structure - monolithic Compatibility: introduced in Archicad 22.