---
id: wiki.generated.program_info
type: wiki
category: other
commands: ["PROGRAM_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROGRAM_INFO

n = REQUEST("PROGRAM_INFO", "", name[, version[, keySerialNumber[, isCommercial]]]) Returns information on the currently running program. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

name: name of the program version: version number of the program keySerialNumber: serial number of the keyplug isCommercial: returns true if there is running a full (commercial) version of the program