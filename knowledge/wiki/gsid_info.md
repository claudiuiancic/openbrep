---
id: wiki.generated.gsid_info
type: wiki
category: other
commands: ["GSID_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### GSID_INFO

n = REQUEST("GSID_INFO", "", userId, organizationIds) Returns, in the given variables, information (as string expressions) on the currently logged-in user. The function return value is the number of successfully retrieved values, or 0 if an error occurred.

userId: unique user Id of the currently logged-in user. Always retrieved if there is a logged-in user. organizationIds: organization Id strings array, can be empty. Expression returns 0 and contains dummy return values (empty strings) if used in parameter script, creating an additional warning.

- Compatibility: introduced in Archicad 26.