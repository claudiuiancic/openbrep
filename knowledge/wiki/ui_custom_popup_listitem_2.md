---
id: wiki.generated.ui_custom_popup_listitem_2
type: wiki
category: other
commands: ["UI_CUSTOM_POPUP_LISTITEM{2}"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### UI_CUSTOM_POPUP_LISTITEM{2}

UI_CUSTOM_POPUP_LISTITEM{2} itemID, fieldID, name, childFlag, image, paramDesc, storeHiddenId, treeDepth, groupingMethod, selectedValDescription, value1, value2, valuesArray1, .... valuen, valuesArrayn

Compatibility: introduced in Archicad 20. Similar to the "UI_CUSTOM_POPUP_INFIELD" and the "UI_CUSTOM_POPUP_INFIELD{2}" Generates a listitem with popup for a value list of a parameter defined in the User Interface script to avoid using the Parameter script. Suitable for lists which can not be requested in Parameter script. For the parameter script restrictions see the section called “REQUEST Options”. itemID: the unique identifier of the listitem. Listitems can be scripted in an arbitrary order and are sorted by itemID. Duplicate listitem

IDs within a listfield are not allowed. fieldID: the unique identifier of the listfield containing this listitem. name: parameter name as string expression for UI_CUSTOM_POPUP_LISTITEM or parameter name with optional actual index values

if array for UI_CUSTOM_POPUP_LISTITEM{2}.

childFlag: childFlag = 0: the listitem is a groupitem (default value if not specified). childFlag = 1: the listitem is a childitem. The parent item is the first groupitem above.

image: file name or index number of the picture stored in the library part. If valid, it is displayed as an icon in the first column of the

listfield in the associated listitem's row.

paramDesc: the visible name of the listitem in the Description column. If left empty, the description is automatically filled up from the

parameter list description of the Library Part. If there is no description there, the name of the parameter is displayed instead.

storeHiddenId, treeDepth: to set up automatic or manual trees. storeHiddenId = 0, treeDepth = 0: works only with array parameters. The "treeDepth" parameter is set automatically by the second dimension (number of columns) of the array. storeHiddenId = 1, treeDepth > 0: works only with single parameters. There must be n * (1 + treeDepth) values defined (first one for the stored ID and the rest for defining the custom tree).

groupingMethod: grouping method for sorting the tree.

- 1: does not sort the groups and values under the same parent.


- 2: sorts the groups and values under the same parent.


![image 20](<GDL_Reference_Guide_28_images/imageFile20.png>)

![image 21](<GDL_Reference_Guide_28_images/imageFile21.png>)

selectedValDescription: the text written in the field, if empty string the text will be the stored ID of the selected item. valuei, valuesArrayi: define tree values one-by-one and/or with a one dimension array.

Example: UI_CUSTOM_POPUP_LISTITEM itemID, fieldID, "stParameterName", 0, "", "",

1, 3, 2, "", ! storeHiddenId, treeDepth, groupingMethod, selectedValDescription "hiddenID1", "type1", "group1", "value1", "hiddenID2", "type1", "group1", "value2", "hiddenID3", "type2", "group2", "value1", "hiddenID4", "type2", "group2", "value2", "hiddenID5", "type2", "", "value3", "hiddenID6", "", "", "value4", "hiddenID7", "", "", "value5"

![image 22](<GDL_Reference_Guide_28_images/imageFile22.png>)