---
id: wiki.generated.property_values_of_parent
type: wiki
category: other
commands: ["PROPERTY_VALUES_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROPERTY_VALUES_OF_PARENT

n = REQUEST("PROPERTY_VALUES_OF_PARENT", propInputIds, propOutputVals) Returns a value dictionary for the given property ID dictionary. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script or used with unknown input dictionary key, causing additional warning. Compatibility: introduced in Archicad 23.

propInputIds: (dictionary) defining the selected property IDs. propInputIds.propertyIds[n]: (array) contains a dictionary for each selected property ID. propInputIds.propertyIds[n].id: (string) the ID of the selected property.

For built-in property IDs see the section called “Built-in Property Guide”. propOutputVals: (dictionary) the property value data for the selected property IDs. propOutputVals.propertyValues[n]: (array) contains dictionaries for each property value. propOutputVals.propertyValues[n].value_status: the status of the selected property value

1: the selected property is available and has value 2: the selected property is available but no value has been defined for it 3: the property is unavailable, or the selected ID is not valid 4: the property value cannot be evaluated

propOutputVals.propertyValues[n].type: the type of the selected property value. This key only exists in case the

propOutputVals.propertyValues[n].value_status is 1 or 2.

- 1: boolean
- 2: integer
- 3: real number
- 4: string


- 5: length
- 6: area
- 7: volume
- 8: angle


propOutputVals.propertyValues[n].value[]: (array) contains the list of the selected property values. Example: dict propInputIds

propInputIds.propertyIds[1].id = "ExampleId1" propInputIds.propertyIds[2].id = "ExampleId2" ... propInputIds.propertyIds[n].id = "ExampleIdn"

dict propOutputVals n = REQUEST ("PROPERTY_VALUES_OF_PARENT", propInputIds, propOutputVals) ! propOutputVals

- ! .propertyValues[1].value_status

- ! .propertyValues[1].type ! .propertyValues[1].value[] ! .propertyValues[2].value_status
- ! .propertyValues[2].type


- ! .propertyValues[2].value[] ! ... ! .propertyValues[n].value_status ! .propertyValues[n].type ! .propertyValues[n].value[]