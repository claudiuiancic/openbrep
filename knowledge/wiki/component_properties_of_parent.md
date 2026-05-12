---
id: wiki.generated.component_properties_of_parent
type: wiki
category: other
commands: ["COMPONENT_PROPERTIES_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_PROPERTIES_OF_PARENT

n = REQUEST("COMPONENT_PROPERTIES_OF_PARENT", propertyType, parentComponentProperties)

Returns the component properties, which are available for at least one of the building material components of the parent object. All properties are returned in one array with the following form: ID, type, group, name. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

AC property: [guid, "", "GroupName", PropertyName] Classification: [guid, "Classification", "", ClassificationSystemName]

propertyType: keyword defining the type of the requested properties. Empty string returns all available types of properties. Possible values: "ACPROPERTY" "CLASSIFICATION"

Compatibility: the request is introduced in Archicad 23. Example:

DIM parentComponentProperties[] n = REQUEST ("COMPONENT_PROPERTIES_OF_PARENT", "", parentComponentProperties) ! parentComponentProperties = [Id1, TypeName1, GroupName1, PropertyName1, ! Id2, TypeName2, GroupName2, PropertyName2, ! ... ! Idn, TypeNamen, GroupNamen, PropertyNamen]