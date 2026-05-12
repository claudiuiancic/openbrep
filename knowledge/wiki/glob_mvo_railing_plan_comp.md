---
id: wiki.generated.glob_mvo_railing_plan_comp
type: wiki
category: other
commands: ["GLOB_MVO_RAILING_PLAN_COMP"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GLOB_MVO_RAILING_PLAN_COMP Railing MVO Component bitset

|2D| |3D| |UI| |Parameter| |Property| |Default|127|
|---|---|---|---|---|---|---|---|---|---|---|---|


mask: returns information about the visible stair components of the floor plan

mask = j1 + 2*j2 + 4*j3 + 8*j4 + 16*j5 + 32*j6 + 64*j7, where each j can be 0 or 1.

- j1: posts
- j2: toprail
- j3: handrails
- j4: rails
- j5: inner posts
- j6: balusters
- j7: panels