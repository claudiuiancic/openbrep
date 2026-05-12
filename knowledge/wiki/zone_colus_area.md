---
id: wiki.generated.zone_colus_area
type: wiki
category: other
commands: ["ZONE_COLUS_AREA"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ZONE_COLUS_AREA

n = REQUEST("ZONE_COLUS_AREA", "", area)

Returns in the area variable the total area of the columns placed in the current zone. Effective only for Zone Stamps. Available only for compatibility reasons. It is recommended to use quantities set in Zone Stamp fix parameters. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.