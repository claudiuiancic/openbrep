---
id: wiki.generated.property_value_of_parent
type: wiki
category: other
commands: ["PROPERTY_VALUE_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROPERTY_VALUE_OF_PARENT

n = REQUEST("PROPERTY_VALUE_OF_PARENT", "id", type, dim1, dim2, propertyValues) Returns value array of the selected property. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility: introduced in Archicad 20. Compatibility: length, area, volume and angle types are introduced in Archicad 22.

- id: (string) the ID of the selected property. For built-in property IDs see the section called “Built-in Property Guide”.


type: the type of the selected property value.

- 1: boolean
- 2: integer
- 3: real number
- 4: string
- 5: length
- 6: area
- 7: volume


- 8: angle


dim1, dim2: the dimensions of the propertyValues array. dim1 = 0, dim2 = 0: simple, scalar value. dim1 > 0, dim2 > 0: list of values.

Example: DIM propertyValues[] n = REQUEST ("PROPERTY_VALUE_OF_PARENT", "ExampleId", type, dim1, dim2, propertyValues)