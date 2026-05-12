---
id: wiki.generated.configuration_number
type: wiki
category: other
commands: ["CONFIGURATION_NUMBER"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### CONFIGURATION_NUMBER

n = REQUEST("CONFIGURATION_NUMBER", "", stConfigurationNumber) Returns the configuration number (as string expression) assigned to the current Archicad license in case of soft license or hardware key. Returns empty string in case of Edu, Trial or Demo licenses. Each configuration number is unique and does not change.

Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility: introduced in Archicad 20.