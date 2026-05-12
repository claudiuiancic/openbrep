---
id: wiki.generated.component_property_values_of_parent
type: wiki
category: other
commands: ["COMPONENT_PROPERTY_VALUES_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_PROPERTY_VALUES_OF_PARENT

n = REQUEST("COMPONENT_PROPERTY_VALUES_OF_PARENT", compPropInput, compPropVals) Returns a value dictionary for the given component ID and property IDs. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script or used with unknown input dictionary key, causing additional warning. Compatibility: introduced in Archicad 23.

compPropInput: (dictionary) defining the selected building material component and property IDs. compPropInput.componentId: (dictionary) contains a dictionary for the selected building material component ID. compPropInput.componentId.id: (integer) the selected building material component ID, available via the

"COMPONENT_IDS_OF_PARENT" REQUEST. compPropInput.propertyIds[n]: (array) contains a dictionary for each selected property ID. compPropInput.propertyIds[n].id: (string) the ID of the selected property.

For built-in property IDs see the section called “Built-in Property Guide”. compPropVals: (dictionary) the building material component property value data for the selected property IDs. compPropVals.propertyValues[n]: (array) contains a dictionary for each property value. compPropVals.propertyValues[n].value_status: the status of the selected property value

1: the selected property is available and has value 2: the selected property is available but no value has been defined for it 3: the property is unavailable, or the selected ID is not valid 4: the property value cannot be evaluated

compPropVals.propertyValues[n].type: the type of the selected property value. This key only exists in case the

compPropVals.propertyValues[n].value_status is 1 or 2.

- 1: boolean
- 2: integer
- 3: real number
- 4: string
- 5: length
- 6: area
- 7: volume
- 8: angle