---
id: wiki.generated.component
type: wiki
category: other
commands: ["COMPONENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT

COMPONENT name, quantity, unit [, proportional_with, code, keycode, unitcode] Local component definition. Scripts can include any number of COMPONENTs.

name: the name of the component (max. 128 characters). quantity: a numeric expression. unit: the string used for unit description. proportional_with: a code between 1 and 6. When listing, the component quantity defined above will be automatically multiplied

by a value calculated for the current listed element:

- 1: item,
- 2: length,
- 3: surface A,
- 4: surface B,
- 5: surface,


- 6: volume.


code: string, defines a code for the component. keycode: string, reference to a key in an external database. The key will be assigned to the component. unitcode: string, reference to a unit in an external database that controls the output format of the component quantity. This will replace

the locally defined unit string.