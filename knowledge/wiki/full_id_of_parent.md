---
id: wiki.generated.full_id_of_parent
type: wiki
category: other
commands: ["FULL_ID_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### FULL_ID_OF_PARENT

n = REQUEST("FULL_ID_OF_PARENT", "", id_string)

For annotation elements linked or hotlinked on the floor plan, returns all identifiers (Master ID) of the linked modules and the parent library parts’ identifier set in the tool’s settings dialog box in the id_string variable (otherwise empty string). Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.