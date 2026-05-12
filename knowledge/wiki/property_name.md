---
id: wiki.generated.property_name
type: wiki
category: other
commands: ["PROPERTY_NAME"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROPERTY_NAME

n = REQUEST("PROPERTY_NAME", "id", typeName, groupName, propertyName) Returns the type, group and name of the selected property. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning. Compatibility: introduced in Archicad 20.

- id: the ID of the selected property (string). See available built-in propery IDs at the section called “Built-in Property Guide”


typeName: the Type of the selected property (string). "IFC": for IFC properties "": other properties

groupName: the Group of the selected property (string).

empty string ("") for Core properties.

propertyName: the Name of the selected property (string).