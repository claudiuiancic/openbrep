---
id: wiki.generated.name_of_program
type: wiki
category: other
commands: ["NAME_OF_PROGRAM"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### NAME_OF_PROGRAM

n = REQUEST("NAME_OF_PROGRAM", "", program_name)

Returns in the given variable the name of the program, e.g., "Archicad". Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

Example: Printing the name of the program

n = REQUEST ("NAME_OF_PROGRAM", "", program_name) PRINT program_name