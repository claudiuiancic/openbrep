---
id: wiki.generated.properties_of_parent
type: wiki
category: other
commands: ["PROPERTIES_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### PROPERTIES_OF_PARENT

n = REQUEST("PROPERTIES_OF_PARENT", propertyType, parentProperties) Returns the properties of the parent object. All properties are returned in one array with the following form: ID, type, group, name. Can be used only in labels. Expression returns 0 and contains dummy return values (empty string or 0) if used in parameter script, causing additional warning.

Core property: [id, "", "", PropertyName] AC property: [guid, "", "GroupName", PropertyName] IFC property: [id, "IFC", "GroupName", PropertyName] Classification: [guid, "Classification", "", ClassificationSystemName] Profile parameter: [guid, "", "Profile Parameters", ParameterName]

propertyType: keyword defining the type of the requested properties. Empty string retruns all types of properties. Possible values: "COREPROPERTY" "ACPROPERTY" "IFCPROPERTY" "CLASSIFICATION" "PROFILEPARAMETER"

Compatibility: the request is introduced in Archicad 20. The property type options and the Classification property type are introduced in Archicad 21, the Profile parameter property type is introduced in Archicad 22.

Example:

DIM parentProperties[] n = REQUEST ("PROPERTIES_OF_PARENT", "", parentProperties) ! parentProperties = [Id1, TypeName1, GroupName1, PropertyName1, ! Id2, TypeName2, GroupName2, PropertyName2, ! ... ! Idn, TypeNamen, GroupNamen, PropertyNamen]