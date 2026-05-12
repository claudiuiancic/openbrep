---
id: wiki.generated.id_of_main
type: wiki
category: other
commands: ["ID_OF_MAIN"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### ID_OF_MAIN

n = REQUEST("ID_OF_MAIN", "", id_string)

For library parts placed on the floor plan, returns the identifier set in the tool’s settings dialog box in the id_string variable (otherwise empty string). Not working on annotation elements (e.g. Label, D/W Marker, Zone Stamp). Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.