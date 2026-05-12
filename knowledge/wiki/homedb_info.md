---
id: wiki.generated.homedb_info
type: wiki
category: other
commands: ["HOMEDB_INFO"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### HOMEDB_INFO

n = REQUEST("HOMEDB_INFO", "", homeDBIntId, homeDBUserId, homeDBName, homeContext) Returns in the given variables the internal ID (integer), the user ID and name (strings) of the home database (where the library part containing this request was placed). homeContext: the contents of homeDBIntId, homeDBUserId, homeDBName depend on the home database

- 1: placed on the floor plan: the story internal ID, index as a string and name
- 2: placed on a section: the section internal ID, reference ID and name
- 3: placed on a detail: the detail internal ID, reference ID and name
- 4: placed on a master layout: the layout internal ID, empty string and name
- 5: placed on a layout: the layout internal ID, number and name


For labels the returned data refers to the labeled element. The collected data can be used to uniquely identify elements in different Archicad databases of a plan file. Causes warning if used in parameter script.