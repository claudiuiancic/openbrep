---
id: wiki.generated.reference_level_data
type: wiki
category: other
commands: ["REFERENCE_LEVEL_DATA"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### REFERENCE_LEVEL_DATA

n = REQUEST("REFERENCE_LEVEL_DATA", "", name1, elev1, name2, elev2,

name3, elev3, name4, elev4) Returns in the given variables the names and elevations of the reference levels as set in the Options/Project Preferences/Reference Levels dialog. The function return value is the number of successfully retrieved values, 0 if an error occurred.