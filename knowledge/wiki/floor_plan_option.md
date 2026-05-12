---
id: wiki.generated.floor_plan_option
type: wiki
category: other
commands: ["FLOOR_PLAN_OPTION"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FLOOR_PLAN_OPTION

n = REQUEST("FLOOR_PLAN_OPTION", "", storyViewpointType) Returns the story viewpoint type which is set in the Model View Options. 0 stands for "Floor Plan", 1 stands for "Ceiling Plan". Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.