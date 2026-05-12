---
id: wiki.generated.ui_custom_popup_infield_2
type: wiki
category: other
commands: ["UI_CUSTOM_POPUP_INFIELD{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_CUSTOM_POPUP_INFIELD{2}

UI_CUSTOM_POPUP_INFIELD{2} name, x, y, width, height, storeHiddenId, treeDepth, groupingMethod, selectedValDescription, value1, value2, valuesArray1, .... valuen, valuesArrayn

Compatibility: introduced in Archicad 20. Generates a popup for a value list of a parameter defined in the User Interface script to avoid using the Parameter script.

Suitable for lists which can not be requested in Parameter script. For the parameter script restrictions see the section called “REQUEST Options”. name: parameter name as string expression for UI_CUSTOM_POPUP_INFIELD or parameter name with optional actual index values

if array for UI_CUSTOM_POPUP_INFIELD{2}. x, y: the position of the edit text, pop-up. width, height: width and height in pixels. storeHiddenId, treeDepth: to set up automatic or manual trees.

- storeHiddenId = 0, treeDepth = 0: works only with array parameters. The "treeDepth" parameter is set automatically by the second dimension (number of columns) of the array.
- storeHiddenId = 1, treeDepth > 0: works only with single parameters. There must be n * (1 + treeDepth) values defined (first one for the stored ID and the rest for defining the custom tree).


groupingMethod: grouping method for sorting the tree.

- 1: does not sort the groups and values under the same parent.

![image 15](<GDL_Reference_Guide_28_images/imageFile15.png>)

- 2: sorts the groups and values under the same parent.


![image 16](<GDL_Reference_Guide_28_images/imageFile16.png>)

selectedValDescription: the text written in the field, if empty string the text will be the stored ID of the selected item. valuei, valuesArrayi: define tree values one-by-one and/or with a one dimension array.

Example: UI_CUSTOM_POPUP_INFIELD "stParameterName", x, y, width, height,

1, 3, 2, "", ! storeHiddenId, treeDepth, groupingMethod, selectedValDescription "hiddenID1", "type1", "group1", "value1", "hiddenID2", "type1", "group1", "value2", "hiddenID3", "type2", "group2", "value1", "hiddenID4", "type2", "group2", "value2", "hiddenID5", "type2", "", "value3", "hiddenID6", "", "", "value4", "hiddenID7", "", "", "value5"

![image 17](<GDL_Reference_Guide_28_images/imageFile17.png>)