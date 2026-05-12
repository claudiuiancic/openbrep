---
id: wiki.generated.calc_angle_unit
type: wiki
category: other
commands: ["CALC_ANGLE_UNIT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CALC_ANGLE_UNIT

n = REQUEST("CALC_ANGLE_UNIT", "", format_string) Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

Example:

format = "" num = 60.55 n = REQUEST ("ANGULAR_DIMENSION", "",format) !"%.2dd" TEXT2 0, 0, STR (format, num) !60.55