---
id: wiki.generated.component_property_tree_of_parent
type: wiki
category: other
commands: ["COMPONENT_PROPERTY_TREE_OF_PARENT"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### COMPONENT_PROPERTY_TREE_OF_PARENT

n = REQUEST("COMPONENT_PROPERTY_TREE_OF_PARENT", propTreeInput, propTreeOutput)

Returns the tree of component properties, which are available for at least one of the building material components of the parent object with a grouping similar to the property selector trees in Archicad. Can be used only in the UI Script of labels and markers. Expression returns 0 and contains dummy return values (empty dictionary) if used in other situations, causing additional warning.

propTreeInput: (dictionary) defines the parameters for collecting properties of the parent object's components. propTreeInput.propertyType: (string) keyword defining the type of the requested properties. This key is optional, if it does not

exist, the request collects all property types. Possible values: "ACPROPERTY" "CLASSIFICATION" "BUILTINPROPERTY"

propTreeOutput: (dictionary) the tree of available properties of the parent object propTreeOutput.treeDepth: (integer) the depth of the property tree propTreeOutput.propertyTree: (array) for each returned property, contains treeDepth + 1 strings: the ID of the property, then

its position in the tree in the form of treeDepth strings

- Example 1:


DICT propTreeInput, propTreeOutput n = REQUEST ("COMPONENT_PROPERTY_TREE_OF_PARENT", propTreeInput, propTreeOutput) ! propTreeOutput.treeDepth = m ! propTreeOutput.propertyTree = [Id1, DisplayName11, ... DisplayName1m, ! Id2, DisplayName21, ... DisplayName2m, ! ... ! Idn, DisplayNamen1, ... DisplayNamenm]

- Example 2:


DICT propTreeInput, propTreeOutput n = REQUEST ("COMPONENT_PROPERTY_TREE_OF_PARENT", propTreeInput, propTreeOutput) if n > 0 then

ui_custom_popup_infield "stParameterName", 10, 20, 300, 19, 1, propTreeOutput.treeDepth, 1, "SelectedValueDescription", propTreeOutput.propertyTree

endif