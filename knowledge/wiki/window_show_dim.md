---
id: wiki.generated.window_show_dim
type: wiki
category: other
commands: ["WINDOW_SHOW_DIM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### WINDOW_SHOW_DIM

n = REQUEST("WINDOW_SHOW_DIM", "", show) Returns 1 in the show variable if in the Model View Options > Window options the "with Markers" is checked, 0 otherwise. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.